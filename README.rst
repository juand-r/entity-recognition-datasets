===============================
Datasets for Entity Recognition
===============================

This repository contains English-language datasets from several domains
annotated with a variety of entity types, useful for entity recognition and
named entity recognition (NER) tasks.

Datasets
========

.. |check| unicode:: 0x2714

The following table shows the list of datasets. The `data` directory also
contains information on where to obtain those datasets which could not be shared
due to licensing restrictions, as well as code to convert them (if necessary)
to the CoNLL 2003 format.

============== =============== ======================= =============================== ==================================
Dataset         Domain            License                 Reference                       Availablility
============== =============== ======================= =============================== ==================================
CONLL 2003      News               DUA (Reuters)        Sang and Meulder, 2003          Easy to find
NIST-IEER       News               None                 NIST 1999 IE-ER                 `NLTK data <https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/ieer.zip>`_
MUC-6           News               LDC                  Grishman and Sundheim, 1996     `LDC 2003T13 <https://catalog.ldc.upenn.edu/LDC2003T13>`_
OntoNotes 5     Various            LDC                  Weischedel et al., 2013         `LDC 2013T19 <https://catalog.ldc.upenn.edu/LDC2013T19>`_
BBN             Various            LDC                  Weischedel & Brunstein, 2005    `LDC 2005T33 <https://catalog.ldc.upenn.edu/LDC2005T33>`_
GMB-1.0.0       Various            None                 Bos et al., 2017                `http://gmb.let.rug.nl/data.php <http://gmb.let.rug.nl/releases/gmb-1.0.0.zip>`_
GUM             Wiki               Several (*2)         Zeldes, 2016                    |check| Included here
wikigold        Wikipedia          CC-BY 4.0            Balasuriya et al., 2009         |check| Included here
Ritter          Twitter            None                 Ritter et al., 2011             |check| Included here
WNUT17          Twitter            CC-BY 4.0            Derczynski et al., 2017         |check| Included here
BTC             Twitter            CC-BY 4.0            Derczynski et al., 2016         |check| Included here
i2b2-2006       Medical            DUA                  Uzuner et al., 2007             `http://www.i2b2.org <https://www.i2b2.org/NLP/DataSets/Main.php>`_
i2b2-2014       Medical            DUA                  Stubbs et al., 2015             `http://www.i2b2.org <https://www.i2b2.org/NLP/DataSets/Main.php>`_
CADEC           Medical            CSIRO                Karimi et al., 2015             http://data.csiro.au/
AnEM            Anatomical         CC-BY-SA 3.0         Ohta et al., 2012               |check| Included here
MITRestaurant   Queries            None                 Liu et al., 2013a               `http://groups.csail.mit.edu/sls/ <https://groups.csail.mit.edu/sls/downloads/restaurant/>`_
MITMovie        Queries            None                 Liu et al., 2013b               `http://groups.csail.mit.edu/sls/ <https://groups.csail.mit.edu/sls/downloads/movie/>`_
MalwareTextDB   Malware            None                 Lim et al., 2017                http://www.statnlp.org/
re3d            Defense            Several (*1)         DSTL, 2017                      |check| Included here
SEC-filings     Finance            CC-BY 3.0            Alvarado et al., 2015           |check| Included here
Assembly        Robotics           X                    Costa et al., 2017              X
============== =============== ======================= =============================== ==================================

Licenses
========

Notes on licenses:

(1) re3d ("Relationship and Entity Extraction Evaluation Dataset") contains
several datasets, with different licenses. These are:

  - CC-BY-SA 3.0 (Wikipedia dataset)
  - CC BY-NC 3.0 (BBC_Online dataset)
  - CC BY 3.0 AU (Australian_Department_of_Foreign_Affairs dataset)
  - public domain (US_State_Department dataset, CENTCOM dataset)
  - UK Open Government Licence v3.0 (UK_Government dataset)
  - Delegation_of_the_European_Union_to_Syria: see
    https://eeas.europa.eu/delegations/syria/8157/legal-notice_en

(2) GUM comprises three datasets, with licenses CC-BY 3.0, CC-BY-SA 3.0 and
    CC-BY-NC-SA 3.0. The annotations are licensed under CC-BY 4.0.

More detailed license information for each dataset can be found in
the corresponding subdirectory.

