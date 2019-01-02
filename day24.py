import re
import copy

input_data = [section.split('\n') for section in open('day24.in','r').read().strip().split('\n\n')]

data = [[re.findall(r'(\d+)[\s\S]+?(\d+)[\s\S]+?(?:\(([\s\S]+?)\)[\s\S]+?)?(\d+) ([a-z]+)[\s\S]+?(\d+)',group) for group in army] for army in input_data]
data = [[re.findall(r'(\d+) units each with (\d+) hit points (?:\(([\s\S]+?)\))? ?with an attack that does (\d+) ([a-z]+) damage at initiative (\d+)',group) for group in army] for army in input_data]

groups_initial = {}
groups_initial.update({int(group[0][-1]): {'units': int(group[0][0]),'HP': int(group[0][1]),'immune': set(),'weak': set(),'damage': int(group[0][-3]),'attack': group[0][-2],'army': 'immune'} for group in data[0] if group})
groups_initial.update({int(group[0][-1]): {'units': int(group[0][0]),'HP': int(group[0][1]),'immune': set(),'weak': set(),'damage': int(group[0][-3]),'attack': group[0][-2],'army': 'infect'} for group in data[1] if group})

data = [group[0] for army in data for group in army if group]

[groups_initial[int(group[-1])][mod.split(' ')[0]].add(word.strip(',')) for group in data for mod in group[2].split('; ') for word in mod.split(' ')[2:]]

def get_power(group):
    return group['units']*group['damage']

def get_damage(attacker,defender):
    attack = attacker['attack']
    modifier = (attack not in defender['immune']) * (1 + (attack in defender['weak']))
    return get_power(attacker)*modifier

def attack(attacker,defender):
    defender['units'] -= get_damage(attacker,defender)//defender['HP']
    if defender['units'] < 1:
        return {}
    else:
        return defender

boost = 0
remaining = 'infect'
while True:
    groups = copy.deepcopy(groups_initial)
    {groups[i].update({'damage': groups_initial[i]['damage']+boost}) for i in groups if groups[i]['army'] == 'immune'}
    new_units = sum(group['units'] for group in groups.values())
    while not all(v['army']=='immune' for v in groups.values()) and not all(v['army'] == 'infect' for v in groups.values()):

        # Targeting
        targets = {}
        remaining = set(groups.keys())
        units = new_units
        while remaining:
            selecting = max(remaining,key = lambda k: (get_power(groups[k]),k))
            possible = {group for group,props in groups.items() if group not in targets.values() and groups[selecting]['army'] != props['army'] and get_damage(groups[selecting],props)}
            if possible:
                targets[selecting] = max(possible,key = lambda k: (get_damage(groups[selecting],groups[k]),get_power(groups[k]),k))
            remaining.remove(selecting)

        # Attacking
        while targets:
            attacking = max(targets)
            defending = targets.pop(attacking)
            if attacking in groups:
                defender = attack(groups[attacking],groups.pop(defending))
                if defender:
                    groups[defending] = defender
        new_units = sum(group['units'] for group in groups.values())
        if units == new_units:
            break
    if boost == 0:
        print('Part 1:',new_units)
    if groups[list(groups.keys())[-1]]['army'] == 'immune':
        break
    boost += 1

print('Part 2:',new_units)
