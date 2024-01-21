from queue import Queue
from heapq import heappop, heappush

def get_shortest_path_length(grid: list, source: tuple, target: tuple) -> int:
    Q = Queue()
    Q.put((0, source))
    visited = {source}
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while Q.empty() == False:
        distance, u = Q.get()
        if u == target:
            return distance
        
        for di, dii in directions:
            new_i, new_ii = u[0] + di, u[1] + dii
            v = (new_i, new_ii)
            if grid[new_i][new_ii] == '#' or v in visited:
                continue
            
            visited.add(v)
            Q.put((distance + 1, v))

    raise Exception('target not found')

def build_Graph(grid: list, nodes: dict) -> dict:
    G = {}
    for node in nodes.keys():
        G[node] = []

    for u in nodes.keys():
        for v in nodes.keys():
            if u == v:
                continue
            distance = get_shortest_path_length(grid, nodes[u], nodes[v])
            G[u].append((v, distance))
    
    return G

def get_key(current_node, collected_items: list) -> tuple:
    return (current_node, *sorted(collected_items))

def get_shortest_path_length_for_all_nodes(G: dict, starting_node: int) -> int:
    distances = {(starting_node, starting_node): 0}
    Q = [(0, starting_node, [starting_node])]
    all_items_count = len(G)
    while Q:
        distance, u, collected_items = heappop(Q)
        key = get_key(u, collected_items)
        if distance != distances[key]:
            continue

        if len(collected_items) == all_items_count + 1 and u == starting_node:
            return distance

        for v, dist in G[u]:
            if v in collected_items and (len(collected_items) != all_items_count or v != starting_node):
                continue
            new_dist = distance + dist
            new_collection = list(collected_items) + [v]
            key = get_key(v, new_collection)
            if key not in distances or distances[key] > new_dist:
                distances[key] = new_dist
                heappush(Q, (new_dist, v, new_collection))

    raise Exception('target not found')

grid = open('input2.txt').read().splitlines()
n = len(grid)
m = len(grid[0])

nums = {}

for i in range(n):
    for ii in range(m):
        if grid[i][ii] not in '#.':
            num = int(grid[i][ii])
            nums[num] = (i, ii)

G = build_Graph(grid, nums)
result = get_shortest_path_length_for_all_nodes(G, 0)
print(result)