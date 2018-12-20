import re

input_data = open('day20.in','r').read().strip()#.split('\n')

facility = input_data[1:-1]
head = {'N': (0,-1), 'S': (0,1), 'W': (-1,0), 'E': (1,0)} 

rooms = {(0,0): 0}
def get_rooms(branch,pos=(0,0)):
    global coordinates
    moved_pos = pos
    while branch:
        c = branch.pop(0)
        if c == '(':
            branch = get_rooms(branch,moved_pos)
        elif c == '|':
            moved_pos = pos
        elif c == ')':
            return branch
        else:
            new_pos = (moved_pos[0] + head[c][0], moved_pos[1] + head[c][1])
            rooms[new_pos] = rooms.get(new_pos,rooms[moved_pos]+1)
            moved_pos = new_pos
    return branch

depth = 1000
get_rooms(list(facility))

print('Part 1:', max(rooms.values()))
print('Part 2:', sum([value >= depth for value in rooms.values()]))

'''
def get_path(branch):
    long_path =['']
    path_index = 0
    index = 0
    while index < len(branch):
        heading = branch[index]
        if heading == '(':
            long_branch,branch_index = get_path(branch[index+1:])
            long_path[path_index] += long_branch
            index += branch_index
        elif heading == '|':
            long_path.append('')
            path_index += 1
        elif heading == ')':
            if long_path[path_index] == '':
                return '',index+1
            return max(long_path,key=lambda e: len(e)),index+1
        else:
            long_path[path_index] += heading
        index += 1
    return max(long_path,key=lambda e: len(e)),None

path,_ = get_path(facility)

print('Part 1:',len(path),'(Original)')

# Part 2 not working

def get_path(branch,doors=0):
    global depth
    branch_doors = [0]
    branch_rooms = [0]
    while branch:
        head = branch.pop(0)
        if head == '(':
            branch,new_doors,new_rooms = get_path(branch,doors+branch_doors[-1])
            branch_doors[-1] += new_doors
            branch_rooms[-1] += new_rooms
        elif head == '|':
            branch_doors.append(0)
            branch_rooms.append(0)
        elif head == ')':
            if branch_doors[-1] == 0:
                return branch,0,max(sum(branch_rooms[:-1])-sum(branch_doors[:-1])/2,0)
            return branch,max(branch_doors),sum(branch_rooms)
        else:
            branch_doors[-1] += 1
            branch_rooms[-1] += (branch_doors[-1]+doors) >= depth
    return [],max(branch_doors),sum(branch_rooms)

_,doors,rooms = get_path(list(facility))

print('Part 1:',doors)
print('Part 2:',rooms,'(Why won\'t you work?!)')
'''
