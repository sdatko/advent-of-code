#!/usr/bin/env python3
#
# --- Day 2: Dive! ---
#
# Now, you need to figure out how to pilot this thing.
#
# It seems like the submarine can take a series of commands like forward 1,
# down 2, or up 3:
# - forward X increases the horizontal position by X units,
# - down X increases the depth by X units,
# - up X decreases the depth by X units.
#
# Note that since you're on a submarine, down and up affect your depth,
# and so they have the opposite result of what you might expect.
#
# The submarine seems to already have a planned course (your puzzle input).
# You should probably figure out where it's going. For example:
#   forward 5
#   down 5
#   forward 8
#   up 3
#   down 8
#   forward 2
#
# Your horizontal position and depth both start at 0. The steps above would
# then modify them as follows:
# - forward 5 adds 5 to your horizontal position, a total of 5.
# - down 5 adds 5 to your depth, resulting in a value of 5.
# - forward 8 adds 8 to your horizontal position, a total of 13.
# - up 3 decreases your depth by 3, resulting in a value of 2.
# - down 8 adds 8 to your depth, resulting in a value of 10.
# - forward 2 adds 2 to your horizontal position, a total of 15.
#
# After following these instructions, you would have a horizontal position
# of 15 and a depth of 10. (Multiplying these together produces 150.)
#
# Calculate the horizontal position and depth you would have after following
# the planned course. What do you get if you multiply your final horizontal
# position by your final depth?
#
#
# --- Solution ---
#
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
