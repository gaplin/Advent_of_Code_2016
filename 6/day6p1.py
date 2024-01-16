from functools import reduce

words = open('input2.txt').read().splitlines()
n = len(words)
m = len(words[0])

occurs = [{} for _ in range(m)]

for word in words:
    for idx, char in enumerate(word):
        if char not in occurs[idx]:
            occurs[idx][char] = 0
        occurs[idx][char] += 1

result = ''
for i in range(m):
    result += reduce(lambda acc, x: x if x[1] > acc[1] else acc, occurs[i].items())[0]

print(result)