import pandas as pd

library = pd.read_csv('library.csv')
mimoset = pd.read_csv('mimoset.csv') # parent
soc = pd.read_csv('soc.csv')
sotmc = pd.read_csv('sotmc.csv')
sottc = pd.read_csv('sottc.csv')
target = pd.read_csv('target.csv')
template = pd.read_csv('template.csv')

merged1 = pd.merge(mimoset, library, how = 'outer')
merged2 = pd.merge(merged1, target, how = 'outer')
merged3 = pd.merge(merged2, template, how = 'outer')
merged4 = pd.merge(merged3, sotmc, how = 'outer')
merged5 = pd.merge(merged4, sottc, how = 'outer')
final = pd.merge(merged5, soc, how = 'outer')

final["Modification"] = ""

subset = ['SubmissionDate','LibraryName', 'Modification',
           'TargetName', 'BriefDescription', 'SubmittedBy']

comp = [c for c in final.columns if c not in subset]

final = final[subset + comp]

final.rename(columns={'SubmissionDate':'Date', 'LibraryName':'Library', 'TargetName':'Target',
                      'BriefDescription':'Post-processing', 'SubmittedBy':'Owner'},
                      inplace=True)

final.to_csv('merged_4.csv')
