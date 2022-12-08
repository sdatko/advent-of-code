#!/usr/bin/env python3
#
# --- Day 1: Chronal Calibration / Part Two ---
#
# You notice that the device repeats the same frequency change list over
# and over. To calibrate the device, you need to find the first frequency
# it reaches twice.
#
# For example, using the same list of changes above, the device would loop
# as follows:
# – Current frequency  0, change of +1; resulting frequency  1.
# – Current frequency  1, change of -2; resulting frequency -1.
# – Current frequency -1, change of +3; resulting frequency  2.
# – Current frequency  2, change of +1; resulting frequency  3.
# – (At this point, the device continues from the start of the list.)
# – Current frequency  3, change of +1; resulting frequency  4.
# – Current frequency  4, change of -2; resulting frequency  2,
#   which has already been seen.
#
# In this example, the first frequency reached twice is 2. Note that your
# device might need to repeat its list of frequency changes many times before
# a duplicate frequency is found, and that duplicates might be found while
# in the middle of processing the list.
#
# Here are other examples:
# – +1, -1 first reaches 0 twice.
# – +3, +3, +4, -2, -4 first reaches 10 twice.
# – -6, +3, +8, +5, -6 first reaches 5 twice.
# – +7, +7, -2, -7, -4 first reaches 14 twice.
#
# What is the first frequency your device reaches twice?
#
#
# --- Solution ---
#
# The difference here is that we iterate over the list of changes within
# an infinite loop (the itertools.cycle() would work well, but no imports...).
# In each step of the loop, we calculate new frequency by adding the next
# change to the current value. Then we check if that frequency was already
# reached – if so, we break the loop; otherwise we add the current frequency
# to the set of previously reached ones and we prepare for checking the next
# change. As an answer we return the frequency we reached for the second time.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        changes = [int(change)
                   for change in file.read().strip().split('\n')]

    i = 0
    frequency = 0
    frequencies = set([frequency])

    while True:
        frequency += changes[i]

        if frequency in frequencies:
            break
        else:
            frequencies.add(frequency)
            i = (i + 1) % len(changes)

    print(frequency)


if __name__ == '__main__':
    main()
