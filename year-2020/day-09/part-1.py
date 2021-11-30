#!/usr/bin/env python3
#
# Task:
# The first step of attacking the weakness in the XMAS data is to find
# the first number in the list (after the preamble) which is not the sum
# of two of the 25 numbers before it. What is the first number that does
# not have this property?
#
# Solution:
# We produce a list of numbers and then sliding window over that list.
# Then we create a set of this window and we calculate a set of complementary
# numbers to every entry from this set and our target value, which is next
# number after the sliding window. Finally we calculate intersection of these
# two sets and if the number of possible solutions is smaller than 2, we found
# our problematic number.
#

INPUT_FILE = 'input.txt'

WINDOW_SIZE = 25


def main():
    numbers = [int(number)
               for number in open(INPUT_FILE, 'r').read().strip().split('\n')]

    index = 0
    while True:
        xmas_numbers = set(numbers[index:index + WINDOW_SIZE])
        new_number = numbers[index + WINDOW_SIZE]

        complementary = set([new_number - xmas_number
                             for xmas_number in xmas_numbers])

        results = list(set.intersection(xmas_numbers, complementary))

        if len(results) < 2:
            print(new_number)
            break

        index += 1


if __name__ == '__main__':
    main()
