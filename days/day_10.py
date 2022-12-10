from typing import List


def part_1(data: List[str]):
    return solve(data)[0]


def part_2(data: List[str]):
    return solve(data)[1]


def solve(data: List[str]):
    cycle = 0
    reg = 1
    sss = 0  # signal strength sum
    screen = ''

    for op in data:
        if op == 'noop':
            cycle, sss, screen = tick(cycle, reg, sss, screen)
        else:
            cycle, sss, screen = tick(cycle, reg, sss, screen)
            cycle, sss, screen = tick(cycle, reg, sss, screen)
            reg += int(op.split()[1])

    return sss, screen


def tick(cycle: int, reg: int, sss: int, screen: str):
    screen += '.#'[(cycle % 40) in range(reg - 1, reg + 2)]
    cycle += 1

    if cycle == 20 or (cycle + 20) % 40 == 0:
        sss += cycle * reg

    if cycle % 40 == 0:
        screen += '\n'

    return cycle, sss, screen
