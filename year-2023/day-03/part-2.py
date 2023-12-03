#!/usr/bin/env python3
#
# --- Day 3: Gear Ratios / Part Two ---
#
# The engineer finds the missing buffer and installs it in the engine!
# As the engine springs to life, you jump in the closest gondola,
# finally ready to ascend to the water source.
#
# You don't seem to be going very fast, though. Maybe something is still wrong?
# Fortunately, the gondola has a phone labeled "help", so you pick it up and
# the engineer answers.
#
# Before you can explain the situation, she suggests that you look out
# the window. There stands the engineer, holding a phone in one hand
# and waving with the other. You're going so slowly that you haven't
# even left the station. You exit the gondola.
#
# The missing buffer wasn't the only issue - one of the gears
# in the engine is wrong. A gear is any * symbol that is adjacent
# to exactly two buffer numbers. Its gear ratio is the result of multiplying
# those two numbers together.
#
# This time, you need to find the gear ratio of every gear and add them all up
# so that the engineer can figure out which gear needs to be replaced.
#
# Consider the same engine schematic again:
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
# In this schematic, there are two gears. The first is in the top left;
# it has buffer numbers 467 and 35, so its gear ratio is 16345. The second gear
# is in the lower right; its gear ratio is 451490. (The * adjacent to 617
# is not a gear because it is only adjacent to one buffer number.)
# Adding up all of the gear ratios produces 467835.
#
# What is the sum of all of the gear ratios in your engine schematic?
#
#
# --- Solution ---
#
# The difference here is that we only consider parts that are placed adjacent
# to the asterisks (*). Instead of storing the parts in a list, we register
# them in a dictionary, where the keys are indexes of asterisks that made
# the parts as valid. At the end, we iterate over that dictionary and identify
# which are our valid gears (consisting of exactly two parts) to calculate
# the ratios. Finally, we return the sum of calculated ratios.
#
# Alternative, obvious approach would involve finding all the asterisks first
# and then identifying the numbers adjacent to these asterisks, however that
# would require major rewrite of previous code, so I did not implement it.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        scheme = file.read().strip().split('\n')

    MIN_X = 0
    MIN_Y = 0
    MAX_Y = len(scheme) - 1
    MAX_X = len(scheme[0]) - 1
    SYMBOLS = set('*')

    buffer = ''
    indexes = set()
    gears_candidates = {}
    ratios = []

    for y, row in enumerate(scheme):
        for x, character in enumerate(row):
            if character.isdigit():
                buffer += character

                # check if character is adjacent to a symbol
                if y > MIN_Y:
                    if x > MIN_X and scheme[y - 1][x - 1] in SYMBOLS:
                        indexes.add((y - 1, x - 1))
                    if scheme[y - 1][x] in SYMBOLS:
                        indexes.add((y - 1, x))
                    if x < MAX_X and scheme[y - 1][x + 1] in SYMBOLS:
                        indexes.add((y - 1, x + 1))
                if x > MIN_X and scheme[y][x - 1] in SYMBOLS:
                    indexes.add((y, x - 1))
                if x < MAX_X and scheme[y][x + 1] in SYMBOLS:
                    indexes.add((y, x + 1))
                if y < MAX_Y:
                    if x > MIN_X and scheme[y + 1][x - 1] in SYMBOLS:
                        indexes.add((y + 1, x - 1))
                    if scheme[y + 1][x] in SYMBOLS:
                        indexes.add((y + 1, x))
                    if x < MAX_X and scheme[y + 1][x + 1] in SYMBOLS:
                        indexes.add((y + 1, x + 1))

            else:  # dot or other symbol
                if buffer and indexes:
                    for index in indexes:
                        if index not in gears_candidates:
                            gears_candidates[index] = []
                        gears_candidates[index].append(int(buffer))
                buffer = ''
                indexes.clear()

        # end of row
        if buffer and indexes:
            for index in indexes:
                if index not in gears_candidates:
                    gears_candidates[index] = []
                gears_candidates[index].append(int(buffer))
        buffer = ''
        indexes.clear()

    # calculate ratio where there are exactly two gears
    for index, gears in gears_candidates.items():
        if len(gears) == 2:
            ratio = gears[0] * gears[1]
            ratios.append(ratio)

    print(sum(ratios))


if __name__ == '__main__':
    main()
