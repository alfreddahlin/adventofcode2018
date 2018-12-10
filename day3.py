import re
import numpy as np
input_data = open('day3.in','r').read().strip().split('\n')

claims = [list(map(int,re.findall(r'([0-9]+)',claim))) for claim in input_data]

fabric = np.zeros((1000,1000))

for nr,x,y,xr,yr in claims:
    fabric[x:(x+xr),y:(y+yr)]+=1
print('Part 1:', (fabric>1).sum())

# Part 2
unique_claim = []
for nr,x,y,xr,yr in claims:
    if((fabric[x:(x+xr),y:(y+yr)]!=1).sum()==0):
        unique_claim.append(nr)
print('Part 2:', unique_claim[0])
