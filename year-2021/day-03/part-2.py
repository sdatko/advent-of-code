#!/usr/bin/env python3
#
# Task:
# Next, you should verify the life support rating, which can be determined
# by multiplying the oxygen generator rating by the CO2 scrubber rating.
# Both the oxygen generator rating and the CO2 scrubber rating are values
# that can be found in your diagnostic report - finding them is the tricky
# part. Both values are located using a similar process that involves filtering
# out values until only one remains. Before searching for either rating value,
# start with the full list of binary numbers from your diagnostic report and
# consider just the first bit of those numbers. Then:
# - Keep only numbers selected by the bit criteria for the type of rating
#   value for which you are searching. Discard numbers which do not match
#   the bit criteria.
# - If you only have one number left, stop; this is the rating value for
#   which you are searching.
# - Otherwise, repeat the process, considering the next bit to the right.
# The bit criteria depends on which type of rating value you want to find:
# - To find oxygen generator rating, determine the most common value (0 or 1)
#   in the current bit position, and keep only numbers with that bit in
#   that position. If 0 and 1 are equally common, keep values with a 1 in
#   the position being considered.
# - To find CO2 scrubber rating, determine the least common value (0 or 1)
#   in the current bit position, and keep only numbers with that bit in
#   that position. If 0 and 1 are equally common, keep values with a 0 in
#   the position being considered.
# Use the binary numbers in your diagnostic report to calculate the oxygen
# generator rating and CO2 scrubber rating, then multiply them together.
# What is the life support rating of the submarine? (Be sure to represent
# your answer in decimal, not binary.)
#
# Solution:
# Here the approach is a bit different. We start with a copy of original
# list of numbers, as we will filter its elements in the process.
# Then we perform a loop on input numbers positions (we assume here each
# number has the same number of bits). For each position:
# - we calculate the number of 0's and 1's in the remaining subset of numbers,
# - we produce new subset by selecting only elements with wanted bit value
#   at current position,
# - we check if we have a single result right now by chance (stop condition).
# The same procedure is conducted for both targets we are calculating (oxygen
# and CO2), the only difference is what wanted values are used for filtering.
# The final step is to take the single remaining elements from each subset,
# convert them to decimal values and multiply.
#

INPUT_FILE = 'input.txt'


def main():
    numbers_str = [line.strip() for line in open(INPUT_FILE, 'r')]

    example_number = numbers_str[0]

    subset_of_numbers = numbers_str[:]
    for index in range(len(example_number)):
        occurrences_of_0 = 0
        occurrences_of_1 = 0

        for number in subset_of_numbers:
            if number[index] == '0':
                occurrences_of_0 += 1
            else:
                occurrences_of_1 += 1

        if occurrences_of_0 > occurrences_of_1:
            wanted_value = '0'
        else:
            wanted_value = '1'

        subset_of_numbers = [number for number in subset_of_numbers
                             if number[index] == wanted_value]

        if len(subset_of_numbers) == 1:
            break

    assert len(subset_of_numbers) == 1
    oxygen_generator_rating = int(subset_of_numbers[0], base=2)

    subset_of_numbers = numbers_str[:]
    for index in range(len(example_number)):
        occurrences_of_0 = 0
        occurrences_of_1 = 0

        for number in subset_of_numbers:
            if number[index] == '0':
                occurrences_of_0 += 1
            else:
                occurrences_of_1 += 1

        if occurrences_of_0 > occurrences_of_1:
            wanted_value = '1'
        else:
            wanted_value = '0'

        subset_of_numbers = [number for number in subset_of_numbers
                             if number[index] == wanted_value]

        if len(subset_of_numbers) == 1:
            break

    assert len(subset_of_numbers) == 1
    CO2_scrubber_rating = int(subset_of_numbers[0], base=2)

    life_support_rating = oxygen_generator_rating * CO2_scrubber_rating

    print(life_support_rating)


if __name__ == '__main__':
    main()
