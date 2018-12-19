from itertools import product

input_data = open('day18.in','r').read().strip().split('\n')
max_x,max_y = len(input_data[0]),len(input_data)
acres = {(int(x),int(y)): input_data[y][x] for x,y in product(range(max_x),range(max_y)) if input_data[y][x] in '|#'}

woods = {a for a in acres if acres[a] == '|'}
lumber = {a for a in acres if acres[a] == '#'}

def plot():
    for y in range(max_y):
        for x in range(max_x):
            if (x,y) in woods:
                print('|',end='')
            elif (x,y) in lumber:
                print('#',end='')
            else:
                print('.',end='')
        print()
    print()
    return

def get_nearby(pos):
    nearby = [(a in woods,a in lumber) for a in product(range(pos[0]-1,pos[0]+2),range(pos[1]-1,pos[1]+2)) if a != pos]
    near_wood,near_lumber = zip(*nearby)
    return (sum(near_wood),sum(near_lumber))

values = set()
consecutive = []
iterations = 1000000000

for minute in range(1,iterations+1):
    new_woods = set()
    new_lumber = set()
    new_clear = set()
    for pos in product(range(max_x),range(max_y)):
        near_wood,near_lumber = get_nearby(pos)
        if pos in woods:
            if near_lumber > 2:
                new_lumber.add(pos)
            else:
                new_woods.add(pos)
        elif pos in lumber and near_wood > 0 and near_lumber > 0:
            new_lumber.add(pos)
        elif pos not in woods and pos not in lumber and near_wood > 2:
            new_woods.add(pos)
    
    woods = new_woods
    lumber = new_lumber
    clear = new_clear
    value = len(woods)*len(lumber)
    if minute == 10:
        print('Part 1:',value)
    if value in values:
        if first == (woods,lumber) and value == consecutive[0]:
            print('Part 2:',consecutive[(iterations-minute) % len(consecutive)])
            break
        else:
            consecutive.append(value)
    else:
        consecutive = [value]
        first = (woods,lumber)
    values.add(value)

