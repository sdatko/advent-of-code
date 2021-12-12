#!/usr/bin/env python3
#
# Task:
# It seems like the individual flashes aren't bright enough to navigate.
# However, you might have a better option:
# the flashes seem to be synchronizing!
# If you can calculate the exact moments when the octopuses will all flash
# simultaneously, you should be able to navigate through the cavern.
# What is the first step during which all octopuses flash?
#
# Solution:
# The code here is basically the same as it was in part 1. The only difference
# is that instead of running a given number of simulation steps, we launch
# an infinite loop with a stop condition: the set of octopus that flashed
# in loop iteration must contain all matrix elements (meaning its length must
# be equal to number of matrix columns times number of matrix rows).
# As answer, we print the step number in which such situation occurred.
#

INPUT_FILE = 'input.txt'


def main():
    grid = [list(map(int, list(characters)))
            for line in open(INPUT_FILE, 'r')
            for characters in line.strip().split()]

    rows = len(grid)
    cols = len(grid[0])

    goal = rows * cols
    step = 0

    while True:
        step += 1
        to_flash = set()
        flashed = set()

        for row in range(rows):
            for col in range(cols):
                grid[row][col] += 1

                if grid[row][col] > 9:
                    to_flash.add((row, col))

        while len(to_flash) > 0:
            (row, col) = to_flash.pop()

            grid[row][col] = 0
            flashed.add((row, col))

            for adjacent_row in range(row - 1, row + 2):
                if adjacent_row < 0 or adjacent_row >= rows:
                    continue

                for adjacent_col in range(col - 1, col + 2):
                    if adjacent_col < 0 or adjacent_col >= cols:
                        continue

                    if (adjacent_row, adjacent_col) in flashed:
                        continue

                    grid[adjacent_row][adjacent_col] += 1

                    if grid[adjacent_row][adjacent_col] > 9:
                        to_flash.add((adjacent_row, adjacent_col))

        if len(flashed) == goal:
            break

    print(step)


if __name__ == '__main__':
    main()
