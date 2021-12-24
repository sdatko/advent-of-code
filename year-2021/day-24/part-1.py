#!/usr/bin/env python3
#
# Task:
# Magic smoke starts leaking from the submarine's arithmetic logic unit (ALU).
# Without the ability to perform basic arithmetic and logic functions,
# the submarine can't produce cool patterns with its Christmas lights!
# It also can't navigate. Or run the oxygen system.
# Don't worry, though - you probably have enough oxygen left to give you
# enough time to build a new ALU.
# The ALU is a four-dimensional processing unit: it has integer variables
# w, x, y, and z. These variables all start with the value 0. The ALU also
# supports six instructions:
# - inp a - Read an input value and write it to variable a.
# - add a b - Add the value of a to the value of b, then store the result
#             in variable a.
# - mul a b - Multiply the value of a by the value of b, then store the result
#             in variable a.
# - div a b - Divide the value of a by the value of b, truncate the result
#             to an integer, then store the result in variable a. (Here,
#             "truncate" means to round the value toward zero.)
# - mod a b - Divide the value of a by the value of b, then store the remainder
#             in variable a. (This is also called the modulo operation.)
# - eql a b - If the value of a and b are equal, then store the value 1
#             in variable a. Otherwise, store the value 0 in variable a.
# In all of these instructions, a and b are placeholders; a will always be
# the variable where the result of the operation is stored (one of w, x, y,
# or z), while b can be either a variable or a number. Numbers can be positive
# or negative, but will always be integers.
# The ALU has no jump instructions; in an ALU program, every instruction
# is run exactly once in order from top to bottom. The program halts after
# the last instruction has finished executing.
# (Program authors should be especially cautious; attempting to execute div
# with b=0 or attempting to execute mod with a<0 or b<=0 will cause the program
# to crash and might even damage the ALU. These operations are never intended
# in any serious ALU program.)
# For example, here is an ALU program which takes an input number, negates it,
# and stores it in x:
#   inp x
#   mul x -1
# Here is an ALU program which takes two input numbers, then sets z to 1
# if the second input number is three times larger than the first input number,
# or sets z to 0 otherwise:
#   inp z
#   inp x
#   mul z 3
#   eql z x
# Here is an ALU program which takes a non-negative integer as input, converts
# it into binary, and stores the lowest (1's) bit in z, the second-lowest (2's)
# bit in y, the third-lowest (4's) bit in x, and the fourth-lowest (8's) bit
# in w:
#   inp w
#   add z w
#   mod z 2
#   div w 2
#   add y w
#   mod y 2
#   div w 2
#   add x w
#   mod x 2
#   div w 2
#   mod w 2
# Once you have built a replacement ALU, you can install it in the submarine,
# which will immediately resume what it was doing when the ALU failed:
# validating the submarine's model number. To do this, the ALU will run
# the MOdel Number Automatic Detector program (MONAD, your puzzle input).
# Submarine model numbers are always fourteen-digit numbers consisting only
# of digits 1 through 9. The digit 0 cannot appear in a model number.
# When MONAD checks a hypothetical fourteen-digit model number, it uses
# fourteen separate inp instructions, each expecting a single digit of
# the model number in order of most to least significant. (So, to check
# the model number 13579246899999, you would give 1 to the first inp
# instruction, 3 to the second inp instruction, 5 to the third inp instruction,
# and so on.) This means that when operating MONAD, each input instruction
# should only ever be given an integer value of at least 1 and at most 9.
# Then, after MONAD has finished running all of its instructions, it will
# indicate that the model number was valid by leaving a 0 in variable z.
# However, if the model number was invalid, it will leave some other non-zero
# value in z.
# MONAD imposes additional, mysterious restrictions on model numbers, and
# legend says the last copy of the MONAD documentation was eaten by a tanuki.
# You'll need to figure out what MONAD does some other way.
# To enable as many submarine features as possible, find the largest valid
# fourteen-digit model number that contains no 0 digits. What is the largest
# model number accepted by MONAD?
#
# Solution:
# We start by reading the input file as list of instructions (every line equals
# to single instruction). Then we implement the ALU unit, that executes defined
# instructions with given input and starting memory set (optional argument).
# Then we simply need to run our implementation on every possible input number
# and only then I realised there is 9^14 combinations to check, which is simply
# too much for finding the results in a reasonable time. Instead  the right
# approach seems to require the reverse engineering of given instructions set.
# After analyzing the puzzle input, I noticed that the code consists of a few
# similar parts that processes each digit of the input number. Further analysis
# showed that each part consists of 18 lines, including 15 lines that are
# exactly the same for all parts and 3 lines that have different parameters.
#    0 {('inp', 'w')}
#    1 {('mul', 'x', '0')}
#    2 {('add', 'x', 'z')}
#    3 {('mod', 'x', '26')}
#    4 {('div', 'z', '1'), ('div', 'z', '26')}
#    5 {('add', 'x', '-5'), ('add', 'x', '11'), ('add', 'x', '-6'),
#       ('add', 'x', '12'), ('add', 'x', '13'), ('add', 'x', '15'),
#       ('add', 'x', '-16'), ('add', 'x', '-11'), ('add', 'x', '-7'),
#       ('add', 'x', '-3'), ('add', 'x', '14')}
#    6 {('eql', 'x', 'w')}
#    7 {('eql', 'x', '0')}
#    8 {('mul', 'y', '0')}
#    9 {('add', 'y', '25')}
#   10 {('mul', 'y', 'x')}
#   11 {('add', 'y', '1')}
#   12 {('mul', 'z', 'y')}
#   13 {('mul', 'y', '0')}
#   14 {('add', 'y', 'w')}
#   15 {('add', 'y', '9'), ('add', 'y', '2'), ('add', 'y', '11'),
#       ('add', 'y', '10'), ('add', 'y', '12'), ('add', 'y', '6'),
#       ('add', 'y', '15'), ('add', 'y', '16'), ('add', 'y', '4')}
#   16 {('mul', 'y', 'x')}
#   17 {('add', 'z', 'y')}
# The instructions above can be written in Python as:
#   def function(digit, z, div, add1, add2):
#       x = (z % 26) + add1  # lines 1-3 and 5
#       z = z // div  # line 4
#
#       if x == digit:  # line 6
#           x = 1
#       else:
#           x = 0
#
#       if x == 0:  # line 7
#           x = 1
#       else:
#           x = 0
#
#       y = 25 * x + 1  # lines 8-11
#       z *= y  # line 12
#       y = (digit + add2) * x  # lines 13-16
#       z += y  # line 17
#
#       return z
# This can be then written in much simpler form as:
#   def function(digit, z, div, add1, add2):
#       x = (z % 26) + add1
#       z = z // div
#
#       if x == digit:
#           return z
#       else:
#           return z * 26 + digit + add2
# The puzzle input can be then write as:
#   z1 = function(d1, 0, 1, 11, 16)
#   z2 = function(d2, z1, 1, 12, 11)
#   z3 = function(d3, z2, 1, 13, 12)
#   z4 = function(d4, z3, 26, -5, 12)
#   z5 = function(d5, z4, 26, -3, 12)
#   z6 = function(d6, z5, 1, 14, 2)
#   z7 = function(d7, z6, 1, 15, 11)
#   z8 = function(d8, z7, 26, -16, 4)
#   z9 = function(d9, z8, 1, 14, 12)
#   zA = function(dA, z9, 1, 15, 9)
#   zB = function(dB, zA, 26, -7, 10)
#   zC = function(dC, zB, 26, -11, 11)
#   zD = function(dD, zC, 26, -6, 6)
#   zE = function(dE, zD, 26, -11, 15)
#   return zE
# Note that in this code the branching is only possible for negative values
# of add1, as because of add2 values the given condition `x == digit` is not
# possible to satisfy for first few function calls. Also when possible,
# we should take the digit that holds in this condition, as it will let us
# reduce the value (return z), while the other (x != digit) will add another
# element (return z*26 + digit + add2) to the sum we want to reach value 0.
# This allows us to find the solution by calculating conditions for digits di.
#   z1 = d1 + 16
#   z2 = (d1 + 16) * 26 + d2 + 11
#   z3 = ((d1 + 16) * 26 + d2 + 11) * 26 + d3 + 12
#   if d4 == d3 + 12 - 5
#     z4 = (d1 + 16) * 26 + d2 + 11
#   if d5 == d2 + 11 - 3
#     z5 = d1 + 16
#   z6 = (d1 + 16) * 26 + d6 + 2
#   z7 = ((d1 + 16) * 26 + d6 + 2) * 26 + d7 + 11
#   if d8 == d7 + 11 - 16
#     z8 = (d1 + 16) * 26 + d6 + 2
#   z9 = ((d1 + 16) * 26 + d6 + 2) * 26 + d9 + 12
#   zA = (((d1 + 16) * 26 + d6 + 2) * 26 + d9 + 12) * 26 + dA + 9
#   if dB == dA + 9 - 7
#     zB = ((d1 + 16) * 26 + d6 + 2) * 26 + d9 + 12
#   if dC == d9 + 12 - 11
#     zC = (d1 + 16) * 26 + d6 + 2)
#   if dD == d6 + 2 - 6
#     zD = d1 + 16
#   if dE == d1 + 16 - 11
#     zE = 0
# In the end:
#   d4 == d3 + 7
#   d5 == d2 + 8
#   d8 == d7 - 5
#   dB == dA + 2
#   dC == d9 + 1
#   dD == d6 - 4
#   dE == d1 + 5
# As the final answer, we print the highest number that satisfies the given
# seven equations. So, we find maximum value of d1, which must be 4, so dE
# is not greater than 9, then the maximum value of d2, which is limited to 1,
# then the maximum value of d3, and so on... The code below finds the solution
# by considering the given conditions and also verifies it is a valid result.
# There are also commented parts that were used.
#

