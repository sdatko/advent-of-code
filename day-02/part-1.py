#!/usr/bin/env python3
#
# Task:
# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number
# of times a given letter must appear for the password to be valid.
# How many passwords are valid according to their policies?
#
# Solution:
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
