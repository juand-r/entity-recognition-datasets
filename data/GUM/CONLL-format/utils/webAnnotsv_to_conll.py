"""
This script can be used to convert Webanno .tsv files to CONLL.
For use with Python 2.

"""

import os

filename = 'GUM_whow_skittles.tsv'

# column indices that we need to know
word_ind = 2
iob_ind =  3

CONLLDIR_BASE = '../data_CONLL-format/'
rootDir_BASE = '../data_orig/gum/coref/tsv/'

def recursively():
    """ This converts every tsv file in the rootDir_BASE to CONLL-format
    and saves it in the CONLLDIR_BASE directory.

    """
    CONLLDIR = CONLLDIR_BASE
    rootDir = rootDir_BASE

    #CONLLDIR is the directory where the new files should be written.
    for dirName, subdirList, fileList in os.walk(rootDir):
        newdir = CONLLDIR+dirName[len(rootDir):]
        if not os.path.exists(newdir):
            os.makedirs(newdir)
        print 'Made directory: ', newdir
        for fname in fileList:
            writefile = os.path.join(newdir, fname)
            readfile = os.path.join(dirName, fname)

            # Parse the file and write to writefile
            file_to_conllfile(readfile, writefile)
            #print 'Wrote to: ', writefile
            #print 'orig: ', readfile

def file_to_conllfile(filename, writefile):
    """ Read in a tsv file, and write to a CONLL-2003 formatted file.

    """
    sentences = file_to_sent_list(filename)
    new_sentences = fix_sentences(sentences)
    #writefile = CONLLDIR+filename
    with open(writefile,'a+') as fd:
        for sent in new_sentences:
            fd.write('\n')
            for tok in sent:
                fd.write(tok[0] + '\t' + tok[1] + '\n')
    print 'Done with file', filename


def file_to_sent_list(filename):
    """ Returns a list of lists; each sublist contains tuples of the form
    (word, pos, ent), but ent is in the CONLL-2012 format, ie it is given
    by things like *, (PERSON* , (NORP) (using brackets rather than IOB
    tags.

    """
    with open(filename,'r') as fd:
        L = fd.readlines()

    # The document is split into pieces, so there are some more # in between these
    # lines; filter them out.
    L = [l for l in L if l[0]!='#']

    sentences = []
    sent = []
    for l in L:
        if l=='\n':
            sentences.append(sent)
            sent = []
        else:
            stripped = l.split()
            word = stripped[word_ind]
            iob = stripped[iob_ind]

            sent.append((word, iob) )
    return sentences

def fix_iob(iob):
    if iob[-1]==']' and iob.find('[')>=1:
        # might have |
        if '|' in iob:
            first = iob[:iob.find('|')]
            second = iob[iob.find('|')+1:]
            iob = first

        LBP = iob.find('[')
        if not iob[LBP+1:-1].isdigit():
            print iob
            raise ValueError("?")
        iob = iob[: iob.find('[')]

    if iob == '_':
        iob = 'O'

    return iob


def fix_sentences(sentences):
    s2 = [ [(w,fix_iob(iob)) for (w,iob) in s] for s in sentences]
    s2 = [x for x in s2 if x!=[]] # eliminate any extra empty spaces
    return s2

############################################################################

