# SH-I

import pandas as pd

name = pd.read_csv('name.csv')
names = name['FileName'].values

name_list = []

for x in range(len(names)):

    n = names[x].split('-')

    date = n[0]

    if date == 'unknownXX':

        date = '00000000'

    elif len(date) == 8:

        if date[0:4] == '????':

            date = '0000' + date[4:8]

        elif date[4:8] == 'XXXX':

            date = date[0:4] + '0000'

        elif date[6:8] == 'XX':

            date = date[0:6] + '00'

    elif len(date) == 9:

        if date[7:9] == 'XX':

            date = date[0:7] + '00'

        if date[4:7] == 'Jan':

            date = date[0:4] + '01' + date[7:9]

        elif date[4:7] == 'Feb':

            date = date[0:4] + '02' + date[7:9]

        elif date[4:7] == 'Mar':

            date = date[0:4] + '03' + date[7:9]

        elif date[4:7] == 'Apr':

            date = date[0:4] + '04' + date[7:9]

        elif date[4:7] == 'May':

            date = date[0:4] + '05' + date[7:9]

        elif date[4:7] == 'Jun':

            date = date[0:4] + '06' + date[7:9]

        elif date[4:7] == 'Jul':

            date = date[0:4] + '07' + date[7:9]

        elif date[4:7] == 'Aug':

            date = date[0:4] + '08' + date[7:9]

        elif date[4:7] == 'Sep':

            date = date[0:4] + '09' + date[7:9]

        elif date[4:7] == 'Oct':

            date = date[0:4] + '10' + date[7:9]

        elif date[4:7] == 'Nov':

            date = date[0:4] + '11' + date[7:9]

        elif date[4:7] == 'Dec':

            date = date[0:4] + '12' + date[7:9]

    if date[4:8] == 'XXXX':

        date = date[0:4] + '0000'

    name_list.append(date + '-' + n[1] + '-' + n[2])

name['FileName'] = name_list

name.to_csv('name_fixed.csv', index = False)

print(name)
