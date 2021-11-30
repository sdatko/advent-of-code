#!/usr/bin/env python3
#
# Task:
# Run your copy of the boot code. Immediately before any instruction
# is executed a second time, what value is in the accumulator?
# - acc increases or decreases a single global value called the accumulator
#   by the value given in the argument. For example, acc +7 would increase
#   the accumulator by 7. The accumulator starts at 0. After an acc
#   instruction, the instruction immediately below it is executed next.
# - jmp jumps to a new instruction relative to itself. The next instruction
#   to execute is found using the argument as an offset from the jmp
#   instruction; for example, jmp +2 would skip the next instruction,
#   jmp +1 would continue to the instruction immediately below it, and
#   jmp -20 would cause the instruction 20 lines above to be executed next.
# - nop stands for No OPeration - it does nothing. The instruction immediately
#   below it is executed next.
#
# Solution:
# We simply go line by line through the input file, performing the necessary
# action, depending on what is the current instruction and adding the indexes
# of visited lines to the set. If next line to process is in the set,
# we can terminate the program and print the current value of accumulator.
#

INPUT_FILE = 'input.txt'


def main():
    instructions = open(INPUT_FILE, 'r').read().split('\n')

    accumulator = 0
    executed_lines = set()

    index = 0
    while True:
        if index in executed_lines:
            break

        executed_lines.add(index)
        operand, value = instructions[index].split()
        index += 1

        if operand == 'nop':
            pass
        elif operand == 'acc':
            accumulator += int(value)
        elif operand == 'jmp':
            index += (int(value) - 1)
        else:
            print('SEGMENTATION PANIC')
            break

    print(accumulator)


if __name__ == '__main__':
    main()
