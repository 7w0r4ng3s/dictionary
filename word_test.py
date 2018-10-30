from Word import Word # the word class including word functions
from Tool import * # the tool scraping data from Google Sheet
import random
from random import sample

gsheet = get_google_sheet(SPREADSHEET_ID, RANGE_NAME)
df = gsheet2df(gsheet)
# print('Dataframe size = ', df.shape)
# print(df.head())

# the word list to store all words, familarity, cn_meaning, meaning
word_list = []
for num in range(df.shape[0]):
    word_list.append(list(df.iloc[num]))

print('{} words retrieved successfully!'.format(len(word_list)))
rand_num = random.sample(range(0,61), 61)

# print word_list in random order
for num in rand_num:
    print(word_list[num])