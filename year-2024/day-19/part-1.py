#!/usr/bin/env python3
#
# --- Day 19: Linen Layout ---
#
# Today, The Historians take you up to the hot springs on Gear Island!
# Very suspiciously, absolutely nothing goes wrong as they begin their
# careful search of the vast field of helixes.
#
# Could this finally be your chance to visit the onsen next door?
# Only one way to find out.
#
# After a brief conversation with the reception staff at the onsen front desk,
# you discover that you don't have the right kind of money to pay the admission
# fee. However, before you can leave, the staff get your attention. Apparently,
# they've heard about how you helped at the hot springs, and they're willing
# to make a deal: if you can simply help them arrange their towels, they'll
# let you in for free!
#
# Every towel at this onsen is marked with a pattern of colored stripes.
# There are only a few patterns, but for any particular pattern, the staff
# can get you as many towels with that pattern as you need. Each stripe can be
# white (w), blue (u), black (b), red (r), or green (g). So, a towel with
# the pattern ggr would have a green stripe, a green stripe, and then a red
# stripe, in that order. (You can't reverse a pattern by flipping a towel
# upside-down, as that would cause the onsen logo to face the wrong way.)
#
# The Official Onsen Branding Expert has produced a list of designs
# - each a long sequence of stripe colors - that they would like to be able
# to display. You can use any towels you want, but all of the towels' stripes
# must exactly match the desired design. So, to display the design rgrgr,
# you could use two rg towels and then an r towel, an rgr towel and then
# a gr towel, or even a single massive rgrgr towel (assuming such towel
# patterns were actually available).
#
# To start, collect together all of the available towel patterns and the list
# of desired designs (your puzzle input). For example:
#
#   r, wr, b, g, bwu, rb, gb, br
#
#   brwrr
#   bggr
#   gbbr
#   rrbgbr
#   ubwu
#   bwurrg
#   brgr
#   bbrgwb
#
# The first line indicates the available towel patterns; in this example,
# the onsen has unlimited towels with a single red stripe (r), unlimited
# towels with a white stripe and then a red stripe (wr), and so on.
#
# After the blank line, the remaining lines each describe a design the onsen
# would like to be able to display. In this example, the first design (brwrr)
# indicates that the onsen would like to be able to display a black stripe,
# a red stripe, a white stripe, and then two red stripes, in that order.
#
# Not all designs will be possible with the available towels. In the above
# example, the designs are possible or impossible as follows:
# – brwrr can be made with a br towel, then a wr towel,
#   and then finally an r towel.
# – bggr can be made with a b towel, two g towels, and then an r towel.
# – gbbr can be made with a gb towel and then a br towel.
# – rrbgbr can be made with r, rb, g, and br.
# – ubwu is impossible.
# – bwurrg can be made with bwu, r, r, and g.
# – brgr can be made with br, g, and r.
# – bbrgwb is impossible.
#
# In this example, 6 of the eight designs are possible with the available
# towel patterns.
#
# To get into the onsen as soon as possible, consult your list of towel
# patterns and desired designs carefully. How many designs are possible?
#
#
# --- Solution ---
#
# We start by reading the input file into two definitions – a list of patterns
# and a list of towels designs, by splitting the data first over two newlines,
# then by comma and space or single newlines respectively. Then, we process
# all the given towels in a loop, verifying using a helper function whether
# each towel design can be represented using available patterns. The function
# takes the towel design (string) and the list of patterns as the arguments.
# If the current towel design is already one of the available patterns, then
# this function simply returns True – the towel design can be expressed with
# one of the patterns. Otherwise we need to check whether any of the patterns
# is a first part of the towel definition – in such cases, we strip that first
# part from he towel design and repeat the verification for the remaining part
# by calling the helper function recursively. Finally, as an answer, we return
# the number of original towel designs that are possible to represent with
# available patterns. Such algorithm works well for the given example data,
# however it is not efficient enough for the actual puzzle input – there are
# too many possibilities and the towel design patterns are too long. Hence,
# the memoization technique (cache) was necessary for the helper function
# to accelerate the verification for the multiple similar cases.
#
# Alternative interesting approach is to join all patterns into a single long
# regular expression, like (aaa*|bbb*|ccc*)*, then just using regex engine
# to verify matches for all given towels designs.
#

INPUT_FILE = 'input.txt'

CACHE = {}


def check(towel, patterns):
    if towel in CACHE:
        return CACHE[towel]

    elif towel in patterns:
        CACHE[towel] = True
        return CACHE[towel]

    else:
        CACHE[towel] = any(
            check(towel[len(pattern):], patterns)
            if towel.startswith(pattern)
            else False
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
        if check(towel, patterns):
            possible += 1

    print(possible)


if __name__ == '__main__':
    main()
