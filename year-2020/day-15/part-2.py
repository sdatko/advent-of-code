#!/usr/bin/env python3
#
# Task:
# Given your starting numbers, what will be the 30000000th number spoken?
#
# Solution:
# No changes, as the original algorithm proven to be effective enough.
# I am not sure if anything can be done better here.
#

INPUT_FILE = 'input.txt'

WANTED_INDEX = 30000000


def main():
    starting_numbers = [int(x)
                        for x in open(INPUT_FILE, 'r').readline().split(',')]

    numbers = {}
    last_number = None
    spoken_number = None

    for i in range(1, WANTED_INDEX + 1):
        if starting_numbers:
            spoken_number = starting_numbers.pop(0)
        last_number = spoken_number

        if last_number not in numbers.keys():
            numbers[last_number] = i - 1
            spoken_number = 0
        else:
            spoken_number = i - 1 - numbers[last_number]
            numbers[last_number] = i - 1

    print(last_number)


if __name__ == '__main__':
    main()
