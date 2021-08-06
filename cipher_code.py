import numpy as np
import string      # to load the characters
import random      # to shuffel and creat substitutional cipher

import re          # for regex
import requests
import os
import textwrap

# 1st step: Generate a random substitution cipher
# make a list of alphabet for key in dictionary
letter1 = list(string.ascii_lowercase)
# make a list of alphabet for value in dictionary
letter2 = list(string.ascii_lowercase)

true_mapping = {}                                 # initialization of dictionary

# to shuffel the second letter to make cipher
random.shuffle(letter2)

'''
for k, v in zip(letter1, letter2):               # put the key and value in the dic
    true_mapping[k] = v
'''

true_mapping = dict(zip(letter1, letter2))  # same code as above


# 2nd Step: Read Moby Dick, creat chracter level Language Model

with open('2701-0.txt', mode='r', encoding="utf8") as Moby:

    text = Moby.read()
    # print(text)


# 3rd step: Encoding and Decoding Functions


# 4th step: Genetic alghorithm
