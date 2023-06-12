"""
File: boggle.py
Name: Brad
----------------------------------------
User will enter 4 rows of 4 single letters at the beginning,
and this program will start to find out all the
vocabularies composed of letters user entered.
"""


# This is the file name of the dictionary txt file.
# We will be checking if a word exists by searching through it.
FILE = 'dictionary.txt'


# Global variable.
vocabulary_list = []  # A list to store all the words in dictionary.txt.
find_list = []  # A list to store all the vocabularies which were found.
counts = 0  # A variable to count how many vocabularies were found.


def main():
	"""
	User will enter 4 rows of 4 single letters at the beginning,
	and this program will start to find out all the
	vocabularies composed of letters user entered.
	"""
	read_dictionary()
	total_letters = check_format_and_enter_letters()  # Store every letters user entered in list.
	if total_letters is not None:  # If the format is wrong, function won't execute find_starting_point(total_letters).
		find_starting_point(total_letters)


def find_starting_point(total_list):
	"""
	:param total_list: (lst) A list contains four lists which contain each row of letters separately.
	:return: This function does not return any value.
	"""
	for y in range(len(total_list)):
		for x in range(len(total_list)):
			start_letter = total_list[x][y]  # Find the start point (First letter).
			boggle(start_letter, '', x, y, total_list, [])
	print(f'There are {counts} words in total.')


def check_format_and_enter_letters():
	"""
	:return:
		total_letter_list (lst): A list contains four lists which contain each row of letters separately.
	"""
	total_letters_list = []
	for i in range(4):
		letters = input(f'{i + 1} row of letters: ')
		letters_list = letters.lower().split()  # Case insensitive.
		# Check whether is user enter four letters.
		if len(letters_list) == 4:
			for letter in letters_list:
				if len(letter) != 1 or letter.isdigit():  # Check whether each data is a single letter.
					print('Illegal input')
					return None
			total_letters_list.append(letters_list)
		else:
			print('Illegal input')
			return None
	return total_letters_list


def boggle(single_letter, vocabulary, start_x, start_y, total_list, coordinate_list):
	"""
	:param single_letter: (str) A letter which is the start of a vocabulary.
	:param vocabulary: (str) An empty string to put letter user entered in it.
	:param start_x: (int) The x coordinate of single_letter.
	:param start_y: (int) The y coordinate of single_letter.
	:param total_list: (lst) A list contains four lists which contain each row of letters separately.
	:param coordinate_list: (lst) To store x and y coordinates of every letter user entered.
	:return: This function does not return any value.
	"""
	global vocabulary_list, find_list, counts
	# Base case.
	if len(vocabulary) >= 4:
		if vocabulary not in find_list:  # Avoid to add repeated word into find_list.
			if vocabulary in vocabulary_list:  # Add vocabulary into find_list if it exist in vocabulary_list.
				find_list.append(vocabulary)
				counts += 1
				print(f'Found "{vocabulary}"')
	# Recursive case.
	"""
	Because every vocabulary which length greater than or equal to 4 all should be printed, 
	if add else condition, as long as the length of vocabulary equal to 4,
	this function will never get into the else condition,
	and vocabulary which length greater than 4 won't be printed.
	"""
	if has_prefix(vocabulary):
		# To get x and y coordinates around start point.
		for i in range(-1, 2, 1):
			for j in range(-1, 2, 1):
				next_x = start_x + i
				next_y = start_y + j
				#  Avoid x and y coordinates out of range.
				if 0 <= next_x < 4:
					if 0 <= next_y < 4:
						if (next_x, next_y) not in coordinate_list:
							# Choose.
							vocabulary += total_list[next_x][next_y]
							coordinate_list.append((next_x, next_y))
							# Explore.
							boggle(single_letter, vocabulary, next_x, next_y, total_list, coordinate_list)
							# Un-choose.
							vocabulary = vocabulary[0:len(vocabulary) - 1]
							coordinate_list.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list.
	"""
	with open(FILE, 'r') as f:
		for vocabulary in f:
			vocabulary_list.append(vocabulary.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid.
	:return: (bool) If there is any words with prefix stored in sub_s.
	"""
	for word in vocabulary_list:
		if word.strip().startswith(sub_s):
			return True
	# Check all vocabularies in dictionary.txt, if there is no vocabulary start with sub_s then return false.
	return False


if __name__ == '__main__':
	main()
