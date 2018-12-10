import re

input_data = open('day0.txt','r').read().strip().split('\n')

data = [re.findall(r'exp',line) for line in input_data]

print(data)

for line in data:
    print(line)
    
