MUC 6 Corpus
============

The MUC 6 corpus can be obtained from the LDC (LDC Catalog No. LDC2003T13)

In our experiments, only the "dryrun training" portion
of the MUC 6 corpus was used (more on this below).

Due to licensing restrictions we could not include the data here. Some notes
on how we processed the data are given below.

Parsing to CONLL-format
-----------------------

1. Set up a new python 2 virtualenv. Then pip install:

    - nltk 3.0.1 (it does not work with later versions)
    - nltk-contrib 3.2.5 (which was the latest version when we obtained it).

2. nltk_contrib/coref won't run out of the box, due to dependency issues and a
   couple errors. We had to edit the files api.py and muc.py in the coref
   directory.
   To fix api.py, comment out class HiddernMarkovModelChunkTaggerTransformI.

3. Copy the relevant MUC files into the nltk data directory. These are of the
   form (the number of xx's is arbitrary here):

        xxxx.ne.xx.sgm

   These files are in MUC-6/data/keys/dryrun-trng.NE-combined.key.v1.3.clean
   Be sure to copy the files to  <nltk data directory>/corpora/muc6

4. Activate the virtualenv. Then in Python run:

   from nltk_contrib.coref import muc
   muc.demo()

   This will save the corpus into CONLL format in the file
   muc6-conll-format.txt

Cleaning the data
-----------------

There are a few issues with the data. We fixed the following:

* A few cases of incorrect sentence segmentation.

* Commas incorrectly tokenized, eg . [course,] rather than [course] [,]

* Colons (:) also incorrectly tokenized; they should be on their own.

* Incorrect tokenization, such as [Mr] [.] [Smith]  This should rather be
  [Mr.] [Smith].  This was done with the following:
  - a.m , p.m
  - Co, Corp, Bros, Inc, Ltd, S.A, Pty, G.m.b.H, N.V (N.V. is Dutch for LLC), S.p.A (Italian)
  - CORP
  - Counting (lists), eg. [1] [.] -> [1.] , and [1] [)] -> [1)]
  - U.S, U.S.A, U.N, U.K, L.A
  - U.S.S.R
  - Month abbreviations (Jan, Feb, Aug, Sept, Oct, Nov, Dec)
  - No [as in number, eg. "No. 1"]
  - Mr, Mrs, Ms, Prof, Dr, Jr, Sr, Rep, Sen, Rev, St, Lt, Gov
  - People's initials (usually first or middle name)
  - US State abbreviations:
        - Calif
        - N.J
        - N.M
        - N.Y
        - N.C
        - N.H
        - R.I
        - Ky
        - Mass
        - [W.Va][.] -> [W.] [Va.]
        - Wash
        - Mich
        - Conn
        - DC
        - Ark
        - Pa
        - Va
        - Ind
        - Ariz
        - Miss
        - Fla
        - Del
        - Nev
        - Ore
        - Tenn
        - Mont
        - Ill
        - Ala
        - Wis
        - Ga
        - La
        - Mo
        - Vt
  - Others:
    J.C [in: J.C . PENNEY Co.]
    R.L [in Tucker Anthony & R.L . Day]
    J.P [in J.P . Morgan]
    J [in: J . Walter Thompson Co.]
    A.G [in: Siemens A.G .]
    C [Stanford C. Berstein]
    Cos [Equitable of Iowa Cos .]
    A.L [A.L . Williams]
    E.W [E.W . Scripps Co.]
    A [Alfred A. Knopf]
    D [D. Lazzaroni & Co.]
    J.L [J.L Henry ]
    W.N [W.N Whelen]
    T [T. Rowe Price ]
    C [C. Itoh]
    E [E. Guigal]
    E.C [E.C Television]
    A.C [A.C. Nielsen]
    L.P [WFRR L.P]
    H.N. & Frances C. Berger Foundation]
    F.W [F.W Dodge Group]
    E [Charles E. Simon]
    R.P. Scherer
    F.H. Faulding
    W.R. Grace

Removal of entities
-------------------

There were less than 20 TIME entities, so these were removed.

Train/test split
----------------

We used stratified_split.py to create a custom train/test split of the data:

TRAIN, TEST = write_new_split('MUC6', 1000, filedir, 'muc6', max_count = 2)

Some mistakes in the original annotation
-----------------------------------------

- "Nomura Research Institute." is labeled as an entity.

- Usually (but not always, see "Ms. Poore"), the title (Mr., Ms., etc) is not
contained in the named entity (unlike in say ACE 2005).

- "70 U.K. and international banks" [891102-0075.ne.v1.3.sgm]. Here
U.K. was unlabeled.

- In the Senate, Edward Kennedy (D., Mass) [891101-0115.ne.v1.3.sgm]. Here
"D" is marked as ORG. (Usually it isn't in MUC 6)

NOTE
----

* The way % and $ are parsed here: they are on different lines, eg. [50] [%]
  This is the correct way.
