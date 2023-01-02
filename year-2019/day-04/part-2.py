#!/usr/bin/env python3
#
# --- Day 4: Secure Container / Part Two ---
#
# An Elf just remembered one more important detail: the two adjacent
# matching digits are not part of a larger group of matching digits.
#
# Given this additional criterion, but still ignoring the range rule,
# the following are now true:
# – 112233 meets these criteria because the digits never decrease
#   and all repeated digits are exactly two digits long.
# – 123444 no longer meets the criteria (the repeated 44 is part
#   of a larger group of 444).
# – 111122 meets the criteria (even though 1 is repeated more than twice,
#   it still contains a double 22).
#
# How many different passwords within the range given in your puzzle input
# meet all of the criteria?
#
#
# --- Solution ---
#
# The difference here is that there is one more condition to consider.
# Long story short, there *must* by at least one pair of same digits.
# For this, we check whether in the list of digits there are any digits that
# appears exactly two times. The rest of the code remains the same.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        a, b = tuple(map(int, file.read().strip().split('-')))

    matching = 0

    for password in range(a, b + 1):
        digits = tuple(map(int, list(str(password))))

        # any adjacent digits must be the same
        if not any([digits[0] == digits[1],
                    digits[1] == digits[2],
                    digits[2] == digits[3],
                    digits[3] == digits[4],
                    digits[4] == digits[5]]):
            continue

        # the digits never decrease
        if not (digits[0] <= digits[1] <= digits[2]
                <= digits[3] <= digits[4] <= digits[5]):
            continue

        # adjacent matching digits are not part of a larger group
        if not any(digits.count(i) == 2 for i in range(10)):
            continue

        matching += 1

    print(matching)


if __name__ == '__main__':
    main()
