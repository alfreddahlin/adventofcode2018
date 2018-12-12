import re

input_data = open('day12.in','r').read().strip().split('\n')

initial_state = re.findall(r'[.#]+',input_data[0])[0]
notes = [re.findall(r'([.#]+) => ([.#])',line)[0] for line in input_data[2:]]
notes = {note[0]: note[1] for note in notes}

def get_pot_sum(state,zero_pos):
    return sum([pot-zero_pos for pot in range(len(state)) if state[pot] == '#'])

def generate(state,generations):
    first, last = state.index('#'), state.rindex('#')
    state = '.'*4+state[first:last+1]+'.'*4
    zero_pos = 4-first

    for gen in range(generations):
        new_state = "".join([notes.get(state[pos-2:pos+3],'.') for pos in range(2,len(state)-2)])
        first, last = new_state.index('#'), new_state.rindex('#')
        new_state = '.'*4+new_state[first:last+1]+'.'*4
        new_zero_pos = zero_pos+2-first

        if state == new_state:
            zero_pos += (new_zero_pos-zero_pos)*(generations-gen)
            return state,zero_pos

        state = new_state
        zero_pos = new_zero_pos
    return state,zero_pos

state,zero_pos = generate(initial_state,20)
print('Part 1:',get_pot_sum(state,zero_pos))

state,zero_pos = generate(initial_state,50000000000)
print('Part 2:',get_pot_sum(state,zero_pos))
