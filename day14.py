
input_data = open('day14.in','r').read().strip()#.split('\n')

recipes = input_data

score = '37'
elf1 = 0
elf2 = 1
while recipes not in score[-7:]:
    score += str(int(score[elf1]) + int(score[elf2]))
    elf1 = (elf1 + int(score[elf1]) + 1) % len(score)
    elf2 = (elf2 + int(score[elf2]) + 1) % len(score)
print('Part 1:', score[int(recipes):int(recipes)+11])
print('Part 2:', score.index(recipes,len(score)-7))

'''# Just slightly faster
rec_len = len(recipes)
score = '37'
elf1 = 0
elf2 = 1
while recipes not in score[-rec_len-1:]:
    elf1_score = int(score[elf1])
    elf2_score = int(score[elf2])
    score += str(elf1_score+elf2_score)
    score_len = len(score)
    elf1 = (elf1+elf1_score+1) % score_len
    elf2 = (elf2+elf2_score+1) % score_len
print('Part 1:',score[int(recipes):int(recipes)+11])
print('Part 2:',score.index(recipes,score_len-7))
'''
