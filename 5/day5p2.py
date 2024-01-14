from hashlib import md5

door_id = open('input2.txt').read().strip()

n = 8
result = [None for _ in range(n)]
id = -1
for _ in range(n):
    while True:
        id += 1
        text = door_id + str(id)
        H = md5(text.encode()).hexdigest()
        if H.startswith('00000'):
            if '0' <= H[5] <= '7':
                position = int(H[5])
                if result[position] == None:
                    result[position] = H[6]
                    break

print(''.join(result))