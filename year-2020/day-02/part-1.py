#!/usr/bin/env python3
#
# --- Day 2: Password Philosophy ---
#
# Your flight departs in a few days from the coastal airport;
# the easiest way down to the coast from here is via toboggan.
#
# The shopkeeper at the North Pole Toboggan Rental Shop is having
# a bad day. "Something's wrong with our computers; we can't log in!"
# You ask if you can take a look.
#
# Their password database seems to be a little corrupted:
# some of the passwords wouldn't have been allowed by the Official
# Toboggan Corporate Policy that was in effect when they were chosen.
#
# To try to debug the problem, they have created a list (your puzzle input)
# of passwords (according to the corrupted database) and the corporate
# policy when that password was set.
#
# For example, suppose you have the following list:
#
#   1-3 a: abcde
#   1-3 b: cdefg
#   2-9 c: ccccccccc
#
# Each line gives the password policy and then the password. The password
# policy indicates the lowest and highest number of times a given letter
# must appear for the password to be valid. For example, `1-3 a` means that
# the password must contain a at least 1 time and at most 3 times.
#
# In the above example, 2 passwords are valid. The middle password, cdefg,
# is not; it contains no instances of b, but needs at least 1. The first
# and third passwords are valid: they contain one a or nine c, both within
# the limits of their respective policies.
#
# How many passwords are valid according to their policies?
#
#
# --- Solution ---
#
# We are processing each line that can be split into two elements:
# the policy and the password itself. The policy can be split into
# the wanted occurrences and the wanted letter. Then we simply check
# that the count of wanted letter in password matches the minimum
# and maximum occurrences.
#

INPUT_FILE = 'input.txt'


def main():
    entries = [line.strip('\n') for line in open(INPUT_FILE, 'r')]

    good_entries = 0

    for entry in entries:
        policy = entry.split(':')[0]
        password = entry.split(':')[1][1:]

        occurrences = policy.split(' ')[0]
        letter = policy.split(' ')[1]

        min_occurrences = int(occurrences.split('-')[0])
        max_occurrences = int(occurrences.split('-')[1])

        if min_occurrences <= password.count(letter) <= max_occurrences:
            good_entries += 1

    print(good_entries)


if __name__ == '__main__':
    main()
