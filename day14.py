
input_data = open('day14.in','r').read().strip()#.split('\n')

recipes = input_data

score = '37'
elf1,elf2 = 0,1
while recipes not in score[-7:]:
    score += str(int(score[elf1]) + int(score[elf2]))
    elf1 = (elf1 + int(score[elf1]) + 1) % len(score)
    elf2 = (elf2 + int(score[elf2]) + 1) % len(score)

print('Part 1:', score[int(recipes):int(recipes)+10])
print('Part 2:', score.index(recipes,len(score)-7))

'''
# Just slightly faster
rec_len = len(recipes)
score = '37'
elf1 = 0
elf2 = 1
while recipes not in score[-rec_len-1:]:
    elf1_score = int(score[elf1])
    elf2_score = int(score[elf2])
    score += str(elf1_score+elf2_score)
    score_len = len(score)
    elf1 += elf1_score+1
    elf1 %= score_len
    elf2 += elf2_score+1
    elf2 %= score_len
print('Part 1:',score[int(recipes):int(recipes)+10])
print('Part 2:',score.index(recipes,score_len-7))

rec_len = len(recipes)
score = [3,7]
elf1 = 0
elf2 = 1
rec_int = [int(i) for i in recipes]
while True:
    elf1_score = score[elf1]
    elf2_score = score[elf2]
    total_score = elf1_score + elf2_score
    score.extend(divmod(total_score,10) if total_score>9 else [total_score])
    score_len = len(score)
    elf1 += elf1_score+1
    elf1 %= score_len
    elf2 += elf2_score+1
    elf2 %= score_len
    if (total_score > 9 and rec_int == score[-rec_len-1:-1]) or rec_int == score[-rec_len:]:
        break
print('Part 1:',"".join([str(i) for i in score[int(recipes):int(recipes)+10]]))
print('Part 2:',len(score)-7+"".join([str(i) for i in score[-7:]]).index(recipes))

print(time2-time0,time2-time2,time3-time2)
'''
