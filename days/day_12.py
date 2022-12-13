from collections import deque


def part_1(data: str):
    heightmap, start, end = parse_data(data)

    return bfs(heightmap, start, end)


def part_2(data: str):
    heightmap, _, end = parse_data(data)
    path_distances = [bfs(heightmap, a, end) for a in heightmap if heightmap[a] == 0]

    return min(path_distances)


def parse_data(data: str):
    rows = data.split()
    getpos = lambda c: ((data.index(c) - data.index(c) // len(rows[0])) % len(rows[0]),
                        (data.index(c) - data.index(c) // len(rows) + 1) // len(rows[0]))
    start, end = getpos('S'), getpos('E')
    rows = data.replace(r'S', 'a').replace('E', 'z').split()
    heightmap = {(x, y): ord(height) - ord('a') for y, row in enumerate(rows) for x, height in enumerate(row)}

    return heightmap, start, end


def bfs(heightmap: dict, start: tuple, end: tuple):
    queue = deque([start])
    distances = {start: 0}

    while queue:
        cur = queue.popleft()

        if cur == end:
            return distances[end]

        for child in [(cur[0] + 1, cur[1]), (cur[0] - 1, cur[1]), (cur[0], cur[1] + 1), (cur[0], cur[1] - 1)]:
            if child in heightmap and child not in distances and heightmap[child] - heightmap[cur] <= 1:
                queue.append(child)
                distances[child] = distances[cur] + 1

    return float('inf')
