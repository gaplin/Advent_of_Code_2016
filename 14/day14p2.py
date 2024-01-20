from queue import Queue
from hashlib import md5

def get_first_triplet(text: str):
    n = len(text)
    for i in range(2, n):
        if text[i] == text[i - 1] == text[i - 2]:
            return text[i]

    return None

def md5Stretched(text: str) -> str:
    for _ in range(2017):
        text = md5(text.encode()).hexdigest()
    return text


salt = open('input2.txt').read().strip()
Q = Queue()
result = ''
id = -1
hashes = []
current_triplet = None
keys = []
while len(keys) < 64:
    id += 1
    text = salt + str(id)
    H = md5Stretched(text)
    hashes.append((H, text))
    triplet = get_first_triplet(H)
    if triplet != None:
        Q.put((triplet, id))
    if current_triplet == None and Q.empty() == False:
        current_triplet = Q.get()
    
    if current_triplet != None and id - current_triplet[1] >= 1000:
        seq = current_triplet[0] * 5
        valid_candidate = False
        for i in range(current_triplet[1] + 1, current_triplet[1] + 1001):
            if seq in hashes[i][0]:
                valid_candidate = True
                break
        if valid_candidate:
            keys.append((current_triplet[1], hashes[current_triplet[1]]))
        current_triplet = None

print(keys[63][0])