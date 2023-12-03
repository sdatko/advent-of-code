#!/usr/bin/env python3
#
# --- Day 3: Gear Ratios ---
#
# You and the Elf eventually reach a gondola lift station; he says
# the gondola lift will take you up to the water source, but this is
# as far as he can bring you. You go inside.
#
# It doesn't take long to find the gondolas, but there seems to be
# a problem: they're not moving.
#
# "Aaah!"
#
# You turn around to see a slightly-greasy Elf with a wrench and a look
# of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't
# working right now; it'll still be a while before I can fix it."
# You offer to help.
#
# The engineer explains that an engine buffer seems to be missing from
# the engine, but nobody can figure out which one. If you can add up
# all the buffer numbers in the engine schematic, it should be easy
# to work out which buffer is missing.
#
# The engine schematic (your puzzle input) consists of a visual representation
# of the engine. There are lots of numbers and symbols you don't really
# understand, but apparently any number adjacent to a symbol, even diagonally,
# is a "buffer number" and should be included in your sum.
# (Periods (.) do not count as a symbol.)
#
# Here is an example engine schematic:
#
#   467..114..
#   ...*......
#   ..35..633.
#   ......#...
#   617*......
#   .....+.58.
#   ..592.....
#   ......755.
#   ...$.*....
#   .664.598..
#
# In this schematic, two numbers are not buffer numbers because they are not
# adjacent to a symbol: 114 (top right) and 58 (middle right). Every other
# number is adjacent to a symbol and so is a buffer number; their sum is 4361.
#
# Of course, the actual engine schematic is much larger. What is the sum
# of all of the buffer numbers in the engine schematic?
#
#
# --- Solution ---
#
# We read the input file into a list of string, which can be conveniently
# browsed like a map (2D array) in Python. From the map we determine max X
# and max Y values, as well as all the symbols other than digits and dots.
# Then we process the map line by line (row), position by position (column).
# For each position, if there is a digit, we construct a number in a variable,
# additionally checking if there is one of symbols around the current position
# – if so, then the number currently under construction would be a valid part.
# If on a current position we encounter a character other than digit, then
# we store the currently constructed number as part (provided that it is valid)
# and we reset our construction buffer. We also need to reset current buffer
# after each row processing (storing the valid part first, if there is such).
# Finally, we return the sum of all recorded parts.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        scheme = file.read().strip().split('\n')

    MIN_X = 0
    MIN_Y = 0
    MAX_Y = len(scheme) - 1
    MAX_X = len(scheme[0]) - 1
    SYMBOLS = set(x for x in ''.join(scheme) if not x.isdigit() and x != '.')

    parts = []
    buffer = ''
    valid = False

    for y, row in enumerate(scheme):
        for x, character in enumerate(row):
            if character.isdigit():
                buffer += character

                # check if character is adjacent to a symbol
                if y > MIN_Y:
                    if x > MIN_X and scheme[y - 1][x - 1] in SYMBOLS:
                        valid = True
                    if scheme[y - 1][x] in SYMBOLS:
                        valid = True
                    if x < MAX_X and scheme[y - 1][x + 1] in SYMBOLS:
                        valid = True
                if x > MIN_X and scheme[y][x - 1] in SYMBOLS:
                    valid = True
                if x < MAX_X and scheme[y][x + 1] in SYMBOLS:
                    valid = True
                if y < MAX_Y:
                    if x > MIN_X and scheme[y + 1][x - 1] in SYMBOLS:
                        valid = True
                    if scheme[y + 1][x] in SYMBOLS:
                        valid = True
                    if x < MAX_X and scheme[y + 1][x + 1] in SYMBOLS:
                        valid = True

            else:  # dot or other symbol
                if buffer and valid:
                    parts.append(int(buffer))
                buffer = ''
                valid = False

        # end of row
        if buffer and valid:
            parts.append(int(buffer))
        buffer = ''
        valid = False

    print(sum(parts))


if __name__ == '__main__':
    main()
