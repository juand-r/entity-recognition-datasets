===============================
Datasets for Entity Recognition
===============================

This repository contains datasets from several domains
annotated with a variety of entity types, useful for entity recognition and
named entity recognition (NER) tasks.


**NOTE: I am no longer actively adding datasets to this list -- there are likely more NER datasets that have appeared since 2020. However, I am happy to add more datasets via issues or pull requests.**

Datasets for NER in English
===========================

.. |check| unicode:: 0x2714

The following table shows the list of datasets for English-language entity recognition (for a list of NER datasets in other languages, see below). The `data` directory
contains information on where to obtain those datasets which could not be shared
due to licensing restrictions, as well as code to convert them (if necessary)
to the CoNLL 2003 format. Links to NER corpora in other languages
are also listed below.

============== =============== ======================= =============================== ==================================
Dataset         Domain            License                 Reference                       Availablility
============== =============== ======================= =============================== ==================================
CONLL 2003      News               DUA                  Sang and Meulder, 2003          `Easy <https://github.com/patverga/torch-ner-nlp-from-scratch/tree/master/data/conll2003/>`_ `to <https://github.com/synalp/NER/tree/master/corpus/CoNLL-2003>`_ `find <https://github.com/glample/tagger/tree/master/dataset>`_
NIST-IEER       News               None                 NIST 1999 IE-ER                 `NLTK data <https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/ieer.zip>`_
MUC-6           News               LDC                  Grishman and Sundheim, 1996     `LDC 2003T13 <https://catalog.ldc.upenn.edu/LDC2003T13>`_
OntoNotes 5     Various            LDC                  Weischedel et al., 2013         `LDC 2013T19 <https://catalog.ldc.upenn.edu/LDC2013T19>`_
BBN             Various            LDC                  Weischedel and Brunstein, 2005    `LDC 2005T33 <https://catalog.ldc.upenn.edu/LDC2005T33>`_
GMB-1.0.0       Various            None                 Bos et al., 2017                `http://gmb.let.rug.nl/data.php <http://gmb.let.rug.nl/releases/gmb-1.0.0.zip>`_
GUM-3.1.0       Wiki               Several (*2)         Zeldes, 2016                    |check| Included here
wikigold        Wikipedia          CC-BY 4.0            Balasuriya et al., 2009         |check| Included here
Ritter          Twitter            None                 Ritter et al., 2011             `No split <https://github.com/aritter/twitter_nlp/blob/master/data/annotated/ner.txt>`_ , `Train/test/dev split <https://github.com/aritter/twitter_nlp/tree/master/data/annotated/wnut16/data>`_
BTC             Twitter            CC-BY 4.0            Derczynski et al., 2016         |check| Included here
WNUT17          Social media       CC-BY 4.0            Derczynski et al., 2017         |check| Included here
i2b2-2006       Medical            DUA                  Uzuner et al., 2007             `http://www.i2b2.org <https://www.i2b2.org/NLP/DataSets/Main.php>`_
i2b2-2014       Medical            DUA                  Stubbs et al., 2015             `http://www.i2b2.org <https://www.i2b2.org/NLP/DataSets/Main.php>`_
CADEC           Medical            CSIRO                Karimi et al., 2015             http://data.csiro.au/
AnEM            Anatomical         CC-BY-SA 3.0         Ohta et al., 2012               |check| Included here
MITRestaurant   Queries            None                 Liu et al., 2013a               `http://groups.csail.mit.edu/sls/ <https://groups.csail.mit.edu/sls/downloads/restaurant/>`_
MITMovie        Queries            None                 Liu et al., 2013b               `http://groups.csail.mit.edu/sls/ <https://groups.csail.mit.edu/sls/downloads/movie/>`_
MalwareTextDB   Malware            None                 Lim et al., 2017                `http://www.statnlp.org/ <http://www.statnlp.org/research/re/MalwareTextDB-1.0.zip>`_
re3d            Defense            Several (*1)         DSTL, 2017                      |check| Included here
SEC-filings     Finance            CC-BY 3.0            Alvarado et al., 2015           |check| Included here
Assembly        Robotics           X                    Costa et al., 2017              X
WikiNEuRal      Wikipedia          CC BY-SA-NC 4.0      Tedeschi et al., 2021           https://github.com/Babelscape/wikineural
MultiNERD       Wikipedia          CC BY-SA-NC 4.0      Tedeschi et al., 2022           https://github.com/Babelscape/multinerd
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

(2) GUM 3.1.0 comprises three datasets, with licenses CC-BY 3.0, CC-BY-SA 3.0 and
    CC-BY-NC-SA 3.0. The annotations are licensed under CC-BY 4.0.

More detailed license information for each dataset can be found in
the corresponding subdirectory.

