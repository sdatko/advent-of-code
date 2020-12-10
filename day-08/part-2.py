#!/usr/bin/env python3
#
# Task:
# Fix the program so that it terminates normally by changing exactly one jmp
# (to nop) or nop (to jmp). What is the value of the accumulator after the
# program terminates?
#
# Solution:
# In addition here we try to work in a loop on copies of original input,
# every time chaning different line. If at some time we reach the end
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
