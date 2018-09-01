The NIST 1999 IE-ER Dataset
===========================

We used the portion of the NIST 1999 IE-ER Evaluation Dataset which is available
in NLTK (the NEWSWIRE development test data, originally in subdirectory
/ie_er_99/english/devtest/newswire/*.ref.nwt


The files can be found in the list of nltk corpora. The files are:

    'APW_19980314': 'Associated Press Weekly, 14 March 1998',
    'APW_19980424': 'Associated Press Weekly, 24 April 1998',
    'APW_19980429': 'Associated Press Weekly, 29 April 1998',
    'NYT_19980315': 'New York Times, 15 March 1998',
    'NYT_19980403': 'New York Times, 3 April 1998',
    'NYT_19980407': 'New York Times, 7 April 1998',

These are located in $NLTK_DATA/corpora/ieer, where NLTK_DATA is the directory
containing the nltk datasets.

For more information on the dataset, see:

http://www.itl.nist.gov/iad/894.01/tests/ie-er/er_99/er_99.htm


How the data was converted to CONLL format
------------------------------------------

In case one would like to replicate this:

1. There was an error (one nested ORG "Smithsonian", right after:
   'the main book publishing arm' in file ieer/NYT_19980407
   This was fixed manually.
   Replace the original ieer/NYT_19980407 in the nltk corpora directory with
   this one.

2. Use the script makeconll.py in the utils directory. From Python 2:
       import makeconll
       makeconll.write_all_to_conll()

   This should write the 6 files to the data directory. Altogether there are
   about 50,000 tokens here. DO NOT RE-RUN (it will overwrite the files).

3. I fixed several errors caused by the nltk corpus reader:

    - &AMP; -> &
    - &UR; and &LR; removed (I checked for QR, QC, HT, MD, but they were not present)
    - Incorrect sentence segmentation
    - : and ; attached to words
    - Removed incorrectly tokenized commas [for entities]
    - periods at end of sentence, incorrectly tokenized
    - parentheses "(" and ")" incorrectly tokenized
    - !, ? incorrectly tokenized
    - `` and ''
    - Proper tokenization for 's
    - Also proper tokenization for n't, 'v, 'm, 'll, 'd, 'r  etc

4. Used script quick_comma_fix.py to fix comma errors.

Removal of entities
-------------------

There were under 20 instances of TIME, so these were removed.

Remarks
-------

The annotation scheme seems very similar to MUC. In addition to the 7 MUC
entity types, there are 3 new entity types here:

    DUR (DURATION), MEA (MEASURE), and CAR (CARDINALITY).

Note: this corpus does not overlap in any way with MUC.  This appeared after
MUC 7 and uses news articles from a different year.