NER in other languages
======================

German
------

- CoNLL 2003 (German): https://www.clips.uantwerpen.be/conll2003/ner/
- GermEval 2014: https://sites.google.com/site/germeval2014ner/data
- Tübingen Treebank of Written German (TüBa-D/Z): http://www.sfs.uni-tuebingen.de/en/ascl/resources/corpora/tueba-dz.html
- Europeana Newspapers (Dutch, French, German): https://github.com/EuropeanaNewspapers/ner-corpora

Dutch
-----

- CoNLL 2002 (Spanish, Dutch): https://www.clips.uantwerpen.be/conll2002/ner/
- Europeana Newspapers (Dutch, French, German): https://github.com/EuropeanaNewspapers/ner-corpora

Spanish
-------

- CoNLL 2002 (Spanish, Dutch): https://www.clips.uantwerpen.be/conll2002/ner/
- AnCora (Spanish, Catalan): http://clic.ub.edu/corpus/en

Portuguese
----------

- HAREM: https://www.linguateca.pt/aval_conjunta/HAREM/harem_ing.html

French
------

- ESTER: http://catalogue.elra.info/en-us/repository/browse/ELRA-S0241/
- Europeana Newspapers (Dutch, French, German): https://github.com/EuropeanaNewspapers/ner-corpora

Italian
-------

- Evalita: http://www.evalita.it/2009/tasks/entity

Hungarian
---------

- Hungarian Named Entity Corpora: http://rgai.inf.u-szeged.hu/index.php?lang=en&page=corpus_ne
- hunNERwiki: http://hlt.sztaki.hu/resources/hunnerwiki.html

Czech
-----

Czech Named Entity Corpus: http://ufal.mff.cuni.cz/cnec

Swedish
-------

- Stockholm Internet Corpus: https://www.ling.su.se/english/nlp/corpora-and-resources/sic


A long list can be found here: http://damien.nouvels.net/resourcesen/corpora.html

References
==========

[Alvarado et al., 2015] Alvarado, Julio Cesar Salinas, Karin Verspoor,
and Timothy Baldwin. Domain adaption of named entity recognition to support
credit risk assessment. In Proceedings of the Australasian Language Technology
Association Workshop 2015, pp. 84-90. 2015.
Accessed: August 2018.

[Balasuriya et al., 2009] Balasuriya, Dominic, Nicky Ringland, Joel Nothman,
Tara Murphy, and James R. Curran. Named entity recognition in wikipedia. In
Proceedings of the 2009 Workshop on The People's Web Meets NLP: Collaboratively
Constructed Semantic Resources, pp. 10-18. Association for Computational
Linguistics, 2009

[Bos et al., 2017] Bos, Johan, Valerio Basile, Kilian Evang,
Noortje J. Venhuizen, and Johannes Bjerva. The Groningen meaning bank.
In Handbook of linguistic annotation, pp. 463-496. Springer, Dordrecht, 2017.

[Derczynski et al., 2016] Derczynski, Leon, Kalina Bontcheva, and Ian Roberts.
Broad twitter corpus: A diverse named entity recognition resource. In
Proceedings of COLING 2016, the 26th International Conference on Computational
Linguistics: Technical Papers, pp. 1169-1179. 2016.
Available from: https://github.com/GateNLP/broad_twitter_corpus
Accessed: August 2018.

[Derczynski et al., 2017] Leon Derczynski, Eric Nichols, Marieke van Erp,
Nut Limsopatham (2017) Results of the WNUT2017 Shared Task on Novel and
Emerging Entity Recognition, in Proceedings of the 3rd Workshop on Noisy,
User-generated Text.
Available at: https://noisy-text.github.io/2017/emerging-rare-entities.html

[DSTL, 2017] Defence Science and Technology Laboratory. 2017. Relationship and
Entity Extraction Evaluation Dataset.  https://github.com/dstl/re3d.
Accessed: January 2018.

[Grishman and Sundheim, 1996] Ralph Grishman and Beth Sundheim. 1996.
Message understanding conference- 6: A brief history. In COLING 1996 Volume 1:
The 16th International Conference on Computational Linguistics.

