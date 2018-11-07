import pandas as pd

df = pd.read_csv('csv/words.csv')

word_list = [] # the dictionary storing all info of individual words

for num in range(df.shape[0]):
    word_list.append(list(df.iloc[num]))

words = [l[0] for l in word_list] # a list stroring all words

def search():
	# TODO: Add comments
	word = input('Enter the vocabulary you want to search: ').lower()

	if word in words:
		row = df[df['word'] == word]
		index = words.index(word)
		print()
		print(word + '\n')
		print('Knew the word before: {}'.format(word_list[index][1]))
		print('Chinese meaning: {}'.format(word_list[index][2]))
		print('English meaning: {}'.format(word_list[index][3]))

	elif word not in words:
		tmp = []
		[tmp.append(item) for item in word_list if word.lower() in item[0].lower()]
		l = [i+1 for i in list(range(len(tmp)))] # index list
		if len(tmp) == 0:
			print('Error: {} not in dictionary. Please try again.'.format(word))
		print()
		print('Do you mean: ')
		word_dict = dict(zip(l, tmp))
		for i in word_dict.keys():
			print(i, word_dict[i][0])

		print()
		choice = int(input('Enter the index: '))-1
		print()
		print(tmp[choice][0])
		print('Knew the word before: {}'.format(tmp[choice][1]))
		print('Chinese meaning: {}'.format(tmp[choice][2]))
		print('English meaning: {}'.format(tmp[choice][3]))
