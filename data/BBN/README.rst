The BBN Pronoun Coreference and Entity Type Corpus
==================================================

The BBN corpus cannot be distributed due to licensing restrictions. It can
be obtained from the LDC (catalog number LDC2005T33)

However, we included a script (bbn2conll.py) that will convert the dataset
into CONLL 2003 format:

1. Put the contents of the BBN dataset (available from LDC, catalog
number LDC2005T33), in directory original_BBN_dataset.

2. Create directory 'data' within the CONLL-format directory.

3. Some minor cleaning must be done (some XML errors). See below for details.

4. Then, in directory utils, in Python 2:

import bbn2conll
bbn2conll.write_all_to_conll()

Cleaning
--------

Label mismatches:

* wsj00c.qa, line 194: mismatch: <TIMEX> more than 4,000 hours </NUMEX>.
  NUMEX should be TIMEX.

Ampersands: turn all & to &amp; for the following files:

    wsj15c.qa
    wsj20b.qa
    ...and many others...

The following were missing the <ROOT> (at start) and </ROOT> at the end; added
them back in (wsj and .qa are omitted for convenience):

    15c
    20b
    20c
    17a
    20a
    03b
    13c
    16c
    17d
    03d
    14a
    16d
    14b
    13b
    04b
    15b
    06b
    13a
    12d
    18b
    17b
    18c
    17c
    18a
    13d
    16a
    19c
    20d
    03c
    04d
    14d
    14c
    04c
    03a
    16b
    15a
    19d
    04a
    15d
    18d

