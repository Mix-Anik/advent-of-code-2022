from typing import List


def part_1(data: List[str]):
    cycles = 0
    reg = 1
    res = 0

    for op in data:
        if op == 'noop':
            cycles, reg, res = cycle(cycles, reg, res)
        else:
            increment = int(op.split()[1])
            cycles, reg, res = cycle(cycles, reg, res)
            cycles, reg, res = cycle(cycles, reg, res)
            reg += increment

    return res


def part_2(data: List[str]):
    cycles = 0
    reg = 1
    res = ''

    for op in data:
        if op == 'noop':
            cycles, reg, res = cycle2(cycles, reg, res)
        else:
            cycles, reg, res = cycle2(cycles, reg, res)
            cycles, reg, res = cycle2(cycles, reg, res)
            reg += int(op.split()[1])

    return res


def cycle(cur: int, reg: int, res: int):
    cur += 1
    if cur != 0 and (cur == 20 or (cur + 20) % 40 == 0):
        res += cur * reg

    return cur, reg, res


def cycle2(cur: int, reg: int, res: int):
    if cur in list(range(reg - 1, reg + 2)):
        res += '#'
    else:
        res += '.'

    cur += 1

    if cur != 0 and cur % 40 == 0:
        cur = 0
        res += '\n'

    return cur, reg, res
