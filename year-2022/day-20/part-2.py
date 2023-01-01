#!/usr/bin/env python3
#
# --- Day 20: Grove Positioning System / Part Two ---
#
# The grove coordinate values seem nonsensical. While you ponder the mysteries
# of Elf encryption, you suddenly remember the rest of the decryption routine
# you overheard back at camp.
#
# First, you need to apply the decryption key, 811589153. Multiply each number
# by the decryption key before you begin; this will produce the actual list
# of numbers to mix.
#
# Second, you need to mix the list of numbers ten times. The order in which
# the numbers are mixed does not change during mixing; the numbers are still
# moved in the order they appeared in the original, pre-mixed list. (So, if -3
# appears fourth in the original list of numbers to mix, -3 will be the fourth
# number to move during each round of mixing.)
#
# Using the same example as above:
#
#   Initial arrangement:
#   811589153, 1623178306, -2434767459, 2434767459, -1623178306, 0, 3246356612
#
#   After 1 round of mixing:
#   0, -2434767459, 3246356612, -1623178306, 2434767459, 1623178306, 811589153
#
#   After 2 rounds of mixing:
#   0, 2434767459, 1623178306, 3246356612, -2434767459, -1623178306, 811589153
#
#   After 3 rounds of mixing:
#   0, 811589153, 2434767459, 3246356612, 1623178306, -1623178306, -2434767459
#
#   After 4 rounds of mixing:
#   0, 1623178306, -2434767459, 811589153, 2434767459, 3246356612, -1623178306
#
#   After 5 rounds of mixing:
#   0, 811589153, -1623178306, 1623178306, -2434767459, 3246356612, 2434767459
#
#   After 6 rounds of mixing:
#   0, 811589153, -1623178306, 3246356612, -2434767459, 1623178306, 2434767459
#
#   After 7 rounds of mixing:
#   0, -2434767459, 2434767459, 1623178306, -1623178306, 811589153, 3246356612
#
#   After 8 rounds of mixing:
#   0, 1623178306, 3246356612, 811589153, -2434767459, 2434767459, -1623178306
#
#   After 9 rounds of mixing:
#   0, 811589153, 1623178306, -2434767459, 3246356612, 2434767459, -1623178306
#
#   After 10 rounds of mixing:
#   0, -2434767459, 1623178306, 3246356612, -1623178306, 2434767459, 811589153
#
# The grove coordinates can still be found in the same way. Here, the 1000th
# number after 0 is 811589153, the 2000th is 2434767459, and the 3000th
# is -1623178306; adding these together produces 1623178306.
#
# Apply the decryption key and mix your encrypted file ten times.
# What is the sum of the three numbers that form the grove coordinates?
#
#
# --- Solution ---
#
# The differences here are is that:
# – we multiply each value read from file by a given key,
# – we repeat the mixing procedure a given number of times.
# So we simply modify the input processing part and we introduce additional
# loop around the main algorithm. The rest of the code is exactly the same
# as it was before.
#

INPUT_FILE = 'input.txt'

KEY = 811589153
TIMES = 10


def main():
    with open(INPUT_FILE, 'r') as file:
        numbers = [(index, int(number) * KEY)
                   for index, number in enumerate(file.read().strip().split())]
        N = len(numbers)

    original_numbers = numbers.copy()

    for _ in range(TIMES):
        for number in original_numbers:
            original_index, value = number
            current_index = numbers.index(number)

            new_index = (current_index + value) % (N - 1)

            numbers.pop(current_index)
            numbers.insert(new_index, number)

    values = [value for _, value in numbers]

    answer = sum([
        values[(values.index(0) + 1000) % N],
        values[(values.index(0) + 2000) % N],
        values[(values.index(0) + 3000) % N],
    ])

    print(answer)


if __name__ == '__main__':
    main()
