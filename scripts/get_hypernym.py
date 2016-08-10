from nltk.corpus import wordnet as wn
import sys

fruit_name = sys.argv[1]
fruit_name = wn.synsets(fruit_name)[0]

print fruit_name.hypernyms()
print wn.synset('snail.n.01').lowest_common_hypernyms(wn.synset('shark.n.01'))
