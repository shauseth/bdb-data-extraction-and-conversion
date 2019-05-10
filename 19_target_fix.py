# SH-I

import pandas as pd

target = pd.read_csv('new_target.csv')
target = target.fillna('unknown')

target['Target'] = '#TargetName ' + target['TargetName'] + ' #TargetSynonyms ' + \
                  target['TargetSynonyms'] + ' #TargetSource ' + \
                  target['TargetSource'] + ' #TargetType ' + \
                  target['TargetType'] + ' #TargetSequence ' + \
                  target['TargetSequence'] + ' #TargetStructure ' + \
                  target['TargetStructure'] + ' #TargetComments ' + \
                  target['TargetComments']

target = target[['TargetID', 'Target']]

print(target)

target.to_csv('target-tagged.csv', index = False)
