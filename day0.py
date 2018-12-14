import re

input_data = open('day10.in','r').read().strip()#.split('\n')

#data = [re.findall(r'exp',line) for line in input_data]
data = re.findall(r'\d+',input_data)

print(data)

for line in data:
    print(line)
    
