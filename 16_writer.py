# SH-I

import pandas as pd

data = pd.read_csv('second-generation-3.csv')
library = pd.read_csv('library-tagged.csv')
target = pd.read_csv('target-tagged.csv')

lib_dict = dict(zip(library['LibraryID'].values, library['Library'].values))
tar_dict = dict(zip(target['TargetID'].values, target['Target'].values))

data['Library'] = data['LibraryID'].map(lib_dict)
data['Target'] = data['TargetID'].map(tar_dict)

for x in range(10):

    name = data.loc[x, 'FileName']
    seq = data.loc[x, 'Sequences']
    dat = data.loc[x, 'Date']
    lib = data.loc[x, 'Library']
    tar = data.loc[x, 'Target']
    ppr = data.loc[x, 'BriefDescription']
    aut = data.loc[x, 'Author']

    file = open(name, 'w')
    file.write('Dat - ' + dat + '\n' + '\n')
    file.write('Lib - ' + lib + '\n' + '\n')
    file.write('Mod - ' + 'No Modification' + '\n' + '\n')
    file.write('Tar - ' + tar + '\n' + '\n')
    file.write('PPr - ' + ppr + '\n' + '\n')
    file.write('Com - ' + '\n' + '\n')
    file.write('Own - ' + aut + '\n' + '\n')
    file.write('**********' + '\n')
    file.write(seq)

    file.close()
