#!/usr/bin/env python3
#
# --- Day 2: Inventory Management System / Part Two ---
#
# Confident that your list of box IDs is complete, you're ready to find
# the boxes full of prototype fabric.
#
# The boxes will have IDs which differ by exactly one character at the same
# position in both strings. For example, given the following box IDs:
#
#   abcde
#   fghij
#   klmno
#   pqrst
#   fguij
#   axcye
#   wvxyz
#
# The IDs abcde and axcye are close, but they differ by two characters
# (the second and fourth). However, the IDs fghij and fguij differ by
# exactly one character, the third (h and u). Those must be the correct boxes.
#
# What letters are common between the two correct box IDs? (In the example
# above, this is found by removing the differing character from either ID,
# producing fgij.)
#
#
# --- Solution ---
#
# The difference here is that we need to find a pair of strings with Hamming
# distance equal to 1 – i.e. that they differ on exactly a single position.
# For this, we check every unique combination of strings and find differences
# on characters at each position. If the number of differences is equal to 1,
# we found our answer – we print everything except the single position where
# the difference is.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        IDs = file.read().strip().split('\n')

    for index, ID1 in enumerate(IDs[:-1]):
        for ID2 in IDs[index + 1:]:
            differences = []

            for position in range(len(ID1)):
                if ID1[position] != ID2[position]:
                    differences.append(position)

            if len(differences) == 1:
                position = differences[0]
                answer = ID1[:position] + ID1[position + 1:]

    print(answer)


if __name__ == '__main__':
    main()
