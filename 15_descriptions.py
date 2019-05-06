# SH-I

import pandas as pd
import os

data = pd.read_csv('second-generation-2.csv')

id_list = []
seq_list = []

for filename in os.listdir('.'):

    if filename == 'desc.py':

        pass

    elif filename == 'second-generation-2.csv':

        pass

    else:

        # get IDs

        split = filename.split('_')
        id = split[0]
        id_list.append(int(id))

        # get sequences

        file = open(filename, 'r')
        seq = file.read()
        seq_list.append(seq)
        file.close()

dict = dict(zip(id_list, seq_list))

data['Sequences'] = data['MimotopeSetID'].map(dict)

print(data)

data.to_csv('second-generation-3.csv', index = False)
