def part_1(data: str):
    return solve(data, 4)


def part_2(data: str):
    return solve(data, 14)


def solve(data: str, marker_len: int):
    for i in range(len(data) - marker_len):
        if len(set(data[i:i + marker_len])) == marker_len:
            return i + marker_len
