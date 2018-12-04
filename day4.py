import re

input_data = open('day4.txt','r').read().strip().split('\n')

sleep_data = [re.findall(r'\d+-(\d+-\d+) \d+:(\d+)] ([a-zA-Z]+)[\S\s]#?(\d+)?',line)[0] for line in sorted(input_data)]

sleep_schedule = {}

for index in range(len(sleep_data)):
    date = sleep_data[index][0]
    minute = int(sleep_data[index][1])
    action = sleep_data[index][2]
    if(action=="Guard"):
        guard = int(sleep_data[index][3])
        if(guard not in sleep_schedule):
            sleep_schedule[guard] = []
    if(action == "wakes"):
        search_index = index-1
        while search_index>=0:
            if(sleep_data[search_index][2] == "Guard"):
                break
            if(sleep_data[search_index][2] == "falls" and sleep_data[search_index-1][2] != "falls"):
                sleep_schedule[guard].extend(list(range(int(sleep_data[search_index][1]),minute)))
                break
            search_index -= 1

most_sleep = (0,0)
for guard,sleep_minutes in sleep_schedule.items():
    if(len(sleep_minutes)>most_sleep[1]):
        most_sleep = (guard,len(sleep_minutes))

print(most_sleep[0]*max(set(sleep_schedule[most_sleep[0]]),key=sleep_schedule[most_sleep[0]].count))

# Part 2

most_sleep = (0,0,0)
for guard,sleep_minutes in sleep_schedule.items():
    if(sleep_minutes):
        sleep_minute = max(set(sleep_minutes),key=sleep_minutes.count)
        guard_most_sleep=(guard,sleep_minute,sleep_minutes.count(sleep_minute))
        if(guard_most_sleep[2]>most_sleep[2]):
            most_sleep = guard_most_sleep

print(most_sleep[0]*most_sleep[1])