Later ...
- Tabassum et al., Code and Named Entity Recognition in StackOverflow https://cocoxu.github.io/publications/ACL2020_stackoverflow_NER.pdf
- LitBank: https://github.com/dbamman/litbank (Bamman, Popat and Shen, An Annotated Dataset of Literary Entities, NAACL 2019)
- NNE: A Dataset for Nested Named Entity Recognition in English Newswire, 2019 https://github.com/nickyringland/nested_named_entities
- Mars Target Encyclopedia - LPSC abstracts labeled data set:  https://zenodo.org/record/1048419#.W5a2CBwnZhE
- Best Buy queries: https://www.kaggle.com/dataturks/best-buy-ecommerce-ner-dataset/home
- Resume entities for NER: https://www.kaggle.com/dataturks/resume-entities-for-ner/home
- FEW-NERD: A Few-shot Named Entity Recognition Dataset https://aclanthology.org/2021.acl-long.248/



Datasets for NER in other languages
===================================

Lexical Named Entity resources
------------------------------

- HeiNER: http://heiner.cl.uni-heidelberg.de/index.shtml
- NECKAr: https://event.ifi.uni-heidelberg.de/?page_id=532#Wikidata_NE_dataset

Code-Switching
--------------

- English-Spanish tweets (CALCS 2018): https://code-switching.github.io/2018/ ; https://code-switching.github.io/2018/files/spa-eng/Release.zip ; http://www.aclweb.org/anthology/W18-3219
- Arabic-Egyptian tweets (CALCS 2018): https://code-switching.github.io/2018/ ; https://code-switching.github.io/2018/files/msa-egy/ArabicTweetsTokenAssigner.zip ; http://www.aclweb.org/anthology/W18-3219
- Hindi-English social media text: https://github.com/SilentFlame/Named-Entity-Recognition ; http://aclweb.org/anthology/W18-2405
- EMNLP 2014 Shared Task - Code-Switched Tweets (Nepali-English, Spanish-English, Mandarin-English, Arabic-Arabic dialects): http://emnlp2014.org/workshops/CodeSwitch/call.html

German
------

- CoNLL 2003 (English, German): https://www.clips.uantwerpen.be/conll2003/ner/
- GermEval 2014: https://sites.google.com/site/germeval2014ner/data
- Tübingen Treebank of Written German (TüBa-D/Z): http://www.sfs.uni-tuebingen.de/en/ascl/resources/corpora/tueba-dz.html
- Europeana Newspapers (Dutch, French, German): https://github.com/EuropeanaNewspapers/ner-corpora ; http://lab.kb.nl/dataset/europeana-newspapers-ner#access
- German EUROPARL transcripts (subset): https://nlpado.de/~sebastian/software/ner_german.shtml
- Named Entity Model for German, Politics (NEMGP): https://www.thomas-zastrow.de/nlp/
- WikiNER: https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500
- WikiNEuRal: https://github.com/Babelscape/wikineural
- MultiNERD: https://github.com/Babelscape/multinerd
- DFKI SmartData Corpus (geo-entities): https://dfki-lt-re-group.bitbucket.io/smartdata-corpus/ (A German Corpus for Fine-Grained Named Entity Recognition and Relation Extraction of Traffic and Industry Events. Martin Schiersch, Veselina Mironova, Maximilian Schmitt, Philippe Thomas, Aleksandra Gabryszak, Leonhard Hennig. Proceedings of LREC, 2018)
- DBpedia abstract corpus (English, German, Dutch, French, Italian, Japanese): http://downloads.dbpedia.org/2015-04/ext/nlp/abstracts/
- DAWT dataset - Densely Annotated Wikipedia Texts across multiple languages (English, Spanish, French, Italian, German, Arabic): https://github.com/klout/opendata/tree/master/wiki_annotation
- Elena Leitner, Georg Rehm, Juli ́an Moreno-Schneider, A Dataset of German Legal Documents for Named Entity Recognition, LREC 2020: http://georg-re.hm/pdf/LREC-2020-Leitner-et-al-preprint.pdf ; Data: https://github.com/elenanereiss/Legal-Entity-Recognition

Dutch
-----

- CoNLL 2002 (Spanish, Dutch): https://www.clips.uantwerpen.be/conll2002/ner/
- Europeana Newspapers (Dutch, French, German): https://github.com/EuropeanaNewspapers/ner-corpora ; http://lab.kb.nl/dataset/europeana-newspapers-ner#access
- MEANTIME Corpus (Parallel corpus: English, Spanish, Italian, Dutch): http://www.newsreader-project.eu/results/data/wikinews/
- WikiNER: https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500
- WikiNEuRal: https://github.com/Babelscape/wikineural
- MultiNERD: https://github.com/Babelscape/multinerd
- DBpedia abstract corpus (English, German, Dutch, French, Italian, Japanese): http://downloads.dbpedia.org/2015-04/ext/nlp/abstracts/
- Dutch parliamentary documents 2015-2016, from 1848.nl (Jonkers, Named Entity Recognition on Dutch Parliamentary Documents using Frog, thesis, University of Amsterdam, 2016): https://github.com/Poezedoez/NER/blob/master/Code/data/lobby/golden_standard
- SONAR 1 - Desmet and Hoste, Fine-grained Dutch named entity recognition, 2014 (hierarchy of classes)
- Corpus-SONAR books and Corpus Gutenberg Dutch: http://blog.namescape.nl/?page_id=85 ; http://portal.clarin.nl/node/1940

