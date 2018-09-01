Corpus
------

The 2014 De-identification dataset can be obtained at:

    https://www.i2b2.org/NLP/DataSets/

Specifically, download the "2014 De-identification and Heart Disease Risk
Factors Challenge.  A data use agreement needs to be signed, so the dataset
could not be included here.

Converting to CONLL format
--------------------------

To obtain the i2b2 2014 deidentification corpus in CONLL format, we used
the tools bundled with NeuroNER, available at:

https://github.com/Franck-Dernoncourt/NeuroNER

1. First follow the instructions in NeuroNER/data/i2b2_2014_deid/readme.md
   Run the python script xml_to_brat.py (this requires Python 3).

2. Use the script brat_to_conll.py located in NeuroNER/src

    Specifically:

    We used 'spacy' (not 'stanford') for tokenizing. We
    downloaded the english language model en_core_web_sm-1.2.0.tar.gz from here:
    https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-1.2.0/en_core_web_sm-1.2.0.tar.gz

    Then:

    python3 -m spacy link en_core_web_sm en_default

    Then run the following in Python 3:

    import brat_to_conll
    brat_to_conll.brat_to_conll(input_folder, output_filepath, 'spacy', 'en_default')

    Run it three times (for the training, testing, and dev data) using the
    appropriate input_folder and output_filepath names.

Note on train/dev split
-----------------------

Note: according to the xml_to_brat.py script:

training-PHI-Gold-Set1 = training set
training-PHI-Gold-Set2 = dev/validation

It appears this is what was used in the paper Lee et al (2017), "Transfer
Learning for Named Entity Recognition with Neural Networks".  They mention
"60% [of train set] corresponds to the full official train set".  The only
way this makes sense is as the fraction train/(train+dev), which is closer to
66% (sentence level).

We could not find this training/dev split mentioned in any other documentation
or papers related to the corpus.

Cleaning the data
-----------------

The last few lines of file 180-03.xml are not formatted correctly in the
final output; these were corrected manually.

Several entity types had too few (<20) instances and were removed. These were
changed as follows:

HEALTHPLAN -> O # 1 mention
URL -> O        # 2 mentions
FAX -> O        # 10 mentions
EMAIL -> O      # 5 mentions
DEVICE -> O     # 7 mentions
LOCATION_OTHER -> 0 # 17 mentions
BIOID -> IDNUM  # 1 mention

Remarks
-------

There are still some sentence segmentation errors in the CONLL-formated files.

Cite as
-------

If using the i2b2 2014 dataset, please cite as:

 - Stubbs A, Uzuner O. (2015). Annotating longitudinal clinical narratives for
   de-identification: The 2014 i2b2/UTHealth corpus
   (http://www.ncbi.nlm.nih.gov/pubmed/26319540.).
   J Biomed Inform. 2015 Aug 28. PII: S1532-0464(15)00182-3. DOI: 10.1016/j.jbi.2015.07.020.

 - Stubbs A, Kotfila C, Uzuner O. (2015). Automated systems for the
   de-identification of longitudinal clinical narratives: Overview of 2014
   i2b2/UTHealth shared task Track 1
   (http://www.ncbi.nlm.nih.gov/pubmed/26225918).
   J Biomed Inform. 2015 Jul 28. PII: S1532-0464(15)00117-3.
   DOI: 10.1016/j.jbi.2015.06.007.

