#!/usr/bin/env python3
#
# Task:
# Suppose the lanternfish live forever and have unlimited food and space.
# Would they take over the entire ocean?
# How many lanternfish would there be after 256 days?
#
# Solution:
# The code that worked was exactly the same as it was for Part 1.
# We only changed how long the simulation takes place.
# However then I noticed that this can be achieved in more efficient way
# – the shifting of all values is not necessary in each loop iteration,
# all we need is to basically increment single position in the array,
# with the position being changed in every iteration. This way instead
# of shifting the values (copying and saving N times) we shift the index
# of position being incremented (one copy and addition needed per iteration).
#

INPUT_FILE = 'input.txt'


def main():
    school = [int(number)
              for line in open(INPUT_FILE, 'r')
              for number in line.strip().split(',')]

    fish = [school.count(number) for number in range(9)]

    for day in range(256):
        current_fish_index = day % 9
        reproduced_fish_index = (current_fish_index + 7) % 9

        reproducing_fish = fish[current_fish_index]
        fish[reproduced_fish_index] += reproducing_fish

    print(sum(fish))


if __name__ == '__main__':
    main()
