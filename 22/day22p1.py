import re

input = open('input2.txt').read().splitlines()[2:]
nodes = {}
for line in input:
    nums = [int(x) for x in re.findall(r'\d+', line)]
    nodes[(nums[0], nums[1])] = nums[2:]

result = 0
for key1 in nodes.keys():
    for key2 in nodes.keys():
        if nodes[key1][1] == 0 or \
            key1 == key2 or \
            nodes[key2][2] < nodes[key1][1]:
            continue
        result += 1

print(result)