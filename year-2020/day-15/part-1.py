#!/usr/bin/env python3
#
# Task:
# In this game, the players take turns saying numbers. They begin by taking
# turns reading from a list of starting numbers (your puzzle input). Then,
# each turn consists of considering the most recently spoken number:
# - If that was the first time the number has been spoken, the current player
#   says 0.
# - Otherwise, the number had been spoken before; the current player announces
#   how many turns apart the number is from when it was previously spoken.
# So, after the starting numbers, each turn results in that player speaking
# aloud either 0 (if the last number is new) or an age (if the last number
# is a repeat).
# Given your starting numbers, what will be the 2020th number spoken?
#
# Solution:
# We use the dictionary to store the information about spoken numbers.
# Each key is a number itself, while the value is a round number when
# the number was last spoken. The number is new, if it is not registered
# as a key in our dictionary yet – in such case we register it and save
# value 0 as end of current round (spoken number). If the given number was
# spoken before, we just need to subtract the value in dictionary from the
# previous round number, obtaining the new "spoken" number and overwrite
# the value of history in dictionary to the previous round number.
# What remains is to process the first rounds – if there are starting numbers,
# we ignore what was done and treat the next elements from this starting list
# as our previously spoken numbers.
#

INPUT_FILE = 'input.txt'

WANTED_INDEX = 2020


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
