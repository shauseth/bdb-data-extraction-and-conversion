# SH-I

import pandas as pd

data = pd.read_csv('second-generation-4.csv')
names = pd.read_csv('names.csv')

# adds old names

old_name_dict = dict(zip(names['MimotopeSetID'].values, names['OldName'].values))

data['OldName'] = data['MimotopeSetID'].map(old_name_dict)
data['OldName'] = data['OldName'].fillna('deleted')

# adds new names

new_name_dict = dict(zip(names['MimotopeSetID'].values, names['NewName'].values))

data['NewName'] = data['MimotopeSetID'].map(new_name_dict)
data['NewName'] = data['NewName'].fillna('deleted')

# adds action

action_dict = dict(zip(names['MimotopeSetID'].values, names['Change'].values))

data['Action'] = data['MimotopeSetID'].map(action_dict)
data['Action'] = data['Action'].fillna('deleted')

print(data)
data.to_csv('second-generation-5.csv', index = False)
