#!/usr/bin/env python3
#
# --- Day 24: Arithmetic Logic Unit / Part Two ---
#
# As the submarine starts booting up things like the Retro Encabulator,
# you realize that maybe you don't need all these submarine features after all.
#
# What is the smallest model number accepted by MONAD?
#
#
# --- Solution ---
#
# The same way we can find an answer for part 2. The only necessary change
# was to invert the argument of the loop with candidates – to range(9, 0, -1).
# However, I was not satisfied with that, so I prepared more generalised
# solution that works assuming the input file format is always similar
# to the one I received (there are only differences in a few specific parts).
# We start by reading the input file and divide the instructions to separate
# groups – parts that define processing per each input digit. Then we iterate
# through the instructions groups. From reverse engineering/analysis we know
# that the condition defined in code is possible to be satisfied only if some
# added integer there is not too high – in given puzzle input it was always
# negative when it was correct, though small positive values should also work.
# So, the first considered addition is done in line 6th and depending on its
# value we perform one of two actions. When the value is too big, the returned
# result will be be increased by multiplying the existing value 26 times and
# adding new term equal to the sum of given digit and some integer (z = z * 26
# + digit + add2). The added term shall eventually become a remainder important
# later to define the conditions, so we save the term elements to a list.
# When the first added value is in appropriate range, we take the last saved
# remainder and we find elements for our digit condition (i.e. digits indexes
# and the difference between their values, including the added components add1
# and add2). Finally we perform checking and conditional assignments of values
# taking the defined restrictions into account. As an answer, we print joined
# array elements (each element represents a single digit of 14-digit number).
#

INPUT_FILE = 'input.txt'


def main():
    instructions = [line.strip('\n').split() for line in open(INPUT_FILE, 'r')]
    digits_instructions = []
    digit_instructions = []

    for instruction in instructions:
        operator = instruction[0]
        if operator == 'inp':
            if digit_instructions:
                digits_instructions.append(digit_instructions)
            digit_instructions = []

        digit_instructions.append(instruction)

    digits_instructions.append(digit_instructions)

    remainders = []
    conditions = []

    for index, digit_instructions in enumerate(digits_instructions):
        current_digit = index + 1
        add1 = int(digit_instructions[5][2])
        add2 = int(digit_instructions[15][2])

        if add1 < 9:
            previous_digit, add2 = remainders.pop()
            conditions.append((previous_digit, current_digit, add2 + add1))

        else:
            remainders.append((current_digit, add2))

    assert len(remainders) == 0

    digits = [0] * 14

    def set_conditionally(value, digit1, digit2, diff_digit1_to_digit2):
        value1 = value
        value2 = value + diff_digit1_to_digit2

        if 1 <= value1 <= 9 and 1 <= value2 <= 9:
            digits[digit1 - 1] = value1
            digits[digit2 - 1] = value2

    for candidate in range(9, 0, -1):
        for condition in conditions:
            digit1, digit2, difference = condition
            set_conditionally(candidate, digit1, digit2, difference)

    print(''.join([str(digit) for digit in digits]))


if __name__ == '__main__':
    main()
