def merged_ranges(ranges: list) -> list:
    result = [list(ranges[0])]
    for low, high in ranges[1:]:
        if low <= result[-1][1]:
            if high > result[-1][1]:
                result[-1][1] = high
        else:
            result.append([low, high])

    return result

ranges = [(int(x[0]), int(x[1])) for x in map(lambda x: x.split('-'), open('input2.txt').read().splitlines())]

ranges.sort()
merged = merged_ranges(ranges)

candidate = 0

for low, high in merged:
    if low <= candidate <= high:
        candidate = high + 1
    else:
        break

print(candidate)
