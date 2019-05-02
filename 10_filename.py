import pandas as pd

pd.options.mode.chained_assignment = None

dataframe = pd.read_csv('dataframe.csv')
unique = pd.read_csv('unique.csv')
mimoset = pd.read_csv('mimoset.csv')

merged = pd.merge(dataframe, unique, on = 'Reference')
merged = merged.drop_duplicates()

brief = mimoset[['MimotopeSetID', 'BriefDescription']]
brief['MimotopeSetID'] = brief['MimotopeSetID'].astype(float)
brief['MimotopeSetID'] = brief['MimotopeSetID'].astype(str)

final = pd.merge(merged, brief, on = 'MimotopeSetID', how = 'left')

dat = pd.read_csv('table/date.csv')
lib = pd.read_csv('table/library.csv')
ppr = pd.read_csv('table/post-processing.csv')
tar = pd.read_csv('table/target.csv')
usr = pd.read_csv('table/user.csv')

dat_d = dict(zip(dat['Date'].values, dat['DateID'].values))
lib_d = dict(zip(lib['Library'].values, lib['LibraryID'].values))
ppr_d = dict(zip(ppr['Post-processing'].values, ppr['PPID'].values))
tar_d = dict(zip(tar['Target'].values, tar['TargetID'].values))
usr_d = dict(zip(usr['User'].values, usr['UserID'].values))

final["DateID"] = final["Date"].map(dat_d)
final["DateID"] = final["DateID"].fillna('unknownXX')
final["LibraryID"] = final["Library"].map(lib_d)
final["LibraryID"] = final["LibraryID"].fillna('XXXXXXX')
final["PPID"] = final["BriefDescription"].map(ppr_d)
final["PPID"] = final["PPID"].fillna('XXXX')
final["TargetID"] = final["Target"].map(tar_d)
final["TargetID"] = final["TargetID"].fillna('xxxx')
final["UserID"] = final["Author"].map(usr_d)
final["UserID"] = final["UserID"].fillna('XXXX')

lib_list = final['LibraryID'].values
list = []

for x in lib_list:

    list.append(str(x)[:7])

final['LibraryID'] = list

final['FileName'] = final['DateID'] + '-' + final['LibraryID'] + 'OO' + final['TargetID'] + final['PPID'] + '-' + final['UserID']

name = final[['MimotopeSetID', 'FileName']]

name.to_csv('name.csv', index = False)

print(name)
