import re

def valid_time(time: int, discs: list) -> bool:
    for id, m, position in discs:
        if (time + position + id) % m != 0:
            return False
        
    return True

input = open('input2.txt')

discs = []
for i, line in enumerate(input):
    nums = [int(x) for x in re.findall(r'\d+', line)]
    discs.append((i + 1, nums[1], nums[3]))

discs.append((7, 11, 0))

time = 0
while valid_time(time, discs) == False:
    time += 1
print(time)