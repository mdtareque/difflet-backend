#!/usr/bin/python
from nltk.corpus import wordnet
import sys


def usage():
    print """usage: python get_hypernym.py <obj1> <obj2>
e.g.
    python get_hypernym.py ship boat
    python get_hypernym.py snail shark"""
    sys.exit()



if len(sys.argv) < 2:
    usage()

obj1 = sys.argv[1]
obj2 = sys.argv[2]
suffix = ".n.01"

def lowest_common_hypernyms(a,b):
    print "lowest_common_hypernyms for [ {}, {} ] = ".format(obj1, obj2),
    print wordnet.synset(obj1 + suffix).lowest_common_hypernyms( wordnet.synset(obj2 + suffix) )

lch = lowest_common_hypernyms
lch(obj1, obj2)

