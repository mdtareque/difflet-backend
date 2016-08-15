#!/usr/bin/python
import nltk
from nltk.corpus import wordnet

""" Similarity between two words
Threshold decided manually, can be tweaked after discussion """

""""
Sample Output:
    similarity(        sparrow, parrot         ) = 0.869565217391  ==> Very similar
    similarity(           ship, boat           ) = 0.909090909091  ==> Very similar

    similarity(            cat, elephant       ) = 0.814814814815  ==> Little similar

    similarity(        dolphin, ship           ) = 0.296296296296  ==> Not similar
    similarity(        giraffe, tiger          ) = 0.521739130435  ==> Not similar
    similarity(          sheep, ship           ) = 0.296296296296  ==> Not similar
    similarity(           ship, cat            ) = 0.32            ==> Not similar

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



