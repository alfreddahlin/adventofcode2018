import re

input_data = open('day5.in','r').read().strip()

def reduce(polymer):
    polymer_reduced = ''
    for char in polymer:
        if polymer_reduced and char == polymer_reduced[-1].swapcase():
            polymer_reduced = polymer_reduced[:-1]
        else:
            polymer_reduced += char
    return polymer_reduced

'''
def reduce(polymer):
    index = 0
    while index < len(polymer)-1:
        if polymer[index] == polymer[index+1].swapcase():
            polymer = polymer[:index]+polymer[index+2:]
            index = (index-1)*(index>0) # index = max(0,index-1)
        else:
            index += 1
    return polymer
'''

polymer=reduce(input_data)

print('Part 1:', len(polymer))

# Part 2

poly_reduced = {}
for char in set(polymer.lower()):
    poly = reduce(re.sub(char+'|'+char.upper(),'', polymer))
    poly_reduced[char] = (poly, len(poly))

print('Part 2:', min(poly_reduced.values(), key = lambda k: k[1])[1])
