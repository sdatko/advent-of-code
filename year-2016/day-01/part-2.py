#!/usr/bin/env python3
#
# --- Day 1: No Time for a Taxicab / Part Two ---
#
# Then, you notice the instructions continue on the back of the Recruiting
# Document. Easter Bunny HQ is actually at the first location you visit twice.
#
# For example, if your instructions are R8, R4, R4, R8, the first location
# you visit twice is 4 blocks away, due East.
#
# How many blocks away is the first location you visit twice?
#
#
# --- Solution ---
#
# The difference here is that we need to record all intermediate steps
# and break the loop over sequences when we encounter position already visited.
# Note that (IMO) this is not clearly explained in the description, but
# the point is an intersection between the first and the last move (R8 east,
# [0,0] -> [8,0]; and R8 north, [4,-4] -> [4,4]; drawing the moves R8 R4 R4 R8
# on a paper helps to visualize that).
#

INPUT_FILE = 'input.txt'

DIRECTIONS = (
    (-1, 0),  # west
    (0, 1),  # north
    (1, 0),  # east
    (0, -1),  # south
)


def main():
    with open(INPUT_FILE, 'r') as file:
        sequences = [(sequence[0], int(sequence[1:]))
                     for sequence in file.read().strip().split(', ')]

    direction = 1  # initially we face north
    position = [0, 0]
    visited = set()

    for turn, distance in sequences:
        if turn == 'L':
            direction = (direction - 1) % len(DIRECTIONS)
        else:
            direction = (direction + 1) % len(DIRECTIONS)

        for step in range(distance):
            position[0] += DIRECTIONS[direction][0]
            position[1] += DIRECTIONS[direction][1]

            if tuple(position) in visited:
                break
            visited.add(tuple(position))
        else:
            continue
        break

    total_distance = abs(position[0]) + abs(position[1])
    print(total_distance)


if __name__ == '__main__':
    main()
