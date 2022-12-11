import re
from functools import reduce
from math import floor, gcd


def part_1(data: str):
    return solve(data, 20, True)


def part_2(data: str):
    return solve(data, 10000, False)


def lcm(*args):
    return reduce(lambda a, b: (a * b) // gcd(a, b), args)


def solve(data: str, rounds: int, divide_wl: bool):
    monkeys = {i: {} for i in range(len(data.split('\n\n')))}
    items = [[int(val.strip()) for val in it.split(',')] for it in re.findall(r'Starting items: ((?:\d+,?\s?)*)', data)]
    operations = re.findall(r'Operation: new = (.*)?', data)
    divisors = [int(val) for val in re.findall(r'divisible by (\d+)?', data)]
    actions = [(int(t), int(f)) for t, f in
               re.findall(r'If true: throw to monkey (\d+)\n\s+If false: throw to monkey (\d+)', data)]

    for i in range(len(monkeys)):
        monkeys[i] = {
            'items': items[i],
            'op': operations[i],
            'divisor': divisors[i],
            'action': actions[i],
            'inspected': 0
        }

    do_rounds(rounds, monkeys, lcm(*divisors), divide_wl)
    si = sorted([monkeys[i]['inspected'] for i in range(len(monkeys))])

    return si[-1] * si[-2]


def do_rounds(amount: int, monkeys: dict, lcm_value: int, divide_wl: bool):
    for _ in range(amount):
        for i in range(len(monkeys)):
            monka = monkeys[i]

            for old in monka['items']:
                new_wl = floor(eval(monka['op']) / 3) if divide_wl else eval(monka['op'])
                throw_to = monka['action'][bool(new_wl % monka['divisor'])]
                monkeys[throw_to]['items'].append(new_wl % lcm_value)

            monka['inspected'] += len(monka['items'])
            monka['items'] = []
