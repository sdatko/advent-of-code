#!/usr/bin/env python3
#
# Task:
# Based on your calculations, the planned course doesn't seem to make
# any sense. You find the submarine manual and discover that the process
# is actually slightly more complicated.
# In addition to horizontal position and depth, you'll also need to track
# a third value, aim, which also starts at 0. The commands also mean something
# entirely different than you first thought:
# - down X increases your aim by X units,
# - up X decreases your aim by X units,
# - forward X does two things:
#   - It increases your horizontal position by X units.
#   - It increases your depth by your aim multiplied by X.
# Again note that since you're on a submarine, down and up do the opposite
# of what you might expect: "down" means aiming in the positive direction.
# Using this new interpretation of the commands, calculate the horizontal
# position and depth you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your
# final depth?
#
# Solution:
# The difference in this part required us to introduce an additional helper
# variable and customize the actions for each given command. The rest remains
# as it was in previous part.
#

INPUT_FILE = 'input.txt'


def main():
    commands = [line.split() for line in open(INPUT_FILE, 'r')]

    horizontal = 0
    depth = 0
    aim = 0

    for direction, value in commands:
        if direction == 'forward':
            horizontal += int(value)
            depth += aim * int(value)
        elif direction == 'up':
            aim -= int(value)
        elif direction == 'down':
            aim += int(value)
        else:
            print('Unrecognized command!')
            print('>>>', direction, value)
            return -1

    print(horizontal * depth)


if __name__ == '__main__':
    main()
