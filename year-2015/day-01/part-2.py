#!/usr/bin/env python3
#
# --- Day 1: Not Quite Lisp / Part Two ---
#
# Now, given the same instructions, find the position of the first character
# that causes him to enter the basement (floor -1). The first character
# in the instructions has position 1, the second character has position 2,
# and so on.
#
# For example:
# – ) causes him to enter the basement at character position 1.
# – ()()) causes him to enter the basement at character position 5.
#
# What is the position of the character that causes Santa to first enter
# the basement?
#
#
# --- Solution ---
#
# The difference here is that we need to interrupt the processing after
# first time the reached floor is negative (below 0). As an answer we return
# the number of steps performed.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        steps = [int(step.replace('(', '1').replace(')', '-1'))
                 for step in list(file.read().strip())]

    floor = 0

    for index, step in enumerate(steps):
        floor += step

        if floor < 0:
            index += 1  # the task assumes that index starts with 1
            break

    print(index)


if __name__ == '__main__':
    main()
