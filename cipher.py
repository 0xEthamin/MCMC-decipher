"""
    Use this program to cipher a text with a random substitution algorithm
"""

from library import get_new_random_alphabet, remove_special_chars


def cipher(string):
    ciphered_text = ""
    alphabet = get_new_random_alphabet()
    for letter in string:
        if letter == " ":
            ciphered_text += " "
        else:
            ciphered_text += chr(alphabet[ord(letter)-97])  # In Unicode a->97 so (ord(letter)-97) give the index in the tab. 0->a 1->b ...

    # Print(alphabet)
    return ciphered_text


input_text = input("Your sentence to cipher : ")
input_text = remove_special_chars(input_text)
print("your clear sentence is: ", input_text)
print("your ciphered sentence is: ", cipher(input_text))
