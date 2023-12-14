#!/usr/bin/env python3
#
# --- Day 14: Parabolic Reflector Dish ---
#
# You reach the place where all of the mirrors were pointing: a massive
# parabolic reflector dish attached to the side of another large mountain.
#
# The dish is made up of many small mirrors, but while the mirrors
# themselves are roughly in the shape of a parabolic reflector dish,
# each individual mirror seems to be pointing in slightly the wrong
# direction. If the dish is meant to focus light, all it's doing right
# now is sending it in a vague direction.
#
# This system must be what provides the energy for the lava! If you focus
# the reflector dish, maybe you can go where it's pointing and use the light
# to fix the lava production.
#
# Upon closer inspection, the individual mirrors each appear to be connected
# via an elaborate system of ropes and pulleys to a large metal platform
# below the dish. The platform is covered in large rocks of various shapes.
# Depending on their position, the weight of the rocks deforms the platform,
# and the shape of the platform controls which ropes move and ultimately
# the focus of the dish.
#
# In short: if you move the rocks, you can focus the dish. The platform
# even has a control panel on the side that lets you tilt it in one
# of four directions! The rounded rocks (O) will roll when the platform
# is tilted, while the cube-shaped rocks (#) will stay in place. You note
# the positions of all of the empty spaces (.) and rocks (your puzzle input).
# For example:
#
#   O....#....
#   O.OO#....#
#   .....##...
#   OO.#O....O
#   .O.....O#.
#   O.#..O.#.#
#   ..O..#O..O
#   .......O..
#   #....###..
#   #OO..#....
#
# Start by tilting the lever so all of the rocks will slide north
# as far as they will go:
#
#   OOOO.#.O..
#   OO..#....#
#   OO..O##..O
#   O..#.OO...
#   ........#.
#   ..#....#.#
#   ..O..#.O.O
#   ..O.......
#   #....###..
#   #....#....
#
# You notice that the support beams along the north side of the platform
# are damaged; to ensure the platform doesn't collapse, you should calculate
# the total load on the north support beams.
#
# The amount of load caused by a single rounded rock (O) is equal to
# the number of rows from the rock to the south edge of the platform,
# including the row the rock is on. (Cube-shaped rocks (#) don't contribute
# to load.) So, the amount of load caused by each rock in each row
# is as follows:
#
#   OOOO.#.O.. 10
#   OO..#....#  9
#   OO..O##..O  8
#   O..#.OO...  7
#   ........#.  6
#   ..#....#.#  5
#   ..O..#.O.O  4
#   ..O.......  3
#   #....###..  2
#   #....#....  1
#
# The total load is the sum of the load caused by all of the rounded rocks.
# In this example, the total load is 136.
#
# Tilt the platform so that the rounded rocks all roll north.
# Afterward, what is the total load on the north support beams?
#
#
# --- Solution ---
#
# We start by reading the input file into a list of strings – the platform
# definition, by splitting the file content over newlines. Then we browse
# the platform to identify the coordinates (x, y) of all rocks and obstacles.
# Next, we sort the rocks coordinates by the Y axis and we attempt to move
# every rock as much as possible upwards – until the next position (nx, ny)
# is valid and not occupied by any obstacle or other rock. Finally, we can
# calculate the total load for the reached arrangement to return as an answer.
#

INPUT_FILE = 'input.txt'

OBSTACLE = '#'
ROCK = 'O'
SPACE = '.'


def main():
    with open(INPUT_FILE, 'r') as file:
        platform = file.read().strip().split('\n')

    height = len(platform)
    total_load = 0

    obstacles = []
    rocks = []

    for y, row in enumerate(platform):
        for x, col in enumerate(row):
            if col == ROCK:
                rocks.append((x, y))
            elif col == OBSTACLE:
                obstacles.append((x, y))

    # roll all rocks north
    rocks = sorted(rocks, key=lambda pair: pair[1])

    for i, (x, y) in enumerate(rocks):
        nx, ny = (x, y - 1)

        while all([nx >= 0,
                   ny >= 0,
                   (nx, ny) not in obstacles,
                   (nx, ny) not in rocks]):
            rocks[i] = (nx, ny)
            nx, ny = (nx, ny - 1)

    # calculate load
    for (_, y) in rocks:
        total_load += (height - y)

    print(total_load)


if __name__ == '__main__':
    main()
