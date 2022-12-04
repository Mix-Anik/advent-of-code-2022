from typing import List


def part_1(data: List[str]):
    return solve(data)[0]


def part_2(data: List[str]):
    return solve(data)[1]


def solve(data: List[str]):
    part1 = 0
    part2 = 0

    for pairs in data:
        p1, p2 = pairs.split(',')
        x1, y1 = [int(s) for s in p1.split('-')]
        x2, y2 = [int(s) for s in p2.split('-')]
        r1, r2 = set(range(x1, y1 + 1)), set(range(x2, y2 + 1))

        if r1.issubset(r2) or r2.issubset(r1):
            part1 += 1

        if r1.intersection(r2):
            part2 += 1

    return [part1, part2]
