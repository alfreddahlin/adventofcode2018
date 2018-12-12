from itertools import product

input_data = open('day11.in','r').read().strip()

serial = int(input_data)

def get_power(x,y):
    rack_id = x+10
    power = (rack_id*y+serial)*rack_id
    power = power//100 % 10
    power = power-5
    return power

# Generate grid with power levels
grid = {(x,y): get_power(x,y) for x,y in product(range(1,301),repeat=2)}

# Generate inverted cumulative sum of each grid element (inverted to simplify indexing since top left is defined as the squares position
grid_sum = {}
for x,y in product(range(300,0,-1),repeat=2):
    grid_sum[(x,y)] = grid[(x,y)] + grid_sum.get((x+1,y), 0) + grid_sum.get((x,y+1), 0) - grid_sum.get((x+1,y+1), 0)

# Calculate total power for every possible square
power_max = 0
for size in range(1,301):
    for x,y in product(range(1,302-size),repeat=2):
        power = grid_sum[(x,y)] + grid_sum.get((x+size,y+size), 0) - grid_sum.get((x+size,y), 0) - grid_sum.get((x,y+size), 0)
        if power > power_max:
            if size == 3: # To save Part 1 answer, assumes 3x3 is better than 1x1 and 2x2
                max_point_3x3 = (x,y)
            power_max = power
            max_point = (x,y,size)

'''
previous = {(x,y): 0 for x,y in product(range(1,301),repeat=2)}
power_max = 0
for size in range(1,301):
    for x,y in product(range(1,302-size),repeat=2):
        power = previous[(x,y)] + sum([grid[(x+s,y+size-1)] for s in range(size)]) + sum([grid[(x+size-1,y+s)] for s in range(size-1)])
        previous[(x,y)] = power
        if power > power_max:
            if size == 3:
                power_max_3x3 = (x,y)
            power_max = power
            max_point = (x,y,size)
'''

print('Part 1:',max_point_3x3)
print('Part 2:',max_point)
