# SH-I

import pandas as pd
import os
from collections import Counter

name = pd.read_csv('name_fixed.csv')

name_array = name['FileName'].values

name_list = []

for x in name_array:

    name_list.append(x)

counts = Counter(name_list)

for s, num in counts.items():

    if num > 1:

        for suffix in range(1, num + 1):

            name_list[name_list.index(s)] = s + '(' + str(suffix) + ')'

name['FileName'] = name_list

dict = dict(zip(name['MimotopeSetID'].values, name['FileName'].values))

for filename in os.listdir('.'):

    list = filename.split('_')

    id = list[0]

    if id in dict:

        os.rename(filename, dict[id])

        print(dict[id])
