def get_value(registers: dict, val: str) -> int:
    if val.isalpha():
        return registers[val]
    return int(val)

def cpy(registers: dict, x: str, y: str) -> None:
    registers[y] = get_value(registers, x)

def inc(registers: dict, x: str) -> None:
    registers[x] += 1

def dec(registers: dict, x: str) -> None:
    registers[x] -= 1

def jnz(program: dict, x: str, y: str) -> bool:
    if get_value(program[0], x) != 0:
        program[1] += get_value(program[0], y)
        return True
    return False


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
        else:
            raise Exception('unknown instruction {} {}'.format(instruction, args))
        
        program[1] += 1

input = open('input2.txt').read().splitlines()
instructions = []
for line in input:
    line = line.split(' ')
    instructions.append([line[0], line[1:]])

registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
program = [registers, 0, instructions]
play(program)
print(registers['a'])