re3d in CONLL format
====================

This dataset is based on the re3d dataset, downloaded in January 2018 from

https://github.com/dstl/re3d

The following changes were made:

- Tokenization and minor cleaning
- Labels for entities with a confidence score less than 0.5 were removed.
- Whenever entities overlapped, only the entity with the largest span was kept.
- The data was converted to CONLL 2003 format.

More information about the content, licensing and modifications of the corpus
is given below.

Note: re3d stands for "Relationship and Entity Extraction Evaluation Dataset"
(see https://github.com/dstl/baleen/wiki/Available-Corpora)

About this corpus
-----------------

The github project (https://github.com/dstl/re3d) README states:

"This dataset was the output of a project carried out by Aleph Insights and
Committed Software on behalf of the Defence Science and Technology Laboratory
(Dstl). The project aimed to create a 'gold standard' dataset that could be
used to train and validate machine learning approaches to natural language
processing (NLP); specifically focusing on entity and relationship extraction
relevant to somebody operating in the role of a defence and security
intelligence analyst. The dataset was therefore constructed using documents
and structured schemas that were relevant to the defence and security analysis
domain."

And:

"The dataset comprised task-specific documents focused on the topic of the
conflict in Syria and Iraq;
The dataset included a range of source and document types, which had differing
levels of relevance to the overall ‘topic' of the dataset and possessed
differing entity densities (i.e. some documents containing a high concentration
of instances with others containing a lower concentration)"

Cleaning
--------

Fixed the following unicode issue: need the entity text and document
text to match but there are cases where e.g. it is \u201c in the document raw
text but ' in the entity name.

In CENTCOM/documents.json:
- line 8, file _id: 6874F49C56340E2BD65BF958916C97AE
  Col. John “J.D.” Dorrian ->  Col. John 'J.D.' Dorrian
- line 19, file _id: E9035FF1D0DA74A11674C82688C05C51
  Richard \"Tex\" Coe -> Richard 'Tex' Coe

Conversion: ldjson to Brat Standoff
-----------------------------------

1. First converted from ldjson to the brat standoff annotation format.
   See the re3d_to_bratann.py script in the utils directory.

   Note: The original dataset included a confidence score for each entity.
   We only kept the entities with score >= 0.5.

2. More cleaning:
   - Removed line 17 ( T1  DocumentReference 339 362  the Book of Revelation)
   from Wikipedia/FD93899C448B33796DBBB7BBFEEFA3A6.ann
   (it is repeated, and includes an unnecessary space).

Conversion: Brat Standoff to CONLL
----------------------------------

   Used the standoff2conll script from here:

   https://github.com/spyysalo/standoff2conll

   This converts from brat standoff annotation format to CONLL format.
   The .ann and .txt files must be in the same directory with nothing else
   in that directory.

   Example usage:

    python standoff2conll.py ../../data/bratann/Wikipedia/GROUPED/FD93899C448B33796DBBB7BBFEEFA3A6 > ../../data/conll/Wikipedia/FD93899C448B33796DBBB7BBFEEFA3A6.conll


   Note: In the event of overlapping entities, standoff2conll chooses the
   entities with maximum span.

More cleaning
-------------

    - Incorrect word segmentations for "U.S." and "U.K." fixed
    - Incorrect segmentation for "Züblin", in file
      Wikipedia/ 2ED27E1CBF9EFDEF369E721DC948D2F4.conll
    - Sentence segmentation errors:
      Fixed Wikipedia/FD93899C448B33796DBBB7BBFEEFA3A6.txt , line 61
    - Tokenization errors, "a.m":
      CENTCOM/E9035FF1D0DA74A11674C82688C05C51
    - Nov.:
      CENTCOM/
      E9035FF1D0DA74A11674C82688C05C51
      F7AC57DBBAD0284C8C0DE6566B9B5C29
      8BC6B4D334BC5607D97A1BA18854B513
      B2E5F55F5D7E31B291D9F76E8E4AC75D
    - Dec:
      CENTCOM/
      FEB7BC61C9765C9859F46B9B634F039F
      E19357552CAE0E45EE364E60A317AC59
      D52939C747F4DB8D1ECF6D415559ADA0
      8BC6B4D334BC5607D97A1BA18854B513
      6874F49C56340E2BD65BF958916C97AE
      482C10613016D2F430C464B2D13A8F41
      28829CF80D445874061C5948E6A3751D
    - Oct:
      CENTCOM/D52939C747F4DB8D1ECF6D415559ADA0
    - Jan:
      CENTCOM/
      F5B5E86320A4E95E92A7EA2FB8E8B484
      76957901E4278B498901454FA209CFFA
      6B183780227A18218A12E917A5BC8654
      5FBCC6E1D5B4B2A699196670789C6B0B
      26CC32861EF7D38FBAE9CABAFC7487E1
    - TITLES:
      - Spc:
        CENTCOM/1B05F2376ED66CA9FFEB00BE752C16DC.conll
      - Dr:
        US_State_Department/E1526BBD89FAB8E7914B3CF5867666CC
      - Lt:
        CENTCOM/F7AC57DBBAD0284C8C0DE6566B9B5C29
        CENTCOM/B2E5F55F5D7E31B291D9F76E8E4AC75D
        CENTCOM/6874F49C56340E2BD65BF958916C97AE
      - Gen:
        CENTCOM/E9035FF1D0DA74A11674C82688C05C51
        CENTCOM/D21D5CC3C9BEF5BF1D44976154E580A5
        CENTCOM/68A04D0D3111DBD88DE961B5727ADFA4
      - Brig:
        CENTCOM/E9035FF1D0DA74A11674C82688C05C51
      - Maj.:
        CENTCOM/D21D5CC3C9BEF5BF1D44976154E580A5
      - Col:
        CENTCOM/
        FEB7BC61C9765C9859F46B9B634F039F
        E9035FF1D0DA74A11674C82688C05C51
        E50B8563BB8395102D95333699FF73A3
        6874F49C56340E2BD65BF958916C97AE
      - Capt:
        CENTCOM/E9035FF1D0DA74A11674C82688C05C51
        CENTCOM/E19357552CAE0E45EE364E60A317AC59
        CENTCOM/D52939C747F4DB8D1ECF6D415559ADA0
      - Sgt:
        CENTCOM/1B05F2376ED66CA9FFEB00BE752C16DC


Eliminating categories with few labels
--------------------------------------

The following categories had only 13 instances or less in the corpus, and so
were elimiated:

CommsIdentifier (4 mentions):

    ./US_State_Department/F669C19A4C3DB410BBEC57ECC5DC62B1.conll:150:@	B-CommsIdentifier
    ./CENTCOM/E9035FF1D0DA74A11674C82688C05C51.conll:134:888	B-CommsIdentifier
    ./CENTCOM/5FBCC6E1D5B4B2A699196670789C6B0B.conll:92:910	B-CommsIdentifier
    ./BBC_Online/A0302EA7B1BDE005835BC09ECBF2930A.conll:1033:@	B-CommsIdentifier

Frequency (3 mentions):

    ./Wikipedia/B7CAC5946BE12615BA4815FFE0FE4C54.conll:154:64	B-Frequency
    ./Wikipedia/B7CAC5946BE12615BA4815FFE0FE4C54.conll:162:12130	B-Frequency
    ./Wikipedia/B7CAC5946BE12615BA4815FFE0FE4C54.conll:192:12	B-Frequency

Vehicle (13 mentions):

    ./CENTCOM/E50B8563BB8395102D95333699FF73A3.conll:292:the	B-Vehicle
    ./CENTCOM/26CC32861EF7D38FBAE9CABAFC7487E1.conll:203:excavators	B-Vehicle
    ./CENTCOM/26CC32861EF7D38FBAE9CABAFC7487E1.conll:290:vehicles	B-Vehicle
    ./CENTCOM/26CC32861EF7D38FBAE9CABAFC7487E1.conll:432:a	B-Vehicle
    ./CENTCOM/26CC32861EF7D38FBAE9CABAFC7487E1.conll:455:vehicles	B-Vehicle
    ./CENTCOM/8BC6B4D334BC5607D97A1BA18854B513.conll:147:vehicles	B-Vehicle
    ./CENTCOM/6B183780227A18218A12E917A5BC8654.conll:102:a	B-Vehicle
    ./CENTCOM/6B183780227A18218A12E917A5BC8654.conll:173:oil	B-Vehicle
    ./CENTCOM/6B183780227A18218A12E917A5BC8654.conll:183:an	B-Vehicle
    ./CENTCOM/6B183780227A18218A12E917A5BC8654.conll:237:vehicles	B-Vehicle
    ./CENTCOM/6B183780227A18218A12E917A5BC8654.conll:263:a	B-Vehicle
    ./CENTCOM/76957901E4278B498901454FA209CFFA.conll:29:vehicles	B-Vehicle
    ./BBC_Online/AEBFCD2500E5B57C7C416020C270EA5A.conll:399:a	B-Vehicle

Train/Test split
----------------

There wasn't a standard test/train split so we created one using the Python
script stratified_split.py.  This can be done via:

TRAIN, TEST = write_new_split('re3d', 200, filedir, 're3d', max_count = 2)

TODO
----

Some foreign (especially Arabic) people and place names may be incorrectly
segmented as well.

Licences
--------

Each part of the dataset has its own license. For license information, see the
LICENSE file in each subdirectory.
