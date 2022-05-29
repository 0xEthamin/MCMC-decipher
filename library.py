"""
    this file contains all the functions useful to the program
"""
import random
import numpy as np

EPSILON = 1e-6


def remove_special_chars(string):
    """ Remove French accented characters and punctuation. Return string in lower case """

    result = " "
    string = string.lower()
    for i in range(len(string)):
        if string[i] in "éèëê":
            result += "e"
        elif string[i] in "àâä":
            result += "a"
        elif string[i] in "îï":
            result += "i"
        elif string[i] in "üûù":
            result += "u"
        elif string[i] in "ôö":
            result += "o"
        elif string[i] in "ÿ":
            result += "y"
        elif string[i] in "ç":
            result += "c"
        elif "a" <= string[i] <= "z":
            result += string[i]
        elif not result[-1] == " ":  # Prevents two spaces
            result += " "
    return result.strip()


def format_all_text(textFile):
    """ Open a text file and format all the content. Return formated text """
    file = open(textFile, "rb")

    content = "init"
    content_formated = ""
    while len(content) != 0:
        content = file.readline().decode("utf-8")
        content_formated += remove_special_chars(content) + " "

    file.close()
    return content_formated


def bigrams_proba(text):
    """ Calculate the probability that each letter will be followed by another. e.g. the probability that an A will be followed by a B
        Return a dictionnary {letter: {letter1 : proba, letter2 : proba}, OtherLetter :  {letter1 : proba, letter2 : proba}} """

    text_formated = format_all_text(text)

    # First we have to count which letter follows which letter at which frequency.
    # e.g. in "AABACBAA " we need to have {A: {A : 2, B: 1, C: 1, " ": 1}, B: {A: 2}, C: {B : 1}}

    bigrams_frequence = {}

    # We also need the total number of times each letter appears.

    number = {}

    i = 0
    while i < len(text_formated)-1:
        letter = text_formated[i]
        next_letter = text_formated[i+1]

        # If the letter is not in the dictionary, then add it
        if letter not in bigrams_frequence:
            bigrams_frequence[letter] = {}

        if next_letter not in bigrams_frequence[letter]:
            bigrams_frequence[letter][next_letter] = 1

        else:
            bigrams_frequence[letter][next_letter] += 1

        if letter not in number:
            number[letter] = 1
        else:
            number[letter] += 1

        i += 1

    # Now it remains to calculate the probabilities. To do this it is sufficient to divide the frequency by the total number

    proba = {}
    for x in bigrams_frequence:
        for y in bigrams_frequence[x]:
            if x not in proba:
                proba[x] = {}

            proba[x][y] = bigrams_frequence[x][y]/number[x]

    return proba  # Dictionnary {letter: {letter1 : proba, letter2 : proba}, OtherLetter :  {letter1 : proba, letter2 : proba}}


def get_new_random_alphabet():
    """ Generates a random array that corresponds to an alphabet by substitution
        Return a table """

    alphabet = []  # The corresponding letter is the index
    for i in range(0, 26):
        random_letter_ord = random.randint(97, 122)  # Unicode a->97 z->122

        if random_letter_ord in alphabet:  # Prevent for same letter
            while random_letter_ord in alphabet:
                random_letter_ord = random.randint(97, 122)

        alphabet.append(random_letter_ord)
    return alphabet


def score_calculator(string, proba_dic):
    """ Calculates the plausibility score of a string based on a probability dictionary
        Return float """

    score = 0
    i = 0
    while i != len(string)-1:
        letter = string[i]
        next_letter = string[i+1]

        if next_letter not in proba_dic[letter]:  # Fill the dictionnary
            proba_dic[letter][next_letter] = 0

        score += np.log(proba_dic[letter][next_letter]+EPSILON)  # I apply a log to have a more user friendly score. +EPSILON to prevent for log(0)

        i += 1

    score = score/len(string)  # I normalize by the length of the text to have a nice score

    return score


def permute_alphabet(alphabet, x, y):
    """ Return a new alphabet by swapping two letters x and y """

    new_alphabet = alphabet.copy()
    new_alphabet[y] = alphabet[x]
    new_alphabet[x] = alphabet[y]
    return new_alphabet


def decipher(text, alphabet):
    """ Apply a code to a text and return the deciphed text """
    deciphed_text = ""
    for letter in text:
        if letter == " ":
            deciphed_text += " "
        else:
            i = 0
            while alphabet[i] != ord(letter):
                i += 1
            deciphed_text += chr(97+i)  # In unicode 97 is "a"
    return deciphed_text
