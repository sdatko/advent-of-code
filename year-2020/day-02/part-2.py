#!/usr/bin/env python3
#
# --- Day 2: Password Philosophy / Part Two ---
#
# While it appears you validated the passwords correctly, they don't
# seem to be what the Official Toboggan Corporate Authentication System
# is expecting.
#
# The shopkeeper suddenly realizes that he just accidentally explained
# the password policy rules from his old job at the sled rental place
# down the street! The Official Toboggan Corporate Policy actually works
# a little differently.
#
# Each policy actually describes two positions in the password, where 1 means
# the first character, 2 means the second character, and so on. (Be careful;
# Toboggan Corporate Policies have no concept of "index zero"!) Exactly one
# of these positions must contain the given letter. Other occurrences
# of the letter are irrelevant for the purposes of policy enforcement.
#
# Given the same example list from above:
#
#   1-3 a: abcde is valid: position 1 contains a and position 3 does not.
#   1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
#   2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
#
# How many passwords are valid according to the new interpretation
# of the policies?
#
#
# --- Solution ---
#
# We are processing each line that can be split into two elements:
# the policy and the password itself. The policy can be split into
# the wanted positions and the wanted letter. Then we simply check
# that the wanted letter only appears at one of the positions.
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

        index1 = int(occurrences.split('-')[0]) - 1
        index2 = int(occurrences.split('-')[1]) - 1

        if (password[index1] == letter) ^ (password[index2] == letter):
            good_entries += 1

    print(good_entries)


if __name__ == '__main__':
    main()
