WNUT 17 Emerging Entities Dataset
=================================

The is the dataset for the WNUT 17 Emerging Entities task.  It contains text
from Twitter, Stack Overflow responses, YouTube comments, and Reddit comments.

This was downloaded from:

http://noisy-text.github.io/2017/emerging-rare-entities.html

Specifically, the following (train, dev, test) files:

http://noisy-text.github.io/2017/files/wnut17train.conll
http://noisy-text.github.io/2017/files/emerging.dev.conll
http://noisy-text.github.io/2017/files/emerging.test.annotated

The same data can also be downloaded from:

https://github.com/leondz/emerging_entities_17

(The files were identical.) For more information about this dataset, see:

http://noisy-text.github.io/2017/files/README.md

and the following paper:

Leon Derczynski, Eric Nichols, Marieke van Erp, Nut Limsopatham (2017)
"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition",
in Proceedings of the 3rd Workshop on Noisy, User-generated Text

Annotation guidelines
---------------------

See http://noisy-text.github.io/2017/files/

See also
--------

The main site has links to papers for the conference.
Also, see the related site for WNUT 2016.

Data Clearning
==============

The following minor changes were made:

1. Removed the trailing whitespaces from wnut17train.conll
2. Replaced \u201c' (starting quotes ") with " (in both dev and test files)
3. Replaced ending quotes " with " (dev and test files)
4. The dev file cannot be read because of "<feff>" Byte Order Mark (BOM)
   character. They were found with /[\uFEFF] and removed.
5. Fixed the following in file emerging.dev.conll:
   I-creative-work -> B-creative-work on line 1674 ("Turn")

The files emerging.dev.conll, emerging.test.annotated and  wnut17train.conll
are in CONLL-format/data


License
-------

This data is distributed under the [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

If you use this data, please cite the relevant paper:

Leon Derczynski, Eric Nichols, Marieke van Erp, Nut Limsopatham; 2017.
Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition.
In Proceedings of the Workshop on Noisy, User-generated Text, at EMNLP.
(http://noisy-text.github.io/2017/pdf/WNUT18.pdf)


