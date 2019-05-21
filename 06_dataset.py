import pandas as pd

pd.options.mode.chained_assignment = None

library = pd.read_csv('library.csv')
mimoset = pd.read_csv('mimoset.csv')
target = pd.read_csv('target.csv')

merged = pd.merge(mimoset, library, how = 'outer')
table = pd.merge(merged, target, how = 'outer')

data = table[['MimotopeSetID','Reference','LibraryName', 'LibraryFrom',
              'LibrarySeqLength', 'LibraryComplexity', 'LibraryTiter',
              'LibraryRandomness', 'LibraryCodingScheme', 'LibraryTopology',
              'LibraryComments', 'TargetName', 'TargetSynonyms', 'TargetSource',
              'TargetType', 'TargetSequence', 'TargetStructure', 'TargetComments']]

data = data.sort_values('MimotopeSetID')
data.reset_index(drop=True, inplace=True)

data = data.fillna('unknown')

dataframe = pd.DataFrame()

dataframe = data[['MimotopeSetID', 'Reference']]

dataframe['Library'] = '#LibraryName ' + data['LibraryName'] + ' #LibraryFrom ' + \
                  data['LibraryFrom'] + ' #LibrarySeqLength ' + \
                  data['LibrarySeqLength'] + ' #LibraryComplexity ' + \
                  data['LibraryComplexity'] + ' #LibraryTiter ' + \
                  data['LibraryTiter'] + ' #LibraryRandomness ' + \
                  data['LibraryRandomness'] + ' #LibraryCodingScheme ' + \
                  data['LibraryCodingScheme'] + ' #LibraryTopology ' + \
                  data['LibraryTopology'] + ' #LibraryComments ' + \
                  data['LibraryComments']

dataframe['Target'] = '#TargetName ' + data['TargetName'] + ' #TargetSynonyms ' + \
                  data['TargetSynonyms'] + ' #TargetSource ' + \
                  data['TargetSource'] + ' #TargetType ' + \
                  data['TargetType'] + ' #TargetSequence ' + \
                  data['TargetSequence'] + ' #TargetStructure ' + \
                  data['TargetStructure'] + ' #TargetComments ' + \
                  data['TargetComments']

print(dataframe)

dataframe.to_csv('dataframe.csv', index = False)
