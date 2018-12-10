import re

input_data = open('day10.in','r').read().strip()

points = re.findall(r'< ?(-?\d+), +(-?\d+)>[\s\S]*?< ?(-?\d+), +(-?\d+)',input_data)
points = [tuple(map(int,point)) for point in points]

size = float('inf')
new_size = size
sec = -1

while new_size <= size:
    sec += 1
    size = new_size
    new_points = [(point[0]+point[2],point[1]+point[3],point[2],point[3]) for point in points]
    x_coords,y_coords,x_speed,y_speed = zip(*new_points)
    x_min_new,x_max_new = min(x_coords),max(x_coords)
    y_min_new,y_max_new = min(y_coords),max(y_coords)
    new_size = (x_max_new-x_min_new)*(y_max_new-y_min_new)
    if new_size > size:
        print('Part 1:')
        for y in range(y_min-1,y_max+2):
            for x in range(x_min-1,x_max+2):
                if any([coord[0] == x and coord[1] == y for coord in points]):
                    print('#',end='')
                else:
                    print(' ',end='')
            print()
    points = new_points
    x_min,x_max,y_min,y_max = x_min_new,x_max_new,y_min_new,y_max_new
            
print('Part 2:',sec)
