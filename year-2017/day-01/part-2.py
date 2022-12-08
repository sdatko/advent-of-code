#!/usr/bin/env python3
#
# --- Day 1: Inverse Captcha / Part Two ---
#
# You notice a progress bar that jumps to 50% completion. Apparently,
# the door isn't yet satisfied, but it did emit a star as encouragement.
# The instructions change:
#
# Now, instead of considering the next digit, it wants you to consider
# the digit halfway around the circular list. That is, if your list contains
# 10 items, only include a digit in your sum if the digit 10/2 = 5 steps
# forward matches it. Fortunately, your list has an even number of elements.
#
# For example:
# – 1212 produces 6: the list contains 4 items,
#   and all four digits match the digit 2 items ahead.
# – 1221 produces 0, because every comparison is between a 1 and a 2.
# – 123425 produces 4, because both 2s match each other,
#   but no other digit has a match.
# – 123123 produces 12.
# – 12131415 produces 4.
#
# What is the solution to your new captcha?
#
#
# --- Solution ---
#
# The difference here is how we select the second digit for later comparison.
# This time it is not the next element, but the element that comes after N / 2,
# assuming N is the total number of digits to examine.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        numbers = [int(number)
                   for number in list(file.read().strip())]

    sum_of_duplicates = 0

    for i in range(len(numbers)):
        digit1 = numbers[i]
        digit2 = numbers[(i + len(numbers) // 2) % len(numbers)]

        if digit1 == digit2:
            sum_of_duplicates += digit1

    print(sum_of_duplicates)


if __name__ == '__main__':
    main()
