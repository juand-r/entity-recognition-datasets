"""
Utility functions for doing stratified random sampling (at the sentence
level) for those corpora which do not have test/train splits, and for saving
the test and train data in CONLL 2003 format in separate directories.

"""
import os
import codecs
from sklearn.model_selection import train_test_split

import utils

def write_new_split(corpus_name, test_size, filedir, filename,
                    seed = 42, max_count = 2):
    """ Do stratified random sampling for a given corpus given by corpus_name,
    and save the results in file filename in directory filedir. Parameter
    test_size indicates the number of sentences to be used in the test set.

    For information on the parameter max_count, see the documentation for
    function stratified_split.

    For now, this only supports stratified_split at the sentence level.

    >>> TRAIN, TEST = write_new_split('CADEC', 1000, filedir, 'cadec', max_count = 2)
    >>> TRAIN, TEST = write_new_split('re3d', 200, filedir, 're3d', max_count = 2)
    >>> TRAIN, TEST = write_new_split('GUM', 1000, filedir, 'gum', max_count = 2)
    >>> TRAIN, TEST = write_new_split('MUC6', 1000, filedir, 'muc6', max_count = 2)
    >>> TRAIN, TEST = write_new_split('NIST_IEER99', 690, filedir, 'nist', max_count = 2)
    >>> TRAIN, TEST = write_new_split('BBN', 10000, filedir, 'bbn', max_count = 2)
    >>> TRAIN, TEST = write_new_split('GMB1', 1000, filedir, 'gmb1', max_count = 2)

    """
    r = utils.read_conll(corpus_name)
    sentences = list(r)
    train_data, test_data = stratified_split(sentences,
                                             test_size,
                                             seed = seed,
                                             max_count = max_count)

    writefile(train_data, os.path.join(filedir,'train'), filename+'-train.conll')
    writefile(test_data, os.path.join(filedir,'test'), filename+'-test.conll')

    return train_data, test_data


#TODO this should be moved to utils.
def writefile(sentences, filedir, filename, sep='\t'):
    """ Write the sentences, in CONLL-format, to a file given by filename
    located in directory filedir.

    """
    DIR = filedir
    WRITEFILE = os.path.join(DIR, filename)
    if not os.path.exists(DIR):
            os.makedirs(DIR)
    if os.path.isfile(WRITEFILE):
        raise ValueError("The file already exists!")
    with codecs.open(WRITEFILE,'a+',encoding='utf-8') as fd:
        for sent in sentences:
            fd.write('\n')
            for tok in sent:
                fd.write(tok[0][0] + sep + tok[1]+'\n')


def stratified_split(sentences, test_size, max_count = 2, seed = 42):
    """
    Uses 'train_test_split' with stratification from scikit learn. However,
    since we want to split on the sentences level, we first map label
    occurrence statistics (only counting B- labels) to integer categories.

    max_count specifies the maximum label count we are interested in from
    the point of view of keeping the classes balanced. For example, say
    max_count = 2, the label set is [B-ADVERSE, B-DISEASE]. Then a sentence
    with 3 counts of B-ADVERSE and 2 counts of B-DISEASE is placed in the same
    bin as sentences with 2 counts of B-ADVERSE and 2 counts of B-DISEASE.

    If a bin only has one element, 'train_test_split' will fail, so in this
    event the element is mapped to the class of sentences with no labels.

    """
    labels = [[iob for (x,iob) in d] for d in sentences]
    tags = list(set([i for s in labels for i in s if i[0]=='B']))
    inds = range(len(labels))

    Y = [_map_labels(l, tags, max_count) for l in labels]

    # Quick fix: if any element in Y only appears once, change it to 0
    ##################################################################
    if len(tags) < 20:
        maxnum = (max_count+1)**len(tags) - 1
        Yfreq = [Y.count(i) for i in range(maxnum+1)]
        fixcounts = [i for i,x in enumerate(Yfreq) if x==1]
        for c in fixcounts:
            Y[Y.index(c)] = 0
    else: # Due to memory issues:
        cc = [Y.count(Y[i]) for i in range(len(Y))]
        for i in range(len(cc)):
            if cc[i] == 1:
                Y[i] = 0
    ###################################################################

    inds_train, inds_test, Y_train, Y_test = train_test_split(inds, Y,
        test_size = test_size, random_state=seed, stratify=Y)

    train_data = [sentences[i] for i in inds_train]
    test_data = [sentences[i] for i in inds_test]

    return train_data, test_data


def check_label_ratios(train_data, test_data, orig_data, tags):
    """ This function can be used to compare the entity class proportions
    before and after the test/train split was made. tags is the set of
    entity class tags to compare.

    """
    train_tagcounts =  [ sum([len([i for i in T if i[1] == tag]) for T in train_data]) for tag in tags]
    test_tagcounts =  [ sum([len([i for i in T if i[1] == tag]) for T in test_data]) for tag in tags]
    orig_tagcounts =  [ sum([len([i for i in T if i[1] == tag]) for T in orig_data]) for tag in tags]

    train_ratios = [float(i)/sum(train_tagcounts) for i in train_tagcounts]
    test_ratios = [float(i)/sum(test_tagcounts) for i in test_tagcounts]
    orig_ratios = [float(i)/sum(orig_tagcounts) for i in orig_tagcounts]

    return train_ratios, test_ratios, orig_ratios


def _map_labels(labels, tags, max_count = 2):
    """

    Parameters
    ----------

    labels are the labels of one sentence

    tags : list
        Must all start with B-
    """
    base = max_count + 1
    counts = [labels.count(t) for t in tags]
    # Any counts greater than max_count are put in the same 'bin' as max_count
    for i in range(len(counts)):
        if counts[i] > max_count:
            counts[i] = max_count

    Y = int("".join(map(str, counts)), base = base)
    return Y


