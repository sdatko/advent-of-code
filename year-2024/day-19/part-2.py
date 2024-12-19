#!/usr/bin/env python3
#
# --- Day 19: Linen Layout / Part Two ---
#
# The staff don't really like some of the towel arrangements you came up with.
# To avoid an endless cycle of towel rearrangement, maybe you should just give
# them every possible option.
#
# Here are all of the different ways the above example's designs can be made:
# – brwrr can be made in two different ways: b, r, wr, r or br, wr, r.
# – bggr can only be made with b, g, g, and r.
#
# gbbr can be made 4 different ways:
# – g, b, b, r
# – g, b, br
# – gb, b, r
# – gb, br
#
# rrbgbr can be made 6 different ways:
# – r, r, b, g, b, r
# – r, r, b, g, br
# – r, r, b, gb, r
# – r, rb, g, b, r
# – r, rb, g, br
# – r, rb, gb, r
#
# bwurrg can only be made with bwu, r, r, and g.
#
# brgr can be made in two different ways: b, r, g, r or br, g, r.
#
# ubwu and bbrgwb are still impossible.
#
# Adding up all of the ways the towels in this example could be arranged into
# the desired designs yields 16 (2 + 1 + 4 + 6 + 1 + 2).
#
# They'll let you into the onsen as soon as you have the list. What do you get
# if you add up the number of different ways you could make each design?
#
#
# --- Solution ---
#
# The difference here is that we need to count all possible representations,
# not just checking if the towel design can be represented – so returning
# an integer instead of a boolean value. Hence, in the helper function all
# the True/False values are replaced with 1 and 0, also the any() call is
# replaced with the sum() function. However, the most important observation
# is that we need to modify the default condition – we need to always split
# the towel design according to all available patterns; this is significant,
# as even though the towel definition may explicitly appear in the patterns,
# it still may be represented using two or more smaller patterns (e.g. design
# `ababab` can be expressed as patter `abab` or two times pattern `ab`).
# Finally, as an answer we return the sum of all possible representations
# of the given towels designs we can create using the given patterns.
#

INPUT_FILE = 'input.txt'

CACHE = {}


def check(towel, patterns):
    if towel in CACHE:
        return CACHE[towel]

    elif towel == '':
        CACHE[towel] = 1
        return CACHE[towel]

    else:
        CACHE[towel] = sum(
            check(towel[len(pattern):], patterns)
            if towel.startswith(pattern)
            else 0
            for pattern in patterns
        )
        return CACHE[towel]


def main():
    with open(INPUT_FILE, 'r') as file:
        patterns, towels = file.read().strip().split('\n\n')

    patterns = patterns.split(', ')
    towels = towels.split()

    possible = 0

    for towel in towels:
        possible += check(towel, patterns)

    print(possible)


if __name__ == '__main__':
    main()
