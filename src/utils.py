"""
This contains some utility functions for reading files, searching for entities,
and other basic tasks.

The functions to_conll_iob, read_conll and get_NER_tagcounts were modified from
http://nlpforhackers.io/named-entity-extraction/

"""
import codecs
import os
from collections import Counter
try:
    import ConfigParser
except:
    import configparser as ConfigParser

import sentence_utils


def get_entities(corpus_name):
    """ Load the dataset from the filesystem corresponding to corpus_name
    (to see the list of allowed names, use utils.list_corpora() ), and extract
    all annotated entities.

    Returns a dict, in which each key is an entity type, which contains a list
    of entity mentions in the corpus.

    """
    r = read_conll(corpus_name); data = list(r)
    data2 = [ [(w,iob) for ((w,p),iob) in d] for d in data]
    data3 = [i for u in data2 for i in u]

    tags = sentence_utils.get_tagset(data, with_prefix=True)
    taglist = set([t[2:] for t in list(tags) if t !='O'])
    entities = {}
    for key in taglist:
        entities[key] = []
    data3.append((u'O',u'O'))
    ent = []
    entitytype = 'None'
    for i,item in enumerate(data3[0:-1]):
        if item[1] != 'O':
            if item[1][0] == 'B':
                ent = []
                ent.append(item[0])
            else: # == I
                if item[1][0] != 'I':
                    raise ValueError("Should be I")
                ent.append(item[0])

            if data3[i+1][1][2:] != item[1][2:] or data3[i+1][1][0] == 'B':
                #print i, item
                entitytype = item[1][2:]
                entities[entitytype].append(' '.join(ent))
    return entities


def list_corpora():
    """ List the available corpora names.

    These are read from file_locations.cfg. More corpus names can be added by
    editing this file.

    """
    config = ConfigParser.RawConfigParser()
    config.read('file_locations.cfg')
    return config.sections()


def get_corpus_location(corpus_name):
    """ Given the corpus_name, this returns a tuple containing, in order:

    - file extension: only files with this file extension will be loaded
    - path to the directory in which the data resides.
    - path to the docs folder, containing both a human-readable summary of the
      dataset, and a machine-readable file indicating entity tagging sceme
      (IOB1, IOB2, etc), and information on which columns are used for tokens,
      entities, or POS tags.

    Parameter: corpus name (use function 'list_corpora' to view options.

    """
    config = ConfigParser.RawConfigParser()
    config.read('file_locations.cfg')
    xx = config.get(corpus_name, 'filename_end')
    xx = xx.split("\n")
    xx = tuple(xx)
    if len(xx)==1:
        xx = xx[0]

    filename_end = xx
    data_dir = config.get(corpus_name, 'data_dir')
    docs_dir = config.get(corpus_name, 'docs_dir')
    return filename_end, data_dir, docs_dir


def get_file_settings(corpus_name):
    """ Returns the data file settings corresponding to a particular corpus name,
    particularly:
    - the column number for the words
    - the column number for POS tags
    - the column number for the entity tag
    - whether there is a file extension restriction when loading the data.
    - the separation type (e.g., space, tab)
    - The entity annotation scheme (IOB1, IOB2, etc.)

    """
    filename_end, data_dir, docs_dir = get_corpus_location(corpus_name)
    config_file = os.path.join(docs_dir, 'corpusconfig.cfg')
    config = ConfigParser.RawConfigParser()
    config.read(config_file)
    IOB = config.get('IOB-format','IOB')
    sep = config.get('file-settings','sep')
    sep = sep.strip("'") # NOTE case of a single space; in case sep is ' '
    if sep=='tab':
        sep = '\t'
    iob_pos = config.get('file-settings','iob_pos')
    iob_pos = int(iob_pos)
    word_pos = config.get('file-settings','word_pos')
    word_pos = int(word_pos)
    pos_pos = config.get('file-settings','pos_pos')
    if pos_pos == 'none':
        pos_pos = word_pos
    pos_pos = int(pos_pos)
    return word_pos, pos_pos, iob_pos, filename_end, sep, IOB #, domain


