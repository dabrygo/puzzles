# Replaces each letter in a string with a neighboring one in the alphabet

import random
from string import ascii_uppercase as ABC


def letter_replacement(string):
    encoded = ""
    string = string.upper()
    for c in string:
        i = ABC.find(c)
        before = ABC[i-1]
        after = ABC[i+1]
        new_c = random.choice([before, after])
        encoded += new_c
    return encoded

print(letter_replacement("Daniel"))


