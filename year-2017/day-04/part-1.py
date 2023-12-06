#!/usr/bin/env python3
#
# --- Day 4: High-Entropy Passphrases ---
#
# A new system policy has been put in place that requires all accounts
# to use a passphrase instead of simply a password. A passphrase consists
# of a series of words (lowercase letters) separated by spaces.
#
# To ensure security, a valid passphrase must contain no duplicate words.
#
# For example:
# – aa bb cc dd ee is valid.
# – aa bb cc dd aa is not valid - the word aa appears more than once.
# – aa bb cc dd aaa is valid - aa and aaa count as different words.
#
# The system's full passphrase list is available as your puzzle input.
# How many passphrases are valid?
#
#
# --- Solution ---
#
# We start by reading the input file into a list of passphrases, each one
# begin a list of words. Then we need to iterate over passphrases and verify
# whether they include only unique words. The sets are great for this task,
# so all we need to do is to verify whether a set of words in passphrase has
# the same number of elements like the original passphrase; if the lengths
# do not match, then there was a duplicate and the passphrase is invalid.
# Finally, we return the number of valid passphrases.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        passphrases = [line.split()
                       for line in file.read().strip().split('\n')]

    valid = 0

    for passphrase in passphrases:
        if len(passphrase) == len(set(passphrase)):
            valid += 1

    print(valid)


if __name__ == '__main__':
    main()