INPUT_FILE = 'input.txt'


def ALU(inputs, instructions, memory=None):
    if not memory:
        memory = {
            'x': 0,
            'y': 0,
            'z': 0,
            'w': 0,
        }

    def _get_value(value):
        if value.lstrip('-').isnumeric():
            value = int(value)
        else:
            value = memory[value]
        return value

    def inp(variable):
        memory[variable] = inputs.pop(0)

    def add(variable, operand):
        value = _get_value(operand)
        new_value = memory[variable] + value
        memory[variable] = new_value

    def mul(variable, operand):
        value = _get_value(operand)
        new_value = memory[variable] * value
        memory[variable] = new_value

    def div(variable, operand):
        value = _get_value(operand)
        new_value = memory[variable] // value
        memory[variable] = new_value

    def mod(variable, operand):
        value = _get_value(operand)
        new_value = memory[variable] % value
        memory[variable] = new_value

    def eql(variable, operand):
        value = _get_value(operand)
        new_value = int(memory[variable] == value)
        memory[variable] = new_value

    for instruction in instructions:
        if len(instruction) == 2:
            operator, operand1 = instruction
            operand2 = 0
        else:
            operator, operand1, operand2 = instruction

        if operator == 'inp':
            inp(operand1)
        elif operator == 'add':
            add(operand1, operand2)
        elif operator == 'mul':
            mul(operand1, operand2)
        elif operator == 'div':
            div(operand1, operand2)
        elif operator == 'mod':
            mod(operand1, operand2)
        elif operator == 'eql':
            eql(operand1, operand2)

    return memory


