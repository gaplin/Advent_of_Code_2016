from copy import deepcopy

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

def out(registers: list, x: str, output: list) -> None:
    output.append(get_value(registers, x))

def get_key(program: list) -> tuple:
    registers, ip = program[0], program[1]
    return (registers['a'], registers['b'], registers['c'], registers['d'], ip)

def play(program: list) -> bool:
    #program -> [registers, ip, instructions]
    states = {get_key(program)}
    outs = []
    instructions = program[2]
    n = len(instructions)
    while 0 <= program[1] < n:
        instruction, args = instructions[program[1]]
        if instruction == 'jnz':
            if jnz(program, *args) == False:
                program[1] += 1
        elif instruction == 'inc':
            inc(program[0], *args)
            program[1] += 1
        elif instruction == 'dec':
            dec(program[0], *args)
            program[1] += 1
        elif instruction == 'cpy':
            cpy(program[0], *args)
            program[1] += 1
        elif instruction == 'out':
            out(program[0], *args, outs)
            if len(outs) > 1:
                if outs[-1] != 1 - outs[-2]:
                    return False
            program[1] += 1
        else:
            raise Exception('unknown instruction {} {}'.format(instruction, args))
        state_key = get_key(program)
        if state_key in states:
            return True
            break
        states.add(state_key)

input = open('input2.txt').read().splitlines()
instructions = []
for line in input:
    line = line.split(' ')
    instructions.append([line[0], line[1:]])

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
program = [registers, 0, instructions]
result = 0
for i in range(10000):
    program_copy = deepcopy(program)
    program_copy[0]['a'] = i
    res = play(program_copy)
    if res == True:
        result = i
        break
print(result)