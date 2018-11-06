import pandas as pd

df = pd.read_csv('csv/words.csv')

def search():
    word = input('Enter the vocabulary you want to search: ').lower()

    if word in list(df['word']):
    	row = df[df['word'] == word]
    	print()
    	print(word + '\n')
    	print()



def search():
    # TODO: move the search method to WordTool.py
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