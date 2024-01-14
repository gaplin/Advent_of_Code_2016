from functools import cmp_to_key

input = open('input2.txt').read().splitlines()

def compare(item1: tuple, item2: tuple) -> int:
    if item1[0] == item2[0]:
        return ord(item1[1]) - ord(item2[1])
    return item2[0] - item1[0]


def get_check_sum(fragments: list) -> str:
    result = ''
    occurs = {}
    for fragment in fragments:
        for char in fragment:
            if char not in occurs:
                occurs[char] = 1
            else:
                occurs[char] += 1

    occurs_lst = []
    for char, occurences in occurs.items():
        occurs_lst.append((occurences, char))
    occurs_lst.sort(key=cmp_to_key(compare))
    for i in range(5):
        result += occurs_lst[i][1]

    return result

result = 0
for line in input:
    fragments = line.split('-')
    id, checksum = fragments[-1].split('[')
    id = int(id)
    checksum = checksum[:-1]
    correct_checksum = get_check_sum(fragments[:-1])
    if correct_checksum == checksum:
        result += id

print(result)