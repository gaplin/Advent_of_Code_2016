from hashlib import md5

door_id = open('input2.txt').read().strip()

result = ''
id = -1
for _ in range(8):
    while True:
        id += 1
        text = door_id + str(id)
        H = md5(text.encode()).hexdigest()
        if H.startswith('00000'):
            result += H[5]
            break

print(result)