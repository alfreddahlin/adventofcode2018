import re

input_data = open('day25.in','r').read().strip().split('\n')

data = [tuple(map(int,line.split(','))) for line in input_data]

def get_distance(pos,target):
    return sum(abs(c1-c2) for c1,c2 in zip(pos,target))

constellations = {}

for n,pos in enumerate(data):
    member = set()
    [member.add(sign) for sign,points in constellations.items() for point in points if get_distance(pos,point) < 4]
    new_sign = set([pos])
    [new_sign.update(new_sign.union(constellations.pop(i))) for i in member]
    constellations[n] = new_sign

print(constellations.keys())
print('Part 1:',len(constellations))
