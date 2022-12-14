import re


def part_1(data: str):
    return solve(data, False)


def part_2(data: str):
    return solve(data, True)


def solve(data: str, is_9001: bool):
    total_stacks = int(re.findall(r'(\d)\n\n', data)[0])
    stacks = {i + 1: re.findall(rf'^(?:.{{4}}){{{i}}}\[([A-Z])\]', data, re.M)[::-1] for i in range(total_stacks)}
    arrangements = [[int(x) for x in arr] for arr in re.findall(r'move (\d+) from (\d+) to (\d+)', data)]

    for amount, from_a, to_b in arrangements:
        stacks[from_a], package = stacks[from_a][:-amount], stacks[from_a][-amount:]
        stacks[to_b].extend(package if is_9001 else package[::-1])

    return ''.join([c[-1] for c in stacks.values() if c])
