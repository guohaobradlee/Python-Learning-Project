"""
File: anagram.py
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""


# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary.
EXIT = '-1'                   # Controls when to stop the loop.


# Global variable
vocabulary_list = []  # A list to store all the words in dictionary.txt.
anagram_list = []  # A list to store all the anagrams.


def main():
    """
    This program recursively finds all the anagram(s)
    for the word input by user and terminates when the
    input string matches the EXIT constant defined at line 19.
    """
    global anagram_list
    read_dictionary()
    index_list = []  # A list to store the index of string of word which user entered.
    print(f'Welcome to stanCode "Anagram Generator" (Or {EXIT} to quit)')
    while True:
        anagram_list.clear()
        index_list.clear()
        input_word = input('Find anagrams for: ')  # A word user entered.
        if input_word == '-1':
            break
        print('Searching...')
        find_anagrams(input_word, '', index_list)
        print(f'{len(anagram_list)} anagrams: {anagram_list}')


def read_dictionary():
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    :return: vocabulary_list(lst): A list store all vocabularies in dictionary.txt.
    """
    with open(FILE, 'r') as f:
        for vocabulary in f:
            vocabulary_list.append(vocabulary.strip())
        return vocabulary_list


def find_anagrams(s, anagram, index_lst):
    """
    :param s: (str) A word user entered.
    :param anagram: (str) An anagram which composed of the letters of 's'.
    :param index_lst: (lst) A list to store the index of string of 's'.
    :return: This function does not return any value.
    """
    global anagram_list, vocabulary_list
    # Base case.
    if len(anagram) == len(s):
        if anagram not in anagram_list:  # Avoid to add repeated word into anagram_list.
            if anagram in vocabulary_list:  # Add anagram into anagram_list if it exist in vocabulary_list.
                anagram_list.append(anagram)
                print(f'Found: {anagram}')
                print('Searching...')
    # Recursive case.
    else:
        if has_prefix(anagram):
            for i in range(len(s)):
                if i not in index_lst:  # Avoid skipping the same letters.
                    # Choose.
                    index_lst.append(i)
                    anagram += s[i]
                    # Explore.
                    find_anagrams(s, anagram, index_lst)
                    # Un-choose.
                    anagram = anagram[0:len(anagram)-1]
                    index_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: (str) A substring that is constructed by the letter in word which user entered
    :return: (bool) If there is any words with prefix stored in sub_s
    """
    for word in vocabulary_list:
        if word.strip().startswith(sub_s):
            return True
    # Check all vocabularies in dictionary.txt, if there is no vocabulary start with sub_s then return false.
    return False


if __name__ == '__main__':
    main()
