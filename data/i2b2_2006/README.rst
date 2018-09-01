The i2b2 2006 dataset
---------------------

The i2b2 2006 Deidentification and Smoking Challenge dataset
(NLP Data Set #1B) can be obtained at:

https://www.i2b2.org/NLP/DataSets/Main.php

A data use agreement needs to be signed, so the dataset could not be
included here.

The dataset includes 889 de-identified discharge summaries with
de-identification challenge annotations.


Downloading the data
--------------------

Download and unzip the following three files:

deid_surrogate_test_all_groundtruth_version2.xml
deid_surrogate_test_all_version2.xml
deid_surrogate_train_all_version2.xml

Move them to the data directory.

Cleaning the data
-----------------

1. The original train xml file is not correct -- we needed to fix the
   mismatched tag on line 25722.

2. There were less than 20 mentions of 'AGE', so these were replaced by 'O'.

Script to convert to CONLL
--------------------------

There is a script, i2b2toconll.py (in the utils directory) that can be used
to convert the data to CONLL format.

To use it:

import i2b2toconll
i2b2toconll.write_all_to_conll()

Note: one of the three files contains test data which is unlabelled, so the
CONLL output from this can be removed.

Cite as
-------

Is using the i2b2 2006 dataset, please cite as:

Uzuner O, Juo Y, Szolovits P, "Evaluating the state-of-the-art in automatic
de-identification". J Am Med Inform Assoc. 2007, 14(5):550-63

