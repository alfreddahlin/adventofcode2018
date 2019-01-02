from itertools import product
import re

input_data = open('day23.in','r').read().strip().split('\n')

data = [re.findall(r'-?\d+',line) for line in input_data]
bots = {(int(x),int(y),int(z)): int(r) for x,y,z,r in data}


def get_distance(pos,target):
    return sum(abs(c1-c2) for c1,c2 in zip(pos,target))

def get_corners(bot,r):
    return {(bot[0]+x,bot[1]+y,bot[2]+z): bot for x,y,z in [(-r,0,0),(r,0,0),(0,-r,0),(0,r,0),(0,0,-r),(0,0,r)]}

r_max = ((0,0,0),0)
for bot,r in bots.items():
    if r > r_max[1]:
        in_range = sum(get_distance(bot,b) <= r for b in bots)
        r_max = ((bot),r)

print('Part 1:',in_range)
bots_corners = {}
{bots_corners.update(get_corners(bot,r)) for bot,r in bots.items()}

r_max = ((0,0,0),0)
for pos in bots_corners:
    n = sum(get_distance(pos,bot)<=r for bot,r in bots.items())
    if n>=r_max[1]:
        if n == r_max[1] and sum(r_max[0]) < sum(pos):
            continue
        r_max = (pos,n)
bot_max = bots_corners[r_max[0]]
corner_max = r_max[0]

r_final = []
for dx,dy,dz in [(dx,dy,dz) for dx,dy,dz in product([-1,0,1],repeat=3) if dx**2+dy**2+dz**2 == 2]:
    pos = corner_max
    r_max = ((0,0,0),0)
    n = r_max[1]
    while n >= r_max[1] and dx < 10000:
        n = sum(get_distance(pos,bot)<=r for bot,r in bots.items())
        if n>=r_max[1]:
            if n == r_max[1] and sum(r_max[0]) <= sum(pos):
                pass
            else:
                r_max = (pos,n)
        pos = (pos[0]+dx,pos[1]+dy,pos[2]+dz)
    r_final.append(r_max)

r_max = max(r_final,key = lambda k: (k[1],sum(k[0])))
print('Part 2:',sum(r_max[0]))
