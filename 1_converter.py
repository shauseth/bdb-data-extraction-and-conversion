import xml.etree.ElementTree as ET
import csv

list_size = 20

tree = ET.parse("mimoset.xml")
root = tree.getroot()

# open a file for writing
library = open("mimoset.csv", 'w')

# create the csv writer object
csvwriter = csv.writer(library)
library_head = []

count1 = 0
count2 = 0

for member in root[1]:

    table = []

    if count1 == 0:

        for i in range(list_size):

            column = root[1][0][i].attrib
            element = column["name"]
            library_head.append(element)

        csvwriter.writerow(library_head)

        count1 = count1 + 1

    for n in range(list_size):

        column = root[1][count2][n].text
        table.append(column)

    count2 = count2 + 1

    csvwriter.writerow(table)

library.close()
