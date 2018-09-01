The GUM Corpus was downloaded on November 2017 from

https://github.com/amir-zeldes/gum

In particular, we use the data from:

https://github.com/amir-zeldes/gum/tree/master/coref/tsv

This was converted to CONLL format.

Attribution
-----------

The GUM corpus was collected and annotated at Georgetown University. For more
information, see the LICENSE, https://corpling.uis.georgetown.edu/gum,
and the following publication:

Zeldes, Amir (2016) "The GUM Corpus: Creating Multilayer Resources in the
Classroom". Language Resources and Evaluation.

Notes
-----
- The NER data is in the coref subdirectory.

Converting to CONLL
-------------------

As the GUM datasets have CC licenses (see the LICENSE file) that permit
sharing and modification, the CONLL-formatted versions are contained in
CONLL-format/data (with a test/train split) and in
CONLL-format/data-by-corpustype (split into categories whow, voyage, news,
interview).

Here are some notes on how we processed the data.

1.) To convert to 'CONLL' format (not worrying about IOB2 here)
    we used the webAnnotsv_to_conll.py in the utils directory:

    import webAnnotsv_to_conll
    webAnnotsv_to_conll.recursively()

2.) Moved the files into the corresponding directories (news, voyage,
    interview, whow).

3.) Data cleaning:

    - In file GUM_interview_licen.tsv, replaced the two
    occurrences of * with O.

    - There was only one entity ("The Independent") tagged as "newspaper"
      entity; so we replaced these with "organization".

Test/Train split
----------------

There wasn't a standard test/train split so we created one using the Python
script stratified_split.py, via:

TRAIN, TEST = write_new_split('GUM', 1000, filedir, 'gum', max_count = 2)
