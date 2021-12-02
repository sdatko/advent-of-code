#!/usr/bin/env python3
#
# Task:
# As the submarine drops below the surface of the ocean, it automatically
# performs a sonar sweep of the nearby sea floor. On a small screen,
# the sonar sweep report (your puzzle input) appears:
# each line is a measurement of the sea floor depth as the sweep looks further
# and further away from the submarine.
# The first order of business is to figure out how quickly the depth increases,
# just so you know what you're dealing with - you never know if the keys will
# get carried into deeper water by an ocean current or a fish or something.
# To do this, count the number of times a depth measurement increases from
# the previous measurement.
# (There is no measurement before the first measurement.)
# How many measurements are larger than the previous measurement?
#
# Solution:
# We start by reading the input file line by line, treating each one as number.
# Then we simply take the first element from that list, so we have first value
# for comparison. Then we go through the remaining list and count whenever
# the new value is larger than the previous.
#

INPUT_FILE = 'input.txt'


def main():
    depths = [int(depth) for depth in open(INPUT_FILE, 'r')]

    increases = 0

    if depths:
        previous = depths.pop(0)

        for depth in depths:
            if depth > previous:
                increases += 1
            previous = depth

    print(increases)


if __name__ == '__main__':
    main()
