#!/usr/bin/python
import nltk
from nltk.corpus import wordnet

""" Similarity between two words
Threshold decided manually, can be tweaked after discussion
"""
def similarity(a, b):
    suf=".n.01"
    a, b = a+suf, b+suf
    w1 = wordnet.synset(a)
    w2 = wordnet.synset(b)
    sim = w1.wup_similarity(w2)
    #print sim,
    output=""
    if sim >= 0.85:
        output="Very similar"
    elif sim >= 0.65:
        output="Little similar"
    else:
        output="Not similar"
    print 'similarity({:>15}, {:15}) = {:<15} ==> {} '.format(a[:a.find('.')],b[:b.find('.')], sim, output)


sim = similarity
# very similar
print
sim("sparrow", "parrot")
sim("ship", "boat")

# little similar
print
sim("cat", "elephant")


# not similar
print
sim("dolphin", "ship")
sim("giraffe", "tiger")
sim("sheep", "ship")
sim("ship", "cat")
