#!/usr/bin/python
from nltk.corpus import wordnet
import sys


def usage():
    print """usage: python hypernym_hierarchy.py <obj>
e.g.
    python hypernym_hierarchy.py ship
    python hypernym_hierarchy.py giraffe"""
    sys.exit()


if len(sys.argv) < 1:
    usage()

oldw = sys.argv[1]

hypernyms_found=[oldw]
while True:
    neww = oldw
    s = wordnet.synsets(neww)
    oldw = s[0].hypernyms()[0].name()
    print "hypernyms of {} = {}".format(neww, oldw)
    oldw = oldw[:oldw.find('.')]
    if oldw in hypernyms_found:
        hypernyms_found.append(oldw)
        print 'Cycle detected [{}]'.format(oldw)
        break
    hypernyms_found.append(oldw)
    #raw_input()  # for interactive next hypernym display

print
print " --> ".join(hypernyms_found)