Afrikaans
---------

- NCHLT Afrikaans Named Entity Annotated Corpus: https://repo.sadilar.org/handle/20.500.12185/299

Spanish
-------

- CoNLL 2002 (Spanish, Dutch): https://www.clips.uantwerpen.be/conll2002/ner/
- AnCora (Spanish, Catalan): http://clic.ub.edu/corpus/en
- DEFT Spanish Treebank (LDC2018T01): https://catalog.ldc.upenn.edu/LDC2018T01
- PANACEA (LAB): http://panacea-lr.eu/en/info-for-researchers/data-sets/dependency-parsed-corpora/dependency-lab-es
- PANACEA (ENV): http://panacea-lr.eu/en/info-for-researchers/data-sets/dependency-parsed-corpora/dependency-env-es
- MEANTIME Corpus (Parallel corpus: English, Spanish, Italian, Dutch): http://www.newsreader-project.eu/results/data/wikinews/
- ACE 2007 (Spanish and Arabic): https://catalog.ldc.upenn.edu/LDC2014T18
- WikiNER: https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500
- WikiNEuRal: https://github.com/Babelscape/wikineural
- MultiNERD: https://github.com/Babelscape/multinerd
- http://www.grupolys.org/~marcos/pub/lrec16.tar.bz2 (used in "Incorporating Lexico-semantic Heuristics into Coreference Resolution Sieves for Named Entity Recognition at Document-level")
- Multilingual corpora with coreferential annotation of person entities (Spanish, Galician, Portuguese): http://gramatica.usc.es/~marcos/lrec.tar.bz2 
- DrugSemantics Gold Standard (Moreno et al., DrugSemantics: A corpus for Named Entity Recognition in Spanish Summaries of Product Characteristics, 2017): https://data.mendeley.com/datasets/fwc7jrc5jr/1
- DBpedia abstract corpus (English, German, Dutch, French, Italian, Japanese): http://downloads.dbpedia.org/2015-04/ext/nlp/abstracts/
- DAWT dataset - Densely Annotated Wikipedia Texts across multiple languages (English, Spanish, French, Italian, German, Arabic): https://github.com/klout/opendata/tree/master/wiki_annotation
- CANTEMIST (CANcer TExt Mining Shared Task – tumor named entity recognition) - named entity recognition of a critical type of concept related to cancer, namely tumor morphology in Spanish medical texts: https://temu.bsc.es/cantemist/

Catalan
-------

- AnCora (Spanish, Catalan): http://clic.ub.edu/corpus/en

Galician
--------

- Galician NER corpus: https://gramatica.usc.es/~marcos/resources/corpus_gal_nec.txt.gz
- Multilingual corpora with coreferential annotation of person entities (Spanish, Galician, Portuguese): http://gramatica.usc.es/~marcos/lrec.tar.bz2 

Basque
------

- Basque Named Entities Corpus (EIEC): http://ixa.eus/node/4486?language=en
- Basque Disambiguated Named Entities Corpus (EDIEC): http://ixa.si.ehu.es/node/4485?language=en
- Egunkaria 2000 corpus (383 newswire texts), mentioned in http://qtleap.eu/wp-content/uploads/2014/04/QTLEAP-2013-D5.1.pdf

Portuguese
----------

- HAREM: https://www.linguateca.pt/aval_conjunta/HAREM/harem_ing.html
- CINTIL corpus: http://cintil.ul.pt/cintilfeatures.html#corpus
- WikiNER: https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500
- WikiNEuRal: https://github.com/Babelscape/wikineural
- MultiNERD: https://github.com/Babelscape/multinerd
- Multilingual corpora with coreferential annotation of person entities (Spanish, Galician, Portuguese): http://gramatica.usc.es/~marcos/lrec.tar.bz2 
- Bosque 8.0 EAGLES format: https://gramatica.usc.es/~marcos/resources/corpora_FLpt.tgz
- LeNER-Br (Brazilian legal documents): https://cic.unb.br/~teodecampos/LeNER-Br/
- Paramopama: a Brazilian-Portuguese Corpus for Named Entity Recognition

French
------

- ESTER: http://catalogue.elra.info/en-us/repository/browse/ELRA-S0241/
- ESTER 2: http://catalogue.elra.info/en-us/repository/browse/ELRA-S0338/
- ETAPE: http://catalogue.elra.info/en-us/repository/browse/ELRA-E0046/
- Europeana Newspapers (Dutch, French, German): https://github.com/EuropeanaNewspapers/ner-corpora ; http://lab.kb.nl/dataset/europeana-newspapers-ner#access
- QUAERO French Medical Corpus: https://quaerofrenchmed.limsi.fr/
- Quaero Broadcast News Extended Named Entity Corpus: http://catalog.elra.info/en-us/repository/browse/ELRA-S0349/
- Quaero Old Press Extended Named Entity corpus: http://catalog.elra.info/en-us/repository/browse/ELRA-W0073/ 
- WikiNER: https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500
- WikiNEuRal: https://github.com/Babelscape/wikineural
- MultiNERD: https://github.com/Babelscape/multinerd
- DBpedia abstract corpus (English, German, Dutch, French, Italian, Japanese): http://downloads.dbpedia.org/2015-04/ext/nlp/abstracts/
- DAWT dataset - Densely Annotated Wikipedia Texts across multiple languages (English, Spanish, French, Italian, German, Arabic): https://github.com/klout/opendata/tree/master/wiki_annotation
- CAp 2017 - (Twitter data), Lopez et al., CAp 2017 challenge: Twitter Named Entity Recognition, 2017: http://cap2017.imag.fr/competition.html

