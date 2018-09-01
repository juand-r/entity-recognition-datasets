Downloaded from
---------------

https://groups.csail.mit.edu/sls/downloads/movie/

More information:
https://groups.csail.mit.edu/sls/downloads/

According to their website, the 'eng' files are simple queries, while the
trivial10k13 are made up of more complex queries.

We used the trivial10k13 portion.

Remarks
-------

I'm not sure why they use a different tag set for
eng and for trivia10k13. Some of the entities seem to
overlap:

eng         trivia10k13
 ----------------------
ACTOR           Actor
CHARACTER       Character_Name
DIRECTOR        Director
GENRE           Genre
PLOT            Plot
YEAR            Year
SONG            Soundtrack
 --------------------------
REVIEW          Opinion (?)

Only in eng:
- RATINGS_AVERAGE
- RATING
- TITLE
- TRAILER

Only in trivial10k13:
-Award
-Origin
-Quote
-Relationship

Note  -- RATING and Opinion are somewhat different
      -- Opinion and REVIEW seem similar, but check again (?)
