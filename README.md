# bdb-data-extraction-and-conversion

BDB is a relational database which contains a collection of XML files found in the xml folder. These files were coverted to CSV and can be found in the csv folder. A nice visualization of how the data in these files is related can be found in relations.png.

These files do not contain the authors and dates for the experiments, however, they have a reference column that contains PubMed IDs. A parser is used to extract the dates and authors from PubMed and collect them in a dataframe.

This data will be used to generate files that have a filename and format suitable for the 48HourDiscovery website.
