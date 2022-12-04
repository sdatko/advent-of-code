#!/usr/bin/env python3
#
# --- Day 4: Camp Cleanup / Part Two ---
#
# It seems like there is still quite a bit of duplicate work planned. Instead,
# the Elves would like to know the number of pairs that overlap at all.
#
# In the above example, the first two pairs (2-4,6-8 and 2-3,4-5)
# don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7,
# 6-6,4-6, and 2-6,4-8) do overlap:
#
#   5-7,7-9 overlaps in a single section, 7.
#   2-8,3-7 overlaps all of the sections 3 through 7.
#   6-6,4-6 overlaps in a single section, 6.
#   2-6,4-8 overlaps in sections 4, 5, and 6.
#
# So, in this example, the number of overlapping assignment pairs is 4.
#
# In how many assignment pairs do the ranges overlap?
#
#
# --- Solution ---
#
# In this part, the only difference is the condition on which we do counting:
# here were are interested in any overlapping (even partial), hence there are
# 4 possible cases: x1 lies between y1 and y2, x2 lies between y1 and y2,
# y1 lies between x1 and x2 or y2 lies between x1 and x2.
# Small note is that originally I attempted to solve it using sets of numbers
# and checking for any intersection, but this solution would not scale well
# when the number ranges would be bigger.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        pairs = [tuple(map(int, pairs.replace('-', ',').split(',')))
                 for pairs in file.read().split()]

    count = 0

    for x1, x2, y1, y2 in pairs:
        if any([x1 <= y1 <= x2,
                x1 <= y2 <= x2,
                y1 <= x1 <= y2,
                y1 <= x2 <= y2]):
            count += 1

    print(count)


if __name__ == '__main__':
    main()
