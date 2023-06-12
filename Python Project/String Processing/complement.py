"""
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    TODO: Use the DNA strand which users keyed in to build the complement.
    """
    dna_strand = input("Please give me a DNA strand and I'll find the complement: ")
    dna_strand = dna_strand.upper()
    new_strand = build_complement(dna_strand)
    print('The complement of '+str(dna_strand)+' is '+str(new_strand))


def build_complement(dna_strand):
    """
    TODO: Find the complementary of nucleotide to build another DNA strand.
    """
    dna_strand = dna_strand.upper()  # Case-insensitive for build_complement()
    complement = ''
    for nucleotide in dna_strand:
        if nucleotide == 'A':
            complement += 'T'
        elif nucleotide == 'T':
            complement += 'A'
        elif nucleotide == 'C':
            complement += 'G'
        elif nucleotide == 'G':
            complement += 'C'
    return complement


###### DO NOT EDIT CODE BELOW THIS LINE ######


if __name__ == '__main__':
    main()