Italian
-------

- KIND: https://github.com/dhfbk/KIND
- Evalita: http://www.evalita.it/2009/tasks/entity
- MEANTIME Corpus (Parallel corpus: English, Spanish, Italian, Dutch): http://www.newsreader-project.eu/results/data/wikinews/
- PANACEA (ENV): http://panacea-lr.eu/en/info-for-researchers/data-sets/dependency-parsed-corpora/dependency-env-it
- PANACEA (LAB): http://panacea-lr.eu/en/info-for-researchers/data-sets/dependency-parsed-corpora/dependency-lab-it
- WikiNER: https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500
- WikiNEuRal: https://github.com/Babelscape/wikineural
- MultiNERD: https://github.com/Babelscape/multinerd
- DBpedia abstract corpus (English, German, Dutch, French, Italian, Japanese): http://downloads.dbpedia.org/2015-04/ext/nlp/abstracts/
- DAWT dataset - Densely Annotated Wikipedia Texts across multiple languages (English, Spanish, French, Italian, German, Arabic): https://github.com/klout/opendata/tree/master/wiki_annotation

Romanian
--------

- RONEC (Dumitrescu and Avram, Introducing RONEC - the Romanian Named Entity Corpus. LREC 2020). Paper: https://arxiv.org/pdf/1909.01247.pdf Data: https://github.com/dumitrescustefan/ronec
- Romanian journalistic corpus (ROCO): http://metashare.elda.org/repository/browse/romanian-journalistic-corpus-roco/038baa80dc7311e5aa0b00237df3e3583781d7c0f2084057aa018a2d63d987e9/
- Romanian Balanced Corpus (ROMBAC): http://metashare.elda.org/repository/browse/romanian-balanced-corpus-rombac/0a7dd85edc7311e5aa0b00237df3e35873a0d662435d42dd94fba48c29dc0065/

Greek
-----

- PANACEA (ENV): http://panacea-lr.eu/en/info-for-researchers/data-sets/dependency-parsed-corpora/dependency-env-el
- PANACEA (LAB): http://panacea-lr.eu/en/info-for-researchers/data-sets/dependency-parsed-corpora/dependency-lab-el

Hungarian
---------

- Hungarian Named Entity Corpora: http://rgai.inf.u-szeged.hu/index.php?lang=en&page=corpus_ne
- hunNERwiki: http://hlt.sztaki.hu/resources/hunnerwiki.html
- NYTK: https://github.com/nytud/NYTK-NerKor

Czech
-----

- Czech Named Entity Corpus: http://ufal.mff.cuni.cz/cnec
- BSNLP 2017 (Croatian, Czech, Polish, Russian, Slovak, Slovene, Ukrainian): http://bsnlp-2017.cs.helsinki.fi/shared_task_results.html
- CzEng 1.0 (Parallel corpus: Czech-English): http://ufal.mff.cuni.cz/czeng/czeng10

Polish
------

- The Polish Sejm Corpus: http://clip.ipipan.waw.pl/PSC
- BSNLP 2017 (Croatian, Czech, Polish, Russian, Slovak, Slovene, Ukrainian): http://bsnlp-2017.cs.helsinki.fi/shared_task_results.html
- Polish Coreference Corpus: http://zil.ipipan.waw.pl/PolishCoreferenceCorpus
- WikiNER: https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500
- WikiNEuRal: https://github.com/Babelscape/wikineural
- MultiNERD: https://github.com/Babelscape/multinerd
- Corpus of Economic News (CEN Corpus): http://www.nlp.pwr.wroc.pl/narzedzia-i-zasoby/zasoby/cen
- KPWr (Korpus Języka Polskiego Politechniki Wrocławskiej/Polish Corpus of Wrocław University of Technology): http://plwordnet.pwr.wroc.pl/index.php?option=com_content&view=article&id=35&Itemid=181&lang=pl ; http://plwordnet.pwr.wroc.pl/attachments/article/35/kpwr-1.1.7z (Broda et al., KPWr: Towards a Free Corpus of Polish, 2012)
- NKJP: http://clip.ipipan.waw.pl/NationalCorpusOfPolish?action=AttachFile&do=view&target=NKJP-PodkorpusMilionowy-1.2.tar.gz

Croatian
--------

- hr500k 1.0:  http://hdl.handle.net/11356/1183
- BSNLP 2017 (Croatian, Czech, Polish, Russian, Slovak, Slovene, Ukrainian): http://bsnlp-2017.cs.helsinki.fi/shared_task_results.html
- ReLDI-NormTagNER-hr (Croatian tweets): http://hdl.handle.net/11356/1170

Slovak
------

