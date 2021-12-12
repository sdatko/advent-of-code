#!/usr/bin/env python3
#
# Task:
# You enter a large cavern full of rare bioluminescent dumbo octopuses!
# They seem to not like the Christmas lights on your submarine, so you
# turn them off for now.
# There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus
# slowly gains energy over time and flashes brightly for a moment when its
# energy is full. Although your lights are off, maybe you could navigate
# through the cave without disturbing the octopuses if you could predict
# when the flashes of light will happen.
# Each octopus has an energy level - your submarine can remotely measure
# the energy level of each octopus (your puzzle input).
# The energy level of each octopus is a value between 0 and 9.
# You can model the energy levels and flashes of light in steps.
# During a single step, the following occurs:
# - First, the energy level of each octopus increases by 1.
# - Then, any octopus with an energy level greater than 9 flashes.
#   This increases the energy level of all adjacent octopuses by 1,
#   including octopuses that are diagonally adjacent. If this causes
#   an octopus to have an energy level greater than 9, it also flashes.
#   This process continues as long as new octopuses keep having their
#   energy level increased beyond 9. (An octopus can only flash at most
#   once per step.)
# - Finally, any octopus that flashed during this step has its energy level
#   set to 0, as it used all of its energy to flash.
# Adjacent flashes can cause an octopus to flash on a step even if it begins
# that step with very little energy. Consider the middle octopus with 1 energy
# in this situation:
#   Before any steps:
#     11111
#     19991
#     19191
#     19991
#     11111
#   After step 1:
#     34543
#     40004
#     50005
#     40004
#     34543
#   After step 2:
#     45654
#     51115
#     61116
#     51115
#     45654
# An octopus is highlighted when it flashed during the given step.
# Given the starting energy levels of the dumbo octopuses in your cavern,
# simulate 100 steps. How many total flashes are there after 100 steps?
#
# Solution:
# We read the input file as matrix of numbers (list of lists in Python).
# Then we repeat described actions for a given number of iterations (steps).
# For start we incrementing each matrix element by 1 and save information
# about any element with value greater than 9 (an octopus that will flash now).
# Then we go over set of octopuses to flash. For each one we reset its energy
# level to 0 and move it from one set (to flash) to another (flashed).
# Next we attempt to increment all adjacent positions to the octopus that
# just flashed – provided that the position is valid (row and column exist
# in the matrix) and that octopus have not already flashed in current step.
# If the increment was done, we also check if this operation caused the value
# to be greater than 9 – if so, we save the element in the set of octopuses
# to flash in current step.
# After processing everything from set of octopuses to slash, we count how many
# flashes were there in current step and then go to next iteration.
# Finally we print the total number of flashes after all iterations.
#

INPUT_FILE = 'input.txt'


def main():
    grid = [list(map(int, list(characters)))
            for line in open(INPUT_FILE, 'r')
            for characters in line.strip().split()]

    steps = 100

    rows = len(grid)
    cols = len(grid[0])

    flashes = 0

    for step in range(steps):
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

        flashes += len(flashed)

    print(flashes)


if __name__ == '__main__':
    main()
