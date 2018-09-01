"""
This script can fix comma tokenization errors.

NOTE: only use this if have already eliminated the commas
corresponding to entity names.

"""
filename = '../data/APW_19980314'

newfile = 'APW_19980314.conll'

def clean():

    newsentences = []
    badlist = []

    #with open(newfile,'a+') as nfd:
    with open(filename,'rb') as fd:
        file_content = fd.read().decode('utf-8').strip()
        annotated_sentences = file_content.split('\n\n')
        for annotated_sentence in annotated_sentences:
            newsentence = []

            annotated_tokens = [seq for seq in annotated_sentence.split('\n')]
            for idx, annotated_token in enumerate(annotated_tokens):
                annotations = annotated_token.split('\t')
                #print annotations
                if len(annotations)==1:
                    # assume this is always caused by having spaces instead
                    # of tabs:
                    annotations = annotations[0].split(annotations[0].count(' ')*' ')

                # Sometimes there are commas incorrectly tokenized, eliminate
                # NOTE: only use this if have already eliminated the commas
                # corresponding to entity names.

                if len(annotations[0])>1 and annotations[0][-1]==',' and '.,' not in annotations[0]:
                    newsentence.append((annotations[0][:-1],annotations[1])  )
                    newsentence.append((u',', annotations[1]))
                    badlist.append( (annotations[0][:-1],annotations[1])  )
                    print annotations
                else:
                    newsentence.append((annotations[0],annotations[1]))

            newsentences.append(newsentence)

    return badlist, newsentences

def savefile(newsentences):
    with open(newfile,'a+') as nfd:
        for sent in newsentences:
            nfd.write('\n')
            for iobword in sent:
                nfd.write(iobword[0]+'\t'+iobword[1]+'\n')

