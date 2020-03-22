# Replaces each letter in a string with a neighboring one in the alphabet

from nltk.corpus import words
from nltk.stem.snowball import SnowballStemmer
import random
import re
import pprint
from string import ascii_uppercase as ABC


WORDS = set(words.words())
STEMMER = SnowballStemmer('english')


def encode(string):
    '''Replace each letter in a string with its alphabetical neighbor.

    For example, encode each:
      - A to Z or B
      - B to A or C
      - Etc.
    '''
    new_words = []
    string = string.upper()
    for match in re.finditer('\w+', string):
        new_word = ""
        word = match.group(0)
        for c in word:
            i = ABC.find(c)
            before = ABC[i-1]
            after = ABC[(i+1)%len(ABC)]
            new_c = random.choice([before, after])
            new_word += new_c
        new_words.append(new_word)
    return '|'.join(new_words)


def attempt_words(word):
    '''Return a list of words that may or may not be real'''
    n = len(word)
    options = [bin(i)[2:].zfill(n) for i in range(2**n)]
    words = []
    for i, option in enumerate(options):
        new_word = ''
        for j, c in enumerate(word):
            choice = option[j]
            k = ABC.find(c)
            if choice == '0':
                new_c = ABC[k-1]
            else:
                new_c = ABC[(k+1)%len(ABC)]
            new_word += new_c
        words.append(new_word)
    return words


def decode(string):
    '''Decipher a string whose letters are replaced with alphabetical neighbors

    For example, the word 'GNS' could be deciphered to 'FOR' or 'HOT'
    '''
    words = string.split('|')
    decoded = []
    for word in words:
        attempts = attempt_words(word)
        lowered = [word.lower() for word in attempts]
        successes = [word for word in lowered if word in WORDS or STEMMER.stem(word) in WORDS]
        if len(successes) == 1:
            translation = successes[0]
        elif len(successes) > 1:
            translation = f"({'|'.join(successes)})"
        else:
            raise ValueError(f"Could not translate '{word}'")
        decoded.append(translation)
    return ' '.join(decoded)


encoded = encode("The quick brown fox jumps over the lazy dog.")
print(encoded)
decoded = decode(encoded)
print(decoded)
