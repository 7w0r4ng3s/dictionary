from Sheet import * # the tool scraping data from Google Sheet
import pandas as pd
import glob
import os

id_list = ['101S-DEzHcZYNDw1VZ7NRXD2nkJQfq2TT_zvH9_1zcfU', '19Sk7PWxUS3wkK7WIsyAShRWzk0RNwbS4680e9CIn9C4']
range_list = ['list_1', 'list_2']

def merge_list():
	""" A function which merges all csv files in the folder and makes a list containing
	all word lists"""

	# User prompt begins
	print('Options')
	print('1 Add Google Sheet \n2 Merge List') # the user has two options
	user_input = input('Type the number to proceed: ')

	if user_input == '1':
		# prompt user the number of the target list
		sheet_id = input('Paste the spreadsheet ID: \n')
		sheet_range = input('Paste the spreadsheet range name: \n')
		id_list.append(sheet_id)
		range_list.append(sheet_range)

	elif user_input == '2':
		# prompt user the number of the target list
		choice = int(input('Enter the number of the list you wish to merge into the database: '))

		# because the previous 'id_list' and 'range_list' index starts from zero
		SPREADSHEET_ID = id_list[choice - 1]
		RANGE_NAME = range_list[choice - 1]

		print()
		print('---------- List Info ----------')
		print('list_{}'.format(choice))
		print('Spreadsheet ID:', SPREADSHEET_ID)
		print('Sheet name:', RANGE_NAME)
		print()
		print('---------- Retrieving Word List ----------')
		print('Merging list {}...'.format(choice))
		print('Waiting...')

		# get the target Google Sheet file and convert it into a pandas dataframe
		gsheet = get_google_sheet(SPREADSHEET_ID, RANGE_NAME)
		df = gsheet2df(gsheet)
		print('{} words retrieved successfully!'.format(df.shape[0]))

		# convert the data frame into a csv file
		df.to_csv('csv/list_{}.csv'.format(choice), encoding='utf-8', index=False)

		os.chdir('/Users/7w0r4ng3s/Desktop/Dictionary/csv')
		results = pd.DataFrame([])
		    
		# merging all list by append them to a single dataframe
		for counter, file in enumerate(glob.glob("list_*")):
		    namedf = pd.read_csv(file, skiprows=0, usecols=[0,1,2,3])
		    results = results.append(namedf)

		# convert the dataframe to a new csv file in the same directory
		# the new csv file containing all words will serve as a database
		results.reset_index(drop=True).to_csv('/Users/7w0r4ng3s/Desktop/Dictionary/csv/words.csv', index=None)

