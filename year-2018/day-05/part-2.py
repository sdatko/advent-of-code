#!/usr/bin/env python3
#
# --- Day 5: Alchemical Reduction / Part Two ---
#
# Time to improve the polymer.
#
# One of the unit types is causing problems; it's preventing the polymer
# from collapsing as much as it should. Your goal is to figure out which
# unit type is causing the most problems, remove all instances of it
# (regardless of polarity), fully react the remaining polymer,
# and measure its length.
#
# For example, again using the polymer dabAcCaCBAcCcaDA from above:
# – Removing all A/a units produces dbcCCBcCcD.
#   Fully reacting this polymer produces dbCBcD, which has length 6.
# – Removing all B/b units produces daAcCaCAcCcaDA.
#   Fully reacting this polymer produces daCAcaDA, which has length 8.
# – Removing all C/c units produces dabAaBAaDA.
#   Fully reacting this polymer produces daDA, which has length 4.
# – Removing all D/d units produces abAcCaCBAcCcaA.
#   Fully reacting this polymer produces abCBAc, which has length 6.
#
# In this example, removing all C/c units was best, producing the answer 4.
#
# What is the length of the shortest polymer you can produce by removing
# all units of exactly one type and fully reacting the result?
#
#
# --- Solution ---
#
# The difference here is that the algorithm needs to be run ~26 times,
# each time on slightly modifed input. So, an additional outer loop
# was added to identify removal of which unit leads to the best solution.
# The original algorithm, from previous part, was effective enough (~1 second),
# though I looked for some optimization ideas in the Internet.
# First, it turned out that the str class has str.swapcase() method,
# which made the additional reacts() function unnecessary.
# Second, it turned out that instead of removing middle part and concatenating
# long strings is not very effective – instead, a much faster algorithm was
# inolving the building of result by appending elements to a new list.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        polymer = file.read().strip()
        units = set(polymer.lower())

    original = polymer[:]
    shortest = len(original)

    for unit in units:
        polymer = original[:].replace(unit, '').replace(unit.upper(), '')
        buffer = []

        for unit in polymer:
            if buffer and unit == buffer[-1].swapcase():
                buffer.pop()
            else:
                buffer.append(unit)

        length = len(buffer)

        if length < shortest:
            shortest = length

    print(shortest)


if __name__ == '__main__':
    main()
