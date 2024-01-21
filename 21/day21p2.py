from itertools import permutations

def swap_position(letters: list, x: int, y: int) -> None:
    letters[x], letters[y] = letters[y], letters[x]

def swap_letters(letters: list, x: str, y: str) -> None:
    i = letters.index(x)
    j = letters.index(y)
    swap_position(letters, i, j)

def rotate_left_steps(letters: list, x: int) -> list:
    n = len(letters)
    x %= n
    result = letters[x:] + letters[:x]
    return result

def rotate_right_steps(letters: list, x: int) -> list:
    n = len(letters)
    x %= n
    result = letters[-x:] + letters[:-x] 
    return result

def rotate_right_letter(letters: list, x: str) -> list:
    i = letters.index(x)
    if i >= 4:
        i += 1
    i += 1
    return rotate_right_steps(letters, i)

def reverse(letters: list, x: int, y: int) -> None:
    limit = (y - x + 1) // 2
    for i in range(0, limit):
        letters[x + i], letters[y - i] = letters[y - i], letters[x + i]
    
def move(letters: list, x: int, y: int) -> None:
    value = letters.pop(x)
    letters.insert(y, value)

input = open('input2.txt').read().splitlines()
pass_text = 'fbgdceah'

for candidate in permutations(pass_text):
    password = [x for x in candidate]
    for line in input:
        line = line.split(' ')
        if line[0] == 'swap':
            if line[1] == 'position':
                swap_position(password, int(line[2]), int(line[5]))
            else:
                swap_letters(password, line[2], line[5])
        elif line[0] == 'rotate':
            if line[1] == 'left':
                password = rotate_left_steps(password, int(line[2]))
            elif line[1] == 'right':
                password = rotate_right_steps(password, int(line[2]))
            else:
                password = rotate_right_letter(password, line[-1])
        elif line[0] == 'reverse':
            reverse(password, int(line[2]), int(line[4]))
        else:
            move(password, int(line[2]), int(line[5]))
    if ''.join(password) == pass_text:
        result = candidate
        break

print(''.join(result))