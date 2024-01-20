import re

input = open('input2.txt').read().splitlines()

bots = {}
moves = {}
outputs = {}
turns = []
for line in input:
    nums = [int(x) for x in re.findall(r'[0-9-]+', line)]
    if line.startswith('value'):
        if nums[1] not in bots:
            bots[nums[1]] = []
        bots[nums[1]].append(nums[0])
        if len(bots[nums[1]]) == 2:
            turns.append(nums[1])
    else:
        if nums[0] not in bots:
            bots[nums[0]] = []
        move = [0, 0]
        if 'low to bot' in line:
            move[0] = ('bot', nums[1])
        else:
            move[0] = ('output', nums[1])
        if 'high to bot' in line:
            move[1] = ('bot', nums[2])
        else:
            move[1] = ('output', nums[2])
        moves[nums[0]] = tuple(move)

while turns != []:
    id = turns.pop()
    low, high = min(bots[id]), max(bots[id])
    
    for value, move in zip([low, high], moves[id]):
        if move[0] == 'bot':
            bots[move[1]].append(value)
            if len(bots[move[1]]) == 2:
                turns.append(move[1])
        else:
            if move[1] not in outputs:
                outputs[move[1]] = []
            outputs[move[1]].append(value)
    bots[id] = []

result = outputs[0][0] * outputs[1][0] * outputs[2][0]
print(result)