# Replaces each letter in a string with a neighboring one in the alphabet

import random
import re
from string import ascii_uppercase as ABC


def letter_replacement(string):
    new_words = []
    string = string.upper()
    for match in re.finditer('\w+', string):
        new_word = ""
        word = match.group(0)
        for c in word:
            i = ABC.find(c)
            before = ABC[i-1]
            after = ABC[i+1]
            new_c = random.choice([before, after])
            new_word += new_c
        new_words.append(new_word)
    return '|'.join(new_words)

print(letter_replacement("To be or not to be. That is the question."))


