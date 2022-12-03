from typing import List
from string import ascii_letters


def part_1(data: List[str]):
    result = 0

    for rucksack in data:
        hs = len(rucksack) // 2
        common ,= set(rucksack[:hs]) & set(rucksack[hs:])
        result += ascii_letters.index(common) + 1

    return result


def part_2(data: List[str]):
    result = 0

    for i in range(0, len(data), 3):
        common ,= set(data[i]) & set(data[i + 1]) & set(data[i + 2])
        result += ascii_letters.index(common) + 1

    return result
