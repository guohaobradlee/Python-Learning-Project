"""
File: caesar.py
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO: Users can enter a ciphered sentence or word, and this program can decipher it.
    """
    secret_number = int(input('Secret number: '))
    # Make the new order of alphabetic sequence.
    new_alphabet = ''
    for i in range(len(ALPHABET)):
        new_alphabet += ALPHABET[(i + secret_number) % 26]
    ciphered = input("What's the ciphered string?")
    ciphered = ciphered.upper()  # Case-insensitive.
    # Save the deciphered string.
    decipher = ''
    for j in range(len(ciphered)):
        # Save the characters which are not alpha in the string.
        if ciphered[j] not in ALPHABET:
            decipher += ciphered[j]
        # Save the characters which are alpha in the string.
        for k in range(len(new_alphabet)):
            if ciphered[j] == ALPHABET[k]:
                decipher += new_alphabet[k]
    print('The deciphered string is: '+str(decipher))


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####


if __name__ == '__main__':
    main()
