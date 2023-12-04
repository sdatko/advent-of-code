#!/usr/bin/env python3
#
# --- Day 3: No Matter How You Slice It / Part Two ---
#
# Amidst the chaos, you notice that exactly one claim doesn't overlap
# by even a single square inch of fabric with any other claim.
# If you can somehow draw attention to it, maybe the Elves will be able
# to make Santa's suit after all!
#
# For example, in the claims above, only claim 3 is intact
# after all claims are made.
#
# What is the ID of the only claim that doesn't overlap?
#
#
# --- Solution ---
#
# The difference here is that after labeling all positions, we repeat all
# steps in order to find a rectangle that covers all positions previously
# labelled as covered by exactly one rectangle.
#
# My original idea involved replacing the counts with sets for each position
# and recording the rectangles IDs covering these positions, then finding one
# ID that appears nowhere else, however as sets operations are pretty slow,
# the current solution is better.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        rects = [tuple(map(int, line.replace('#', '')
                                    .replace('@', '')
                                    .replace(',', ' ')
                                    .replace(':', '')
                                    .replace('x', ' ')
                                    .split()))
                 for line in file.read().strip().split('\n')]

    area = {}

    for rect in rects:
        _, x, y, width, height = rect

        for xi in range(x, x + width):
            for yi in range(y, y + height):
                index = (xi, yi)

                if index not in area:
                    area[index] = 0

                area[index] += 1

    for rect in rects:
        ID, x, y, width, height = rect
        unique = True

        for xi in range(x, x + width):
            for yi in range(y, y + height):
                index = (xi, yi)

                if area[index] > 1:
                    unique = False
                    break

            if not unique:
                break

        if unique:
            print(ID)


if __name__ == '__main__':
    main()
