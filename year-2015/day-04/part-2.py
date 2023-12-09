#!/usr/bin/env python3
#
# --- Day 4: The Ideal Stocking Stuffer / Part Two ---
#
# Now find one that starts with six zeroes.
#
#
# --- Solution ---
#
# The difference here is that we need to find a hash that starts with 000000.
# Except for the condition, the rest of the code remains the same.
#

import hashlib

INPUT_FILE = 'input.txt'


def MD5(string):
    return hashlib.md5(string.encode()).hexdigest()


def main():
    with open(INPUT_FILE, 'r') as file:
        key = file.read().strip()

    iteration = 0

    while True:
        md5sum = MD5(key + str(iteration))

        if md5sum.startswith('000000'):
            break

        iteration += 1

    print(iteration)


if __name__ == '__main__':
    main()
