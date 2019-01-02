import re

input_data = open('day25.in','r').read().strip().split('\n')

data = [tuple(map(int,line.split(','))) for line in input_data]

def get_distance(pos,target):
    return sum(abs(c1-c2) for c1,c2 in zip(pos,target))

constellations = {}

for pos in data:
    member = set()
    [member.add(const_id) for const_id,points in constellations.items() for point in points if get_distance(pos,point) < 4]
    new_sign = set([pos])
    [new_sign.update(new_sign.union(constellations.pop(i))) for i in member]
    constellations[pos] = new_sign

print('Part 1:',len(constellations))
