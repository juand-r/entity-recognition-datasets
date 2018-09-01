"""
This will convert the portion of the NIST 1999 IE-ER Dataset in NLTK
to CONLL format.

NOTE: unfortunately the IEER corpus has already tokenized the words for us
but not the sentences, so we need to do a bit of pre-processing.

"""


from nltk.corpus import ieer
from nltk.tree import Tree
import nltk

ieer.fileids()
#print(docs[0].text)
CONLL_WRITE = '../data/'

def tree2conll_without_postags(t):
    tags = []
    for child in t:
        try:
            category = child.label()
            if category in {'LOCATION','PERSON','ORGANIZATION','DATE','TIME','DURATION','CARDINAL','MONEY','MEASURE'}:
                category = category[0:3]
            elif category == 'PERCENT':
                category = 'PCT'
            else:
                print category
                raise ValueError("!!??")

            prefix = "B-"
            for contents in child:
                if isinstance(contents, Tree):
                    raise ValueError("Tree is too deeply nested to be printed in CoNLL format")
                tags.append((contents, prefix+category))
                prefix = "I-"
        except AttributeError:
            tags.append((child, "O"))
    return tags


def get_breaks(words, rr):
    L = [0]
    for i in range(len(rr)):
        #print i
        #print L
        appended = False
        for j in range(L[i],len(words)):
            if ' '.join(words[L[i]:j]) == rr[i]:
                #print rr[i]
                #print '\n'
                L.append(j)
                appended = True
        if not appended and i != len(rr)-1 :
            print 'Failed.', i
            print rr[i]
            raise ValueError("?")

    return L

def parse_doc(filename, index):

    docs = ieer.parsed_docs(filename)
    dt = docs[index].text
    words = dt.leaves()
    tags = tree2conll_without_postags(dt)

    rr = nltk.sent_tokenize(' '.join(words))
    # small fixes:
    if filename =='NYT_19980315' and index==11:
        rr[8]=rr[8]+rr[9]
        rr.remove(rr[9])
    if filename == 'NYT_19980407':
        if index == 4:
            rr[19]=rr[19]+rr[20]
            rr.remove(rr[20])
        if index == 13:
            rr[9] = rr[9]+rr[10]
            rr.remove(rr[10])

    L =get_breaks(words, rr)
    L.append(len(tags)) # otherwise you miss the last sentence of the document.
    tags = [tags[L[i]:L[i+1]] for i in range(len(L)-1)]
    return tags

def write_conll(filename):
    """ For example: filename = 'APW_19980314'

    """
    docs = ieer.parsed_docs(filename)
    numdocs = len(docs)

    conllfile = CONLL_WRITE + filename
    with open(conllfile, 'a+') as nfd:
        for index in range(numdocs):
            nfd.write('\n')
            nfd.write('-DOCSTART- -X- -X- O')
            nfd.write('\n')
            sentences = parse_doc(filename, index)
            for sent in sentences:
                nfd.write('\n')
                for iobword in sent:
                    nfd.write(iobword[0]+'\t'+iobword[1]+'\n')

def write_all_to_conll():
    filenames = ieer.fileids()
    for filename in filenames:
        write_conll(filename)
        print 'Done with ', filename


