from functools import cmp_to_key


def compare(left: list or int, right: list or int):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1

    if isinstance(right, int):
        right = [right]

    if isinstance(left, int):
        left = [left]

    if isinstance(left, list) and isinstance(right, list):
        for a, b in zip(left, right):
            tmp = compare(a, b)

            if tmp != 0:
                return tmp

        if len(left) < len(right):
            return 1
        elif len(left) > len(right):
            return -1

        return 0

    return -1


def part_1(data: str):
    pairs = data.split('\n\n')
    result = 0

    for idx, pair in enumerate(pairs):
        parts = pair.split('\n')
        left, right = eval(parts[0]), eval(parts[1])
        in_order = compare(left, right)

        if in_order == 1:
            result += idx + 1

    return result


def part_2(data: str):
    data = data.replace('\n\n', '\n')
    packets = [eval(p) for p in data.split()]
    packets.extend([[[2]], [[6]]])
    packets.sort(key=cmp_to_key(compare), reverse=True)

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
