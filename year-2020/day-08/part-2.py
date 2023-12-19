#!/usr/bin/env python3
#
# --- Day 8: Handheld Halting / Part Two ---
#
# After some careful analysis, you believe that exactly
# one instruction is corrupted.
#
# Somewhere in the program, either a jmp is supposed to be a nop,
# or a nop is supposed to be a jmp. (No acc instructions were harmed
# in the corruption of this boot code.)
#
# The program is supposed to terminate by attempting to execute
# an instruction immediately after the last instruction in the file.
# By changing exactly one jmp or nop, you can repair the boot code
# and make it terminate correctly.
#
# For example, consider the same program from above:
#
#   nop +0
#   acc +1
#   jmp +4
#   acc +3
#   jmp -3
#   acc -99
#   acc +1
#   jmp -4
#   acc +6
#
# If you change the first instruction from nop +0 to jmp +0, it would create
# a single-instruction infinite loop, never leaving that instruction. If you
# change almost any of the jmp instructions, the program will still eventually
# find another jmp instruction and loop forever.
#
# However, if you change the second-to-last instruction (from jmp -4
# to nop -4), the program terminates! The instructions are visited
# in this order:
#
#   nop +0  | 1
#   acc +1  | 2
#   jmp +4  | 3
#   acc +3  |
#   jmp -3  |
#   acc -99 |
#   acc +1  | 4
#   nop -4  | 5
#   acc +6  | 6
#
# After the last instruction (acc +6), the program terminates by attempting
# to run the instruction below the last instruction in the file. With this
# change, after the program terminates, the accumulator contains the value 8
# (acc +1, acc +1, acc +6).
#
# Fix the program so that it terminates normally by changing exactly one
# jmp (to nop) or nop (to jmp). What is the value of the accumulator after
# the program terminates?
#
#
# --- Solution ---
#
# In addition here we try to work in a loop on copies of original input,
# every time changing different line. If at some time we reach the end
# of file, we have the solution. We can skip checking changes for lines
# that are modifying the accumulator.
#

INPUT_FILE = 'input.txt'


def main():
    instructions = open(INPUT_FILE, 'r').read().split('\n')

    exit = 0

    for line in range(len(instructions)):
        corrected_instructions = instructions[:]

        if instructions[line].startswith('acc'):
            continue
        elif instructions[line].startswith('nop'):
            corrected_instructions[line] = instructions[line].replace('nop',
                                                                      'jmp')
        elif instructions[line].startswith('jmp'):
            corrected_instructions[line] = instructions[line].replace('jmp',
                                                                      'nop')

        accumulator = 0
        executed_lines = set()

        index = 0
        while True:
            if index in executed_lines:
                break
            if index >= len(instructions) - 1:
                exit = 1
                break

            executed_lines.add(index)
            operand, value = corrected_instructions[index].split()
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

        if exit:
            break

    print(accumulator)


if __name__ == '__main__':
    main()
