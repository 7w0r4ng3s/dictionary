from Word import Word # the word class including word functions
from Tool import * # the tool scraping data from Google Sheet

gsheet = get_google_sheet(SPREADSHEET_ID, RANGE_NAME)
df = gsheet2df(gsheet)
# print('Dataframe size = ', df.shape)
# print(df.head())

# the word list to store all words, familarity, cn_meaning, meaning
word_list = []
for num in range(df.shape[0]):
    word_list.append(list(df.iloc[num]))

