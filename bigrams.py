'''
Created on Oct 13, 2015

@author: Bogdan Vasilescu
'''

from __future__ import print_function

from itertools import islice
import os

import nltk

# Read tokenized corpus
corpusFile = open(os.path.abspath('data/django.code.lexed.txt'), 'r')
corpus = corpusFile.read().split()

# Build a frequency distribution for tokens
fd_tokens = nltk.FreqDist(corpus)

# How many tokens are there?
print('\rHow many tokens are there?')
print(len(fd_tokens.keys()))

# How often does a particular token occur?
# (can be indexed as a dictionary)
print('\rHow many times does the token "for" appear?')
print(fd_tokens['for'])

# Sort by most common token, descending
sfd_tokens = sorted(fd_tokens.items(),
                    key=lambda tpl: -int(tpl[1]))

# Which are the most popular 20 tokens?
print('\rWhich are the most popular 20 tokens?')
for (token, count) in sfd_tokens[:20]:
    print(token, count)

# Build a frequency distribution for bigrams
fd_2gram = nltk.FreqDist(nltk.ngrams(corpus, 2))

# How many bigrams are there?
print('\rHow many bigrams are there?')
print(len(fd_2gram.keys()))

# Sort by most common bigram, descending
sfd_2gram = sorted(fd_2gram.items(),
                   key=lambda tpl: -int(tpl[1]))

# Which are the most popular 20 bigrams?
print('\rWhich are the most popular 20 bigrams?')
for (bigram, count) in sfd_2gram[:20]:
    print(bigram, count)

## Which are the most popular 20 trigrams starting with "for"?
#fd_3gram = nltk.FreqDist(nltk.ngrams(corpus, 3))
#for_3gram = sorted([(trigram,count)
#                    for (trigram,count) in fd_3gram.items()
#                    if trigram[0]=='for'],
#                   key=lambda tpl: -int(tpl[1]))
#print('\rWhich are the most popular 20 trigrams starting with "for"?')
#for (trigram, count) in for_3gram[:20]:
#    print(trigram, count)

# Which are the most popular 20 bigrams starting with "for"?
for_2gram = sorted([(bigram,count)
                    for (bigram,count) in fd_2gram.items()
                    if bigram[0]=='for'],
                   key=lambda tpl: -int(tpl[1]))
print('\rWhich are the most popular 20 bigrams starting with "for"?')
for (bigram, count) in for_2gram[:20]:
    print(bigram, count)

# an nltk.ConditionalFreqDist() counts frequencies of pairs.
# When given a list of bigrams, it maps each first word of a bigram
# to a FreqDist over the second words of the bigram.
cf_2gram = nltk.ConditionalFreqDist(nltk.ngrams(corpus, 2))
#print(cf_2gram)

print('\rAlternative solution using ConditionalFreqDist')

# conditions() in a ConditionalFreqDist are like keys()
# in a dictionary
# How many different starting tokens are there in all bigrams?
print('\rHow many different starting tokens are there in all bigrams?')
print(len(cf_2gram.conditions()))
#print(cf_2gram.conditions()[:10])

# the cf_2gram entry for "for" is a FreqDist
print('\rThe cf_2gram entry for "for" is a FreqDist')
print(*islice(cf_2gram['for'].items(), 20), sep="\n")

# here are the words that can follow after "for".
# We first access the FreqDist associated with "for",
# then the keys in that FreqDist
print('\rHow many different tokens can follow after "for"?')
print(len(cf_2gram["for"].keys()))
print('\rWhich are the most popular 20?')
for (token, count) in sorted(cf_2gram["for"].items(),
                             key=lambda tpl: -tpl[1])[:20]:
    print(str(tuple(['for', token])) + ' ' + str(count))

# an nltk.ConditionalProbDist() maps pairs to probabilities.
# One way in which we can do this is by using Maximum Likelihood Estimation (MLE)
cp_2gram = nltk.ConditionalProbDist(cf_2gram, nltk.MLEProbDist)

# This again has conditions() wihch are like dictionary keys
#print(cp_2gram.conditions()[:20])

# Here is what we find for "for": a Maximum Likelihood Estimation-based probability distribution,
# as a MLEProbDist object.
# We can find the words that can come after "for" by using the function samples()
print('\r20 tokens that come after "for"')
print(*islice(cp_2gram["for"].samples(), 20), sep="\n")

# What is the probability of "i" coming after "for"?
print('\rWhat is the probability of "i" coming after "for"?')
print(cp_2gram["for"].prob("i"))

print('\rWhat is the probability of "e" coming after "for"?')
print(cp_2gram["for"].prob("e"))

print('\rThe most probable 20 tokens that come after "for"')
for token in sorted(cp_2gram["for"].samples(),
                key=lambda e: -cp_2gram["for"].prob(e))[:20]:
    print(token, cp_2gram["for"].prob(token))


# We can draw a random word to follow "for"
# based on the probabilities of the bigrams
print('\rRandom word to follow "for"')
print(cp_2gram["for"].generate())

# Generate random code
print('\rRandom code starting from "for"')
word = "for"
for index in range(50):
    word = cp_2gram[ word ].generate()
    print(word,)


