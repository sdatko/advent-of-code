#!/usr/bin/env python3
#
# Task:
# Find the two entries that sum to 2020;
# what do you get if you multiply them together?
#
# Solution:
# Build a set of input numbers and the set of complementary numbers.
# If there is a number B, complementary to A, such as B = 2020 - A,
# then it should be present in both sets. We can find it by intersection
# of this two sets.
#

INPUT_FILE = 'input.txt'
WANTED_NUMBER = 2020


def main():
    expenses = [int(expense) for expense in open(INPUT_FILE, 'r')]

    numbers = set(expenses)
    complementary = set([WANTED_NUMBER - expense for expense in expenses])

    results = list(set.intersection(numbers, complementary))
    solution = results[0] * results[1]

    print(solution)


if __name__ == '__main__':
    main()
