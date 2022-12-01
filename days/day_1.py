from typing import List


def calc_calories(data: List[str]):
    calories = []
    cur_cal = 0

    for item in data:
        if not item:
            calories.append(cur_cal)
            cur_cal = 0
            continue

        cur_cal += int(item)

    calories.append(cur_cal)

    return calories


def part_1(data: List[str]):
    calories = calc_calories(data)

    return max(calories)


def part_2(data: List[str]):
    calories = calc_calories(data)

    return sum(sorted(calories)[-3:])
