def dragon_curve(a: list) -> list:
    result = [*a, '0']
    b = list(map(lambda x: '1' if x == '0' else '0', reversed(a)))
    result += b
    return result

def gen_checksum(a: list) -> list:
    n = len(a)
    result = []
    for i in range(0, n, 2):
        if a[i] == a[i + 1]:
            result.append('1')
        else:
            result.append('0')

    return result

target_size = 35651584
state = [x for x in open('input2.txt').read().strip()]
n = len(state)
while n < target_size:
    state = dragon_curve(state)
    n = len(state)
state = state[:target_size]

checksum = state
while len(checksum) % 2 == 0:
    checksum = gen_checksum(checksum)

print(''.join(checksum))