import re
from collections import deque

input_data = open('day9.in','r').read().strip()

players,marbles = map(int,re.findall(r'\d+',input_data))

def get_score(players,marbles):
    circle = deque([0])
    scores = [0 for p in range(players)]
    for current_marble in range(1,marbles+1):
        if current_marble%23:
            circle.rotate(-1)
            circle.append(current_marble)
        else:
            circle.rotate(7)
            scores[current_marble%players] += current_marble + circle.pop()
            circle.rotate(-1)
    return max(scores)

print('Part 1:',get_score(players,marbles))
print('Part 2:',get_score(players,100*marbles))

'''
def get_score(players,marbles):
    circle = {0:[0,0]}
    scores = [0 for p in range(players)]
    current_pos = 0
    for current_marble in range(1,marbles+1):
        if current_marble%23:
            circle[current_marble] = [circle[current_pos][1],circle[circle[current_pos][1]][1]]
            circle[circle[current_marble][0]][1] = current_marble
            circle[circle[current_marble][1]][0] = current_marble
            current_pos = current_marble
        else:
            for i in range(7):
                current_pos = circle[current_pos][0]
            removed_marble = current_pos
            scores[current_marble%players] += current_marble + removed_marble
            circle[circle[removed_marble][0]][1] = circle[removed_marble][1]
            circle[circle[removed_marble][1]][0] = circle[removed_marble][0]
            current_pos = circle[removed_marble][1]
            circle.pop(removed_marble)
    return max(scores)
'''
