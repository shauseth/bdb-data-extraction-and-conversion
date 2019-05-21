import pandas as pd
import itertools

unique = pd.read_csv('unique.csv')

user = pd.DataFrame()

user['User'] = unique['Author']
user = user.drop_duplicates()

def getString(length = 4, characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):

    for s in itertools.product(characters, repeat = length):

        yield ''.join(s)

list = []

for s in getString():

    list.append(s)

user['UserID'] = list[:len(user)]

user = user[['UserID', 'User']]

user.to_csv('user.csv', index = False)

print(user)
