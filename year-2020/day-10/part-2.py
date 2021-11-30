#!/usr/bin/env python3
#
# Task:
# What is the total number of distinct ways you can arrange the adapters
# to connect the charging outlet to your device?
#
# Solution:
# After analyzing the data (differences), we noticed there are only values
# 1 and 3 – this simplifies the solution, but probably considering values
# 2 would also be simple. Basically, what we can do in our setup, according
# to the task, is that we can drop some combinations of devices where the
# differences are a series of ones.
#
# If there is 3 after the 1, we cannot drop this one either, as it would
# create a difference of 4. We can only alter the number of previous ones.
# We are not sure if there is a generic formula, but the possibilities
# for the first few cases would be as follows:
#
# 1   => 1 possibility
#
# 1 1
# . 1   => 2 possibilities
#
# 1 1 1   1
# . 1 1   2
# 1 . 1   3
# . . 1   4  => 4 possibilities
#
# 1 1 1 1   1
# . 1 1 1   2
# 1 . 1 1   3
# 1 1 . 1   4
# . . 1 1   5
# 1 . . 1   6
# . 1 . 1   7  => 7 possibilities
# , . . 1   8  -- invalid
#
# 1 1 1 1 1   1
# . 1 1 1 1   2
# 1 . 1 1 1   3
# 1 1 . 1 1   4
# 1 1 1 . 1   5
# . . 1 1 1   6
# 1 . . 1 1   7
# 1 1 . . 1   8
# 1 . 1 . 1   9
# . 1 . 1 1   10
# . 1 1 . 1   11
# . 1 . . 1   12
# . . 1 . 1   13  => 13 possibilities
# . . . 1 1   14  -- invalid
# 1 . . . 1   15  -- invalid
# . . . . 1   16  -- invalid
#
# The final answer would be a multiplication of all possibilities related
# to the present groups of differences of ones in our dataset.
#
# Self note: probably it would be something related to Newton's formula
#            ~ how many ways to remove 1 or 2 elements from the set of
#            N-1 elements, provided that there is no gap of 3 produced?
#            TODO(sdatko): check in free time
#

INPUT_FILE = 'input.txt'

SOCKET_VALUE = 3


def main():
    numbers = sorted(
        [int(number)
            for number in open(INPUT_FILE, 'r').read().strip().split('\n')]
    )
    numbers.insert(0, 0)  # the socket is first device
    numbers.append(max(numbers) + 3)  # our device is the last

    differences = [numbers[i + 1] - numbers[i]
                   for i in range(len(numbers) - 1)]

    previous = 0
    count = 0
    counts = []

    for difference in differences:
        if difference != previous:
            if previous == 1:
                counts.append(count)
            previous = difference
            count = 1
        else:
            count += 1

    possibilities = 1
    for count in counts:
        if count == 1:
            possibilities *= 1
        elif count == 2:
            possibilities *= 2
        elif count == 3:
            possibilities *= 4
        elif count == 4:
            possibilities *= 7
        elif count == 5:
            possibilities *= 8

    print(possibilities)


if __name__ == '__main__':
    main()
