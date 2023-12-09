#!/usr/bin/env python3
#
# --- Day 5: How About a Nice Game of Chess? ---
#
# You are faced with a security door designed by Easter Bunny engineers
# that seem to have acquired most of their security knowledge by watching
# hacking movies.
#
# The eight-character password for the door is generated one character
# at a time by finding the MD5 hash of some Door ID (your puzzle input)
# and an increasing integer index (starting with 0).
#
# A hash indicates the next character in the password if its hexadecimal
# representation starts with five zeroes. If it does, the sixth character
# in the hash is the next character of the password.
#
# For example, if the Door ID is abc:
# – The first index which produces a hash that starts with five zeroes
#   is 3231929, which we find by hashing abc3231929; the sixth character
#   of the hash, and thus the first character of the password, is 1.
# – 5017308 produces the next interesting hash, which starts with 000008f82...,
#   so the second character of the password is 8.
# – The third time a hash starts with five zeroes is for abc5278568,
#   discovering the character f.
#
# In this example, after continuing this search a total of eight times,
# the password is 18f47a30.
#
# Given the actual Door ID, what is the password?
#
#
# --- Solution ---
#
# We read the input as a string from a file. Then, we perform a loop as long
# as we do not find 8 characters – in each iteration, we calculate the MD5 sum
# from string combined by the given input ID and the current iteration number,
# then we check if the calculated hash starts with 5 zeros – if so, we save
# the sixth character of the calculated MD5 hash as our next password element.
# Finally, once all 8 characters were found, we return the password.
#

import hashlib

INPUT_FILE = 'input.txt'


def MD5(string):
    return hashlib.md5(string.encode()).hexdigest()


def main():
    with open(INPUT_FILE, 'r') as file:
        ID = file.read().strip()

    password = ''
    iteration = 0

    while len(password) < 8:
        md5sum = MD5(ID + str(iteration))

        if md5sum.startswith('00000'):
            password += md5sum[5]

        iteration += 1

    print(password)


if __name__ == '__main__':
    main()
