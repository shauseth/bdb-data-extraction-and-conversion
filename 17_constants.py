# SH-I

import pandas as pd

data = pd.read_csv('second-generation-6.csv')

sequences = data['Sequences'].values
seq_list = []

for x in sequences:

    y = x.split('\n')
    y = y[:-1]
    y.insert(0, y.pop())

    y_list = ['0 0 XX XX XX ' + y[0]]

    for i, item in enumerate(y[1:]): # gives index and element in list

        y_list.append(str(i + 1) + ' 0 XX OO NA ' + item)

    y_list = ['index mindex Primer Mod Nuc AA XX'] + y_list

    seq_list.append('\n'.join(y_list))

data['Sequences'] = seq_list

data.to_csv('second-generation-7.csv', index = False)
