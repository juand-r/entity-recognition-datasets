"""
This script can transform the re3d (json streaming, LDJSON format) to
brat standoff annotation format.

For example, the re3d lines are as follows:

T1 \t Organization 0 4 \t Sony

(a space separates Organization, 0 and 4).

NOTE: differences -- will not do 'discontinuous entities';
                  -- will not label separate entities via numbers, i.e.,
                     all entities will be "T1". This is fine since we are not
                     doing co-reference resolution.

Question - should just keep the entity annotations with confidence > 0.5 ? Or
           keep all of them? We decided to only keep the entities with a
           confidence score >= 0.5.

Brat standoff format: http://brat.nlplab.org/standoff.html

NOTE: To later convert from brat standoff to CONLL format, we used the script
standoff2conll from https://github.com/spyysalo/standoff2conll

"""
import json
import codecs
import os

# TOGGLE WHETHER TO ONLY KEEP THOSE WITH CONFIDENCE >0.5, or to keep all.
CONF_FILTER = True

if CONF_FILTER:
    confidence_val = 0.5
else:
    confidence_val = 0.0

DIR = '../../'
DATADIR = DIR+'data/'
BRATDIR = DIR+'CONLL-format/data/bratann/'

# example:
# TOPDIRNAME = 'Australian_Department_of_Foreign_Affairs'

def write_txt_files(TOPDIRNAME):
    """ Call this to save the raw text in .txt files in a text directory.

    """
    DIR_read = os.path.join(DATADIR,TOPDIRNAME)
    DIR_txtwrite = os.path.join(BRATDIR,TOPDIRNAME,'text/')
    text_list = ldjson_to_listofdicts(os.path.join(DIR_read , 'documents.json'))

    for i in range(len(text_list)):
        with codecs.open(DIR_txtwrite + text_list[i]['_id']+'.txt','w',"utf-8") as fd:
            fd.write(text_list[i]['text'])

def ldjson_to_listofdicts(FILENAME):
    L = []
    with open(FILENAME) as f:
        for line in f:
            row = json.loads(line)
            L.append(row) # results in a list of dicts
    return L


def process(TOPDIRNAME):
    """ Call this to save .ann files with entity annotations in brat standoff
    style.

    """
    DIR_read = os.path.join(DATADIR,TOPDIRNAME)
    DIR_annwrite = os.path.join(BRATDIR,TOPDIRNAME,'ann/')
    text_list = ldjson_to_listofdicts(os.path.join(DIR_read , 'documents.json'))
    entities_list = ldjson_to_listofdicts(os.path.join(DIR_read, 'entities.json'))

    d_id = [s['_id'] for s in text_list]

    exceptions = {'Targeted Operations Against ISIL Terrorists Navy',
                  'Boris Johnson A Foreign Office spokesman',
                  'Johnson A'} #entities to ignore; they are wrong!

    for i,e in enumerate(entities_list):
        print i, e['value']
        #e = entities_list[0]
        doc = text_list[ d_id.index(e['documentId']) ]
        doc_id = doc['_id']
        doc_text = doc['text']
        if e['value'] not in exceptions:
            if doc_text[e['begin']:e['end']] != e['value']:
                raise ValueError("PROBLEM!")

            if e['confidence'] >= confidence_val:
                with codecs.open( DIR_annwrite + doc_id + '.ann','a+',"utf-8") as fd:
                    if CONF_FILTER:
                        line_to_write = 'T1'+ '\t' + e['type']+' '+str(e['begin'])+' '+str(e['end']) + '\t'+ e['value']+'\n'
                    else:
                        line_to_write = 'T1'+ '\t' + e['type']+' '+str(e['begin'])+' '+str(e['end']) + ' ' + str(e['confidence']) + '\t'+ e['value']+'\n'
                    fd.write(line_to_write)