[Karimi et al., 2015] Sarvnaz Karimi, Alejandro Metke-Jimenez, Madonna Kemp,
and Chen Wang. 2015. Cadec: A corpus of adverse drug event annotations.
Journal of biomedical informatics, 55:73-81. Available at https://data.csiro.au
Accessed: November 2017.

[Lim et al., 2017] Lim, Swee Kiat, Aldrian Obaja Muis, Wei Lu, and
Chen Hui Ong. MalwareTextDB: A database for annotated malware articles.
In Proceedings of the 55th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), vol. 1, pp. 1557-1567. 2017.

[Liu et al., 2013a] Jingjing Liu, Panupong Pasupat, Scott Cyphers, and
Jim Glass. 2013. Asgard: A portable architecture for multilingual dialogue
systems. In Acoustics, Speech and Signal Processing (ICASSP), 2013 IEEE
International Conference on, pages 8386-8390. IEEE.
Available at https://groups.csail.mit.edu/sls/downloads/restaurant/
Accessed: January 2018

[Liu et al., 2013b] Jingjing Liu, Panupong Pasupat, Yining Wang, Scott Cyphers,
and Jim Glass. 2013. Query understanding enhanced by hierarchical parsing
structures. In Automatic Speech Recognition and Understanding (ASRU),
2013 IEEE Workshop on, pages 72-77. IEEE.
Available at https://groups.csail.mit.edu/sls/downloads/movie/
We used the trivia10k13 portion. Accessed: January 2018

[NIST, 1999 IE-ER] NIST. 1999. Information Extraction - Entity Recognition
Evaluation. http://www.nist.gov/speech/tests/ieer/er_99/er_99.htm.
The newswire development test data only (included in the NLTK package).

[Ohta et al., 2012] Tomoko Ohta, Sampo Pyysalo, Jun'ichi Tsujii and Sophia
Ananiadou. 2012. Open-domain Anatomical Entity Mention Detection. In
Proceedings of ACL 2012 Workshop on Detecting Structure in Scholarly Discourse
(DSSD), pp. 27-36.
Available at: http://www.nactem.ac.uk/anatomy/ and
https://github.com/openbiocorpora/anem Accessed: November 2017.

[Ritter et al., 2011] Alan Ritter, Sam Clark, Mausam, and Oren Etzioni. 2011.
Named entity recognition in tweets: An experimental study. In Proceedings of
the 2011 Conference on Empirical Methods in Natural Language Processing,
pages 1524-1534, Edinburgh, Scotland, UK., July. Association for Computational
Linguistics.
Accessed January 2018.

[Sang and Meulder, 2003] Erik F. Tjong Kim Sang and Fien De Meulder. 2003.
Introduction to the CoNLL-2003 shared task: Languageindependent named entity
recognition. In Proceedings of the Seventh Conference on Natural Language
Learning at HLT-NAACL 2003.

[Stubbs et al., 2015] Amber Stubbs and Ozlem Uzuner. 2015. Annotating
longitudinal clinical narratives for de-identification: The 2014 i2b2/UTHealth
corpus. Journal of biomedical informatics, 58:S20-S29. Available at
https://www.i2b2.org/NLP/DataSets/ Accessed: February 2018.

[Uzuner et al., 2007] Ozlem Uzuner, Yuan Luo, and Peter Szolovits. 2007.
Evaluating the state-of-the-art in automatic de-identification. Journal of the
American Medical Informatics Association, 14(5):550-563. Available at
https://www.i2b2.org/NLP/DataSets/ Accessed: February 2018.

[Weischedel and Brunstein, 2005] Ralph Weischedel and Ada Brunstein. 2005.
BBN pronoun coreference and entity type corpus. Linguistic Data Consortium,
Philadelphia.

[Weischedel et al., 2013] Weischedel, Ralph, Martha Palmer, Mitchell Marcus,
Eduard Hovy, Sameer Pradhan, Lance Ramshaw, Nianwen Xue et al. Ontonotes
release 5.0 ldc2013t19. Linguistic Data Consortium, Philadelphia, PA (2013).

[Zeldes, 2017] Amir Zeldes. 2017. The GUM corpus: creating multilayer
resources in the classroom. Language Resources and Evaluation, 51(3):581-612.
Available at https://github.com/amir-zeldes/gum/tree/master/coref/tsv/
Accessed: November 2017.
