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
    for i in range(len(long_sequence)-len(short_sequence)+1):
        difference = 0
        sameness = 0
        # Fine the sameness or differences between DNA strand and DNA sequence.
        for j in range(len(short_sequence)):
            if short_sequence[j] == long_sequence[j+i]:
                sameness += 1
            else:
                difference += 1
        similarity = sameness / (sameness + difference)  # Calculating similarities.
        # Find out the most similar DNA sequence after comparing the similarities.
        if similarity > max_similarity:
            dna_strand = i
            dna = ''
            for k in range(len(short_sequence)):
                ch = long_sequence[dna_strand+k]
                dna += ch
        max_similarity = homology(max_similarity, similarity)
    print('The best match is '+str(dna))


def homology(t1, t2):
    """
    :param t1: The value to be compared with t2.
    :param t2: Another value to be compared with t1.
    :return result: The bigger value will be return.
    """
    if t1 > t2:
        return t1
    else:
        return t2


if __name__ == '__main__':
    main()
