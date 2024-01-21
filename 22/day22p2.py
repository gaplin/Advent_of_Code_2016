import re
from functools import reduce
from queue import Queue

def find_empty_node(nodes: dict) -> tuple:
    empty_nodes = []
    for pos, (_, usage) in nodes.items():
        if usage == 0:
            empty_nodes.append(pos)
    
    assert len(empty_nodes) == 1
    return empty_nodes[0]

def shortest_path_length(empty_node: tuple, data_node: tuple, directions: list, nodes: dict) -> int:
    currenet_state = (0, empty_node, data_node)
    target = (0, 0)
    Q = Queue()
    visited = {(empty_node, data_node)}
    Q.put(currenet_state)

    while Q.empty() == False:
        distance, empty, data = Q.get()
        if data == target:
            return distance
        
        for dx, dy in directions:
            v = (empty[0] + dx, empty[1] + dy)
            if v not in nodes or nodes[empty][0] < nodes[v][1]:
                continue
            
            next_state = (v, data) if data != v else (v, empty)
            if next_state not in visited:
                visited.add(next_state)
                Q.put((distance + 1, *next_state))

input = open('input2.txt').read().splitlines()[2:]
nodes = {}
for line in input:
    nums = [int(x) for x in re.findall(r'\d+', line)]
    nodes[(nums[0], nums[1])] = [nums[2], nums[3]]

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
max_x = reduce(lambda acc, cords: acc if cords[1] != 0 else max(acc, cords[0]), nodes.keys(), 0)
empty_node = find_empty_node(nodes)
result = shortest_path_length(empty_node, (max_x, 0), directions, nodes)
print(result)