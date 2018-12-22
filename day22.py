from itertools import product
import re

input_data = open('day22.in','r').read().strip()

depth,target_x,target_y = re.findall(r'-?\d+',input_data)
depth = int(depth)
target = (int(target_x),int(target_y))
#depth,target = 510,(10,10)

def get_erosion(x,y):
    if x == 0:
        geo_index = (y*48271)
    elif y == 0:
        geo_index = (x*16807)
    elif (x,y) == target:
        geo_index = 0
    else:
        geo_index = cave[(x-1,y)]*cave[(x,y-1)]
    erosion = (geo_index + depth) % 20183
    cave[(x,y)] = erosion
    return

def add_cave(index,times = 1):
    for i in range(times):
        if index:
            for x in range(cave_size[0]):
                get_erosion(x,cave_size[1])
        else:
            for y in range(cave_size[1]):
                get_erosion(cave_size[0],y)
        cave_size[index] += 1
        
        
def get_adjacent(pos):
    return [(x,y) for x,y in product(range(pos[0]-1,pos[0]+2),range(pos[1]-1,pos[1]+2)) if 0<=x and 0<=y and abs(pos[0]-x) + abs(pos[1]-y) == 1]

def get_new_step(queue,step,target):
    return

def get_path(cave,target):
    current_step = (0,0,1)
    seen = set([current_step])
    queue = {current_step: 0}
    while current_step[:-1] != target:
        current_step = min(queue,key = lambda k: queue[k]+abs(target[0]-k[0])+abs(target[1]-k[1])+7*(k[2]!=1))
        current_cost = queue.pop(current_step)
        new_paths = {}
        for new_pos in get_adjacent(current_step):
            e = current_step[2]
            current_pos = current_step[:-1]
            change_cost = 0
            if new_pos[0] >= cave_size[0]:
                add_cave(0)
            elif new_pos[1] >= cave_size[1]:
                add_cave(1)
            if e != cave[new_pos]%3:
                change_cost = 0
            elif abs(cave[current_pos]%3-cave[new_pos]%3) == 1:
                e = (min(cave[current_pos]%3,cave[new_pos]%3)-1) % 3
                change_cost = 7
            elif abs(cave[current_pos]%3-cave[new_pos]%3) == 2:
                e = 1
                change_cost = 7
            new_step = (new_pos[0],new_pos[1],e)
            new_cost = current_cost+1 + change_cost
            if new_step not in seen:
                new_paths.update({new_step: new_cost})
            elif new_step in queue:
                new_paths.update({new_step: min(queue[new_step],new_cost)})
        queue.update(new_paths)
        seen.update(new_paths.keys())
    if current_step[2] != 1:
        current_cost += 7
        current_step = (current_step[0],current_step[1],1)
    return current_cost

cave = {(0,0): 0}
cave_size = [1,1]
add_cave(0,target[0])
add_cave(1,target[1])

print('Part 1:',sum(v%3 for v in cave.values()))

print('Part 2:',get_path(cave,target))
