def get_value(registers: dict, val: str) -> int:
    if val.isalpha():
        return registers[val]
    return int(val)

def cpy(registers: dict, x: str, y: str) -> None:
    if y.isalpha() == False:
        return
    registers[y] = get_value(registers, x)

def inc(program: list, x: str) -> None:
    idx = program[1]
    n = len(program[2])
    if idx + 4 < n:
        if program[2][idx + 1][0] == 'dec' and program[2][idx + 2][0] == 'jnz' and program[2][idx + 3][0] == 'dec' and program[2][idx + 4][0] == 'jnz':
            program[1] = idx + 4
            a = program[0][program[2][idx + 1][1][0]]
            b = program[0][program[2][idx + 3][1][0]]
            program[0][program[2][idx][1][0]] += a * b
            program[0][program[2][idx + 1][1][0]] = 0
            program[0][program[2][idx + 3][1][0]] = 0
            return
        
    program[0][x] += 1

def dec(program: list, x: str) -> None:
    idx = program[1]
    n = len(program[2])
    if idx + 2 < n:
        if program[2][idx + 1][0] == 'inc' and program[2][idx + 2][0] == 'jnz':
            program[1] = idx + 2
            b = program[0][program[2][idx][1][0]]
            program[0][program[2][idx + 1][1][0]] += b
            program[0][program[2][idx][1][0]] = 0
            return
    program[0][x] -= 1

def jnz(program: list, x: str, y: str) -> bool:
    if get_value(program[0], x) != 0:
        program[1] += get_value(program[0], y)
        return True
    return False

def tgl(program: list, x: str) -> None:
    idx = program[1] + get_value(program[0], x)
    n = len(program[2])
    if idx < 0 or idx >= n:
        return
    
    instruction = program[2][idx]
    if len(instruction[1]) == 1:
        if instruction[0] == 'inc':
            instruction[0] = 'dec'
        else:
            instruction[0] = 'inc'
    else:
        if instruction[0] == 'jnz':
            instruction[0] = 'cpy'
        else:
            instruction[0] = 'jnz'

def play(program: list) -> None:
    #program -> [registers, ip, instructions]
    instructions = program[2]
    n = len(instructions)
    while 0 <= program[1] < n:
        instruction, args = instructions[program[1]]
        if instruction == 'jnz':
            if jnz(program, *args) == True:
                continue
        elif instruction == 'inc':
            inc(program, *args)
        elif instruction == 'dec':
            dec(program, *args)
        elif instruction == 'cpy':
            cpy(program[0], *args)
        elif instruction == 'tgl':
            tgl(program, *args)
        else:
            raise Exception('unknown instruction {} {}'.format(instruction, args))
        program[1] += 1

input = open('input2.txt').read().splitlines()
instructions = []
for line in input:
    line = line.split(' ')
    instructions.append([line[0], line[1:]])

registers = {'a': 12, 'b': 0, 'c': 0, 'd': 0}
program = [registers, 0, instructions]
play(program)
print(registers['a'])