def winning_position(n: int) -> int:
    last = 2
    for i in range(4, n + 1):
        crossed = i // 2 + 1
        displacement = 1 + last
        if 1 + displacement >= crossed:
            displacement += 1
        last = displacement % i

    return last + 1

    
n = int(open('input2.txt').read().strip())
print(winning_position(n))