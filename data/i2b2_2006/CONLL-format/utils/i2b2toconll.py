import re
import os
import xml.etree.ElementTree as ET
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer
#NOTE: I tried a few of the other ones and TreebankWordTokenizer worked best.
import nltk

# Example filename:
filename = 'deid_surrogate_train_all_version2.xml'

DATADIR = '../original_data/'
CONLLDIR = '../data/'


def write_all_to_conll():
	filenames = os.listdir(DATADIR)
	for filename in filenames:
		writeconll(filename)


def writeconll(filename):
	print filename
	readname = os.path.join(DATADIR, filename)
	store = parse_all(readname)

	writename = os.path.join(CONLLDIR, filename+'.conll')
	with open(writename, 'a+') as fd:
		for i in store:
			if i[0] != '\n':
				#fd.write(i[0]+'\n')
				fd.write(i[0]+'\t'+i[1]+'\n')
			else:
				fd.write('\n')


def parse_all(filename):
	store = parse_docs(filename)
	s2 = clean(store) # remove the /n
	s3 = make_newlist(s2)
	s4 = tokenizeit(s3) #tokenize (properly!) the text fragments
	s5 = make_newlist(s4)
	 # last step: remove \n if more than one in a row:
	s6 = remove_consecutive_newlines(s5)
	return s6


def parse_docs(filename):

	#with open('wsj00a.qa') as fd:
	with open(filename,'r') as fd:
		data = fd.read()

	root = ET.fromstring(data)
	docs = root.getchildren()
	#c1 = docs[1]
	store = []
	for ii,doc in enumerate(docs):
		#print ii
		p = parse_doc(doc)
		store.extend(p)
	return store


def parse_doc(c1):

	children = c1.getchildren()

	if c1.tag !='RECORD' or children[0].tag != 'TEXT':
		raise ValueError("What is going on?")

	children = children[0].getchildren()

	iobs_text = [c.text for c in children]
	iobs_type = [c.attrib.get('TYPE') for c in children]
	store = []
	for i,item in enumerate(c1.itertext()):
		#print i,item
		if item in iobs_text:
			ind = iobs_text.index(item) # index of first match
			if iobs_type[ind] is not None:
				# clean up the item text:
				clean_item = item.strip(' ')
				store.append((clean_item, iobs_type[ind]))
			# remove the FIRST match:
			iobs_text.remove(item)
			iobs_type.remove(iobs_type[ind])
		else:
			#print i,item
			item = item.strip(' ')
			store.append((item,'O'))
	return store


def clean(store):
	# first remove all the '' fragments:
	store = [i for i in store if i[0] != '']

	# first fix all the /n:
	for i,x in enumerate(store):
		spl = splitit(x[0])
		store[i] =  (spl, store[i][1])
	return store


def splitit(t):
    """ t is a string. This works like splitlines(True) ought to
    work but doesn't. For example: for t='\n This is another one\n'
    t.splitlines(True) gives
    ['\n', ' This is another one\n']
    whereas splitit(t) gives:
    ['\n', 'This is another one', '\n']
    Similarly, the word tokenizer also removes the delimiters, which I
    want to keep to avoid sentence segmentation errors.

    """
    if t== '':
        return t
    t = t+'\n'
    store = []
    s=""
    for i in t:
        if i == '\n':
            store.append(s)
            store.append('\n')
            s=""
        else:
            s = s+i
    store = store[:-1]
    store = [i.strip(' ') for i in store if i != '']
    return store

#NOTE use this once there are a bunch of ['\n','blabla'].  THEN need
# to word tokenize each one again, and then run this again.
def make_newlist(L):
    """
    eg.  L = [(['This', 'is', 'a'], 'O'), (['worm'], 'animal')]
    """
    #print L
    newL = []
    for ii,i in enumerate(L):
        if isinstance(i[0],list):
            iob = i[1]
            for tok in i[0]:
                newL.append((tok,iob))
        else:
			print ii
			raise ValueError("!?")
    return newL


def shall_use_split(text, do_not_tokenize):
	#x[0][-4:] in {'Inc.','N.V.','Ltd.'} or x[0][-5:] in {'Corp.'} or x[0][-6:] in {'S.p.A.'} or x[0][-3:] in {'Co.'}:
	dd = {3:[],4:[],5:[],6:[],7:[],8:[]}
	for i in do_not_tokenize:
		dd[len(i)].append(i)
	# Only checks the end of the string (for now..)
	if any([text[-k:] in dd[k] for k in [3,4,5,6,7,8]]):
		willsplit = True
	else:
		willsplit = False
	return willsplit


def remove_consecutive_newlines(store):
	newstore = []
	for i,x in enumerate(store[:-1]):
		if not (x[0] == '\n' and store[i+1][0] == '\n'):
			newstore.append(x)
	return newstore


def tokenizeit(store):
	#NOTE: how to tokenize stuff with &, like AT&T, S&L or S&P ?  Note this
	# seems to be done differently in different corpora.
	tokenizer = TreebankWordTokenizer()

	do_not_tokenize = ['Mr.','Dr.','Mrs.','Ms.','Prof.','Jr.','Sr.','Rep.',
	'Sen.','Rev.','St.','Lt.','Gov.','Gen.','Brig.','Maj.','Col.','Capt.',
	'Sgt.','M.D.',
	'U.S.','U.K.','U.N.','L.A.','U.S.S.R.','U.S.A.','B.C.',
	'N.V.','G.m.b.H.','S.p.A.','B.V.','N.A.',
	'Pty.','S.A.','Ltd.','Inc.','Bros.','Corp.','Co.','CORP.','L.P.','A.G.',
	'Ltda.','E.U.','I.B.M.','D.T.',
	'Nov.', 'Dec.','Jan.','Feb.','Aug.','Sept.','Sep.','Oct.','a.m.','p.m.',
	'Mass.','Calif.','N.J.','N.M.','N.Y.','N.C.','N.H.','R.I.','Ky.','Va.',
	'S.C.','Neb.',
	'Wash.','Mich.','Conn.','D.C.','Ark.','Pa.','Ind.','Ariz.','Miss.','Fla.',
	'Del.','Nev.','Ore.','Tenn.','Mont.','Ill.','Ala.','Wis.','Ga.','La.',
	'Mo.','Vt.',
	'Blvd.','Ave.','Ln.','Rd.',
	'No.']
	pat = re.compile(r'[0-9][.,]{0,1}[0-9]*')

	for i,x in enumerate(store):
		if x[0] == '\n':
			store[i] =  ([x[0]], store[i][1])
		#elif any([i in x[0] for i in do_not_tokenize]) and
		#elif '$' not in x[0] and '%' not in x[0]: #x[0] in do_not_tokenize: #{'Mr.','Dr.'}:
		elif x[0] in do_not_tokenize:
			toks = [x[0]]
			store[i] =  (toks, store[i][1])
		elif shall_use_split(x[0], do_not_tokenize):
			#x[0][-4:] in {'Inc.','N.V.','Ltd.'} or x[0][-5:] in {'Corp.'} or x[0][-6:] in {'S.p.A.'} or x[0][-3:] in {'Co.'}:
			toks = x[0].split(' ')
			#print 'Plain split on: ', x[0]
			store[i] =  (toks, store[i][1])
		elif '%' in x[0]:
			toks = tokenizer.tokenize(x[0])
			store[i] = (toks, store[i][1] )
		else:
			#NOTE It seems like this is already tokenized inline in the xml,
			# so this way (just splitting spaces) may be best here.
			toks = x[0].split(' ')
			store[i] =  (toks, store[i][1])
	return store


