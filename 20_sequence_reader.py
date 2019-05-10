# SH-I

import pandas as pd
from collections import Counter

data = pd.read_csv('second-generation-6.csv')
library = pd.read_csv('library-tagged.csv')
target = pd.read_csv('target-tagged.csv')

# analyse sequences

sequences = data['Sequences'].values

# takes sequence and gives dictionary

def read_seq(sequence):

    seq = sequence.split('\n')
    seq = seq[:-1]

    total = seq[-1]
    seq = seq[:-1]

    total = total.split(' ')
    total = int(total[-1])

    seq_list = []
    val_list = []

    for x in seq:

        x = x.split(' ')
        seq_list.append(x[0])

        if x[-1]:

            val_list.append(int(x[-1]))

        elif x[-2]:

            val_list.append(int(x[-2]))

    seq_dict = dict(zip(seq_list, val_list))

    seq_dict['Total'] = total

    return seq_dict

for seq in sequences:

    print('Output:')
    print(read_seq(seq))
