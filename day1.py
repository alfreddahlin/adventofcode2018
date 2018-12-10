import numpy as np

input_data = open('day1.in','r').read().strip().split('\n') 

freq_delta = [int(number) for number in input_data]
print('Part 1:', sum(freq_delta))

# Part 2

index = 0
freq_current = 0
freq_history = set()
while freq_current not in freq_history:
    freq_history.add(freq_current)
    freq_current += freq_delta[index]
    index=(index+1)%len(freq_delta)
print('Part 2:', freq_current)

'''
freq = np.cumsum(freq_delta)

freq_repeat = None
index = 0
while freq_repeat == None:
    if freq[index] in freq[0:index]:
        freq_repeat = freq[index]
        break
    index+=1
    if index >= len(freq):
        freq=np.append(freq,freq[-1]+np.cumsum(freq_delta))
print(freq_repeat)
'''