- BSNLP 2017 (Croatian, Czech, Polish, Russian, Slovak, Slovene, Ukrainian): http://bsnlp-2017.cs.helsinki.fi/shared_task_results.html
- Slovak Categorized News Corpus: https://nlp.web.tuke.sk/pages/categorizednews

Slovene
-------

- BSNLP 2017 (Croatian, Czech, Polish, Russian, Slovak, Slovene, Ukrainian): http://bsnlp-2017.cs.helsinki.fi/shared_task_results.html
- ssj500k:  http://www.slovenscina.eu/tehnologije/ucni-korpus ; http://eng.slovenscina.eu/tehnologije/ucni-korpus ; https://www.clarin.si/repository/xmlui/handle/11356/1029 ;  NOTE: for v 2.2 see: http://hdl.handle.net/11356/1210
- Slovene news: http://zitnik.si/mediawiki/index.php?title=Datasets#Slovene_news ; http://zitnik.si/mediawiki/images/7/7d/Rtvslo_dec2011.tsv ; http://zitnik.si/mediawiki/images/5/5e/Rtvslo_dec2011_v2.tsv
- Janes-Tag 2.0 (social media text) https://www.clarin.si/repository/xmlui/handle/11356/1123 ; see also: Fišer et al., The Janes project: language resources and tools for Slovene user generated content, 2018.

Ukrainian
---------

- BSNLP 2017 (Croatian, Czech, Polish, Russian, Slovak, Slovene, Ukrainian): http://bsnlp-2017.cs.helsinki.fi/shared_task_results.html
- Ukrainian Brown NER Corpus: https://github.com/lang-uk/ner-uk ; http://lang.org.ua/en/corpora/

Serbian
-------

- SETimes.SR - http://hdl.handle.net/11356/1200
- Named Entities evaluation corpus for Serbian: http://www.korpus.matf.bg.ac.rs/SrpNEval/
- ReLDI-NormTagNER-sr (Serbian tweets): http://hdl.handle.net/11356/1171

Bulgarian
---------

- BulTreeBank (BTB)

Icelandic
---------

- MIM-GOLD-NER (Ingólfsdóttir, Svanhvít Lilja, Sigurjón Þorsteinsson, and Hrafn Loftsson. "Towards High Accuracy Named Entity Recognition for Icelandic." Proceedings of the 22nd Nordic Conference on Computational Linguistics. 2019): http://www.malfong.is/index.php?pg=mim_gold_ner

Danish
------

- DaNE: Hvingelby et al., [DaNE: A Named Entity Resource for Danish.](http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.565.pdf), LREC 2020: https://github.com/alexandrainst/danlp/
- Danish Propbank (DPB): http://catalog.elra.info/en-us/repository/browse/ELRA-W0117/
- Arboretum treebank: http://catalog.elra.info/en-us/repository/browse/ELRA-W0084/

Norwegian
---------

