from typing import List


def part_1(data: List[str]):
    return solve(data)[0]


def part_2(data: List[str]):
    return solve(data)[1]


def solve(data: List[str]):
    part1 = part2 = 0

    for pairs in data:
        x1, y1, x2, y2 = [int(s) for s in pairs.replace(',', '-').split('-')]
        r1, r2 = set(range(x1, y1 + 1)), set(range(x2, y2 + 1))
        part1 += int(r1 <= r2 or r2 <= r1)
        part2 += int(bool(r1 & r2))

    return [part1, part2]
