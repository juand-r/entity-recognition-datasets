# Fix label mismatch: NUMEX that should be TIMEX:
sed -i '194s/NUMEX/TIMEX/' original_BBN_dataset/data/WSJtypes-subtypes/wsj00c.qa

# Fix ampersand issue: & -> %amp;
sed -i 's/&amp;/TTEMP/g' original_BBN_dataset/data/WSJtypes-subtypes/*
sed -i 's/&/&amp;/g' original_BBN_dataset/data/WSJtypes-subtypes/*
sed -i 's/TTEMP/\&amp;/g' original_BBN_dataset/data/WSJtypes-subtypes/*

# Fix broken or missing  <ROOT> and </ROOT>:
python rootadd.py

