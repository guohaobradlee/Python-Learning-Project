"""
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    TODO: This program can help users to find the most similar DNA sequence in DNA strand.
    """
    long_sequence = input('Please give me a DNA sequence to search: ')
    short_sequence = input('What DNA sequence would you like to match? ')
    long_sequence = long_sequence.upper()  # Case-insensitive.
    short_sequence = short_sequence.upper()  # Case-insensitive.
    max_similarity = 0
    best_dna = ''  # Save the most similar dna strand
    for i in range(len(long_sequence)-len(short_sequence)+1):
        difference = 0
        sameness = 0
        for j in range(len(short_sequence)):  # Fine the sameness or differences between DNA strand and DNA sequence.
            if short_sequence[j] == long_sequence[j+i]:
                sameness += 1
            else:
                difference += 1
        similarity = sameness / (sameness + difference)  # Calculating similarities.
        if similarity > max_similarity:  # Find out the most similar DNA sequence after comparing the similarities.
            max_similarity = similarity
            best_dna = ''
            for k in range(len(short_sequence)):
                ch = long_sequence[i+k]
                best_dna += ch
    if len(best_dna) != 0:
        print('The best match is ' + str(best_dna))
    else:
        print('No best match in the DNA sequence.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == '__main__':
    main()
