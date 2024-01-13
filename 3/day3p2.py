import re

nums = [[int(y) for y in re.findall(r'\d+', x)] for x in open('input2.txt').read().splitlines()]

sides = [[], [], []]
result = 0
for idx, (x, y, z) in enumerate(nums):
    sides[0].append(x)
    sides[1].append(y)
    sides[2].append(z)
    if idx % 3 == 2:
        for idx, (x, y, z) in enumerate(sides):
            if x + y > z and x + z > y and y + z > x:
                result += 1
        sides = [[], [], []]            

print(result)