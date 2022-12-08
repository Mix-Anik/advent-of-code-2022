from typing import List


def part_1(data: List[str]):
    heightmap = {(x, y): int(height) for y, row in enumerate(data) for x, height in enumerate(row)}
    visible = len(data) * 2 + (len(data[0]) - 2) * 2

    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            cur = heightmap[(x, y)]

            if (all([heightmap[(i, y)] < cur for i in range(x)]) or
                    all([heightmap[(x + 1 + i, y)] < cur for i in range(len(data) - x - 1)]) or
                    all([heightmap[(x, i)] < cur for i in range(y)]) or
                    all([heightmap[(x, y + 1 + i)] < cur for i in range(len(data[0]) - y - 1)])):
                visible += 1

    return visible


def part_2(data: List[str]):
    heightmap = {(x, y): int(height) for y, row in enumerate(data) for x, height in enumerate(row)}
    scores = []
    shape = (len(data[0]), len(data))

    for y in range(1, shape[1] - 1):
        for x in range(1, shape[0] - 1):
            cur = heightmap[(x, y)]
            l = r = b = t = 0

            for i in range(x)[::-1]:
                l += 1
                if heightmap[(i, y)] >= cur:
                    break

            for i in range(x + 1, shape[0]):
                r += 1
                if heightmap[(i, y)] >= cur:
                    break

            for i in range(y)[::-1]:
                t += 1
                if heightmap[(x, i)] >= cur:
                    break

            for i in range(y + 1, shape[1]):
                b += 1
                if heightmap[(x, i)] >= cur:
                    break

            scores.append(l * r * t * b)

    return max(scores)
