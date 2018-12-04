from itertools import compress

input_data = open('day2.txt','r').read().strip().split('\n')

occurrances = [dict((letter,id.count(letter)) for letter in set(id)) for id in input_data]

twos = sum([2 in id.values() for id in occurrances])
threes = sum([3 in id.values() for id in occurrances])
print('Part 1: ' + str(twos*threes))

# Part 2

for index in range(len(input_data)):
    for index2 in range(index+1,len(input_data)):
        match_list = []
        for char1,char2 in zip(input_data[index],input_data[index2]):
            match_list.append(char1!=char2)
        if sum(match_list)==1:
            print('Part 2: ' + list(compress(input_data,match_list))[0])
