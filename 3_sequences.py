import pandas as pd

mimoset = pd.read_csv('mimoset_modified.csv')
seq1 = pd.DataFrame()

ID = [i+1 for i in range(len(mimoset))]
primer = ["XX" for i in range(len(mimoset))]
mod = ["XX" for i in range(len(mimoset))]
nuc = ["XX" for i in range(len(mimoset))]

seq1['ID'] = ID
seq1['Mod'] = mod
seq1['Nuc'] = nuc

seq2 = mimoset['Sequences']

final = pd.concat([seq1, seq2], axis=1)

final.rename(columns={'Sequences':'AA'}, inplace=True)

final.to_csv('sequences.csv', index = False)
