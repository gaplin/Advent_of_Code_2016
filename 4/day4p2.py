from functools import cmp_to_key

input = open('input2.txt').read().splitlines()

def get_shifted_name(fragments: list, offset: int) -> str:
    new_fragments = []
    for fragment in fragments:
        part = ''
        for char in fragment:
            new_ord = (ord(char) - ord('a') + offset) % 26 + ord('a')
            part += chr(new_ord)
        new_fragments.append(part)
    return '-'.join(new_fragments)

result = 0
for line in input:
    fragments = line.split('-')
    id, checksum = fragments[-1].split('[')
    id = int(id)
    checksum = checksum[:-1]
    real_name = get_shifted_name(fragments[:-1], id)
    if real_name == 'northpole-object-storage':
        result = id
        break

print(result)