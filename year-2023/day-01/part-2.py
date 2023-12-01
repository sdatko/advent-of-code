#!/usr/bin/env python3
#
# --- Day 1: Trebuchet?! / Part Two ---
#
# Your calculation isn't quite right. It looks like some of the digits are
# actually spelled out with letters: one, two, three, four, five, six, seven,
# eight, and nine also count as valid "digits".
#
# Equipped with this new information, you now need to find the real first
# and last digit on each line. For example:
#
#   two1nine
#   eightwothree
#   abcone2threexyz
#   xtwone3four
#   4nineeightseven2
#   zoneight234
#   7pqrstsixteen
#
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76.
# Adding these together produces 281.
#
# What is the sum of all of the calibration values?
#
#
# --- Solution ---
#
# The difference here is that we need to consider also the spelled digits.
# The obvious approach would be to find a first and last position of any digit,
# either written as a single character or a word, however a code I started
# to prepare was too long for day 01 IMO, hence I took alternative approach.
# I replaced the meaningful words in such a way that their beginning and ending
# could still be reused (because as it turned out, in real input, the string
# `zoneight234` corresponds to digits 18234 – the `e` is part of both 1 and 8).
# Then we continue like in part 1.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        lines = file.read().strip().split('\n')

    calibration_values = []

    for line in lines:
        line = line.replace('one', 'on1e')
        line = line.replace('two', 't2wo')
        line = line.replace('three', 'th3ree')
        line = line.replace('four', 'fo4ur')
        line = line.replace('five', 'fi5ve')
        line = line.replace('six', 'si6x')
        line = line.replace('seven', 'se7ven')
        line = line.replace('eight', 'ei8ght')
        line = line.replace('nine', 'ni9ne')
        digits = [character for character in line if character.isnumeric()]

        calibration_value = int(digits[0] + digits[-1])
        calibration_values.append(calibration_value)

    print(sum(calibration_values))


if __name__ == '__main__':
    main()
