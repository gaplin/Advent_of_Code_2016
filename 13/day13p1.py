from queue import Queue

def f(x, y):
    return x * x + 3 * x + 2 * x * y + y + y * y

def count_bits(num) -> int:
    res = 0
    while num > 0:
        res += num & 1
        num >>= 1
    
    return res

def is_open(x, y, fav) -> bool:
    S = f(x, y) + fav
    bits = count_bits(S)
    return bits % 2 == 0

def get_distance(source, target, directions, fav_number) -> int:
    Q = Queue()
    Q.put((0, position))
    visited = {source}

    while Q.empty() == False:
        distance, u = Q.get()
        if u == target:
            return distance
        
        for di, dii in directions:
            new_i, new_ii = u[0] + di, u[1] + dii
            if new_i < 0 or new_ii < 0 or is_open(new_ii, new_i, fav_number) == False or (new_i, new_ii) in visited:
                continue
            visited.add((new_i, new_ii))
            Q.put((distance + 1, (new_i, new_ii)))

    raise Exception('Target not found')


fav_number = int(open('input2.txt').read().strip())

position = (1, 1)
target = (39, 31)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
result = get_distance(position, target, directions, fav_number)
print(result)