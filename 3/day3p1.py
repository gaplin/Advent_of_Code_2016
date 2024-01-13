import re

sides = [[int(y) for y in re.findall(r'\d+', x)] for x in open('input2.txt').read().splitlines()]

result = 0
for x, y, z in sides:
    if x + y > z and x + z > y and y + z > x:
        result += 1

print(result)