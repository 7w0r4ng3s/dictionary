from get_sheet import * # the tool scraping data from Google Sheet
import pandas as pd
import glob
import os

# all list info
id_list = ['101S-DEzHcZYNDw1VZ7NRXD2nkJQfq2TT_zvH9_1zcfU', '19Sk7PWxUS3wkK7WIsyAShRWzk0RNwbS4680e9CIn9C4']
range_list = ['list_1', 'list_2']

# prompt user the number of the target list
choice = int(input('Enter the number of the list: \n'))

SPREADSHEET_ID = id_list[choice - 1]
RANGE_NAME = range_list[choice - 1]
print('---------- List Info ----------')
print('Spreadsheet ID:', SPREADSHEET_ID)
print('Sheet name:', RANGE_NAME)
print()

print('---------- Retrieve Word List ----------')
print('Waiting...')
gsheet = get_google_sheet(SPREADSHEET_ID, RANGE_NAME)
df = gsheet2df(gsheet)
print('{} words retrieved successfully!'.format(df.shape[0]))
print()

# convert the particular word list to a csv file with file name 'list_#.csv'
df.to_csv('csv/list_{}.csv'.format(choice), encoding='utf-8', index=False)

os.chdir('/Users/7w0r4ng3s/Desktop/Dictionary/csv')
results = pd.DataFrame([])
    
# merging all list by append them to a single dataframe
for counter, file in enumerate(glob.glob("list_*")):
    namedf = pd.read_csv(file, skiprows=0, usecols=[0,1,2,3])
    results = results.append(namedf)

# convert the dataframe to a new csv file in the same directory
# the new csv file containing all words will serve as a database
results.reset_index(drop=True).to_csv('/Users/7w0r4ng3s/Desktop/Dictionary/csv/words.csv')