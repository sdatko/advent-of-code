#!/usr/bin/env python3
#
# --- Day 10: Adapter Array / Part Two ---
#
# To completely determine whether you have enough adapters, you'll need
# to figure out how many different ways they can be arranged. Every
# arrangement needs to connect the charging outlet to your device.
# The previous rules about when adapters can successfully connect still apply.
#
# The first example above (the one that starts with 16, 10, 15) supports
# the following arrangements:
#
#   (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
#   (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
#   (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
#   (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
#   (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
#   (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
#   (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
#   (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)
#
# (The charging outlet and your device's built-in adapter are shown
# in parentheses.) Given the adapters from the first example, the total
# number of arrangements that connect the charging outlet to your device is 8.
#
# The second example above (the one that starts with 28, 33, 18)
# has many arrangements. Here are a few:
#
#   (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#   32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)
#
#   (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#   32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 49, (52)
#
#   (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#   32, 33, 34, 35, 38, 39, 42, 45, 46, 48, 49, (52)
#
#   (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#   32, 33, 34, 35, 38, 39, 42, 45, 46, 49, (52)
#
#   (0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31,
#   32, 33, 34, 35, 38, 39, 42, 45, 47, 48, 49, (52)
#
#   (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#   46, 48, 49, (52)
#
#   (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#   46, 49, (52)
#
#   (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#   47, 48, 49, (52)
#
#   (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#   47, 49, (52)
#
#   (0), 3, 4, 7, 10, 11, 14, 17, 20, 23, 25, 28, 31, 34, 35, 38, 39, 42, 45,
#   48, 49, (52)
#
# In total, this set of adapters can connect the charging outlet
# to your device in 19208 distinct arrangements.
#
# You glance back down at your bag and try to remember why you brought so many
# adapters; there must be more than a trillion valid ways to arrange them!
# Surely, there must be an efficient way to count the arrangements.
#
# What is the total number of distinct ways you can arrange the adapters
# to connect the charging outlet to your device?
#
#
# --- Solution ---
#
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
