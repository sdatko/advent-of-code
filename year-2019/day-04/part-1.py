#!/usr/bin/env python3
#
# --- Day 4: Secure Container ---
#
# You arrive at the Venus fuel depot only to discover it's protected
# by a password. The Elves had written the password on a sticky note,
# but someone threw it out.
#
# However, they do remember a few key facts about the password:
# – It is a six-digit number.
# – The value is within the range given in your puzzle input.
# – Two adjacent digits are the same (like 22 in 122345).
# – Going from left to right, the digits never decrease;
#   they only ever increase or stay the same (like 111123 or 135679).
#
# Other than the range rule, the following are true:
# – 111111 meets these criteria (double 11, never decreases).
# – 223450 does not meet these criteria (decreasing pair of digits 50).
# – 123789 does not meet these criteria (no double).
#
# How many different passwords within the range given in your puzzle input
# meet these criteria?
#
#
# --- Solution ---
#
# We start by reading the input into two numbers – the lower and the upper
# bound of digits range – by splitting the file over a dash/minus character
# and mapping the result into the integers. Then for each password in a range
# we check the two given conditions that must be satisfied: there is any pair
# of the same digits and every next digit must be greater or equal to previous.
# Finally we return the number of matching passwords.
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

        matching += 1

    print(matching)


if __name__ == '__main__':
    main()
