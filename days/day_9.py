from typing import List


def part_1(data: List[str]):
    visited = simulate(data, 2)

    return len({*visited[1]})


def part_2(data: List[str]):
    visited = simulate(data, 10)

    return len({*visited[9]})


def simulate(data: List[str], knot_amount: int):
    knots = {i: [0, 0] for i in range(knot_amount)}
    visited = {i: [(0, 0)] for i in range(knot_amount)}

    for step in data:
        direction, amount = step.split()

        for i in range(int(amount)):
            move(knots, visited, direction)

    return visited


def move(knots: dict, visited: dict, direction: str):
    head_increment = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    knots[0] = [a + b for a, b in zip(knots[0], head_increment[direction])]

    for i in range(1, len(knots)):
        cur, ahead = knots[i], knots[i - 1]
        is_diagonal = (abs(ahead[0] - cur[0]) > 1 and abs(ahead[1] - cur[1]) == 1) or \
                      (abs(ahead[1] - cur[1]) > 1 and abs(ahead[0] - cur[0]) == 1)
        cur[0] += (1 if ahead[0] - cur[0] > 0 else -1) * int(abs(ahead[0] - cur[0]) > 1 or is_diagonal)
        cur[1] += (1 if ahead[1] - cur[1] > 0 else -1) * int(abs(ahead[1] - cur[1]) > 1 or is_diagonal)

        visited[i].append(tuple(cur))
