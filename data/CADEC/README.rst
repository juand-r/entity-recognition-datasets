CADEC dataset
=============

The CADEC v.2 dataset was accessed on November 2017 from:

https://data.csiro.au/dap/landingpage?execution=e3s2

NOTE: the original corpus includes nested entities.

For more information on the dataset, see Karimi et al., Cadec: A corpus of
adverse drug event annotations. Journal of biomedical informatics, 55:73-81.

Due to licensing restrictions, we cannot redistribute this dataset. Some notes
on how we processed this dataset are given below.

Files
-----

For NER, the important data directories are cadec/original and
cadec/text:

- cadec/text: contains the original raw text
- cadec/original: annotations of the entities in row/column format
  (tab-separated), with some comments starting with # interspersed. The columns
  are, in order:
    - T1, T2 etc (we ignore this)
    - entity type (ADR, Drug, Disease, Symptom, Finding)
    - first character position
    - 1+last character position
    - the entity text

Processing to CONLL
-------------------

First we fixed the following mistake:
    - In file DICLOFENAC-SODIUM.7.ann:
      On line 8, 421 was changed to 411.

The data is in brat standoff format. To convert it to CONLL format, we used
the standoff2conll script from:

https://github.com/spyysalo/standoff2conll

This converts from brat standoff annotation format to CONLL format.
The corresponding .ann and .txt files must be in the same directory with
nothing else in that directory.

Note: In the event of overlapping entities, standoff2conll chooses the
entities with maximum span.

Cleaning
--------

- We removed the following files (the original files
were empty and there is nothing there.)

    - VOLTAREN-XR.9.conll
    - LIPITOR.40.conll

Remarks
-------

- The standoff2conll.py resolves the following:
  - Discontinuous spans are replaced by full spans if possible
    (sometimes this is not possible as there is no full span
    replacement, and the tags are ignored).
  - When spans are nested, the largest span is chosen.

Test/Train split
----------------

There wasn't a standard test/train split so we created one using the Python
script stratified_split.py, via:

TRAIN, TEST = write_new_split('CADEC', 1000, filedir, 'cadec', max_count = 2)
