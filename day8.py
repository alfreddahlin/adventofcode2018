import re

input_data = open('day8.in','r').read().strip().split(' ')
input_data = [int(data) for data in input_data]

def get_meta(data, key = 'sum'):
    num_child = data.pop(0)
    num_meta = data.pop(0)
    meta_sum = []
    for child in range(num_child):
        data,meta_child = get_meta(data, key = key)
        meta_sum.append(meta_child)
    if num_child == 0 or key == 'sum':
        return data[num_meta:],sum(data[:num_meta])+sum(meta_sum)
    return data[num_meta:],sum([meta_sum[i-1] if i <= num_child and i > 0 else 0 for i in data[:num_meta]])

_,meta_sum = get_meta(list(input_data))
print('Part 1:',meta_sum)

# Part 2

_,meta_value = get_meta(list(input_data), key = 'value')
print('Part 2:',meta_value)


'''
def get_sum(data):
    num_child = data.pop(0)
    num_meta = data.pop(0)
    meta_sum = 0
    for child in range(num_child):
        data,meta_child = get_sum(data)
        meta_sum += meta_child
    return data[num_meta:],sum(data[:num_meta])+meta_sum
'''
