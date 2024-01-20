first_row = [x for x in open('input2.txt').read().strip()]

m = len(first_row)
grid = [first_row]
n = 1
target_n = 400000

while n < target_n:
    previous_row = grid[-1]
    next_row = []
    for i in range(m):
        l, c, r = '.', '.', '.'
        if i > 0:
            l = previous_row[i - 1]
        c = previous_row[i]
        if i < m - 1:
            r = previous_row[i + 1]
        
        if l == '^' and c == '^' and r != '^' or\
            c == '^' and r == '^' and l != '^' or\
            l == '^' and c != '^' and r != '^' or\
            r == '^' and c != '^' and l != '^':
            next_row.append('^')
        else:
            next_row.append('.')
    grid.append(next_row)
    n += 1

result = 0
for row in grid:
    result += row.count('.')

print(result)