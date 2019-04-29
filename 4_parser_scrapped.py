from lxml import html
import requests

line1 = 'https://www.ncbi.nlm.nih.gov/pubmed/?term='
ref = '17881351'
line2 = '&report=medline&format=text'

page = requests.get(line1+ref+line2)
tree = html.fromstring(page.content)

data = tree.xpath('//pre/text()')

def date_parser(element):

    for i in data:
        lines = str(i).split(element)

    line_list = lines[1].splitlines()
    return line_list[0]

def author_parser(element):

    list = []
    n = 1

    for i in data:
        lines = str(i).split(element)

    for i in range(int(len(lines)/2)):
        line_list = lines[n].splitlines()
        list.append(line_list[0])
        n =+ 2

    return list

def author_parser_mod(element):

    list = []
    n = 1

    for i in data:
        lines = str(i).split(element)

    for i in range(int(len(lines)/2)):
        line_list = lines[n].splitlines()
        list.append(line_list[0])
        n =+ 2

    return list

date = date_parser('DP  - ')
author = author_parser('FAU - ')

print(date)
print(author)
