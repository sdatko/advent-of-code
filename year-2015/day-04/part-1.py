#!/usr/bin/env python3
#
# --- Day 4: The Ideal Stocking Stuffer ---
#
# Santa needs help mining some AdventCoins (very similar to bitcoins)
# to use as gifts for all the economically forward-thinking little
# girls and boys.

# To do this, he needs to find MD5 hashes which, in hexadecimal, start
# with at least five zeroes. The input to the MD5 hash is some secret key
# (your puzzle input, given below) followed by a number in decimal.
# To mine AdventCoins, you must find Santa the lowest positive number
# (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
#
# For example:
# – If your secret key is abcdef, the answer is 609043, because the MD5 hash
#   of abcdef609043 starts with five zeroes (000001dbbfa...), and it is
#   the lowest such number to do so.
# – If your secret key is pqrstuv, the lowest number it combines with to make
#   an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash
#   of pqrstuv1048970 looks like 000006136ef....
#
#
# --- Solution ---
#
# We start by reading the secret key from the input file. Then in an infinite
# loop we attempt to find the number that appended s string to the secret key
# would produce a MD5 hash that starts with string 00000. Once such hash was
# encountered, we return the number for which it occurred.
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

        if md5sum.startswith('00000'):
            break

        iteration += 1

    print(iteration)


if __name__ == '__main__':
    main()
