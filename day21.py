import re

input_data = open('day21.in','r').read().strip().split('\n')

def addr(values,reg):
    reg[values[2]] = reg[values[0]]+reg[values[1]]
    return reg
def addi(values,reg):
    reg[values[2]] = reg[values[0]]+values[1]
    return reg
def mulr(values,reg):
    reg[values[2]] = reg[values[0]]*reg[values[1]]
    return reg
def muli(values,reg):
    reg[values[2]] = reg[values[0]]*values[1]
    return reg

def banr(values,reg):
    reg[values[2]] = reg[values[0]]&reg[values[1]]
    return reg
def bani(values,reg):
    reg[values[2]] = reg[values[0]]&values[1]
    return reg
def borr(values,reg):
    reg[values[2]] = reg[values[0]]|reg[values[1]]
    return reg
def bori(values,reg):
    reg[values[2]] = reg[values[0]]|values[1]
    return reg

def setr(values,reg):
    reg[values[2]] = reg[values[0]]
    return reg
def seti(values,reg):
    reg[values[2]] = values[0]
    return reg

def gtir(values,reg):
    reg[values[2]] = values[0] > reg[values[1]]
    return reg
def gtri(values,reg):
    reg[values[2]] = reg[values[0]] > values[1]
    return reg
def gtrr(values,reg):
    reg[values[2]] = reg[values[0]] > reg[values[1]]
    return reg

def eqir(values,reg):
    reg[values[2]] = values[0] == reg[values[1]]
    return reg
def eqri(values,reg):
    reg[values[2]] = reg[values[0]] == values[1]
    return reg
def eqrr(values,reg):
    reg[values[2]] = reg[values[0]] == reg[values[1]]
    return reg

ip_reg = int(re.findall(r'\d+',input_data.pop(0))[0])
instructions = [re.findall(r'([a-z]+) (\d+) (\d+) (\d+)',line)[0] for line in input_data]
instructions = [(eval(i[0]),tuple(map(int,i[1:]))) for i in instructions]

def run_instructions(reg):
    ip = reg[ip_reg]
    seen = {}
    count = 0
    while ip < len(instructions):
        reg = instructions[ip][0](instructions[ip][1],reg)
        if ip == 17: # Skip loop, initiate counter to target instead of 0
            count_reg = instructions[17][1][2]
            target_reg = instructions[20][1][1] 
            reg[count_reg] = reg[target_reg]//256
        reg[ip_reg] += 1
        ip = reg[ip_reg]
        count += 1
        if ip == 28:
            if reg[3] in seen:
                return seen
            seen[reg[3]] = count
    return seen

seen = run_instructions([0,0,0,0,0,0])

min_count = min(seen,key= lambda k: seen[k])
max_count = max(seen,key= lambda k: seen[k])
print('Part 1:',min_count)
print('Part 2:',max_count)
