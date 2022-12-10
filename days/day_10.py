from typing import List


def part_1(data: List[str]):
    return solve(data)[0]


def part_2(data: List[str]):
    return solve(data)[1]


def solve(data: List[str]):
    cycles = 0
    reg = 1
    sss = 0  # signal strength sum
    screen = ''

    for op in data:
        if op == 'noop':
            cycles, sss, screen = tick(cycles, reg, sss, screen)
        else:
            cycles, sss, screen = tick(cycles, reg, sss, screen)
            cycles, sss, screen = tick(cycles, reg, sss, screen)
            reg += int(op.split()[1])

    return sss, screen


def tick(cycle: int, reg: int, sss: int, screen: str):
    screen += '.#'[(cycle % 40) in list(range(reg - 1, reg + 2))]
    cycle += 1

    if cycle == 20 or (cycle + 20) % 40 == 0:
        sss += cycle * reg

    if cycle % 40 == 0:
        screen += '\n'

    return cycle, sss, screen
