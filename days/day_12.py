from collections import deque
from typing import List
from string import ascii_lowercase


def part_1(data: List[str]):
    heightmap, start, end = parse_data(data)

    return bfs(heightmap, start, end)


def part_2(data: List[str]):
    heightmap, _, end = parse_data(data)
    path_distances = [bfs(heightmap, a, end) for a in heightmap if heightmap[a] == 0]

    return min(path_distances)


def parse_data(data: List[str]):
    start = None
    end = None

    for idx, line in enumerate(data):
        if 'S' in line:
            start = (line.index('S'), idx)
        if 'E' in line:
            end = (line.index('E'), idx)

    heightmap = {(x, y): 0 if height == 'S' else 25 if height == 'E' else ascii_lowercase.index(height) for y, row in
                 enumerate(data) for x, height in enumerate(row)}

    return heightmap, start, end


def neighbours(heightmap: dict, pos: tuple):
    result = []

    for neighbour in [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]:
        if neighbour in heightmap:
            result.append(neighbour)

    return result


def bfs(heightmap: dict, start: tuple, end: tuple):
    queue = deque([start])
    distances = {start: 0}

    while queue:
        cur = queue.popleft()

        if cur == end:
            return distances[end]

        for child in neighbours(heightmap, cur):
            if child not in distances and heightmap[child] - heightmap[cur] <= 1:
                queue.append(child)
                distances[child] = distances[cur] + 1

    return float('inf')
