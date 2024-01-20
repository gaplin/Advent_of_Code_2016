from queue import Queue
from hashlib import md5

def gen_hash(text: str) -> str:
    return md5(text.encode()).hexdigest()

def get_longest_path_length(source: tuple, target: tuple, passcode: str, directions: list, n: int) -> int:
    Q = Queue()
    Q.put(('', source))

    result = 0
    while Q.empty() == False:
        path, u = Q.get()
        if u == target:
            result = len(path)
            continue
        
        doors = gen_hash(passcode + path)
        for idx, (di, dii, symbol) in enumerate(directions):
            if doors[idx] not in 'bcdef':
                continue
            
            new_i, new_ii = u[0] + di, u[1] + dii
            if new_i < 0 or new_i >= n or new_ii < 0 or new_ii >= n:
                continue

            Q.put((path + symbol, (new_i, new_ii)))

    return result

passcode = open('input2.txt').read().strip()
source = (0, 0)
target = (3, 3)
directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
result = get_longest_path_length(source, target, passcode, directions, 4)

print(result)