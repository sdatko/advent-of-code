#!/usr/bin/env python3
#
# --- Day 3: Spiral Memory ---
#
# You come across an experimental new kind of memory stored
# on an infinite two-dimensional grid.
#
# Each square on the grid is allocated in a spiral pattern starting
# at a location marked 1 and then counting up while spiraling outward.
# For example, the first few squares are allocated like this:
#
#   17  16  15  14  13
#   18   5   4   3  12
#   19   6   1   2  11
#   20   7   8   9  10
#   21  22  23---> ...
#
# While this is very space-efficient (no squares are skipped), requested
# data must be carried back to square 1 (the location of the only access
# port for this memory system) by programs that can only move up, down,
# left, or right. They always take the shortest path: the Manhattan Distance
# between the location of the data and square 1.
#
# For example:
# – Data from square 1 is carried 0 steps, since it's at the access port.
# – Data from square 12 is carried 3 steps, such as: down, left, left.
# – Data from square 23 is carried only 2 steps: up twice.
# – Data from square 1024 must be carried 31 steps.
#
# How many steps are required to carry the data from the square identified
# in your puzzle input all the way to the access port?
#
#
# --- Solution ---
#
# We start by reading the input value from a file, expecting a single integer.
# Then we prepare a bunch of helper variables; as we will be tracking position
# in 2D-space, the complex numbers are coming handy. After analyzing the moves
# pattern in the example, we basically need to follow a series of steps that
# involves moving in a direction for some distance, then turning, moving again
# for the same distance, then turning once more and increasing the distance
# to move next, starting with distance 1 and direction right. In other words,
# the pattern is: 1, turn, 1, turn, 2, turn, 2, turn, 3, turn, 3 turn, 4, ...;
# and so on until at some point we travelled the assumed distance.
# Finally, we return the L1 distance to the position we reached.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        data = int(file.read().strip())

    move = [
        complex(1, 0),  # right
        complex(0, -1),  # up
        complex(-1, 0),  # left
        complex(0, 1),  # down
    ]
    position = complex(0, 0)

    distance_to_turn = 1
    steps_in_direction = 0
    times_turned = 0

    total_distance = 1
    while total_distance < data:
        position += move[0]
        steps_in_direction += 1
        total_distance += 1

        if steps_in_direction == distance_to_turn:  # turn
            move.append(move.pop(0))
            steps_in_direction = 0
            times_turned += 1

            if times_turned == 2:
                distance_to_turn += 1
                times_turned = 0

    print(int(abs(position.real) + abs(position.imag)))


if __name__ == '__main__':
    main()
