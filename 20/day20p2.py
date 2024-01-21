def merged_ranges(ranges: list) -> list:
    result = [list(ranges[0])]
    for low, high in ranges[1:]:
        if low <= result[-1][1]:
            if high > result[-1][1]:
                result[-1][1] = high
        else:
            result.append([low, high])

    return result

limit = 4294967295
ranges = [(int(x[0]), int(x[1])) for x in map(lambda x: x.split('-'), open('input2.txt').read().splitlines())]
ranges.append((-1, -1))
ranges.append((limit + 1, limit + 1))
ranges.sort()

merged = merged_ranges(ranges)

result = 0
n = len(merged)

for i in range(1, n):
    result += merged[i][0] - merged[i - 1][1] - 1

print(result)
