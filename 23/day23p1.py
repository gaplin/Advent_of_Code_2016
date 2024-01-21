def get_value(registers: dict, val: str) -> int:
    if val.isalpha():
        return registers[val]
    return int(val)

def cpy(registers: dict, x: str, y: str) -> None:
    if y.isalpha() == False:
        return
    registers[y] = get_value(registers, x)

def inc(registers: dict, x: str) -> None:
    registers[x] += 1

def dec(registers: dict, x: str) -> None:
    registers[x] -= 1

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
            inc(program[0], *args)
        elif instruction == 'dec':
            dec(program[0], *args)
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

registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
program = [registers, 0, instructions]
play(program)
print(registers['a'])