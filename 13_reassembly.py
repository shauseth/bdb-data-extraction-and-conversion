# SH-I

import pandas as pd
import itertools

def getString(length, characters):

    for s in itertools.product(characters, repeat = length):

        yield ''.join(s)

library = pd.read_csv('csv/library.csv')
mimoset = pd.read_csv('csv/mimoset.csv')
target = pd.read_csv('csv/target.csv')
info = pd.read_csv('table/datasets/info.csv')

library = library.fillna('unknown')
target = target.fillna('unknown')

post_processing = pd.DataFrame()

library['Library'] = '#LibraryName ' + library['LibraryName'] + ' #LibraryFrom ' + \
                  library['LibraryFrom'] + ' #LibrarySeqLength ' + \
                  library['LibrarySeqLength'] + ' #LibraryComplexity ' + \
                  library['LibraryComplexity'] + ' #LibraryTiter ' + \
                  library['LibraryTiter'] + ' #LibraryRandomness ' + \
                  library['LibraryRandomness'] + ' #LibraryCodingScheme ' + \
                  library['LibraryCodingScheme'] + ' #LibraryTopology ' + \
                  library['LibraryTopology'] + ' #LibraryComments ' + \
                  library['LibraryComments']

target['Target'] = '#TargetName ' + target['TargetName'] + ' #TargetSynonyms ' + \
                  target['TargetSynonyms'] + ' #TargetSource ' + \
                  target['TargetSource'] + ' #TargetType ' + \
                  target['TargetType'] + ' #TargetSequence ' + \
                  target['TargetSequence'] + ' #TargetStructure ' + \
                  target['TargetStructure'] + ' #TargetComments ' + \
                  target['TargetComments']

post_processing['Post-processing'] = mimoset['BriefDescription'].unique()
post_processing = post_processing.fillna('unknown')

library = library[['LibraryID', 'Library']]
mimoset = mimoset[['MimotopeSetID', 'Sequences', 'TargetID', 'LibraryID', 'BriefDescription', 'Reference']]
target = target[['TargetID', 'Target']]

date_dict = dict(zip(info['Reference'].values, info['Date'].values))
author_dict = dict(zip(info['Reference'].values, info['Author'].values))

mimoset['Date'] = mimoset['Reference'].map(date_dict)
mimoset['Date'] = mimoset['Date'].fillna('0000')
mimoset['Author'] = mimoset['Reference'].map(author_dict)
mimoset['Author'] = mimoset['Author'].fillna('# unknown')

mimoset['Author'] = mimoset['Author'] + ' #Reference ' + mimoset['Reference']

# generates library tags

lib_list = []
n = 1010001

for x in range(len(library['Library'])):

    lib_list.append(str(n))

    n = n + 1

library['LibraryTag'] = lib_list

# generates target tags

tar_list = []

for s in getString(4, 'abcdefghijklmnopqrstuvwxyz'):

    tar_list.append(s)

tar_list = tar_list[:len(target['Target'])]

target['TargetTag'] = tar_list

# generates post-processing tag

pp_list = []

for s in getString(4, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):

    pp_list.append(s)

pp_list = pp_list[:len(post_processing['Post-processing'])]

post_processing['PPTag'] = pp_list

# generates author tag

author_list = []

for s in getString(4, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):

    author_list.append(s)

author_list = author_list[:len(info['Author'])]

info['AuthorTag'] = author_list

# generates date tag

date_list1 = []
date_list2 = []
dates = info['Date'].values

def date_tag(date):

    date = date.split(' ')

    return ''.join(date)

for x in dates:

    if len(date_tag(x)) == 9:

        date_list1.append(date_tag(x))

    elif len(date_tag(x)) == 7:

        date_list1.append(date_tag(x) + '00')

    elif len(date_tag(x)) == 4:

        date_list1.append(date_tag(x) + '0000')

    else:

        date_list1.append('00000000')

for date in date_list1:

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

    else:

        date = date

    date_list2.append(date)

info['DateTag'] = date_list2

date_tag_dict = dict(zip(info['Reference'].values, info['DateTag'].values))
author_tag_dict = dict(zip(info['Reference'].values, info['AuthorTag'].values))

mimoset['DateTag'] = mimoset['Reference'].map(date_tag_dict)
mimoset['DateTag'] = mimoset['DateTag'].fillna('00000000')
mimoset['AuthorTag'] = mimoset['Reference'].map(author_tag_dict)
mimoset['AuthorTag'] = mimoset['AuthorTag'].fillna('XXXX')

lib_dict = dict(zip(library['LibraryID'].values, library['LibraryTag'].values))
tar_dict = dict(zip(target['TargetID'].values, target['TargetTag'].values))
pp_dict = dict(zip(post_processing['Post-processing'].values, post_processing['PPTag'].values))

mimoset['LibraryTag'] = mimoset['LibraryID'].map(lib_dict)
mimoset['LibraryTag'] = mimoset['LibraryTag'].fillna('1010001')
mimoset['TargetTag'] = mimoset['TargetID'].map(tar_dict)
mimoset['TargetTag'] = mimoset['TargetTag'].fillna('xxxx')
mimoset['PPTag'] = mimoset['BriefDescription'].map(pp_dict)
mimoset['PPTag'] = mimoset['PPTag'].fillna('XXXX')

mimoset['FileName'] = mimoset['DateTag'] + '-' + mimoset['LibraryTag'] + 'OO' + mimoset['TargetTag'] + mimoset['PPTag'] + '-' + mimoset['AuthorTag']

print(mimoset)
