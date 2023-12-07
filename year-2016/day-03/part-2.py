#!/usr/bin/env python3
#
# --- Day 3: Squares With Three Sides / Part Two ---
#
# Now that you've helpfully marked up their design documents, it occurs
# to you that triangles are specified in groups of three vertically.
# Each set of three numbers in a column specifies a triangle.
# Rows are unrelated.
#
# For example, given the following specification, numbers with the same
# hundreds digit would be part of the same triangle:
#
#   101 301 501
#   102 302 502
#   103 303 503
#   201 401 601
#   202 402 602
#   203 403 603
#
# In your puzzle input, and instead reading by columns,
# how many of the listed triangles are possible?
#
#
# --- Solution ---
#
# The difference here is that we read the input file into a single long list
# of numbers. Then we iterate over the list using a window slice of size 9,
# constructing 3 triangles within that window. We count the triangles that
# are possible to construct and finally we return the number of such triangles.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        buffer = list(map(int, file.read().strip().replace('\n', ' ').split()))

    possible = 0

    for i in range(0, len(buffer), 9):
        for j in range(3):
            a, b, c = sorted([
                buffer[i + j + 0],
                buffer[i + j + 3],
                buffer[i + j + 6],
            ])

            if (a + b) > c:
                possible += 1

    print(possible)


if __name__ == '__main__':
    main()
