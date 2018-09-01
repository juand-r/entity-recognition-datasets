Due to licensing restrictions, the BBN Pronoun Coreference and Entity Type
Corpus cannot be distributed. It can be obtained from the LDC.

However, we included a script that will convert the dataset into CONLL 2003
format.

1. Put the contents of the BBN dataset (available from LDC, catalog
number LDC2005T33), in this directory.

2. Create directory `data` within CONLL-format

3. Some minor cleaning must be done (some XML errors). See BBN/README.rst
   for the details.

4. Then, in directory utils, in Python 2:

from bbn2conll import *
write_all_to_conll()

This will write the BBN corpus into CONLL-formatted files in the directory
CONLL-format/data/

