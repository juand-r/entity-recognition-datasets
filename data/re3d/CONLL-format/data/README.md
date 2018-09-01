This directory is for the train and test split of the re3d data.

To produce the train/test split used in the paper, run the following
in Python 2 from within the src directory:

```
import stratified_split as s
filedir = '../data/re3d/CONLL-format/data'
TR, TE = s.write_new_split('re3d',200,filedir,'re3d',max_count=2)
```

This will create subdirectories `train` and `test`.