- Bjarte Johansen, Named-Entity Recognition for Norwegian, Proceedings of the 22nd Nordic Conference on Computational Linguistics. 2019 (https://www.aclweb.org/anthology/W19-6123.pdf) Data: https://github.com/ljos/navnkjenner
- Fredrik Jørgensen et al., NorNE: Annotating Named Entities for Norwegian, 2019 (https://arxiv.org/pdf/1911.12146.pdf). Data: https://github.com/ltgoslo/norne/ ; https://www.nb.no/sprakbanken/show?serial=oai%3Anb.no%3Asbr-49

Swedish
-------

- Stockholm Internet Corpus: https://www.ling.su.se/english/nlp/corpora-and-resources/sic
- SUC 3.0: https://spraakbanken.gu.se/eng/resource/suc3
- Swedish manually annotated NER: https://github.com/klintan/swedish-ner-corpus/
- Medical wikipedia data (Almgren et al., Named Entity Recognition in Swedish Health Records with Character-Based Deep Bidirectional LSTMs, 2016): https://github.com/olofmogren/biomedical-ner-data-swedish  

Finnish
-------

- data sets for Finnish Named Entity Recoginition: https://github.com/mpsilfve/finer-data
- Turku NER corpus: https://github.com/TurkuNLP/turku-ner-corpus

Estonian
--------

- Estonian NER corpus: https://metashare.ut.ee/repository/browse/estonian-ner-corpus/88d030c0acde11e2a6e4005056b40024f1def472ed254e77a8952e1003d9f81e/

Latvian and Lithuanian
----------------------

- https://github.com/accurat-toolkit/TildeNER/tree/master/TEST (Pinnis,  	Latvian and Lithuanian Named Entity Recognition with TildeNER, LREC 2012)
- Training data for the LV Tagger: https://github.com/PeterisP/LVTagger/tree/master/NerTrainingData

Turkish
-------

- K̈ucuk and Can, A Tweet Dataset Annotated for Named Entity Recognition and Stance Detection, 2019: https://github.com/dkucuk/Tweet-Dataset-NER-SD
- K̈ucuk et al., Named Entity Recognition on Turkish Tweets: http://optima.jrc.it/Resources/2014_JRC_Twitter_TR_NER-dataset.zip
- English/Turkish Wikipedia Named-Entity Recognition and Text Categorization Dataset (http://arxiv.org/abs/1702.02363): https://data.mendeley.com/datasets/cdcztymf4k/1

Kazakh
------

- KazNERD: https://arxiv.org/pdf/2111.13419.pdf, https://github.com/IS2AI/KazNERD

Uyghur
------

- Uyghur Named Entity Relation corpus: https://github.com/kaharjan/UyNeRel (Abiderexiti et al., Annotation Schemes for Constructing Uyghur Named Entity Relation Corpus. IALP 2016)

Armenian
--------

- pioNER (gold-standard and silver-standard datasets): https://github.com/ispras-texterra/pioner (Ghukasyan et al., pioNER: Datasets and Baselines for Armenian Named Entity Recognition, 2018)

Coptic
------

- The Coptic Universal Dependency Treebank: https://github.com/UniversalDependencies/UD_Coptic-Scriptorium/tree/dev (see also https://copticscriptorium.org/treebank.html). This contains 46,000 tokens of nested (non-)named and Wikified entities from Sahidic Coptic texts.

Amharic
-------

- SAY corpus (see "Named entity recognition for Amharic using deep learning"): https://github.com/geezorg/data/tree/master/amharic/tagged/nmsu-say ; http://data.geez.org/

Arabic
------

- AQMAR Arabic Wikipedia Named Entity Corpus: http://www.cs.cmu.edu/~ark/ArabicNER/
- NE3L named entities Arabic corpus (Arabic, Chinese, Russian): http://catalog.elra.info/en-us/repository/browse/ELRA-W0078/
- REFLEX Entity Translation (Parallel corpus: English, Arabic, Chinese): https://catalog.ldc.upenn.edu/LDC2009T11
- ANERCorp: http://users.dsic.upv.es/~ybenajiba/downloads.html (See also: http://alias-i.com/lingpipe/demos/tutorial/ne/read-me.html)
- ACE 2003 (English, Chinese, Arabic): https://catalog.ldc.upenn.edu/LDC2004T09
- ACE 2004 (English, Chinese, Arabic): https://catalog.ldc.upenn.edu/LDC2005T09
- ACE 2005 (English, Chinese, Arabic): https://catalog.ldc.upenn.edu/LDC2006T06
- ACE 2007 (Spanish and Arabic): https://catalog.ldc.upenn.edu/LDC2014T18
- OntoNotes 5 (English, Arabic, Chinese): https://catalog.ldc.upenn.edu/LDC2013T19
- DAWT dataset - Densely Annotated Wikipedia Texts across multiple languages (English, Spanish, French, Italian, German, Arabic): https://github.com/klout/opendata/tree/master/wiki_annotation


Persian
-------

- ArmanPersoNERCorpus: http://islrn.org/resources/399-379-640-828-6/ ; https://github.com/HaniehP/PersianNER

Sindhi
------

- SiNER: https://aclanthology.org/2020.lrec-1.361/, https://github.com/AliWazir/SiNER-dataset

Urdu
----

- IJCNLP 2008 SSEAL: http://ltrc.iiit.ac.in/ner-ssea-08/index.cgi?topic=5
- UNER Dataset (Khan et al., Named Entity Dataset for Urdu Named Entity Recognition Task, 2016). Available at http://www.iiu.edu.pk/?page_id=5181
- MK-PUCIT: https://www.dropbox.com/sh/1ivw7ykm2tugg94/AAB9t5wnN7FynESpo7TjJW8la ; see: Kanwal et al., Urdu Named Entity Recognition: Corpus Generationand Deep Learning Applications, 2019 


Hindi
-----
- HiNER: https://github.com/cfiltnlp/HiNER
- Hindi Health Dataset: https://www.kaggle.com/aijain/hindi-health-dataset/home
- FIRE 2015, ESM-IL (English, Hindi, Tamil, Malayalam) : http://au-kbc.org/nlp/ESM-FIRE2015/#traincorpus
- FIRE NER 2013 (English, Hindi, Tamil, Malayalam, Bengali): http://au-kbc.org/nlp/NER-FIRE2013/
- IJCNLP 2008 SSEAL: http://ltrc.iiit.ac.in/ner-ssea-08/index.cgi?topic=5

Bengali
-------

- FIRE NER 2013 (English, Hindi, Tamil, Malayalam, Bengali): http://au-kbc.org/nlp/NER-FIRE2013/
- IJCNLP 2008 SSEAL: http://ltrc.iiit.ac.in/ner-ssea-08/index.cgi?topic=5
- Bengali-NER: https://github.com/Rifat1493/Bengali-NER, https://ieeexplore.ieee.org/document/8944804
- NER-Bangla: https://github.com/MISabic/NER-Bangla-Dataset, https://content.iospress.com/articles/journal-of-intelligent-and-fuzzy-systems/ifs179349

Telugu
------

- NER_Telugu: https://github.com/anikethjr/NER_Telugu
- IJCNLP 2008 SSEAL: http://ltrc.iiit.ac.in/ner-ssea-08/index.cgi?topic=5
- Named Entity Annotated Corpora for Telugu: http://www.tdil-dc.in/index.php?option=com_download&task=showresourceDetails&toolid=982&lang=en

Maithili
--------

- The first named entity recognizer in Maithili: Resource creation and system development: https://content.iospress.com/articles/journal-of-intelligent-and-fuzzy-systems/ifs210051

Nepali
------

- EverestNER: https://journals.flvc.org/FLAIRS/article/view/130725, https://github.com/nowalab/everest-ner

Marathi
-------

- Named Entity Annotated Corpora for Marathi: http://www.tdil-dc.in/index.php?option=com_download&task=showresourceDetails&toolid=979&lang=en
- L3Cube MahaNER: https://arxiv.org/abs/2204.06029  https://github.com/l3cube-pune/MarathiNLP

Punjabi
-------

- Named Entity Annotated Corpora for Punjabi: http://www.tdil-dc.in/index.php?option=com_download&task=showresourceDetails&toolid=980&lang=en

Tamil
-----

- FIRE 2015, ESM-IL (English, Hindi, Tamil, Malayalam) : http://au-kbc.org/nlp/ESM-FIRE2015/#traincorpus
- FIRE NER 2013 (English, Hindi, Tamil, Malayalam, Bengali): http://au-kbc.org/nlp/NER-FIRE2013/

Malayalam
---------

- FIRE 2015, ESM-IL (English, Hindi, Tamil, Malayalam) : http://au-kbc.org/nlp/ESM-FIRE2015/#traincorpus
- FIRE NER 2013 (English, Hindi, Tamil, Malayalam, Bengali): http://au-kbc.org/nlp/NER-FIRE2013/

Oriya/Odia
----------

- IJCNLP 2008 SSEAL: http://ltrc.iiit.ac.in/ner-ssea-08/index.cgi?topic=5

Sinhala/Sinhalese
-----------------

- LORELEI (LDC2018E57)

Thai
----

- thai-named-entity-recognition-data: https://github.com/PyThaiNLP/thai-named-entity-recognition-data
- Thai named entity corpora: http://pioneer.chula.ac.th/~awirote/resources/corpora--data.html ; http://pioneer.chula.ac.th/~awirote/Data-Nutcha.zip ; http://pioneer.chula.ac.th/~awirote/Data-Sasiwimon.zip ; http://pioneer.chula.ac.th/~awirote/Data-Nattadaporn.zip
- LST20: https://huggingface.co/datasets/lst20 ; https://arxiv.org/abs/2008.05055
- Thai-NNER: https://github.com/vistec-AI/Thai-NNER , https://aclanthology.org/2022.findings-acl.116

Indonesian
----------

- IDENTIC: http://metashare.elda.org/repository/browse/identic/fed3fada7ef111e5aa3b001dd8b71c66c98eee36eabd42f18ffd9a95da9104cc/
- https://github.com/yohanesgultom/nlp-experiments/tree/master/data/ner

Vietnamese
----------

- VLSP 2016: http://vlsp.org.vn/resources-vlsp2016 ; https://github.com/undertheseanlp/ner
- VLSP 2018: http://vlsp.org.vn/resources-vlsp2018 ; https://github.com/undertheseanlp/ner
- PhoNER_COVID19: https://github.com/VinAIResearch/PhoNER_COVID19

Japanese
--------

- IREX: https://nlp.cs.nyu.edu/irex/Package/
- MET-2 (Japanese, Chinese): https://www-nlpir.nist.gov/related_projects/muc/
- BCCWJ Basic NE corpus: https://sites.google.com/site/projectnextnlpne/en (Iwakura et al., Constructing a Japanese Basic Named Entity Corpus of Various Genres, NEWS 2016)
- DBpedia abstract corpus (English, German, Dutch, French, Italian, Japanese): http://downloads.dbpedia.org/2015-04/ext/nlp/abstracts/
- Data from: Mai et al., An Empirical Study on Fine-Grained Named Entity Recognition, COLING 2018 (English, Japanese): https://fgner.alt.ai/duc/ene/testsets/comp/
- Wikipedia NER Corpus: https://github.com/stockmarkteam/ner-wikipedia-dataset
- WikiANN: https://elisa-ie.github.io/wikiann/  
- GSD: Conversion of the UD GSD dataset to named entities by Megagon Labs  https://github.com/megagonlabs/UD_Japanese-GSD
- KWDLC: Kyoto University Web Document Leads Corpus   https://nlp.ist.i.kyoto-u.ac.jp/EN/index.php?KWDLC  https://github.com/ku-nlp/KWDLC  https://nagisa.readthedocs.io/en/latest/tutorial_ner.html

Korean
------

- National Institute of Korean Language (ROK) - NER Corpus: https://github.com/digitalprk/KoreaNER ; https://ithub.korean.go.kr/user/total/referenceView.do?boardSeq=5&articleSeq=118&boardGb=T&isInsUpd&boardType=CORPUS
- KMOU NER - https://github.com/kmounlp/NER
- Korean Language Understanding Evaluation - KLUE NER - https://klue-benchmark.com/tasks/69/overview/description
- https://github.com/songys/entity
- HLCT 2016 corpus, with updates - https://github.com/machinereading/KoreanNERCorpus

Chinese
-------

- ACE 2003 (English, Chinese, Arabic): https://catalog.ldc.upenn.edu/LDC2004T09
- ACE 2004 (English, Chinese, Arabic): https://catalog.ldc.upenn.edu/LDC2005T09
- ACE 2005 (English, Chinese, Arabic): https://catalog.ldc.upenn.edu/LDC2006T06
- OntoNotes 5 (English, Arabic, Chinese): https://catalog.ldc.upenn.edu/LDC2013T19
- MET-2 (Japanese, Chinese): https://www-nlpir.nist.gov/related_projects/muc/
- REFLEX Entity Translation (Parallel corpus: English, Arabic, Chinese): https://catalog.ldc.upenn.edu/LDC2009T11
- NE3L named entities Chinese corpus (Arabic, Chinese, Russian): http://catalogue.elra.info/en-us/repository/browse/ELRA-W0079/
- Original Short-Message Data Collation I in Chinese (named entities): http://catalog.elra.info/en-us/repository/browse/ELRA-W0045_04/ 
- Original Short-Message Data Collation II in Chinese (named entities): http://catalog.elra.info/en-us/repository/browse/ELRA-W0045_08/
- ERE DEFT Corpora (Parallel corpus: English, Chinese): Mott et al., Parallel Chinese-English Entities, Relations and Events Corpora, 2016 (LDC2015E78 , LDC2014E114)
- Chinese Weibo: DEFT ERE style annotations for named and nominal mentions on Chinese social media (Weibo): https://github.com/hltcoe/golden-horse


Russian
-------

- BSNLP 2017 (Croatian, Czech, Polish, Russian, Slovak, Slovene, Ukrainian): http://bsnlp-2017.cs.helsinki.fi/shared_task_results.html
- NE3L named entities Russian corpus (Arabic, Chinese, Russian): https://catalog.elra.info/en-us/repository/browse/ELRA-W0080/
- WikiNER: https://figshare.com/articles/Learning_multilingual_named_entity_recognition_from_Wikipedia/5462500
- WikiNEuRal: https://github.com/Babelscape/wikineural
- MultiNERD: https://github.com/Babelscape/multinerd
- factRuEval-2016: https://github.com/dialogue-evaluation/factRuEval-2016
- RuREBus 2020 (Russian Relation Extraction for Business) corpus https://github.com/dialogue-evaluation/RuREBus

Yoruba
------

- GV-Yorùbá-NER. Data: https://github.com/ajesujoba/YorubaTwi-Embedding/tree/master/Yoruba/Yor%C3%B9b%C3%A1-NER ; Data statement: https://drive.google.com/file/d/177xu-O2FTJ7VJQ-0ohCWjVd1qu61Tvml/view Paper: Jesujoba O Alabi, Kwabena Amponsah-Kaakyire, David I Adelani, and Cristina Espãna-Bonet. Massive vs. curated word embeddings for low-resourced languages. the case of Yorùbá and Twi. In LREC, 2020 (https://arxiv.org/abs/1912.02481)

Swahili
-------

- Helsinki Corpus of Swahili 2.0 (HCS 2.0) Annotated Version: http://metashare.csc.fi/repository/browse/helsinki-corpus-of-swahili-20-hcs-20-annotated-version/232c1910b9eb11e5915e005056be118e59fb2e920f1f4c0cafc94915fc6f5cac/ See: Shah et al., 2010. SYNERGY: A Named Entity Recognition System for Resource-scarce Languages such as Swahili using Online Machine Translation

isiNdebele
----------

- NCHLT isiNdebele Named Entity Annotated Corpus: https://repo.sadilar.org/handle/20.500.12185/306

Xhosa
-----

- NCHLT isiXhosa Named Entity Annotated Corpus: https://repo.sadilar.org/handle/20.500.12185/312

Zulu
----

- NCHLT isiZulu Named Entity Annotated Corpus: https://repo.sadilar.org/handle/20.500.12185/319

Sepedi
------

- NCHLT Sepedi Named Entity Annotated Corpus: https://repo.sadilar.org/handle/20.500.12185/328

Sesotho
-------

- NCHLT Sesotho Named Entity Annotated Corpus: https://repo.sadilar.org/handle/20.500.12185/334

Setswana 
--------

- NCHLT Setswana Named Entity Annotated Corpus: https://repo.sadilar.org/handle/20.500.12185/341

Siswati
-------
 
- NCHLT Siswati Named Entity Annotated Corpus: https://repo.sadilar.org/handle/20.500.12185/346

Venda
-----

- NCHLT Tshivenda Named Entity Annotated Corpus: https://repo.sadilar.org/handle/20.500.12185/355

Xitsonga
--------

- NCHLT Xitsonga Named Entity Annotated Corpus: https://repo.sadilar.org/handle/20.500.12185/362

Latin
-----

- Herodotos Project: https://github.com/alexerdmann/Herodotos_Project_Annotation


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
Available at: https://github.com/GateNLP/broad_twitter_corpus
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
