#!/usr/bin/env python3
#
# Task:
# The final step in breaking the XMAS encryption relies on the invalid number
# you just found: you must find a contiguous set of at least two numbers in
# your list which sum to the invalid number from step 1.
# To find the encryption weakness, add together the smallest and largest
# number in this contiguous range.
# What is the encryption weakness in your XMAS-encrypted list of numbers?
#
# Solution:
# Here we just implement another sliding window on the input list of numbers,
# but with various width – from minimum size 2 to the end of array. Then we
# produce a subset of that window and calculate a sum of its elements.
# If it is equal to our wrong number, we have what we need.
# The additional break, if sum for current start and window size exceeds
# already our target number, reduces the processing time significantly.
#

INPUT_FILE = 'input.txt'

WINDOW_SIZE = 25


def main():
    numbers = [int(number)
               for number in open(INPUT_FILE, 'r').read().strip().split('\n')]

    wrong_number = 0

    index = 0
    while True:
        xmas_numbers = set(numbers[index:index + WINDOW_SIZE])
        new_number = numbers[index + WINDOW_SIZE]

        complementary = set([new_number - xmas_number
                             for xmas_number in xmas_numbers])

        results = list(set.intersection(xmas_numbers, complementary))

        if len(results) < 2:
            wrong_number = new_number
            break

        index += 1

    for start in range(0, len(numbers) - 2):
        for end in range(2, len(numbers) - start):
            subset = set(numbers[start:start + end])

            if sum(subset) > wrong_number:
                break

            if sum(subset) == wrong_number:
                print(min(subset) + max(subset))
                return


if __name__ == '__main__':
    main()
