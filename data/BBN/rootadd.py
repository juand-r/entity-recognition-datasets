import os
DIR = 'original_BBN_dataset/data/WSJtypes-subtypes/'

filenames = os.listdir(DIR)

for filename in filenames:
    with open(DIR + filename, 'r') as f:
        d = f.read()

    if d[0:6] != '<ROOT>':
        d = '<ROOT>' + d

    if d[-10:] == '\r\n</ROOT\r\n':
        d = d[:-10] + '\r\n</ROOT>\r\n'

    if d[-10:] == '\r\n</DOC>\r\n':
        d = d + '</ROOT>\r\n'

    with open(DIR + filename, 'w') as f:
        f.write(d)
