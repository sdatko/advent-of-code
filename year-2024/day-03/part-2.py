#!/usr/bin/env python3
#
# --- Day 3: Mull It Over / Part Two ---
#
# As you scan through the corrupted memory, you notice that some
# of the conditional statements are also still intact. If you handle
# some of the uncorrupted conditional statements in the program,
# you might be able to get an even more accurate result.
#
# There are two new instructions you'll need to handle:
# – The do() instruction enables future mul instructions.
# – The don't() instruction disables future mul instructions.
#
# Only the most recent do() or don't() instruction applies.
# At the beginning of the program, mul instructions are enabled.
#
# For example:
#
#   xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
#
# This corrupted memory is similar to the example from before, but
# this time the mul(5,5) and mul(11,8) instructions are disabled because
# there is a don't() instruction before them. The other mul instructions
# function normally, including the one at the end that gets re-enabled
# by a do() instruction.
#
# This time, the sum of the results is 48 (2*4 + 8*5).
#
# Handle the new instructions; what do you get if you add up all
# of the results of just the enabled multiplications?
#
#
# --- Solution ---
#
# The difference in this part is that we need to consider two more operations:
# do() and don't(). All we need to do, is to ignore part of programs between
# the first occurrence of `don't()` and first occurrence of `do()` after that.
# If there is only `don't()`, but no `do()` after that, we remove everything
# until the end of program.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        program = file.read()

    muls = []

    pos = 0

    while True:
        index = program.find('don\'t()', pos)
        if index < 0:
            break

        index2 = program.find('do()', index)

        if index2 < 0:
            program = program[:index]
        else:
            index2 += 4  # place index after the `do()`
            program = program[:index] + program[index2:]

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
