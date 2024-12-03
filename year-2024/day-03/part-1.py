#!/usr/bin/env python3
#
# --- Day 3: Mull It Over ---
#
# "Our computers are having issues, so I have no idea if we have any Chief
# Historians in stock! You're welcome to check the warehouse, though," says
# the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop.
# The Historians head out to take a look.
#
# The shopkeeper turns to you. "Any chance you can see why our computers
# are having issues again?"
#
# The computer appears to be trying to run a program, but its memory
# (your puzzle input) is corrupted. All of the instructions have been
# jumbled up!
#
# It seems like the goal of the program is just to multiply some numbers.
# It does that with instructions like mul(X,Y), where X and Y are each
# 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get
# a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.
#
# However, because the program's memory has been corrupted, there are also
# many invalid characters that should be ignored, even if they look like part
# of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34),
# or mul ( 2 , 4 ) do nothing.
#
# For example, consider the following section of corrupted memory:
#
#   xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
#
# Only the four highlighted sections are real mul instructions. Adding up
# the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).
#
# Scan the corrupted memory for uncorrupted mul instructions.
# What do you get if you add up all of the results of the multiplications?
#
#
# --- Solution ---
#
# We start by reading the input file into a string, without any additional
# processing involved (there are newlines, we keep them!). Then we process
# the program going for all positions from start to end – we find the first
# possible occurence of text `mul(`, then the comma character `,` and closing
# bracket `)`, then we check if everything between these occurences are
# numbers – and if so, we multiply these numbers and add to the list of values.
# Finally, as an answer we return the sum of calculated values.
#
# The obvious solution involve regular expressions, but I decided to not
# import anything here (e.g. re module in Python) so I had to implement
# different approach.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        program = file.read()

    muls = []

    # NOTE: everything below could be just...
    # pairs = re.findall(r'mul[(](\d+),(\d+)[)]', program)
    # for pair in pairs:
    #     muls.append(int(pair[0]) * int(pair[1]))

    pos = 0

    while True:
        index = program.find('mul(', pos)
        if index < 0:
            break

        index += 3  # place index at the end of `mul(`

        index2 = program.find(',', index)
        if index2 < 0:
            break

        index3 = program.find(')', index2)
        if index3 < 0:
            break

        if not index < index2 < index3:
            break

        valid = True

        for i in range(index + 1, index2):
            if not program[i].isdigit():
                valid = False
                break
        else:
            number1 = int(program[index + 1:index2])

        for i in range(index2 + 1, index3):
            if not program[i].isdigit():
                valid = False
                break
        else:
            number2 = int(program[index2 + 1:index3])

        if valid:
            muls.append(number1 * number2)

        pos = index

    print(sum(muls))


if __name__ == '__main__':
    main()
