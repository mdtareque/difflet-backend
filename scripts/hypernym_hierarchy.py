#!/usr/bin/python
from nltk.corpus import wordnet
import sys


"""
This program outputs all the hypernyms till the most higher level hypernyms is found

Sample Output
 python hypernym_hierarchy.py lion
 hypernyms of lion = big_cat.n.01
 hypernyms of big_cat = feline.n.01
 hypernyms of feline = carnivore.n.01
 hypernyms of carnivore = placental.n.01
 hypernyms of placental = mammal.n.01
 hypernyms of mammal = vertebrate.n.01
 hypernyms of vertebrate = chordate.n.01
 hypernyms of chordate = animal.n.01
 hypernyms of animal = organism.n.01
 hypernyms of organism = living_thing.n.01
 hypernyms of living_thing = whole.n.02
 hypernyms of whole = concept.n.01
 hypernyms of concept = idea.n.01
 hypernyms of idea = content.n.05
 hypernyms of content = collection.n.01
 hypernyms of collection = group.n.01
 hypernyms of group = abstraction.n.06
 hypernyms of abstraction = concept.n.01
 Cycle detected [concept]

 lion --> big_cat --> feline --> carnivore --> placental --> mammal --> vertebrate --> chordate --> animal --> organism --> living_thing --> whole --> concept --> idea --> content --> collection --> group --> abstraction --> concept


"""


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