def iob1_to_iob2(annotated_sentence):
    """ Converts list of annotated sentences with entities encoded in the IOB1
    scheme to a list with entities encoded in IOB2.

    Parameters
    ----------
    annotated_sentence : list
        The list contains tuples (w1, t1, iob1), where w1 is the token and
        iob1 is the entity type.

    Remark: CONLL2003 actually uses "IOB1" and we want to use "IOB2". For the
    difference, between them, see:
    Tjong Kim Sang and Veenstra, Representing Text Chunks (1999).

    """
    proper_iob_tokens = []
    for idx, annotated_token in enumerate(annotated_sentence):
        word, tag, ner = annotated_token

        if ner != 'O':
            if idx == 0:
                ner = "B-" + ner[2:]
            elif ner[0:2] == 'B-':
                ner = 'B-'+ner[2:]
            elif annotated_sentence[idx - 1][2][2:] == ner[2:]:
                ner = "I-" + ner[2:]
            else:
                ner = "B-" + ner[2:]
        proper_iob_tokens.append((word, tag, ner))
    return proper_iob_tokens


def to_conll_iob(annotated_sentence):
    """ Transforms sentences encoded without an IOB-prefix (just the entity
    type), to sentences with IOB2-type tags.

    Parameters
    ----------

    annotated_sentence : list
        List of tuples in the form (w,t,iob)

    """
    proper_iob_tokens = []
    for idx, annotated_token in enumerate(annotated_sentence):
        word, tag, ner = annotated_token

        if ner != 'O':
            if idx == 0:
                ner = "B-" + ner
            elif annotated_sentence[idx - 1][2] == ner:
                ner = "I-" + ner
            else:
                ner = "B-" + ner
        proper_iob_tokens.append((word, tag, ner))
    return proper_iob_tokens


def read_conll(corpus_name):
    """ Load the corpus given by corpus_name. This will be represented as a
    generator, to give a list of lists of tuples. Each element in the list is
    a sentence. For a list of available corpus names see utils.list_corpora()

    Each sentence contains a list of tuples of the form:

    ((w, t), iob)

    where w is the token, t is the POS tag (if available; if not availabe it
    is the same as the token), and iob is the iob tag.

    The data will also be converted to IOB2 format if it wasn't in that format
    already.

    Usage
    -----

    >>> data = list(utils.read_conll('Wikigold'))

    """
    word_pos, pos_pos, iob_pos, filename_end, sep, IOB = get_file_settings(corpus_name)
    corpus_root = get_corpus_location(corpus_name)[1]

    if not os.path.exists(corpus_root):
        raise ValueError("The data directory specified in file_locations.cfg does not exist.")

    for root, dirs, files in os.walk(corpus_root):
        for filename in files:
            if filename.endswith(filename_end):
                with open(os.path.join(root, filename), 'rb') as file_handle:
                    try:
                        file_content = file_handle.read().decode('utf-8').strip()
                    except:
                        raise ValueError("Can't process!")
                    # Split sentences:
                    annotated_sentences = file_content.split('\n\n')

                    for annotated_sentence in annotated_sentences:
                        if annotated_sentence not in ['-DOCSTART- -X- O O', '-DOCSTART- -X- -X- O']:
                            # Split words:
                            annotated_tokens = [seq for seq in annotated_sentence.split('\n')]
                            standard_form_tokens = []

                            for idx, annotated_token in enumerate(annotated_tokens):
                                if sep=='multispace':
                                    annotations = annotated_token.split()   # Split annotations
                                else:
                                    annotations = annotated_token.split(sep)   # Split annotations
                                try:
                                    word, tag, ner = annotations[word_pos], annotations[pos_pos], annotations[iob_pos]
                                except:
                                    print(annotations)
                                    #raise ValueError("??")
                                if IOB =='IO':
                                # Transform to IOB format if it is not already.
                                    if ner != 'O':
                                        ner = ner.split('-')[1]
                                    if tag in ('LQU', 'RQU'):
                                        tag = "``"

                                    standard_form_tokens.append((word, tag, ner))
                                    conll_tokens = to_conll_iob(standard_form_tokens)
                                elif IOB == 'IOB1':
                                    standard_form_tokens.append( (word,tag, ner))
                                    conll_tokens = iob1_to_iob2(standard_form_tokens)
                                elif IOB == 'none':
                                    standard_form_tokens.append((word, tag, ner))
                                    conll_tokens = to_conll_iob(standard_form_tokens)
                                elif IOB == 'IOB2':
                                    # This is for the Seminars_and_Job_postings
                                    # data:
                                    if ner=='0':
                                        ner = 'O'
                                    standard_form_tokens.append((word, tag, ner))
                                    conll_tokens = standard_form_tokens
                                else:
                                    raise ValueError('Variable IOB has wrong value.')

                            yield [((w, t), iob) for w, t, iob in conll_tokens]


