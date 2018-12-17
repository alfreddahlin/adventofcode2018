import re

input_data = open('day16.in','r').read().strip().split('\n\n')

opcodes = [re.findall(r'(\d+)+',line) for line in input_data]
program = opcodes.pop(-1)

opcodes = [[list(map(int,codes[i:i+4])) for i in range(0,len(codes),4)] for codes in opcodes if codes]
program = [tuple(map(int,program[i:i+4])) for i in range(0,len(program),4)]

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

operations = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

print('Part 1:',sum([sum([op(code[1][1:],list(code[0])) == code[2] for op in operations]) > 2 for code in opcodes]))

# Part 2

lookup = {}
while len(lookup) < len(operations):
    for op in operations:
        if op in lookup.values():
            continue
        matches = {}
        for code in opcodes:
            code_id = code[1][0]
            if code_id in lookup:
                continue
            reg_in = list(code[0])
            reg_out = code[2]
            values = code[1][1:]
            if op(values,reg_in) == reg_out:
                matches[code_id] = matches.get(code_id,0) + 1
                match_id = code_id
        if len(matches) == 1 and matches[match_id] == len(list(filter(lambda code: code[1][0] == match_id, opcodes))):
            lookup[list(matches.keys())[0]] = op

reg = [0,0,0,0]
for op in program:
    reg = lookup[op[0]](op[1:],reg)
print('Part 2:',reg[0])
