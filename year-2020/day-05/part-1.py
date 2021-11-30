#!/usr/bin/env python3
#
# Task:
# Instead of zones or groups, this airline uses binary space partitioning
# to seat people. A seat might be specified like FBFBBFFRLR, where F means
# "front", B means "back", L means "left", and R means "right".
#
# The first 7 characters will either be F or B; these specify exactly one
# of the 128 rows on the plane (numbered 0 through 127). Each letter tells
# you which half of a region the given seat is in. Start with the whole list
# of rows; the first letter indicates whether the seat is in the front
# (0 through 63) or the back (64 through 127). The next letter indicates
# which half of that region the seat is in, and so on until you're left
# with exactly one row.
#
# The last three characters will be either L or R; these specify exactly
# one of the 8 columns of seats on the plane (numbered 0 through 7).
# The same process as above proceeds again, this time with only three steps.
# L means to keep the lower half, while R means to keep the upper half.
#
# So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.
# Every seat also has a unique seat ID: multiply the row by 8, then add
# the column. In this example, the seat has ID 44 * 8 + 5 = 357.
#
# As a sanity check, look through your list of boarding passes.
# What is the highest seat ID on a boarding pass?
#
# Solution:
# Although the description is long and complex, basically every seat ID
# is encoded with binary number, where F and L are zeros and B and R are ones.
# So we replace the characters in the specification and then decode this
# as binary number to decimal base. Finally we just select the highest ID.
#

INPUT_FILE = 'input.txt'


def main():
    entries = [line.strip('\n') for line in open(INPUT_FILE, 'r')]

    highest_ID = -1

    for entry in entries:
        row_spec = entry[:7].replace('F', '0').replace('B', '1')
        col_spec = entry[7:].replace('L', '0').replace('R', '1')

        row = int(row_spec, 2)
        col = int(col_spec, 2)

        seat_ID = row * 8 + col

        if seat_ID > highest_ID:
            highest_ID = seat_ID

    print(highest_ID)


if __name__ == '__main__':
    main()
