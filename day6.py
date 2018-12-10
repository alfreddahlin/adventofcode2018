import re
from itertools import product

input_data = open('day6.in','r').read().strip().split('\n')

coords = [tuple(map(int,re.findall(r'(\d+), (\d+)', line)[0])) for line in input_data]
x_lim,y_lim = [(min(c),max(c)) for c in zip(*coords)]

danger_size = {point: 0 for point in coords}
safe_size = 0

for x,y in product(range(x_lim[0],x_lim[1]+1), range(y_lim[0],y_lim[1]+1)):
    closest = min(coords, key = lambda k: abs(k[0]-x)+abs(k[1]-y))
    if x in x_lim or y in y_lim:
        danger_size[closest] = float('NaN')
    else:
        danger_size[closest] += 1

# Part 2

    distance = sum([abs(point[0]-x)+abs(point[1]-y) for point in coords])
    if distance < 10000:
        safe_size += 1

print('Part 1:', max(danger_size.values()))

print('Part 2:', safe_size)
