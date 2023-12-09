#!/usr/bin/env python3
#
# --- Day 5: How About a Nice Game of Chess? / Part Two ---
#
# As the door slides open, you are presented with a second door that uses
# a slightly more inspired security mechanism. Clearly unimpressed by
# the last version (in what movie is the password decrypted in order?!),
# the Easter Bunny engineers have worked out a better solution.
#
# Instead of simply filling in the password from left to right, the hash
# now also indicates the position within the password to fill. You still
# look for hashes that begin with five zeroes; however, now, the sixth
# character represents the position (0-7), and the seventh character
# is the character to put in that position.
#
# A hash result of 000001f means that f is the second character
# in the password. Use only the first result for each position,
# and ignore invalid positions.
#
# For example, if the Door ID is abc:
# – The first interesting hash is from abc3231929, which produces 0000015...;
#   so, 5 goes in position 1: _5______.
# – In the previous method, 5017308 produced an interesting hash; however,
#   it is ignored, because it specifies an invalid position (8).
# – The second interesting hash is at index 5357525, which produces 000004e...;
#   so, e goes in position 4: _5__e___.
#
# You almost choke on your popcorn as the final character falls into place,
# producing the password 05ace8e3.
#
# Given the actual Door ID and this new method, what is the password? Be extra
# proud of your solution if it uses a cinematic "decrypting" animation.
#
#
# --- Solution ---
#
# The difference here is that instead of appending newly discovered characters,
# we need to set them at specific positions in the produced password. Hence,
# the initial password value with characters that would not be returned by MD5
# function call, so we can verify for sure whether the position was assigned.
# The cinematic "decrypting" animation was also prepared – every few iterations
# we display the part of just calculated hash (it changes every time in loop)
# on password positions that were not yet assigned – this gives an effect of
# randomly changing characters until a given position was there set assigned.
# The cursor hiding and showing was added for better display in terminal.
# The mechanism is enabled only on demand, so its output (that involves a lot
# of carriage returns) does not mess with the automated testing via script.
#

import hashlib

INPUT_FILE = 'input.txt'

ANIMATION = False


def MD5(string):
    return hashlib.md5(string.encode()).hexdigest()


def main():
    with open(INPUT_FILE, 'r') as file:
        ID = file.read().strip()

    password = ['_'] * 8
    iteration = 0

    if ANIMATION:
        print('\033[?25l', end='\r')  # hide cursor
        print(''.join(password), end='\r')

    while password.count('_'):
        md5sum = MD5(ID + str(iteration))

        if md5sum.startswith('00000'):
            if md5sum[5] in ['0', '1', '2', '3', '4', '5', '6', '7']:
                index = int(md5sum[5])

                if password[index] == '_':
                    password[index] = md5sum[6]

        if ANIMATION and (iteration % 50000) == 0:  # do not print too often
            for index, character in enumerate(password):
                if character == '_':
                    print(md5sum[index], end='')
                else:
                    print(character, end='')
            print('\r', end='')

        iteration += 1

    if ANIMATION:
        print('\033[?25h', end='')  # show cursor

    print(''.join(password))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        if ANIMATION:
            print('\033[?25h', end='')  # show cursor
