import pandas as pd

unique = pd.read_csv('unique.csv')
date = pd.DataFrame()

dates = unique['Date'].values
dateIDs = []

def dateID(date):

    date = date.split(' ')

    return ''.join(date)

for x in dates:

    if len(dateID(x)) == 9:

        dateIDs.append(dateID(x))

    elif len(dateID(x)) == 7:

        dateIDs.append(dateID(x) + 'XX')

    elif len(dateID(x)) == 4:

        dateIDs.append(dateID(x) + 'XXXX')

date['DateID'] = dateIDs
date['Date'] = unique['Date']

date.to_csv('date.csv', index = False)

print(date)
