from itertools import product
import copy

input_data = open('day15.in','r').read().strip().split('\n')

initial_cave = {(x,y): '.' for x,y in product(range(len(input_data[0])),range(len(input_data))) if input_data[y][x] == '.'}
initial_units = {(x,y): {'race': input_data[y][x],'health': 200,'damage':3,'tick':0} for x,y in product(range(len(input_data[0])),range(len(input_data))) if input_data[y][x] in 'EG'}

def move(pos):
    stats = units.pop(pos)
    targets = [get_nearby(unit) for unit in units if units[unit]['race'] != stats['race']]
    new_pos = get_path(pos,[point for points in targets for point in points])
    new_pos = new_pos[0]
    attack(new_pos,stats)
    stats['tick'] += 1
    units[new_pos] = stats
    if new_pos != pos:
        cave[pos] = cave.pop(new_pos)
    return new_pos

def attack(pos,stats):
    nearby = [point for point in get_nearby(pos) if point in units and stats['race'] != units[point]['race']]
    if nearby:
        closest = min(nearby, key = lambda k: (units[k]['health'],k[1],k[0]))
        units[closest]['health'] -= stats['damage']
        if units[closest]['health'] < 1:
            units.pop(closest)
            cave[closest] = '.'
        return True
    return False

def get_path(pos,targets):
    if pos in targets:
        return [pos]
    else:
        targets = [target for target in targets if target in cave]
        queue = set([step for step in get_nearby(pos) if step in cave])
        seen = set(queue)
        path = {i: [] for i in queue}
        path_short = []
        while queue:
            next_step = min(queue,key = lambda p: (len(path[p]),path[p][0][1],path[p][0][0]) if path[p] else (0,p[1],p[0]))
            new_steps = [step for step in get_nearby(next_step) if step in cave and (step not in seen or step in path)]
            path[next_step].append(next_step)
            path.update({step: path.get(step,list(path[next_step])) for step in new_steps})
            if path_short and len(path[next_step]) > len(path_short[0]):
                return min(path_short,key = lambda p: (len(p),p[-1][1],p[-1][0]))
            elif next_step in targets:
                path_short.append(path[next_step])
            path.pop(next_step)
            queue.update([step for step in new_steps if step not in seen])
            seen.update(new_steps)
            queue.remove(next_step)
        return [pos] if not path_short else path_short[0]

def get_nearby(pos):
    px = pos[0]
    py = pos[1]
    return [(x,y) for x,y in product(range(px-1,px+2),range(py-1,py+2)) if abs(x-px+y-py) == 1]

def plot():
    for y in range(max(cave,key = lambda k: k[1])[1]+2):
        units_row = ''
        for x in range(max(cave,key = lambda k: k[0])[0]+2):
            if (x,y) in units:
                print(units[(x,y)]['race'],end='')
                units_row += units[(x,y)]['race']+'('+str(units[(x,y)]['health'])+'), '
            elif (x,y) in cave:
                print('.',end='')
            else:
                print('#',end='')
        print('  '+units_row)
    return

num_elves = sum([stats['race'] == 'E' for stats in initial_units.values()])
damage = [5,20]
attempt = 3
while damage[0] != damage[1]:
    cave = copy.deepcopy(initial_cave)
    units = copy.deepcopy(initial_units)
    for unit in units:
        if units[unit]['race'] == 'E':
            units[unit]['damage'] = attempt
    while not all([stats['race'] == list(units.values())[0]['race'] for stats in units.values()]):
        unit = min(units, key = lambda k: (units[k]['tick'],k[1],k[0]))
        move(unit)
        if sum([stats['race'] == 'E' for stats in units.values()]) < num_elves and attempt != 3:
            damage[0] = attempt+1
            break
    if attempt >= damage[0]:
        damage[1] = attempt
    if attempt == 3:
        tick = min(units.values(),key = lambda k: k['tick'])['tick']
        health = sum([units[unit]['health'] for unit in units])
        print('Part 1:',tick*health)
    attempt = damage[0]+int((damage[1]-damage[0])/2)

tick = min(units.values(),key = lambda k: k['tick'])['tick']
health = sum([units[unit]['health'] for unit in units])
print('Part 2:',tick*health)
