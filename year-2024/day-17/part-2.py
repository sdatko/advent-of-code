#!/usr/bin/env python3
#
# --- Day 17: Chronospatial Computer / Part Two ---
#
# Digging deeper in the device's manual, you discover the problem:
# this program is supposed to output another copy of the program!
# Unfortunately, the value in register A seems to have been corrupted.
# You'll need to find a new value to which you can initialize register A
# so that the program's output instructions produce an exact copy
# of the program itself.
#
# For example:
#
#  Register A: 2024
#  Register B: 0
#  Register C: 0
#
#  Program: 0,3,5,4,3,0
#
# This program outputs a copy of itself if register A is instead initialized
# to 117440. (The original initial value of register A, 2024, is ignored.)
#
# What is the lowest positive initial value for register A that causes
# the program to output a copy of itself?
#
#
# --- Solution ---
#
# The difference in this part is that we need to find a register value that
# would make the code from previous part to output the expected values, which
# are the same as the program given in input. For this we can take an approach
# of trials and errors, supplying various values as inputs and analyzing their
# impact on the output, similarly like collisions for hashing algorithms are
# being found. However, we can make this process much more efficient by reverse
# enigineering the program, as it is fairly simple:
#
#   2,4,1,1,7,5,1,5,4,0,5,5,0,3,3,0
#
# Knowing the architecture from previous part, it consists of 8 operations:
#
#   2,4, 1,1, 7,5, 1,5, 4,0, 5,5, 0,3, 3,0
#
# That can be more human-friendly expressed via following assembler:
#
#   bst,4 bxl,1 cdv,5 bxl,5 bxc,0 out,5 adv,3 jnz,0
#
# Which can be translated to following Python code:
#
#   while registers['A'] != 0:  # 3,0
#     registers['B'] = register['A'] % 8  # 2,4
#     registers['B'] = registers['B'] ^ 1  # 1,1
#     registers['C'] = registers['A'] // (2 ** registers['B'])  # 7,5
#     registers['B'] = registers['B'] ^ 5  # 1,5
#     registers['B'] = registers['B'] ^ registers['C']  # 4,0
#     output.append(registers['B'] % 8)  # 5,5
#     registers['A'] = registers['A'] // 8  # 0,3
#
# Effectively, this program takes 3 lowest bits from register A (the modulo 8
# operation), then performs some calculation on taken value (using register B
# for storing the intermediate results), finally outputting the 3 lowest bits
# of the result and shifting the remaining value in the register A by 3 bits
# (division by 8). This is repeated as long as there is any value remaining
# in register A. Hence, the input will be produced by a number of 3-bit values
# (octal numbers, from 0 to 7) equal to the length of the program (16 values),
# concatenated and converted from base 8 to decimal base. The most significant
# bits of input value will be visible as the last values in output. Because
# during the calculations the remaining value of register A is also involved
# (see register C in the code above), it is much easier to start analysis
# from finding the values of most significant bits first (comparing with last
# output value), then the less significant bits (and second to last output),
# and so on. It is important to notice that for some positions there appear
# to be more than one value possible, that may be rejected when verifying next
# positions later, so we cannot stop just after first match and we need to
# consider all successful variants on each position. The part of original code
# that was implementing the defined computer operations was moved to a separate
# function block, for a greater clarity of the final code. Finally, we take
# the smallest of possible numbers and print it as an answer.
#

INPUT_FILE = 'input.txt'


def process(program, register_A=0, register_B=0, register_C=0):
    registers = {
        'A': register_A,
        'B': register_B,
        'C': register_C,
    }

    def combo(operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return registers['A']
        elif operand == 5:
            return registers['B']
        elif operand == 6:
            return registers['C']
        elif operand == 7:
            print('Attempted to call a reserved operand')
            exit(1)
        else:
            print(f'Unknown combo operand: {operand}')
            exit(1)

    pointer = 0
    output = []

    while True:
        try:
            opcode = program[pointer]
            operand = program[pointer + 1]

        except IndexError:
            break  # stop execution

        if opcode == 0:  # adv
            numerator = registers['A']
            denominator = 2 ** combo(operand)
            registers['A'] = numerator // denominator

        elif opcode == 1:  # bxl
            registers['B'] = registers['B'] ^ operand

        elif opcode == 2:  # bst
            registers['B'] = combo(operand) % 8

        elif opcode == 3:  # jnz
            if registers['A'] != 0:
                pointer = operand
                continue  # skip default pointer incrementation

        elif opcode == 4:  # bxc
            registers['B'] = registers['B'] ^ registers['C']
            pass  # intentionally ignore operand

        elif opcode == 5:  # out
            value = combo(operand) % 8
            output.append(value)

        elif opcode == 6:  # bdv
            numerator = registers['A']
            denominator = 2 ** combo(operand)
            registers['B'] = numerator // denominator

        elif opcode == 7:  # cdv
            numerator = registers['A']
            denominator = 2 ** combo(operand)
            registers['C'] = numerator // denominator

        else:
            print('Uknown opcode {opcode} at pointer: {pointer}')
            exit(1)

        pointer += 2  # default pointer incrementation

    return tuple(output)


def main():
    with open(INPUT_FILE, 'r') as file:
        registers, program = file.read().strip().split('\n\n')

    registers = [register.split(':')
                 for register in registers.replace('Register', '')
                                          .replace(' ', '')
                                          .strip()
                                          .split()]
    registers = {name: int(value)
                 for name, value in registers}

    program = tuple(map(int,
                        program.replace('Program:', '').strip().split(',')))

    expected = program
    solutions = set()

    input_8 = [0] * len(program)
    queue = [(0, input_8)]  # position, input bits

    while queue:
        position, input_8 = queue.pop()
        next_position = position + 1

        for candidate in (0, 1, 2, 3, 4, 5, 6, 7):
            input_8[position] = candidate
            input_10 = int(''.join(str(numeral) for numeral in input_8),
                           base=8)

            output = process(program, input_10)

            if output == expected:  # complete solution
                solutions.add(input_10)

            elif next_position < len(program):  # check for partial solution
                partial_output = tuple(reversed(output))[:next_position]
                partial_expected = tuple(reversed(program))[:next_position]

                if partial_output == partial_expected:
                    queue.append((next_position, input_8.copy()))

    print(min(solutions))


if __name__ == '__main__':
    main()
