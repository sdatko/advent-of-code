#!/usr/bin/env python3
#
# Task:
# Considering every single measurement isn't as useful as you expected:
# there's just too much noise in the data. Instead, consider sums of
# a three-measurement sliding window.
# Your goal now is to count the number of times the sum of measurements
# in this sliding window increases from the previous sum. Stop when there
# aren't enough measurements left to create a new three-measurement sum.
# How many sums are larger than the previous sum?
#
# Solution:
# The difference here is that we need to sum a few values for comparison,
# instead of taking just each array element. To achieve this, we introduce
# additional variable and implement a sliding window within the for loop.
# As first value for comparison, we take a sum of first few elements from
# the input list. Then just the first index (0) is omitted in the loop.
#

INPUT_FILE = 'input.txt'


def main():
    depths = [int(depth) for depth in open(INPUT_FILE, 'r')]

    previous = 0
    increases = 0
    window_size = 3

    previous = sum(depths[:window_size])

    for index in range(1, len(depths) - window_size + 1):
        current = sum(depths[index:index + window_size])
        if current > previous:
            increases += 1
        previous = current

    print(increases)


if __name__ == '__main__':
    main()
