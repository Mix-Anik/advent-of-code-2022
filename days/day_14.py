import re
from typing import List


def visualize(grid: dict, bounds: list):
    res = ''

    for y in range(bounds[0][1], bounds[1][1] + 1):
        for x in range(bounds[0][0], bounds[1][0] + 1):
            res += grid[(x, y)]
        res += '\n'

    print(res)


def part_1(data: List[str]):
    grid, bounds = parse_data(data)

    while (new_grid := drop_sand(grid, bounds)) != grid:
        grid = new_grid

    # visualize(grid, bounds)

    return len([v for v in grid.values() if v == 'o'])


def part_2(data: List[str]):
    max_y = max([int(y) for y in re.findall(r',(\d+)\s', ';'.join(data))])
    half_len = 200
    data.append(f'{500 - half_len},{max_y + 2} -> {500 + half_len},{max_y + 2}')

    grid, bounds = parse_data(data)

    while (new_grid := drop_sand(grid, bounds)) != grid:
        grid = new_grid

    # visualize(grid, bounds)

    return len([v for v in grid.values() if v == 'o']) + 1


def parse_data(data: List[str]):
    rocks = {}
    bounds = [[float('inf'), 0], [0, 0]]

    for line in data:
        prev = None

        for coords in line.split(' -> '):
            x, y = coords.split(',')
            x, y = int(x), int(y)

            if prev and x != prev[0]:
                for i in range(min(x, prev[0]), max(x, prev[0]) + 1):
                    rocks[(i, y)] = '#'

            if prev and y != prev[1]:
                for i in range(min(y, prev[1]), max(y, prev[1]) + 1):
                    rocks[(x, i)] = '#'

            if x < bounds[0][0]:
                bounds[0][0] = x
            if x > bounds[1][0]:
                bounds[1][0] = x
            if y > bounds[1][1]:
                bounds[1][1] = y

            prev = (x, y)

    grid = {(x, y): '.' for x in range(bounds[0][0], bounds[1][0] + 1) for y in range(bounds[0][1], bounds[1][1] + 1)}
    grid.update(rocks)

    return grid, bounds


def drop_sand(grid: dict, bounds: list):
    sand_pos = (500, 0)
    new_grid = grid.copy()

    for y in range(1, bounds[1][1] + 2):
        next_point = (sand_pos[0], y)
        next_point_left = (sand_pos[0] - 1, y)
        next_point_right = (sand_pos[0] + 1, y)
        bottom = new_grid.get(next_point, None)
        left = new_grid.get(next_point_left, None)
        right = new_grid.get(next_point_right, None)
        new_sand_pos = None

        if bottom and new_grid[next_point] == '.':
            new_grid[next_point] = 'o'
            new_sand_pos = next_point
        elif left and new_grid[next_point_left] == '.':
            new_grid[next_point_left] = 'o'
            new_sand_pos = next_point_left
        elif right and new_grid[next_point_right] == '.':
            new_grid[next_point_right] = 'o'
            new_sand_pos = next_point_right

        if (not bottom) or (bottom != '.' and not left) or (bottom != '.' and left != '.' and not right):
            new_grid[sand_pos] = '.'

        if not new_sand_pos:
            break

        new_grid[sand_pos] = '.'
        sand_pos = new_sand_pos

    return new_grid
