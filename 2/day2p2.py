instructions = open('input2.txt').read().splitlines()

keypad = [
    [None, None, '1', None, None], 
    [None, '2', '3', '4', None], 
    ['5', '6', '7', '8', '9'], 
    [None, 'A', 'B', 'C', None], 
    [None, None, 'D', None, None]
]
n = 5
directions = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}

result = ''
current_position = (2, 0)
for sequence in instructions:
    for char in sequence:
        direction = directions[char]
        new_i, new_ii = current_position[0] + direction[0], current_position[1] + direction[1]
        if new_i < 0 or new_i >= n or new_ii < 0 or new_ii >= n or keypad[new_i][new_ii] == None:
            continue
        current_position = (new_i, new_ii)
    result += keypad[current_position[0]][current_position[1]]

print(result)