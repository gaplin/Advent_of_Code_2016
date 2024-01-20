from copy import deepcopy
from queue import Queue

def get_key(elevator: int, floors: list) -> tuple:
    floor_tuples = []
    for generators, chips in floors:
        generators.sort()
        chips.sort()
        floor_tuples.append((tuple(generators), tuple(chips)))

    return (elevator, tuple(floor_tuples))
    
def get_target(floors: list) -> tuple:
    generators = []
    for gens, _ in floors:
        generators += gens
    
    floors = [[[], []] for _ in range(4)]
    floors[3][0] = generators
    floors[3][1] = generators
    return get_key(3, floors)

def valid_arrangement(floors: list) -> bool:
    for gens, chips in floors:
        if len(gens) > 0 and len(chips) > 0:
            for chip in chips:
                if chip not in gens:
                    return False
                
    return True

def get_next_states(elevator: int, floors: list) -> list:
    result = []
    # 1 gen
    for gen in floors[elevator][0]:
        for height in [elevator + 1, elevator - 1]:
            if height < 0 or height >= 4:
                continue
            floors_copy = deepcopy(floors)
            floors_copy[elevator][0].remove(gen)
            floors_copy[height][0].append(gen)
            if valid_arrangement(floors_copy):
                result.append((height, floors_copy))
    # 2 gens
    for i, gen1 in enumerate(floors[elevator][0]):
        for gen2 in floors[elevator][0][:i]:
            for height in [elevator + 1, elevator - 1]:
                if height < 0 or height >= 4:
                    continue
                floors_copy = deepcopy(floors)
                floors_copy[elevator][0].remove(gen1)
                floors_copy[elevator][0].remove(gen2)
                floors_copy[height][0].append(gen1)
                floors_copy[height][0].append(gen2)
                if valid_arrangement(floors_copy):
                    result.append((height, floors_copy))

    # 1 chip
    for chip in floors[elevator][1]:
        for height in [elevator + 1, elevator - 1]:
            if height < 0 or height >= 4:
                continue
            floors_copy = deepcopy(floors)
            floors_copy[elevator][1].remove(chip)
            floors_copy[height][1].append(chip)
            if valid_arrangement(floors_copy):
                result.append((height, floors_copy))

    # 2 chips
    for i, chip1 in enumerate(floors[elevator][1]):
        for chip2 in floors[elevator][1][:i]:
            for height in [elevator + 1, elevator - 1]:
                if height < 0 or height >= 4:
                    continue
                floors_copy = deepcopy(floors)
                floors_copy[elevator][1].remove(chip1)
                floors_copy[elevator][1].remove(chip2)
                floors_copy[height][1].append(chip1)
                floors_copy[height][1].append(chip2)
                if valid_arrangement(floors_copy):
                    result.append((height, floors_copy))

    # 1 chip 1 gen
    for gen in floors[elevator][0]:
        for chip in floors[elevator][1]:
            if gen != chip:
                continue
            for height in [elevator + 1]:
                if height < 0 or height >= 4:
                    continue
                floors_copy = deepcopy(floors)
                floors_copy[elevator][0].remove(gen)
                floors_copy[elevator][1].remove(chip)
                floors_copy[height][0].append(gen)
                floors_copy[height][1].append(chip)
                if valid_arrangement(floors_copy):
                    result.append((height, floors_copy))
            
    return result

def build_graph(starting_position: list, target_key: tuple) -> dict:
    G = {}
    first_key = get_key(0, starting_position)
    visited = {first_key}
    G[first_key] = set()
    Q = Queue()
    Q.put((0, starting_position))

    while Q.empty() == False:
        elevator, floors = Q.get()
        current_key = get_key(elevator, floors)
        if current_key == target_key:
            continue

        next_states = get_next_states(elevator, floors)
        for new_elevator, new_floors in next_states:
            next_key = get_key(new_elevator, new_floors)
            G[current_key].add(next_key)
            if next_key not in visited:
                Q.put((new_elevator, new_floors))
                visited.add(next_key)
                G[next_key] = set()

    return G

def get_shortest_path(G: dict, source, target) -> int:
    Q = Queue()
    Q.put((0, source))
    visited = {source}

    while Q.empty() == False:
        distance, u = Q.get()
        if u == target:
            return distance
        
        for v in G[u]:
            if v not in visited:
                visited.add(v)
                Q.put((distance + 1, v))
        
    raise Exception('target not found')

import re

input = open('input2.txt').read().splitlines()

floors = [[] for _ in range(4)]
for id, line in enumerate(input):
    generators = re.findall(r'[a-z-]+ generator', line)
    floors[id].append([x.split(' ')[0] for x in generators])

    microchips = re.findall(r'[a-z-]+ microchip', line)
    floors[id].append([x.split(' ')[0].split('-')[0] for x in microchips])

target_node = get_target(floors)
starting_node = get_key(0, floors)
G = build_graph(floors, target_node)
print(len(G))
result = get_shortest_path(G, starting_node, target_node)
print(result)