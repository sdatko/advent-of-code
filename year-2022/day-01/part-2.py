#!/usr/bin/env python3
#
# --- Day 1: Calorie Counting / Part Two ---
#
# By the time you calculate the answer to the Elves' question, they've already
# realized that the Elf carrying the most Calories of food might eventually
# run out of snacks.
#
# To avoid this unacceptable situation, the Elves would instead like to know
# the total Calories carried by the top three Elves carrying the most Calories.
# That way, even if one of those Elves runs out of snacks, they still have
# two backups.
#
# In the example above, the top three Elves are the fourth Elf (with 24000
# Calories), then the third Elf (with 11000 Calories), then the fifth Elf
# (with 10000 Calories). The sum of the Calories carried by these three elves
# is 45000.
#
# Find the top three Elves carrying the most Calories.
# How many Calories are those Elves carrying in total?
#
#
# --- Solution ---
#
# The difference here is that we need to take 3 biggest elements, not just one,
# For that, we sort the obtained values with descending order (reverse=True)
# and we select first 3 elements from the sorted collection.
# Then the answer is just a sum of those 3 final elements.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        elves = [list(map(int, elf.strip().split('\n')))
                 for elf in file.read().split('\n\n')]

    top_three = sorted([sum(elf) for elf in elves], reverse=True)[:3]

    print(sum(top_three))


if __name__ == '__main__':
    main()
