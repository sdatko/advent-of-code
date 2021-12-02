#!/usr/bin/env python3
#
# Task:
# It seems like the submarine can take a series of commands like forward 1,
# down 2, or up 3:
# - forward X increases the horizontal position by X units,
# - down X increases the depth by X units,
# - up X decreases the depth by X units.
# Note that since you're on a submarine, down and up affect your depth,
# and so they have the opposite result of what you might expect.
# Calculate the horizontal position and depth you would have after following
# the planned course. What do you get if you multiply your final horizontal
# position by your final depth?
#
# Solution:
# We read the input file line by line, producing a list of elements like
# [direction, value]. Then we simply go over that list, using the first
# part of element (direction) to determine the action (what to modify)
# and the second part to alter the helper variables.
# Finally we simply print the multiplication of both helper variables.
#

INPUT_FILE = 'input.txt'


def main():
    commands = [line.split() for line in open(INPUT_FILE, 'r')]

    horizontal = 0
    depth = 0

    for direction, value in commands:
        if direction == 'forward':
            horizontal += int(value)
        elif direction == 'up':
            depth -= int(value)
        elif direction == 'down':
            depth += int(value)
        else:
            print('Unrecognized command!')
            print('>>>', direction, value)
            return -1

    print(horizontal * depth)


if __name__ == '__main__':
    main()
