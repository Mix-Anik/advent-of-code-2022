from typing import List
from string import ascii_letters


def part_1(data: List[str]):
    result = 0

    for rucksack in data:
        hs = int(len(rucksack) / 2)
        common = list(set(rucksack[:hs]).intersection(rucksack[hs:]))[0]
        result += ascii_letters.index(common) + 1

    return result


def part_2(data: List[str]):
    result = 0

    for idx in range(0, len(data), 3):
        common = list(set(data[idx]).intersection(data[idx + 1]).intersection(data[idx + 2]))[0]
        result += ascii_letters.index(common) + 1

    return result
