import re

input_data = open('day19.in','r').read().strip().split('\n')

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
    ip = 0
    seen = set()
    while ip not in seen:
        seen.add(ip)
        reg = instructions[ip][0](instructions[ip][1],reg)
        reg[ip_reg] += 1
        ip = reg[ip_reg]
    number = max(reg)
    summed = 0
    for i in range(1,number+1):
        if number%i == 0:
            summed += i
    return summed

answer1 = run_instructions([0,0,0,0,0,0])
print('Part 1:',answer1)
answer2 = run_instructions([1,0,0,0,0,0])
print('Part 2:',answer2)
