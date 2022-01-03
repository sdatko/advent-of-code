#!/usr/bin/env python3
#
# --- Day 3: Binary Diagnostic ---
#
# The submarine has been making some odd creaking noises, so you ask it
# to produce a diagnostic report just in case.
#
# The diagnostic report (your puzzle input) consists of a list of binary
# numbers which, when decoded properly, can tell you many useful things
# about the conditions of the submarine. The first parameter to check
# is the power consumption.
#
# You need to use the binary numbers in the diagnostic report to generate
# two new binary numbers (called the gamma rate and the epsilon rate).
# The power consumption can then be found by multiplying the gamma rate
# by the epsilon rate.
#
# Each bit in the gamma rate can be determined by finding the most common
# bit in the corresponding position of all numbers in the diagnostic report.
# For example, given the following diagnostic report:
#   00100
#   11110
#   10110
#   10111
#   10101
#   01111
#   00111
#   11100
#   10000
#   11001
#   00010
#   01010
#
# Considering only the first bit of each number, there are five 0 bits and
# seven 1 bits. Since the most common bit is 1, the first bit of the gamma
# rate is 1.
#
# The most common second bit of the numbers in the diagnostic report is 0,
# so the second bit of the gamma rate is 0.
#
# The most common value of the third, fourth, and fifth bits are 1, 1, and 0,
# respectively, and so the final three bits of the gamma rate are 110.
#
# So, the gamma rate is the binary number 10110, or 22 in decimal.
#
# The epsilon rate is calculated in a similar way; rather than use the most
# common bit, the least common bit from each position is used.
# So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate
# (22) by the epsilon rate (9) produces the power consumption, 198.
#
# Use the binary numbers in your diagnostic report to calculate the gamma rate
# and epsilon rate, then multiply them together. What is the power consumption
# of the submarine? (Be sure to represent your answer in decimal, not binary.)
#
#
# --- Solution ---
#
# First, we produce the list of numbers by reading the input file.
# For convenience to access each position we leave the numbers as strings.
# Then we prepare helper variables, one of which is a list of dictionaries
# that will be used to count occurrences of 0's and 1's at each position
# in the input numbers.
# Next we takie each number from the input list and iterate over its elements
# (bits), incrementing the value for corresponding bit and position (index)
# in the list of occurrences.
# Finally, we produce bit representation (as string) of gamma and epsilon
# rates by looking into the produced list of occurrences and taking into
# account whether at given position there were more 0's or 1's.
# Having that, we just need to convert bit strings into integers (base=2),
# multiply the obtained values and print the result.
#

INPUT_FILE = 'input.txt'


def main():
    numbers_str = [line.strip() for line in open(INPUT_FILE, 'r')]

    gamma_rate_str = ''
    epsilon_rate_str = ''

    example_number = numbers_str[0]
    occurrences = [{'0': 0, '1': 0} for _ in range(len(example_number))]

    for number_str in numbers_str:
        for index, bit in enumerate(number_str):
            occurrences[index][bit] += 1

    for index, bits in enumerate(occurrences):
        if bits['0'] > bits['1']:
            gamma_rate_str += '0'
            epsilon_rate_str += '1'
        else:
            gamma_rate_str += '1'
            epsilon_rate_str += '0'

    gamma_rate = int(gamma_rate_str, base=2)
    epsilon_rate = int(epsilon_rate_str, base=2)

    power_consumption = gamma_rate * epsilon_rate

    print(power_consumption)


if __name__ == '__main__':
    main()
