
import os

properties = {}
properties['country'] = {
    'capital',
    'largestCity',
    'legislature',
    'areaKm',
    'areaRank',
    'populationEstimate',
    'gdpPpp',
    'currency',
    'timeZone',
    'dateFormat',
    'anthem',
    'drivesOn',
    'animal',
    'bird',
    'flower'
}

properties['animal'] = {
    'phylum',
    'subphylum',
    'classis',
    'familia',
    'genus',
    'species'
}

properties['programming_languages'] = {
    'paradigm',
    'designer',
    'developer',
    'writtenIn',
    'influencedBy',
    'influenced',
    'latestReleaseVersion',
    'operatingSystem',
    'license'
}

print 'Categories present:'
for cat in properties.keys():
    print cat

print 
print 'Entities list:'
os.system('ls index')
print 
print 'Enter category entity'
inp = raw_input()
category,A = inp.split(' ')
path = './index/'


lines = []
with open(path+A) as f:
    lines = f.readlines()


diff_list = {}
for line in lines:
    line = line.strip()

    property = line.split(' ')[0]
    value = ' '.join(line.split(' ')[1:])

    if property in properties[category]:
            diff_list[property] = value

for property,value in diff_list.items(): 
    print "%-25s %40s" % (property,value)

'''
diff_list = {}
for line in lines:
    line = line.strip()
    property = line.split(' ')[0]
    value = ' '.join(line.split(' ')[1:])
    if property in properties[category]:
            diff_list[property] = (value,None)

with open(path+B) as f:
    lines = f.readlines()


for line in lines:
    line = line.strip()
    property = line.split(' ')[0]
    value = ' '.join(line.split(' ')[1:])
    if property in properties[category]:
        if property in diff_list:
            diff_list[property] = (diff_list[property][0],value)

for property,values in diff_list.items(): 
    print "%-25s %40s %40s" % (property,values[0],values[1])
'''




