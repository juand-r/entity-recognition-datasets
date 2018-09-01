"""
 Utility functions not related to I/O, that can be directly applied to a list
 of lists, where each sublist is a sentence, and contains entries of the form
 ((word, pos_tag, dom), iob)

"""
from collections import Counter
import copy


def flatten(sentences):
    """ Flatten a list.

    """
    f = [i for sublist in sentences for i in sublist]
    return f


def get_tagset(sentences, with_prefix):
    """ Returns the set of entity types appearing in the list of sentences.

    If with_prefix is True, it returns both the B- and I- versions for each
    entity found. If False, it merges them (i.e., removes the prefix and only
    returns the entity type).

    """
    iobs = [iob for sent in sentences for (x,iob) in sent]
    tagset = set(iobs)
    if not with_prefix:
        tagset = set([t[2:] for t in list(tagset) if t != 'O'])
    return tagset


def get_IOB_counts(sentences):
    """ Return a counter with IOB labels and their frequency.

    """
    types2 =[ j[1] for sublist in sentences for j in sublist] #list of IOBs
    ner_tags = Counter()

    for i,x in enumerate(types2):
        ner_tags[x] += 1

    return ner_tags


def get_word_counts(sentences, exclude_O = False):
    """ Return a Counter containing the number of times each word has appeared
    within the list of sentences.

    Parameters
    ----------

    sentences : list
        List of lists (sentences)

    exclude_O : bool
        If True, does not count words that have 'O' labels; that is, only
        words corresponding to entities will be counted.

    """
    f = flatten(sentences)

    if exclude_O:
        words = [x[0] for (x, iob) in f if iob != 'O']
    else:
        words = [x[0] for (x, iob) in f]

    word_count = Counter()
    for x in words:
        word_count[x] += 1

    return word_count


def remove_prefix(tok):
    if tok[:2] in {'B-', 'I-'}:
        tok = tok[2:]
    return tok


def sents_no_prefix(sents):
    newsents = copy.deepcopy(sents)
    s22 = [[ [list(x[0]),x[1]] for x in s] for s in newsents]
    fixed = [[ (tuple(x[0]), remove_prefix(x[1])) for x in s] for s in s22]
    return fixed

