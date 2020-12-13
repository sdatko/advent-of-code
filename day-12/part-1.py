#!/usr/bin/env python3
#
# Task:
# The navigation instructions (your puzzle input) consists of a sequence
# of single-character actions paired with integer input values. After staring
# at them for a few minutes, you work out what they probably mean:
# - Action N means to move north by the given value.
# - Action S means to move south by the given value.
# - Action E means to move east by the given value.
# - Action W means to move west by the given value.
# - Action L means to turn left the given number of degrees.
# - Action R means to turn right the given number of degrees.
# - Action F means to move forward by the given value in the direction
#   the ship is currently facing.
# The ship starts by facing east. Only the L and R actions change
# the direction the ship is facing. (That is, if the ship is facing east
# and the next instruction is N10, the ship would move north 10 units,
# but would still move east if the following action were F.)
#
# Solution:
# We read the input file, treating each line as a instruction to perform.
# Then we process the instructions one by one, assuming we are in a coordinate
# system as given below. If instruction is one of N, S, E, W, we simply change
# the current position (x, y) values. When it is a rotation L or R, the vector
# for direction is recalculated – a simplification here is made due to a fact
# that input data contains only rotations by a right angle (90 degrees),
# so we can just iterate left or right through a vector of possible values
# for the direction. When there is a F instruction, we add the multiplied value
# of direction to the current position.
#      A N
#      |
# -----+----> E
#      |
#      |
#

INPUT_FILE = 'input.txt'


def main():
    instructions = [line.strip('\n') for line in open(INPUT_FILE, 'r')]

    position = [0, 0]
    direction = [1, 0]

    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'N':
            position[1] += value
        elif action == 'S':
            position[1] -= value
        elif action == 'E':
            position[0] += value
        elif action == 'W':
            position[0] -= value
        elif action == 'L':
            directions = [
                [1, 0],
                [0, -1],
                [-1, 0],
                [0, 1],
            ]
            index = directions.index(direction)
            index -= value / 90
            index %= len(directions)
            direction = directions[int(index)]
        elif action == 'R':
            directions = [
                [1, 0],
                [0, -1],
                [-1, 0],
                [0, 1],
            ]
            index = directions.index(direction)
            index += value / 90
            index %= len(directions)
            direction = directions[int(index)]
        elif action == 'F':
            position[0] += value * direction[0]
            position[1] += value * direction[1]
        else:
            print('BAD INPUT:', instruction)
            return 1

    print(sum([abs(value) for value in position]))


if __name__ == '__main__':
    main()
