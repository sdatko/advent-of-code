#!/usr/bin/env python3
#
# --- Day 3: Toboggan Trajectory / Part Two ---
#
# Time to check the rest of the slopes - you need to minimize the probability
# of a sudden arboreal stop, after all.
#
# Determine the number of trees you would encounter if, for each
# of the following slopes, you start at the top-left corner and
# traverse the map all the way to the bottom:
#
# – Right 1, down 1.
# – Right 3, down 1. (This is the slope you already checked.)
# – Right 5, down 1.
# – Right 7, down 1.
# – Right 1, down 2.
#
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s)
# respectively; multiplied together, these produce the answer 336.
#
# What do you get if you multiply together the number of trees encountered
# on each of the listed slopes?
#
#
# --- Solution ---
#
# This is basically the same as previous one, just with more paths
# to consider. We moved the calculation to a different function and
# then execute if for defined slopes.
#

INPUT_FILE = 'input.txt'
TREE = '#'


def trees_by_slope(grid, move_x, move_y):
    trees = 0

    pos_x = 0
    pos_y = 0

    size_x = len(grid[0])
    size_y = len(grid)

    while pos_y != (size_y - 1):
        pos_x += move_x
        pos_x %= size_x
        pos_y += move_y

        if grid[pos_y][pos_x] == TREE:
            trees += 1

    return trees


def main():
    grid = [line.strip('\n') for line in open(INPUT_FILE, 'r')]

    moves = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2],
    ]

    result = 1

    for move_x, move_y in moves:
        result *= trees_by_slope(grid, move_x, move_y)

    print(result)


if __name__ == '__main__':
    main()
