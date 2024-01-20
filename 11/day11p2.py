def get_shortest_path(floors: list) -> int:
    result = 0
    items = 0
    for i in range(3):
        items += len(floors[i][0]) + len(floors[i][1])
        result += max(0, 2 * (items - 1) - 1)
    
    return result

import re

input = open('input2.txt').read().splitlines()

floors = [[] for _ in range(4)]
for id, line in enumerate(input):
    generators = re.findall(r'[a-z-]+ generator', line)
    floors[id].append([x.split(' ')[0] for x in generators])

    microchips = re.findall(r'[a-z-]+ microchip', line)
    floors[id].append([x.split(' ')[0].split('-')[0] for x in microchips])

floors[0][0].append('elerium')
floors[0][1].append('elerium')
floors[0][0].append('dilithium')
floors[0][1].append('dilithium')
result = get_shortest_path(floors)
print(result)