from Tool import * # the tool scraping data from Google Sheet
import random
from random import sample
from sklearn.utils import shuffle


print('Spreadsheet ID:', SPREADSHEET_ID)
print('Sheet name:', RANGE_NAME)

# access the Google Sheet by target SPREADSHEET_ID and RANGE_NAME
gsheet = get_google_sheet(SPREADSHEET_ID, RANGE_NAME)
df = gsheet2df(gsheet)
print('{} words retrieved successfully!'.format(df.shape[0]))


word_list = []
for num in range(df.shape[0]):
    word_list.append(list(df.iloc[num]))
    
print('{} words retrieved successfully!'.format(len(word_list)))


# generate all words in the list in random order
rand_list = []
rand_num = random.sample(range(0,len(word_list)), len(word_list))
for num in rand_num:
    rand_list.append(word_list[num])


def search():
	word = input('Enter the vocabulary you want to search: ').lower()

	if word in [l[0] for l in rand_list]:
		row = df[df['word'] == word]
		index = [l[0] for l in rand_list].index(word)
		print()
		print(word + '\n')
		print('Knew the word before: {}'.format(rand_list[index][1]))
		print('Chinese meaning: {}'.format(rand_list[index][2]))
		print('English meaning: {}'.format(rand_list[index][3]))
	else:
		print('Error: {} not in list_1'.format(word))
		search()

search()