def main():
    instructions = [line.strip('\n').split() for line in open(INPUT_FILE, 'r')]

    #
    # Brute force solution – will not finish in reasonable time
    #

    # def decrement_inputs(inputs):
    #     inputs[-1] = inputs[-1] - 1
    #     bias = 0

    #     for index in range(len(inputs) - 1, 0, -1):
    #         inputs[index] += bias
    #         bias = 0

    #         if inputs[index] <= 0:
    #             inputs[index] = 9
    #             bias = -1

    #     return inputs

    # inputs = [9] * 14

    # while inputs[0] > 0:
    #     result = ALU(inputs.copy(), instructions)
    #     valid = result['z']

    #     if valid == 0:
    #         print(inputs)
    #         break

    #     decrement_inputs(inputs)

    #
    # Compare code sections per each digit
    #

    # digits_instructions = []
    # digit_instructions = []

    # for instruction in instructions:
    #     operator = instruction[0]
    #     if operator == 'inp':
    #         if digit_instructions:
    #             digits_instructions.append(digit_instructions)
    #         digit_instructions = []

    #     digit_instructions.append(instruction)

    # digits_instructions.append(digit_instructions)

    # for line in range(len(digits_instructions[0])):
    #     cmds = set([tuple(digits_instructions[index][line])
    #                 for index in range(len(digits_instructions))])
    #     print(line, cmds)

    digits = [0] * 14

    def set_conditionally(value, digit1, digit2, diff_digit1_to_digit2):
        value1 = value
        value2 = value + diff_digit1_to_digit2

        if 1 <= value1 <= 9 and 1 <= value2 <= 9:
            digits[digit1 - 1] = value1
            digits[digit2 - 1] = value2

    for candidate in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        # d4 == d3 + 7
        set_conditionally(candidate, 3, 4, 7)
        # d5 == d2 + 8
        set_conditionally(candidate, 2, 5, 8)
        # d8 == d7 - 5
        set_conditionally(candidate, 7, 8, -5)
        # dB == dA + 2
        set_conditionally(candidate, 10, 11, 2)
        # dC == d9 + 1
        set_conditionally(candidate, 9, 12, 1)
        # dD == d6 - 4
        set_conditionally(candidate, 6, 13, -4)
        # dE == d1 + 5
        set_conditionally(candidate, 1, 14, 5)

    print(''.join([str(digit) for digit in digits]))

    result = ALU(digits, instructions)
    assert result['z'] == 0


if __name__ == '__main__':
    main()
