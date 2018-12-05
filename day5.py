import re

input_data = open('day5.txt','r').read().strip()

polymer = input_data
#polymer = 'dabAcCaCBAcCcaDA'

def reduce(polymer):
    index = 0
    while index < len(polymer)-1:
        if abs(ord(polymer[index])-ord(polymer[index+1]))==32:
            polymer = polymer[:index]+polymer[index+2:]
            index = (index-1)*(index>0) # index = max(0,index-1)
        else:
            index += 1
    return polymer

print('Part 1:', len(reduce(polymer)))

# Part 2

poly_reduced = {}
for char in set(polymer.lower()):
    poly = reduce(re.sub(char+'|'+char.upper(),'', polymer))
    poly_reduced[char] = (poly, len(poly))

print('Part 2:', poly_reduced[min(poly_reduced, key = lambda k: poly_reduced[k][1])][1])

