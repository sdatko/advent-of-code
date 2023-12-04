#!/usr/bin/env python3
#
# --- Day 5: Alchemical Reduction ---
#
# You've managed to sneak in to the prototype suit manufacturing lab.
# The Elves are making decent progress, but are still struggling with
# the suit's size reduction capabilities.
#
# While the very latest in 1518 alchemical technology might have solved
# their problem eventually, you can do better. You scan the chemical
# composition of the suit's material and discover that it is formed by
# extremely long polymers (one of which is available as your puzzle input).
#
# The polymer is formed by smaller units which, when triggered, react with
# each other such that two adjacent units of the same type and opposite
# polarity are destroyed. Units' types are represented by letters;
# units' polarity is represented by capitalization. For instance, r and R
# are units with the same type but opposite polarity, whereas r and s are
# entirely different types and do not react.
#
# For example:
# – In aA, a and A react, leaving nothing behind.
# – In abBA, bB destroys itself, leaving aA.
#   As above, this then destroys itself, leaving nothing.
# – In abAB, no two adjacent units are of the same type,
#   and so nothing happens.
# – In aabAAB, even though aa and AA are of the same type,
#   their polarities match, and so nothing happens.
#
# Now, consider a larger example, dabAcCaCBAcCcaDA:
#
#   dabAcCaCBAcCcaDA  The first 'cC' is removed.
#   dabAaCBAcCcaDA    This creates 'Aa', which is removed.
#   dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
#   dabCBAcaDA        No further actions can be taken.
#
# After all possible reactions, the resulting polymer contains 10 units.
#
# How many units remain after fully reacting the polymer you scanned?
# (Note: in this puzzle and others, the input is large; if you copy/paste
# your input, make sure you get the whole thing.)
#
#
# --- Solution ---
#
# We start by reading the input file into a string. Then we move through
# the polymer from start to its end, unit by unit, every time checking
# if current unit reacts with the next unit – if so, then we remove the
# the both units, and move back by one position (because this one can now
# react with the next remaining unit). Finally, after reaching the end
# of polymer, we return the final length.
#

INPUT_FILE = 'input.txt'


def reacts(unit1, unit2):
    return ((unit1.islower() and unit1.upper() == unit2)
            or
            (unit1.isupper() and unit1.lower() == unit2))


def main():
    with open(INPUT_FILE, 'r') as file:
        polymer = file.read().strip()

    index = 0

    while index < len(polymer) - 1:
        if reacts(polymer[index], polymer[index + 1]):
            polymer = polymer[:index] + polymer[index + 2:]

            if index > 0:
                index -= 1

        else:
            index += 1

    print(len(polymer))


if __name__ == '__main__':
    main()
