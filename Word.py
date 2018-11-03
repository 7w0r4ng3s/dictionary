

class Word:

	def __init__(self, word, fam, cn_meaning, meaning):
		self.word = word
		self.fam = fam
		self.cn_meaning = cn_meaning
		self.meaning

	def add_word(self, new_word, new_cn_meaning, new_meaning):
		# add new word in a dict
		self.word = new_word
		self.new_cn_meaning = new_cn_meaning
		self.new_meaning = new_meaning


	# get info of a specific word in the dict
	def get_word(self):
		print('The current word is [{}]'.format(self.word))
		return self.word

	def get_cn_meaning(self):
		print('The word [{}] means [{}] in Chinese'.format(self.word, self.cn_meaning))
		return self.cn_meaning

	def get_meaning(self):
		print('The word [{}] means [{}] in English',format(self.word, self.meaning))
		return self.meaning


	def print_dict():
		pass



