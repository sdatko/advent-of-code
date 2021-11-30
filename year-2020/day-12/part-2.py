#!/usr/bin/env python3
#
# Task:
# Before you can give the destination to the captain, you realize that
# the actual action meanings were printed on the back of the instructions
# the whole time.
# Almost all of the actions indicate how to move a waypoint which is relative
# to the ship's position:
# - Action N means to move the waypoint north by the given value.
# - Action S means to move the waypoint south by the given value.
# - Action E means to move the waypoint east by the given value.
# - Action W means to move the waypoint west by the given value.
# - Action L means to rotate the waypoint around the ship left
#   (counter-clockwise) the given number of degrees.
# - Action R means to rotate the waypoint around the ship right
#   (clockwise) the given number of degrees.
# - Action F means to move forward to the waypoint a number of times
#   equal to the given value.
# The waypoint starts 10 units east and 1 unit north relative to the ship.
# The waypoint is relative to the ship; that is, if the ship moves,
# the waypoint moves with it.
# Figure out where the navigation instructions actually lead.
# What is the Manhattan distance between that location and
# the ship's starting position?
#
# Solution:
# In this part, the interpretation of direction vector has changed.
# The actions N, S, E, W alter not a position, but the value of direction.
# The action of F remains as it was.
# The biggest change is related to rotations, as now we do not work only
# on a normalized vectors. For this purpose, the simplified calculation
# based on a rotation matrices was introduced. The calculations is done
# always as the N-times rotation by 90 degrees counter- or clockwise.
#

INPUT_FILE = 'input.txt'


def main():
    instructions = [line.strip('\n') for line in open(INPUT_FILE, 'r')]

    position = [0, 0]
    direction = [10, 1]

    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        if action == 'N':
            direction[1] += value
        elif action == 'S':
            direction[1] -= value
        elif action == 'E':
            direction[0] += value
        elif action == 'W':
            direction[0] -= value
        elif action == 'L':
            rotation_matrix = [
                [0, -1],
                [1, 0]
            ]
            for i in range(int(value / 90)):
                new_direction = direction[:]
                new_direction[0] = rotation_matrix[0][1] * direction[1]
                new_direction[1] = rotation_matrix[1][0] * direction[0]
                direction = new_direction[:]
        elif action == 'R':
            rotation_matrix = [
                [0, 1],
                [-1, 0]
            ]
            for i in range(int(value / 90)):
                new_direction = direction[:]
                new_direction[0] = rotation_matrix[0][1] * direction[1]
                new_direction[1] = rotation_matrix[1][0] * direction[0]
                direction = new_direction[:]
        elif action == 'F':
            position[0] += value * direction[0]
            position[1] += value * direction[1]
        else:
            print('BAD INPUT:', instruction)
            return 1

    print(sum([abs(value) for value in position]))


if __name__ == '__main__':
    main()
