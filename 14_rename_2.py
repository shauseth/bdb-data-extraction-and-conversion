# SH-I

import pandas as pd
import os

name = pd.read_csv('second-generation-2.csv')

ID_list = []

for x in name['MimotopeSetID'].values:

    ID_list.append(str(x))

name['MimotopeSetID'] = ID_list

dict = dict(zip(name['MimotopeSetID'].values, name['FileName'].values))

for filename in os.listdir('.'):

    list = filename.split('_')

    id = list[0]

    if id in dict:

        os.rename(filename, dict[id])

        print(dict[id])
