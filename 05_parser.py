from Bio.Entrez import efetch, read
from Bio import Entrez

# Enter own e-mail
Entrez.email = 'shauryaseth@hotmail.com'

# Enter PubMed ID
ref = '8596952'

# Fetches date
def date(pmid):

    handle = efetch(db = 'pubmed', id = pmid, retmode = 'xml')

    xml_data = read(handle)['PubmedArticle'][0]
    data = xml_data['MedlineCitation']['Article']['Journal']['JournalIssue']['PubDate']

    if 'Day' in data:

        day = data['Day']

    else: day = ''

    return data['Year'] + ' ' + data['Month'] + ' ' + day

# Fetches author
def author(pmid):

    handle = efetch(db = 'pubmed', id = pmid, retmode = 'xml')

    xml_data = read(handle)['PubmedArticle'][0]
    data = xml_data['MedlineCitation']['Article']['AuthorList']

    author_list = []

    for n in range(len(data)):

        author = data[n]
        name = author['ForeName'] + ' ' + author['LastName']
        aff_info = author['AffiliationInfo']

        if aff_info:

            aff = aff_info[0]['Affiliation']

        else: aff = ''

        author_list.append('#Name ' + name)

        if aff:

            author_list.append('#Affiliation ' + aff)

    author_str = ' '.join(author_list)

    return author_str

date = date(ref)
authors = author(ref)

print(date)
print(authors)
