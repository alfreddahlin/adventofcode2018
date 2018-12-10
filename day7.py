import re

input_data = open('day7.in','r').read().strip().split('\n')

steps = [re.findall(r' ([A-Z]) ',line) for line in input_data]

def stepper(steps,workers):
    first,second = zip(*steps)
    letters = set(first+second)
    
    time_letter = {char: ord(char)-4 for char in letters}
    previous = {char: [step[0] for step in list(filter(lambda item: item[1]==char,steps))] for char in letters}
    
    left = letters
    queue = []
    working = {}
    order = ''
    current_time = 0
    while left or queue or working:
        for step in filter(lambda char: all([c in order for c in previous[char]]),left):
            queue.append(step)
        left.difference_update(queue)
        queue.sort()
        while len(working) < workers and queue:
            step = queue.pop(0)
            working[step] = current_time + time_letter[step]
        step_finished = min(working, key = working.get)
        order += step_finished
        current_time = working.pop(step_finished)
    return order,current_time

order,_ = stepper(steps,1)
print('Part 1:',order)

_,current_time = stepper(steps,5)
print('Part 2:',current_time)
