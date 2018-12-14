
input_data = open('day13.in','r').read().split('\n')

orientations = ['^','<','v','>']
straight = {orientations[i]: orientations[i] for i in range(len(orientations))}
left = {orientations[i]: orientations[(i+1)%4] for i in range(len(orientations))}
right = {orientations[i]: orientations[(i-1)%4] for i in range(len(orientations))}
turn_forward = {'^':right,'v':right,'<':left,'>':left}
turn_backward = {'^':left,'v':left,'<':right,'>':right}
turn_straight = {'^':straight,'v':straight,'<':straight,'>':straight}
turn_order = [left,straight,right]
turn_type = {'/':turn_forward,'\\':turn_backward,'|':turn_straight,'-':turn_straight,'+':turn_order}
travel = {'^':(0,-1),'<':(-1,0),'v':(0,1),'>':(1,0)}

tracks = {(x,y): input_data[y][x] for y in range(len(input_data)) for x in range(len(input_data[y])) if input_data[y][x] != ' '}
carts = {(pos): [tracks[pos],0,0] for pos in tracks if any([tracks[pos] == char for char in orientations])}

for pos in carts:
    orientation = carts[pos][0]
    if orientation in '^v':
        tracks[pos] = '|'
    elif orientation in '<>':
        tracks[pos] = '-'

def move_cart(pos,props):
    pos = tuple(p+dp for p,dp in zip(pos,travel[props[0]]))
    track = tracks[pos]
    if track == '+':
        props[0] = turn_type[track][props[1]][props[0]]
        props[1] = (props[1]+1) % 3
    else:
        props[0] = turn_type[track][props[0]][props[0]]
    props[2] += 1
    return pos,props

tick = 0
collided = False
while len(carts) > 1 or list(carts.values())[0][2] < tick:
    cart = min(carts, key = lambda t: (carts[t][2],t[0],t[1]))
    pos,props = move_cart(cart,carts.pop(cart))
    if not carts.pop(pos,False):
        carts[pos] = props
    else:
        tick = props[2]
        if not collided: # Part 1
            collided = True
            print('Part 1:',pos)

print('Part 2:',list(carts)[0])
