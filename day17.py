import re

input_data = open('day17.in','r').read().strip().split('\n')

input_data = [re.findall(r'([xy])=(\d+[\.]*?)+, ([xy])=(\d+)..(\d+)',line) for line in input_data]
ground = set({(int(t[1]),r) if t[0] == 'x' else (r,int(t[1])) for l in input_data for t in l for r in range(int(t[3]),int(t[4])+1)})

def plot():
    for y in range(max(ground,key = lambda t: t[1])[1]+2):
        for x in range(min(ground)[0]-2,max(ground)[0]+3):
            if (x,y) in water:
                print('~',end='')
            elif (x,y) in passed:
                print('|',end='')
            elif (x,y) in ground:
                print('#',end='')
            elif (x,y) == source:
                print('+',end='')
            else:
                print('.',end='')
        print()
    return

def below(pos):
    return (pos[0],pos[1]+1)
def above(pos):
    return (pos[0],pos[1]-1)
def left(pos):
    return (pos[0]-1,pos[1])
def right(pos):
    return (pos[0]+1,pos[1])


def pour(source,depth):
    if not source or below(source) in passed:
        return
    front = below(source)
    while front not in ground and front not in water:
        passed.add(front)
        front = below(front)
        if front[1] > depth:
            return

    source_left = None
    source_right = None
    fill = []
    while not source_left and not source_right:
        front = above(front)
        passed.add(front)
        water.update(fill)
        fill = [front]
        source_left,passed_left = flow(front,left)
        source_right,passed_right = flow(front,right)
        fill.extend(passed_left+passed_right)
        pour(source_left,depth)
        pour(source_right,depth)
    return

def flow(front,direction):
    fill = []
    search = direction(front)
    while search not in ground:
        passed.add(search)
        if below(search) not in ground and below(search) not in water:
            return search,fill
        else:
            fill.append(search)
        search = direction(search)
    return None,fill

start = min(ground,key = lambda t: t[1])[1]
depth = max(ground,key = lambda t: t[1])[1]
source = (500,start-1)
water = set()
passed = set()
pour(source,depth)

print('Part 1:',len(passed))
print('Part 2:',len(water))
