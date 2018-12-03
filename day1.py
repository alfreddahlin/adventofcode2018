import numpy as np

input_data = open('day1.txt','r').read().strip().split('\n') 

freq_delta = list(map(int,input_data))
print(sum(freq_delta))

# Part 2

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
