from Word import Word # the word class including word functions
from Tool import * # the tool scraping data from Google Sheet
import random
from random import sample


gsheet = get_google_sheet(SPREADSHEET_ID, RANGE_NAME)
df = gsheet2df(gsheet)
print('Dataframe size = ', df.shape)
print(df.head())


# the word list to store all words, familarity, cn_meaning, meaning
word_list = []
for num in range(df.shape[0]):
    word_list.append(list(df.iloc[num]))
    
print('{} words retrieved successfully!'.format(len(word_list)))


# generate all words in the list in random order
rand_list = []
rand_num = random.sample(range(0,len(word_list)), len(word_list))
for num in rand_num:
    rand_list.append(word_list[num])


word = [l[0] for l in rand_list] # a list to store individual word
fam = [l[1] for l in rand_list] # a list to store individual familarity
cn_meaning = [l[2] for l in rand_list] # a list to store individual chinese meaning
meaning = [l[3] for l in rand_list] # a list to store individual English meaning