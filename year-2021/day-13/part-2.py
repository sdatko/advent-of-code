#!/usr/bin/env python3
#
# Task:
# Finish folding the transparent paper according to the instructions.
# The manual says the code is always eight capital letters.
# What code do you use to activate the infrared thermal imaging camera system?
#
# Solution:
# This part extends the previous code – instead of considering a single fold,
# we iterate in a loop over all defined foldings. Then all we need to do is
# to draw the remaining positions (small 2D area) to read the answer.

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        puzzle_input = file.read().split('\n\n')

    positions = [tuple(map(int, line.strip().split(',')))
                 for line in puzzle_input[0].splitlines()]
    foldings = [tuple(line.strip().replace('fold along ', '').split('='))
                for line in puzzle_input[1].splitlines()]
    foldings = [(axis, int(value)) for (axis, value) in foldings]

    for (axis, value) in foldings:
        for index, (x, y) in enumerate(positions):
            if axis == 'x':
                if x < value:
                    continue
                positions[index] = (2*value - x, y)
            if axis == 'y':
                if y < value:
                    continue
                positions[index] = (x, 2*value - y)

    positions = set(positions)
    max_x = max([x for (x, y) in positions])
    max_y = max([y for (x, y) in positions])

    area = [[' '] * (max_x + 1) for _ in range(max_y + 1)]

    for (x, y) in positions:
        area[y][x] = '#'

    for line in area:
        print(''.join(line))


if __name__ == '__main__':
    main()
