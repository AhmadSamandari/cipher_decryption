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

# print(true_mapping)

# 2nd Step: Read Moby Dick, creat chracter level Language Model
# initaite the the markov model for bigram with a matrix with add one smoothing
Ma = np.ones((26, 26))

# initaite the unigram vectors
pi = np.zeros(26)


# now we need functions to update the markov model by occurance of repitation aa, ab, ...
def update_the_index(char1, char2):
  # In ascii :ord('a') = 97 , ord('b') = 98 ,....
    i = ord(char1) - 97  # now a = 0, b = 1
    j = ord(char2)
    Ma[i, j] += 1


# also update the unigram
def update_the_index2(char):
    i = ord(char) - 97
    pi[i] += 1


# now lets calculate the log probability of single word/ token
def calculate_log_prob(word):
    # print('word:' word)
    i = ord(word[0]) - 97
    logp = np.log(pi[i])

    for char in word[1:]:
        j = ord(word(char)) - 97
        logp += np.log(Ma[i, j])  # to update the probability in the matrix
        i = j  # update the j, now i =1, j = 2 then i = 2 j = 3 then ...

    return logp


# now lets to calculate the probability of sequence of words
def calculate_log_prob2(words):
    # input is string, first break it to words
    if words == str:
        words = words.split()

    logp = 0
    for word in words:
        logp += calculate_log_prob(word)

    return logp


with open('2701-0.txt', mode='r', encoding="utf8") as Moby:

    text = Moby.read()
    # print(text)


# 3rd step: Encoding and Decoding Functions


# 4th step: Genetic alghorithm
