instructions = open('input2.txt').read().splitlines()

nums = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
n = 3
directions = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}

result = ''
current_position = (1, 1)
for sequence in instructions:
    for char in sequence:
        direction = directions[char]
        new_i, new_ii = current_position[0] + direction[0], current_position[1] + direction[1]
        if new_i < 0 or new_i >= n or new_ii < 0 or new_ii >= n:
            continue
        current_position = (new_i, new_ii)
    result += nums[current_position[0]][current_position[1]]

print(result)