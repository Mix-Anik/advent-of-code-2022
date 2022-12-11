import re
from math import floor, lcm


def part_1(data: str):
    items = re.findall(r'Starting items: ((?:\d+,?\s?)*)', data)
    monkeys = {i: [int(x.strip()) for x in items[i].split(',')] for i in range(len(items))}
    operations = re.findall(r'Operation: new = (.*)?', data)
    tests = re.findall(r'divisible by (\d+)?', data)
    tests_actions = re.findall(r'If true: throw to monkey (\d+)\n\s+If false: throw to monkey (\d+)', data)
    inspected = {i: 0 for i in range(len(monkeys))}

    for r in range(20):
        for i in range(len(monkeys)):
            inspected[i] += len(monkeys[i])

            for old in monkeys[i]:
                new_wl = eval(operations[i])
                new_wl = floor(new_wl / 3)
                throw_to = int(tests_actions[i][int(new_wl % int(tests[i]) != 0)])
                monkeys[throw_to].append(new_wl)

            monkeys[i] = []

    si = sorted(inspected.values())

    return si[-1] * si[-2]


def part_2(data: str):
    items = re.findall(r'Starting items: ((?:\d+,?\s?)*)', data)
    monkeys = {i: [int(x.strip()) for x in items[i].split(',')] for i in range(len(items))}
    operations = re.findall(r'Operation: new = (.*)?', data)
    tests = re.findall(r'divisible by (\d+)?', data)
    tests_actions = re.findall(r'If true: throw to monkey (\d+)\n\s+If false: throw to monkey (\d+)', data)
    inspected = {i: 0 for i in range(len(monkeys))}
    lcm_value = lcm(*[int(x) for x in tests])

    for r in range(10000):
        for i in range(len(monkeys)):
            inspected[i] += len(monkeys[i])

            for old in monkeys[i]:
                new_wl = eval(operations[i])

                divisor = int(tests[i])
                if new_wl % divisor == 0:
                    throw_to = int(tests_actions[i][0])
                    monkeys[throw_to].append(new_wl % lcm_value)
                else:
                    throw_to = int(tests_actions[i][1])
                    monkeys[throw_to].append(new_wl)

            monkeys[i] = []

    si = sorted(inspected.values())

    return si[-1] * si[-2]

