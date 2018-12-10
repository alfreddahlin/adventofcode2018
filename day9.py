import re

input_data = open('day9.in','r').read().strip()
#input_data = '9 players; last marble is worth 25 points'
#input_data = '10 players; last marble is worth 1618 points'


data = re.findall(r'\d+',input_data)

players = int(data[0])
marbles = int(data[1])

def get_score(players,marbles):
    circle = {0:[0,0]}
    scores = [0 for p in range(players)]
    current_pos = 0
    current_player = 0
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
            scores[current_player] += current_marble + removed_marble
            circle[circle[removed_marble][0]][1] = circle[removed_marble][1]
            circle[circle[removed_marble][1]][0] = circle[removed_marble][0]
            current_pos = circle[removed_marble][1]
            circle.pop(removed_marble)
        current_player = (current_player+1)%players
    return max(scores)

print('Part 1:',get_score(players,marbles))
print('Part 2:',get_score(players,100*marbles))
