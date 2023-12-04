#!/usr/bin/env python3
#
# --- Day 3: No Matter How You Slice It ---
#
# The Elves managed to locate the chimney-squeeze prototype fabric for
# Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall
# of the warehouse in the middle of the night). Unfortunately, anomalies are
# still affecting them - nobody can even agree on how to cut the fabric.
#
# The whole piece of fabric they're working on is a very large square
# - at least 1000 inches on each side.
#
# Each Elf has made a claim about which area of fabric would be ideal
# for Santa's suit. All claims have an ID and consist of a single rectangle
# with edges parallel to the edges of the fabric. Each claim's rectangle
# is defined as follows:
#
# – The number of inches between the left edge of the fabric
#   and the left edge of the rectangle.
# – The number of inches between the top edge of the fabric
#   and the top edge of the rectangle.
# – The width of the rectangle in inches.
# – The height of the rectangle in inches.
#
# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle
# 3 inches from the left edge, 2 inches from the top edge, 5 inches wide,
# and 4 inches tall. Visually, it claims the square inches of fabric
# represented by # (and ignores the square inches of fabric represented by .)
# in the diagram below:
#
#   ...........
#   ...........
#   ...#####...
#   ...#####...
#   ...#####...
#   ...#####...
#   ...........
#   ...........
#   ...........
#
# The problem is that many of the claims overlap, causing two or more claims
# to cover part of the same areas. For example, consider the following claims:
#
#   #1 @ 1,3: 4x4
#   #2 @ 3,1: 4x4
#   #3 @ 5,5: 2x2
#
# Visually, these claim the following areas:
#
#   ........
#   ...2222.
#   ...2222.
#   .11XX22.
#   .11XX22.
#   .111133.
#   .111133.
#   ........
#
# The four square inches marked with X are claimed by both 1 and 2.
# (Claim 3, while adjacent to the others, does not overlap either of them.)
#
# If the Elves all proceed with their own plans, none of them will have enough
# fabric. How many square inches of fabric are within two or more claims?
#
#
# --- Solution ---
#
# We start by reading the input file into a 2D list of numbers, as the numeric
# values are all what we care about – we split over newlines, then in each line
# we remove the #, @ and : characters and replace comma and x with space,
# with mapping everything into a tuple of integers. Then we perform a loop
# over the list of tuples – each tuple has 5 numbers, specifying a rectangle.
# Within the loop, we find every possible Xi,Yi values covered by current
# rectangle and we label such positions as covered by additional rectangle.
# Finally, we count the number of tiles (unique Xi,Yi positions) that were
# covered by more than 1 rectangle.
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

    overlappings = len([x for x in area.values() if x > 1])

    print(overlappings)


if __name__ == '__main__':
    main()
