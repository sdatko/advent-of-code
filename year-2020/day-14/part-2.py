#!/usr/bin/env python3
#
# --- Day 14: Docking Data / Part Two ---
#
# For some reason, the sea port's computer system still can't communicate
# with your ferry's docking program. It must be using version 2
# of the decoder chip!
#
# A version 2 decoder chip doesn't modify the values being written at all.
# Instead, it acts as a memory address decoder. Immediately before a value
# is written to memory, each bit in the bitmask modifies the corresponding
# bit of the destination memory address in the following way:
#
# – If the bitmask bit is 0, the corresponding memory
#   address bit is unchanged.
# – If the bitmask bit is 1, the corresponding memory
#   address bit is overwritten with 1.
# – If the bitmask bit is X, the corresponding memory
#   address bit is floating.
#
# A floating bit is not connected to anything and instead fluctuates
# unpredictably. In practice, this means the floating bits will take
# on all possible values, potentially causing many memory addresses
# to be written all at once!
#
# For example, consider the following program:
#
#   mask = 000000000000000000000000000000X1001X
#   mem[42] = 100
#   mask = 00000000000000000000000000000000X0XX
#   mem[26] = 1
#
# When this program goes to write to memory address 42,
# it first applies the bitmask:
#
#   address: 000000000000000000000000000000101010  (decimal 42)
#   mask:    000000000000000000000000000000X1001X
#   result:  000000000000000000000000000000X1101X
#
# After applying the mask, four bits are overwritten, three of which
# are different, and two of which are floating. Floating bits take
# on every possible combination of values; with two floating bits,
# four actual memory addresses are written:
#
#   000000000000000000000000000000011010  (decimal 26)
#   000000000000000000000000000000011011  (decimal 27)
#   000000000000000000000000000000111010  (decimal 58)
#   000000000000000000000000000000111011  (decimal 59)
#
# Next, the program is about to write to memory address 26
# with a different bitmask:
#
#   address: 000000000000000000000000000000011010  (decimal 26)
#   mask:    00000000000000000000000000000000X0XX
#   result:  00000000000000000000000000000001X0XX
#
# This results in an address with three floating bits,
# causing writes to eight memory addresses:
#
#   000000000000000000000000000000010000  (decimal 16)
#   000000000000000000000000000000010001  (decimal 17)
#   000000000000000000000000000000010010  (decimal 18)
#   000000000000000000000000000000010011  (decimal 19)
#   000000000000000000000000000000011000  (decimal 24)
#   000000000000000000000000000000011001  (decimal 25)
#   000000000000000000000000000000011010  (decimal 26)
#   000000000000000000000000000000011011  (decimal 27)
#
# The entire 36-bit address space still begins initialized to the value 0
# at every address, and you still need the sum of all values left in memory
# at the end of the program. In this example, the sum is 208.
#
# Execute the initialization program using an emulator for a version 2 decoder
# chip. What is the sum of all values left in memory after it completes?
#
#
# --- Solution ---
#
# We need to put more work in processing addresses now, leaving the value
# unchanged. First, the address value we represent as a 36-bits long string
# of values 0 and 1. Then, we iterate over each character (bit) of a given
# mask and if there is value 1 or X, we overwrite the corresponding value
# in the address string. Then we need to generate all possible combinations
# of addresses, where each X can be 0 or 1. For this, we start with an array
# of single element (current address string) and then we perform a processing
# in a loop as long as there is letter X in the first address string in our
# array. If so, we remove this first element (address) from the array (list),
# produce two new addresses, one with value 0 in place of this X, one with
# value 1 in the place, then we append them to the array of addresses.
# This loop will finish, when all possible combinations of addresses will be
# generated. Finally we just need to save the values the dictionary, where
# keys are our calculated addresses, and after all instructions are processed
# we return the sum of values in our dictionary (memory map).
#

INPUT_FILE = 'input.txt'


def main():
    instructions = [line.strip('\n') for line in open(INPUT_FILE, 'r')]

    mask = None
    memory = {}

    for instruction in instructions:
        if instruction.startswith('mask = '):
            mask = instruction.split(' = ')[1]

        elif instruction.startswith('mem['):
            address, value = instruction.split(' = ')
            address = format(int(address[4:-1]), '036b')
            value = int(value)

            for i, bit in enumerate(mask):
                if bit in ('1', 'X'):
                    address = address[:i] + bit + address[i + 1:]

            addresses = [address]

            while True:
                address = addresses.pop(0)

                if 'X' not in address:
                    addresses.append(address)
                    break

                index = address.find('X')
                addresses.append(address[:index] + '0' + address[index + 1:])
                addresses.append(address[:index] + '1' + address[index + 1:])

            for address in addresses:
                memory[address] = value

        else:
            print('VALUE ERROR')
            return 1

    print(sum(memory.values()))


if __name__ == '__main__':
    main()
