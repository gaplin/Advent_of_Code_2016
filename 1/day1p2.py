moves = [(x[0], int(x[1:])) for x in open('input2.txt').read().strip().split(', ')]

turns = {
    'L': lambda x, y: (-y, x),
    'R': lambda x, y: (y, -x)
}

current_position = [0, 0]
current_direction = (-1, 0)
visied_positions = {(0, 0)}

for turn, steps in moves:
    current_direction = turns[turn](*current_direction)
    for _ in range(steps):
        current_position[0] += current_direction[0]
        current_position[1] += current_direction[1]
        key = tuple(current_position)
        if key in visied_positions:
            result = abs(current_position[0]) + abs(current_position[1])
            break
        visied_positions.add(key)
    else:
        continue
    break

print(result)