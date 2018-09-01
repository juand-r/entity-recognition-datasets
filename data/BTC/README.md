# Broad Twitter Corpus

This is the Broad Twitter corpus, a dataset of tweets collected over stratified times, places and social uses. The goal is to represent a broad range of activities, giving a dataset more representative of the language used in this hardest of social media formats to process. Further, the BTC is annotated for named entities. The entities and the crowd annotations are all provided with the corpus, as well as (where possible) the raw twitter JSON.

You can find the full description of the corpus at http://www.aclweb.org/anthology/C16-1111

## Use

The BTC is released as CC-BY 4.0. If you use this data, you should cite the accompanying paper:

  Broad Twitter Corpus: A Diverse Named Entity Recognition Resource. Leon Derczynski, Kalina Bontcheva, and Ian Roberts. Proceedings of COLING, pages 1169-1179 2016.

The paper's full open access, and can be found easily; here's one link: http://www.aclweb.org/anthology/C16-1111

## Sections

Section|Region|Collection period|Description|Annotators|Tweet count
---|---|---|---|---|---
A | UK| 2012.01| General collection |Expert| 1000
B |UK |2012.01-02 |Non-directed tweets |Expert |2000
E |Global| 2014.07| Related to MH17 disaster| Crowd & expert |200
F |Stratified |2009-2014| Twitterati |Crowd & expert |2000
G |Stratified| 2011-2014| Mainstream news| Crowd & expert| 2351
H |Non-UK| 2014 |General collection |Crowd & expert |2000

## Format

The data is provided in up to three formats: CoNLL, JSON, and GATE XML. JSON is the richest of these. For the JSON, we generally provide the raw tweet JSON from twitter, augmented with fields describing token offsets, token texts, and token labels. In some cases (sections A and B), some tweets have been deleted, and so only the rehydrateable tweets are provided. In these cases, the GATE XML annotations are canonical. The ".no-labels.json" files are the raw result from the Twitter API with no additional information. Not all sections are available in all formats with annotations, but this will improve as we re-export the corpus into new formats and update data. At a minimum, CONLL format data is given for all sections.

Plain annotation data from CrowdFlower is also provided, in the .annotations/ directories. This is to assist future users working on crowdsourcing, e.g. on predicting the utility of a worker judgment.

As well as CONLL-format annotations, for each document in each section, there's a .json file. This file has one record per line, each record corresponding to a document. At a minimum, every record will have a "tokens" and a "labels" list, which are the tokenized text and matching BIO labels for person, organization and location entities. There may be other data in the case that the whole tweet from the Twitter API was available at distribution time.  Additionally, there may be an "annotation offsets" parameter that aligns the token annotations to the plain text in the tweet (often in the top-level "text" object, if the tweet's there).
