#!/usr/bin/env python3
#
# --- Day 20: Grove Positioning System ---
#
# It's finally time to meet back up with the Elves. When you try to contact
# them, however, you get no reply. Perhaps you're out of range?
#
# You know they're headed to the grove where the star fruit grows, so if you
# can figure out where that is, you should be able to meet back up with them.
#
# Fortunately, your handheld device has a file (your puzzle input) that
# contains the grove's coordinates! Unfortunately, the file is encrypted
# - just in case the device were to fall into the wrong hands.
#
# Maybe you can decrypt it?
#
# When you were still back at the camp, you overheard some Elves talking
# about coordinate file encryption. The main operation involved in decrypting
# the file is called mixing.
#
# The encrypted file is a list of numbers. To mix the file, move each number
# forward or backward in the file a number of positions equal to the value
# of the number being moved. The list is circular, so moving a number off
# one end of the list wraps back around to the other end as if the ends
# were connected.
#
# For example, to move the 1 in a sequence like 4, 5, 6, 1, 7, 8, 9,
# the 1 moves one position forward: 4, 5, 6, 7, 1, 8, 9. To move the -2
# in a sequence like 4, -2, 5, 6, 7, 8, 9, the -2 moves two positions
# backward, wrapping around: 4, 5, 6, 7, 8, -2, 9.
#
# The numbers should be moved in the order they originally appear
# in the encrypted file. Numbers moving around during the mixing
# process do not change the order in which the numbers are moved.
#
# Consider this encrypted file:
#
#   1
#   2
#   -3
#   3
#   -2
#   0
#   4
#
# Mixing this file proceeds as follows:
#
#   Initial arrangement:
#   1, 2, -3, 3, -2, 0, 4
#
#   1 moves between 2 and -3:
#   2, 1, -3, 3, -2, 0, 4
#
#   2 moves between -3 and 3:
#   1, -3, 2, 3, -2, 0, 4
#
#   -3 moves between -2 and 0:
#   1, 2, 3, -2, -3, 0, 4
#
#   3 moves between 0 and 4:
#   1, 2, -2, -3, 0, 3, 4
#
#   -2 moves between 4 and 1:
#   1, 2, -3, 0, 3, 4, -2
#
#   0 does not move:
#   1, 2, -3, 0, 3, 4, -2
#
#   4 moves between -3 and 0:
#   1, 2, -3, 4, 0, 3, -2
#
# Then, the grove coordinates can be found by looking at the 1000th, 2000th,
# and 3000th numbers after the value 0, wrapping around the list as necessary.
# In the above example, the 1000th number after 0 is 4, the 2000th is -3,
# and the 3000th is 2; adding these together produces 3.
#
# Mix your encrypted file exactly once. What is the sum of the three numbers
# that form the grove coordinates?
#
#
# --- Solution ---
#
# We start by reading the input as a list of numbers, just by splitting
# the file by any white space character. Additionally we store the original
# index of every number, to make them distinguishable (items are non-unique).
# Then we iterate over a copy of given list (to preserve the processing order):
# for every number (actually, a pair or original index and its value), we find
# its current index in the array, then we add to that index the numeric value
# of a number and finally we move the number by popping it from current index
# and inserting it under new index.
# It is important to notice that when calculating a new index in a circular
# list, we need to take the modulo of `N - 1`, not `N` – because after popping
# the element, there are less elements and the `N - 1`-th index corresponds
# in a circular list to the same position as index `0` (see illustration below)
#
#   elements: [ 1, 2, 3, 4, 5 ]
#   indices:   0  1  2  3  4  5
#
#   circular list: ... 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
#                  ----------------------------------------------------
#   insertion index:  0  1  2  3  4  5              0  1  2  3  4  5
#                                    0  1  2  3  4  5
#
# For the answer, we find the index of element with value 0 and we sum
# the value of elements of that index +1000, +2000 and +3000 (modulo N).
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        numbers = [(index, int(number))
                   for index, number in enumerate(file.read().strip().split())]
        N = len(numbers)

    for number in numbers.copy():
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
