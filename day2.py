from itertools import compress

input_data = open('day2.in','r').read().strip().split('\n')

occurrances = [{letter: id.count(letter) for letter in set(id)} for id in input_data]

twos = sum([2 in id.values() for id in occurrances])
threes = sum([3 in id.values() for id in occurrances])
print('Part 1:', twos*threes)

# Part 2

for index in range(len(input_data)):
    for index2 in range(index+1,len(input_data)):
        match_list = [char1 == char2 for char1,char2 in zip(input_data[index],input_data[index2])]
        if match_list.count(False)==1:
            print('Part 2:', "".join(compress(input_data[index],match_list)))
