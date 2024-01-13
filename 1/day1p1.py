moves = [(x[0], int(x[1:])) for x in open('input2.txt').read().strip().split(', ')]

turns = {
    'L': lambda x, y: (-y, x),
    'R': lambda x, y: (y, -x)
}

current_position = [0, 0]
current_direction = (-1, 0)

for turn, steps in moves:
    current_direction = turns[turn](*current_direction)
    current_position[0] += steps * current_direction[0]
    current_position[1] += steps * current_direction[1]

result = abs(current_position[0]) + abs(current_position[1])
print(result)