
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

print 'Enter two entities'
inp = raw_input()
A,B = inp.split(' ')
category = 'country'
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





