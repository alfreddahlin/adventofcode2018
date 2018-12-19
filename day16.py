import re

input_data = open('day16.in','r').read().strip().split('\n\n')

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

opcodes = [re.findall(r'(\d+)+',line) for line in input_data]
program = opcodes.pop(-1)

instructions = [[list(map(int,codes[i:i+4])) for i in range(0,len(codes),4)] for codes in opcodes if codes]
program = [tuple(map(int,program[i:i+4])) for i in range(0,len(program),4)]

operations = set([addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr])

op_lookup = {}

possibles = []
for reg_in,instruction,reg_out in instructions:
    opcode = instruction[0]
    values = instruction[1:]
    possibles.append(set(op for op in operations if op(values,list(reg_in)) == reg_out))
    op_lookup[opcode]= possibles[-1].intersection(op_lookup.get(opcode,operations))
    
print('Part 1:',sum([len(possible) > 2 for possible in possibles]))

while not all([len(v) == 1 for v in op_lookup.values()]):
    for code,unique in op_lookup.items():
        if len(unique) == 1:
            op_lookup.update({op: possible.difference(unique) for op,possible in op_lookup.items() if code != op})

op_lookup = {opcode: op.pop() for opcode,op in op_lookup.items()}

reg = [0,0,0,0]
for code in program:
    reg = op_lookup[code[0]](code[1:],reg)
print('Part 2:',reg[0])

'''
matches = [[op(code[1:],list(reg_in)) == reg_out for op in operations] for reg_in,code,reg_out in instructions]
print('Part 1:',sum([sum(match) > 2 for match in matches]))
#print('Part 1:',sum([sum([op(code[1:],list(reg_in)) == reg_out for op in operations]) > 2 for reg_in,code,reg_out in instructions]))

# Part 2

lookup = {}
while len(lookup) < len(operations):
    for op in operations:
        if op in lookup.values():
            continue
        matches = {}
        for reg_in,code,reg_out in instructions:
            code_id = code[0]
            values = code[1:]
            if code_id in lookup:
                continue
            if op(values,list(reg_in)) == reg_out:
                matches[code_id] = matches.get(code_id,0) + 1
                match_id = code_id
        if len(matches) == 1 and matches[match_id] == len(list(filter(lambda code: code[1][0] == match_id, instructions))):
            lookup[list(matches.keys())[0]] = op
            
reg = [0,0,0,0]
for code in program:
    reg = lookup[code[0]](code[1:],reg)
print('Part 2:',reg[0])
'''
