#!/usr/bin/env python3
#
# --- Day 1: Sonar Sweep / Part Two ---
#
# Considering every single measurement isn't as useful as you expected:
# there's just too much noise in the data.
#
# Instead, consider sums of a three-measurement sliding window.
# Again considering the above example:
#   199  A
#   200  A B
#   208  A B C
#   210    B C D
#   200  E   C D
#   207  E F   D
#   240  E F G
#   269    F G H
#   260      G H
#   263        H
#
# Start by comparing the first and second three-measurement windows.
# The measurements in the first window are marked A (199, 200, 208); their sum
# is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its
# sum is 618. The sum of measurements in the second window is larger than the
# sum of the first, so this first comparison increased.
#
# Your goal now is to count the number of times the sum of measurements in this
# sliding window increases from the previous sum. So, compare A with B, then
# compare B with C, then C with D, and so on. Stop when there aren't enough
# measurements left to create a new three-measurement sum.
#
# In the above example, the sum of each three-measurement window is as follows:
#   A: 607 (N/A - no previous sum)
#   B: 618 (increased)
#   C: 618 (no change)
#   D: 617 (decreased)
#   E: 647 (increased)
#   F: 716 (increased)
#   G: 769 (increased)
#   H: 792 (increased)
#
# In this example, there are 5 sums that are larger than the previous sum.
#
# Consider sums of a three-measurement sliding window. How many sums are larger
# than the previous sum?
#
#
# --- Solution ---
#
# The difference here is that we need to sum a few values for comparison,
# instead of taking just each array element. To achieve this, we introduce
# additional variable and implement a sliding window within the for loop.
# As first value for comparison, we take a sum of first few elements from
# the input list. Then just the first index (0) is omitted in the loop.
#

INPUT_FILE = 'input.txt'


def main():
    depths = [int(depth) for depth in open(INPUT_FILE, 'r')]

    previous = 0
    increases = 0
    window_size = 3

    previous = sum(depths[:window_size])

    for index in range(1, len(depths) - window_size + 1):
        current = sum(depths[index:index + window_size])
        if current > previous:
            increases += 1
        previous = current

    print(increases)


if __name__ == '__main__':
    main()
