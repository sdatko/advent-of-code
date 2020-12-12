#!/usr/bin/env python3
#
# Task:
# As soon as people start to arrive, you realize your mistake. People don't
# just care about adjacent seats - they care about the first seat they can
# see in each of those eight directions!
# Now, instead of considering just the eight immediately adjacent seats,
# consider the first seat in each of those eight directions.
# Also, people seem to be more tolerant than you expected: it now takes five
# or more visible occupied seats for an occupied seat to become empty.
# Given the new visibility method and the rule change for occupied seats
# becoming empty, once equilibrium is reached, how many seats end up occupied?
#
# Solution:
# Main change here is related to the way of finding first seat in a given
# direction. What is important is that basically we ignore the floors (.)
# when looking through the grid. For this we implemented a function that
# tries elements one by one in a given axis until one of wanted values
# is encountered.
#

INPUT_FILE = 'input.txt'

EMPTY_SEAT = 'L'
OCCUPIED_SEAT = '#'
FLOOR = '.'


def safe_grid_get(array, index_y, index_x, default=None):
    if index_y < 0 or index_x < 0:
        return default
    try:
        return array[index_y][index_x]
    except IndexError:
        return default


def find_occupied(grid, x, y, direction_x, direction_y):
    pos_x = x
    pos_y = y

    while True:
        pos_x = pos_x + direction_x
        pos_y = pos_y + direction_y

        seat = safe_grid_get(grid, pos_y, pos_x)

        if seat in [OCCUPIED_SEAT, EMPTY_SEAT, None]:
            return seat


def can_be_occupied(grid, x, y):
    neighbors = [
        find_occupied(grid, x, y, -1, -1),
        find_occupied(grid, x, y, 0, -1),
        find_occupied(grid, x, y, +1, -1),
        find_occupied(grid, x, y, -1, 0),
        find_occupied(grid, x, y, +1, 0),
        find_occupied(grid, x, y, -1, +1),
        find_occupied(grid, x, y, 0, +1),
        find_occupied(grid, x, y, +1, +1)
    ]

    if OCCUPIED_SEAT in neighbors:
        return False
    else:
        return True


def shall_be_free(grid, x, y):
    neighbors = [
        find_occupied(grid, x, y, -1, -1),
        find_occupied(grid, x, y, 0, -1),
        find_occupied(grid, x, y, +1, -1),
        find_occupied(grid, x, y, -1, 0),
        find_occupied(grid, x, y, +1, 0),
        find_occupied(grid, x, y, -1, +1),
        find_occupied(grid, x, y, 0, +1),
        find_occupied(grid, x, y, +1, +1)
    ]

    if neighbors.count(OCCUPIED_SEAT) >= 5:
        return True
    else:
        return False


def main():
    grid = [list(line.strip('\n')) for line in open(INPUT_FILE, 'r')]

    size_x = len(grid[0])
    size_y = len(grid)

    while True:
        new_grid = [row[:] for row in grid]
        changed = False

        for y in range(size_y):
            for x in range(size_x):
                if grid[y][x] == EMPTY_SEAT and can_be_occupied(grid, x, y):
                    new_grid[y][x] = OCCUPIED_SEAT
                    changed = True
                elif grid[y][x] == OCCUPIED_SEAT and shall_be_free(grid, x, y):
                    new_grid[y][x] = EMPTY_SEAT
                    changed = True

        if changed:
            grid = new_grid
        else:
            break

    print(sum([row.count(OCCUPIED_SEAT) for row in grid]))


if __name__ == '__main__':
    main()
