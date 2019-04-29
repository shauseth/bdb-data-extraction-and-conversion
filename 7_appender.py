import pandas as pd
from Bio.Entrez import efetch, read
from Bio import Entrez

# Enter own e-mail
Entrez.email = 'shauryaseth@hotmail.com'

# Turns off warnings
pd.options.mode.chained_assignment = None

dataframe = pd.read_csv('dataframe.csv')
ref = pd.DataFrame()

ref['Reference'] = dataframe.loc[:, 'Reference'].values

def date(pmid):

    handle = efetch(db = 'pubmed', id = pmid, retmode = 'xml')

    xml_data = read(handle)['PubmedArticle']

    if xml_data:

        xml_list = xml_data[0]

        data = xml_list['MedlineCitation']['Article']['Journal']['JournalIssue']['PubDate']

        if 'Day' in data:

            day = data['Day']

        else: day = ''

        if 'Month' in data:

            month = data['Month'] + ' '

        else: month = ''

        if 'Year' in data:

            year = data['Year'] + ' '

        else: year = ''

        return year + month + day

    else: return ''

def author(pmid):

    handle = efetch(db = 'pubmed', id = pmid, retmode = 'xml')

    xml_data = read(handle)['PubmedArticle']

    if xml_data:

        xml_list = xml_data[0]

        data = xml_list['MedlineCitation']['Article']['AuthorList']

        author_list = []

        for n in range(len(data)):

            author = data[n]

            if 'ForeName' in author:

                fore = author['ForeName'] + ' '
                
            else:

                fore = ''
                
            if 'LastName' in author:

                last = author['LastName']
                
            else:

                last = ''

            name = fore + last
            
            aff_info = author['AffiliationInfo']

            if aff_info:

                aff = aff_info[0]['Affiliation']

            else: aff = ''

            author_list.append('#Name ' + name)

            if aff:

                author_list.append('#Affiliation ' + aff)

        author_str = ' '.join(author_list)

        return author_str
    
    else: return ''

date_list = []
author_list = []

for x in ref['Reference'].values:

    if x.isdigit():

        a = date(x)
        b = author(x)
        date_list.append(a)
        author_list.append(b)

        print(a[:8] + ' ' + b[:46] + '...')

    elif x == 'unknown':

        date_list.append('unknown')
        author_list.append('unknown')

    else:

        date_list.append('known')
        author_list.append('known')

ref['Date'] = date_list
ref['Author'] = author_list

ref.to_csv('output.csv', index = False)

print('')
print("Data saved to output.csv")
