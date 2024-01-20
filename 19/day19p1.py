def winning_position(n: int) -> int:
    pow = 1
    last_pow = 1
    while pow <= n:
        last_pow = pow
        pow <<= 1

    n -= last_pow
    return 2 * n + 1

n = int(open('input2.txt').read().strip())
print(winning_position(n))