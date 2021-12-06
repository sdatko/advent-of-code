#!/usr/bin/env python3
#
# Task:
# The sea floor is getting steeper. Maybe the sleigh keys got carried this way?
# A massive school of glowing lanternfish swims past. They must spawn quickly
# to reach such large numbers - maybe exponentially quickly? You should model
# their growth rate to be sure.
# Although you know nothing about this specific species of lanternfish,
# you make some guesses about their attributes. Surely, each lanternfish
# creates a new lanternfish once every 7 days.
# However, this process isn't necessarily synchronized between every
# lanternfish - one lanternfish might have 2 days left until it creates
# another lanternfish, while another might have 4. So, you can model each
# fish as a single number that represents the number of days until it creates
# a new lanternfish.
# Furthermore, you reason, a new lanternfish would surely need slightly longer
# before it's capable of producing more lanternfish: two more days for its
# first cycle.
# Realizing what you're trying to do, the submarine automatically produces
# a list of the ages of several hundred nearby lanternfish (your puzzle input).
# Find a way to simulate lanternfish.
# How many lanternfish would there be after 80 days?
#
# Solution:
# We read the input file, producing a list of integer values representing the
# time for each fish to reproduce. Then we generate a list with counts of fish
# for each time value (basically a histogram of values). Then in a loop we go
# over this list and save the first element (number of fish reproducing on that
# day), then we shift values in the array (decrement the time for each fish
# to reproduce). Finally in the loop we increment the number of fish with time
# 6 (7 days to reproduce) and add new fish to end of our list (9 days to go).
# As the answer, we simply take sum of list elements after the loop.
#

INPUT_FILE = 'input.txt'


def main():
    school = [int(number)
              for line in open(INPUT_FILE, 'r')
              for number in line.strip().split(',')]

    fish = [school.count(number) for number in range(9)]

    for day in range(80):
        reproducing_fish = fish[0]

        for index in range(1, 9):
            fish[index - 1] = fish[index]

        fish[6] += reproducing_fish
        fish[8] = reproducing_fish

    print(sum(fish))


if __name__ == '__main__':
    main()
