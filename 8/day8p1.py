import re

input = open('input2.txt')

operations = []
for line in input:
    nums = [int(x) for x in re.findall(r'\d+', line)]
    if line.startswith('rect'):
        operations.append(('rect', nums))
    elif 'column' in line:
        operations.append(('column', nums))
    else:
        operations.append(('row', nums))

n = 6
m = 50
grid = [['.' for _ in range(m)] for _ in range(n)]

for op_type, nums in operations:
    if op_type == 'rect':
        for i in range(nums[1]):
            for ii in range(nums[0]):
                grid[i][ii] = '#'
    elif op_type == 'row':
        grid[nums[0]] = grid[nums[0]][-nums[1]:] + grid[nums[0]][:m - nums[1]]
    else:
        for i in range(n):
            grid[i].append(grid[(i - nums[1]) % n][nums[0]])
        for i in range(n):
            grid[i][nums[0]] = grid[i].pop()

result = 0
for row in grid:
    result += row.count('#')

print(result)