def attach_domain(corpus, domt):
    """ Indicates whether the corpus is src (source) or tgt
    (target) corpus when doing trainsfer learning.

    This will return a list of lists of the form ((w,t,d),iob), where
    d is the domain ('src' or 'tgt') given by domt.

    Parameters
    ----------

    corpus : list
        List of lists containing tuples of form ((w,t), iob)
    domt : str
        Either 'src' or 'tgt'.

    """
    if domt not in {'src','tgt'}: # Domain type - source or target
        raise ValueError("domt must be 'src' or 'tgt'.")

    data_with_domain = [[((w,t,domt),iob) for ((w,t),iob) in d] for d in corpus]
    return data_with_domain


def get_NER_tagcounts(corpus_name):
    """ Return count values for number of tokens for each entity type
    (including the 'O' type, i.e., not an entity).

    Remark
    ------

    This reads the information from the filesystem directly, and does not
    convert to IOB2 format.

    """
    word_pos, pos_pos, iob_pos, filename_end, sep, IOB = get_file_settings(corpus_name)
    corpus_root = get_corpus_location(corpus_name)[1]

    ner_tags = Counter()

    for root, dirs, files in os.walk(corpus_root):
        for filename in files:
            if filename.endswith(filename_end):
                with open(os.path.join(root, filename), 'rb') as file_handle:
                    file_content = file_handle.read().decode('utf-8').strip()
                    # Split sentences:
                    annotated_sentences = file_content.split('\n\n')

                    for annotated_sentence in annotated_sentences:
                        if annotated_sentence not in ['-DOCSTART- -X- O O', '-DOCSTART- -X- -X- O']:
                            # Split words:
                            annotated_tokens = [seq for seq in annotated_sentence.split('\n')]
                            standard_form_tokens = []

                            for idx, annotated_token in enumerate(annotated_tokens):
                                if sep=='multispace':
                                    annotations = annotated_token.split()   # Split annotations
                                else:
                                    annotations = annotated_token.split(sep)   # Split annotations

                                word, tag, ner = annotations[word_pos], annotations[pos_pos], annotations[iob_pos]
                                ner_tags[ner] += 1

    return ner_tags


def read_NER_output(filename):
    """ Reads CONLL-formatted NER output from a file.

    Remarks
    -------

    This assumes the file is in IOB2, not IOBES, and that sep is space.

    """
    sep = ' '
    word_pos = 0
    iob_pos = -1
    with open(filename, 'rb') as file_handle:
        try:
            file_content = file_handle.read().decode('utf-8').strip()
        except:
            raise ValueError('Cant process the file.')
        # Split sentences:
        annotated_sentences = file_content.split('\n\n')

        for annotated_sentence in annotated_sentences:
            # Split words:
            annotated_tokens = [seq for seq in annotated_sentence.split('\n')]
            standard_form_tokens = []

            for idx, annotated_token in enumerate(annotated_tokens):
                if sep=='multispace':
                    annotations = annotated_token.split()   # Split annotations
                else:
                    annotations = annotated_token.split(sep)   # Split annotations

                try:
                    word, ner = annotations[word_pos], annotations[iob_pos]
                except:
                    raise ValueError("Error!")

                standard_form_tokens.append((word, ner))
                conll_tokens = standard_form_tokens

            yield [((w,w), iob) for w, iob in conll_tokens]

def _getlist(config, section, option, ints=False):
    """ Get a list of config values from the appropriate section of the
    configuration file.

    """
    vals = config.get(section, option)
    if vals is not None:
        vals = vals.split('\n')
        if ints:
            vals = [int(i) for i in vals]
    return vals


# This function is probably not a good idea; it assumes that the entity
# descriptions in the corpusconfig.cfg file are exactly the same as the ones
# in the corpus.
#def get_entity_types(corpus_name):
#    """ Returns the entity types for a given corpus
#
#    """
#    filename_end, data_dir, docs_dir = get_corpus_location(corpus_name)
#    config_file = os.path.join(docs_dir, 'corpusconfig.cfg')
#    config = ConfigParser.RawConfigParser()
#    config.read(config_file)
#    entity_types = config.get('entities','entities').split('\n')
#    return entity_types


