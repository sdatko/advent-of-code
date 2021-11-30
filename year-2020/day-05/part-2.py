#!/usr/bin/env python3
#
# Task:
# It's a completely full flight, so your seat should be the only missing
# boarding pass in your list. However, there's a catch: some of the seats
# at the very front and back of the plane don't exist on this aircraft,
# so they'll be missing from your list as well.
# Your seat wasn't at the very front or back, though;
# the seats with IDs +1 and -1 from yours will be in your list.
# What is the ID of your seat?
#
# Solution:
# First we produce a set of all possibly available seats IDs – every seat
# is coded on 10 digits, so there are (2^N - 1) possibilities in total.
# Then we remove every seat we know is occupied from this list.
# Finally we check if in remaining available seats are such ones that
# have previous and next seat occupied.
#

INPUT_FILE = 'input.txt'


def main():
    entries = [line.strip('\n') for line in open(INPUT_FILE, 'r')]

    available_seats = set(range(2**10))  # range(N) goes to N-1, so it is ok
    occupied_seats = set()

    for entry in entries:
        row_spec = entry[:7].replace('F', '0').replace('B', '1')
        col_spec = entry[7:].replace('L', '0').replace('R', '1')

        row = int(row_spec, 2)
        col = int(col_spec, 2)

        seat_ID = row * 8 + col

        available_seats.remove(seat_ID)
        occupied_seats.add(seat_ID)

    for seat_ID in available_seats:
        if seat_ID - 1 in occupied_seats and seat_ID + 1 in occupied_seats:
            print(seat_ID)


if __name__ == '__main__':
    main()
