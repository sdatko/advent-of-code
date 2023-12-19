#!/usr/bin/env python3
#
# --- Day 1: Report Repair / Part Two ---
#
# The Elves in accounting are thankful for your help; one of them even
# offers you a starfish coin they had left over from a past vacation.
# They offer you a second one if you can find three numbers in your
# expense report that meet the same criteria.
#
# Using the above example again, the three entries that sum to 2020 are 979,
# 366, and 675. Multiplying them together produces the answer, 241861950.
#
# In your expense report, what is the product of the three entries
# that sum to 2020?
#
#
# --- Solution ---
#
# Build a set of input numbers and the set of numbers that are complementary
# to all possible pairs in the first set. If there is a number that satisfies
# the equation A + B + C = 2020, we can find the number C in the complementary
# set. This works only if there is exactly one such triplet in the data set.
#

INPUT_FILE = 'input.txt'
WANTED_NUMBER = 2020


def main():
    expenses = [int(expense) for expense in open(INPUT_FILE, 'r')]

    numbers = set(expenses)
    pairs = [(a, b) for a in expenses for b in expenses if a != b]
    complementary = set([WANTED_NUMBER - a - b for a, b in pairs])

    results = list(set.intersection(numbers, complementary))
    solution = results[0] * results[1] * results[2]

    print(solution)


if __name__ == '__main__':
    main()
