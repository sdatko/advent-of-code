#!/usr/bin/env python3
#
# Task:
# Starting at the top-left corner of your map and following
# a slope of right 3 and down 1, how many trees (#) would you encounter?
#
# Solution:
# We simply interpret the input file as a grid with periodic boundaries.
# After each step in the grid (with modulo) we check what is the current
# symbol at given position. If it is #, we add one.
#

INPUT_FILE = 'input.txt'
TREE = '#'

MOVE_X = 3
MOVE_Y = 1


def main():
    grid = [line.strip('\n') for line in open(INPUT_FILE, 'r')]

    trees = 0

    pos_x = 0
    pos_y = 0

    size_x = len(grid[0])
    size_y = len(grid)

    while pos_y != (size_y - 1):
        pos_x += MOVE_X
        pos_x %= size_x
        pos_y += MOVE_Y

        if grid[pos_y][pos_x] == TREE:
            trees += 1

    print(trees)


if __name__ == '__main__':
    main()
