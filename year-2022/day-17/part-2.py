#!/usr/bin/env python3
#
# --- Day 17: Pyroclastic Flow / Part Two ---
#
# The elephants are not impressed by your simulation. They demand to know
# how tall the tower will be after 1000000000000 rocks have stopped!
# Only then will they feel confident enough to proceed through the cave.
#
# In the example above, the tower would be 1514285714288 units tall!
#
# How tall will the tower be after 1000000000000 rocks have stopped?
#
#
# --- Solution ---
#
# The difference here is that we need to conduct much longer simulation.
# Unfortunately, it does scale linearly with the number of rocks to place,
# which means it would take over about 3 years until we have the result.
# The key here is to notice that as we repeat shapes and moves infinitely,
# there must be a repeating pattern in the outcome at some point. To detect
# that pattern, we need to save the information about the simulation after
# each rock placed, including the current shape ID and last movement ID,
# as well as the current layout of rocks in arena. For the last mentioned,
# the relative positions should be used, so at any level it is not depending
# on the current real height (i.e. otherwise it would always be unique).
# For some reason, multiple attempts on representing the rocks layout have
# worked fine on my real task input, but it did not work on the example input.
# What finally worked for all tested cases was the relative difference between
# all top heights in each column, so apparently that is enough.
# Having the cycle detected, we can then use modular arithmetics to predict
# what would be the height after any number of rocks placed in the future.
# It is helpful for calculations to store the history of current heights
# for each rock placed in the arena during simulation (until the cycle occurs).
#

INPUT_FILE = 'input.txt'

WIDTH = 7
HOW_MUCH_ABOVE = 3
HOW_MUCH_FROM_LEFT = 2

NUMBER_OF_ROCKS = 1_000_000_000_000


def main():
    with open(INPUT_FILE, 'r') as file:
        moves = list(file.read().strip())

    shapes = (
        ['@@@@'],
        [' @ ',
         '@@@',
         ' @ '],
        ['  @',
         '  @',
         '@@@'],
        ['@',
         '@',
         '@',
         '@'],
        ['@@',
         '@@'],
    )

    rocks = []
    history = [0]
    CACHE = dict()

    heights = [0] * WIDTH
    height = max(heights)
    movement = 0
    cut_level = 0
    rock = 0

    while rock < NUMBER_OF_ROCKS:
        # select shape
        shape = shapes[rock % len(shapes)]

        # extend the arena
        height = max(heights) + HOW_MUCH_ABOVE + len(shape)

        # spawn rock
        indices = []
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                if shape[i][j] != ' ':
                    indices.append([height - 1 - i, HOW_MUCH_FROM_LEFT + j])

        # move rock
        while True:
            move = moves[movement]
            movement = (movement + 1) % len(moves)

            # effect of wind – first case (right)
            if move == '>':
                if all(j < (WIDTH - 1) and [i, j + 1] not in rocks
                       for i, j in indices):
                    indices = [[i, j + 1] for i, j in indices]

            # effect of wind – second case (left)
            if move == '<':
                if all(j > 0 and [i, j - 1] not in rocks
                       for i, j in indices):
                    indices = [[i, j - 1] for i, j in indices]

            # attempt to move down – if possible
            if all(i > 0 and [i - 1, j] not in rocks
                   for i, j in indices):
                indices = [[i - 1, j] for i, j in indices]
                continue

            # otherwise we place the rock
            else:
                for i, j in indices:
                    if i + 1 > heights[j]:
                        heights[j] = i + 1
                rocks.extend(indices)

                # forget rocks that are not relevant anymore
                to_check = set(i for i, j in indices)
                for i in sorted(to_check):
                    if all([i, j] in rocks for j in range(WIDTH)):
                        cut_level = i
                        rocks = [[i, j] for i, j in rocks if i >= cut_level]

                break

        history.append(max(heights))
        rock += 1

        # Cycle detection
        key = (
            rock % len(shapes),  # shape ID
            (movement - 1) % len(moves),  # movement ID
            tuple(max(heights) - h for h in heights),  # state
            # tuple(h - cut_level for h in heights),  # state
            # tuple(sorted((max(heights) - i, j) for i, j in rocks)),  # state
            # tuple(sorted((i - cut_level, j) for i, j in rocks)),  # state
        )

        if key in CACHE:
            cycle_beginning, cycle_initial_height = CACHE[key]
            cycle_length = rock - cycle_beginning
            height_difference = max(heights) - cycle_initial_height

            rocks_todo = NUMBER_OF_ROCKS - rock
            cycles_todo = rocks_todo // cycle_length
            remainder = rocks_todo % cycle_length

            break  # We have everything we need for a fast forward

        else:
            CACHE[key] = (rock, max(heights))

    height = max(heights)
    height += cycles_todo * height_difference
    height += history[remainder + cycle_beginning] - cycle_initial_height

    print(height)


if __name__ == '__main__':
    main()
