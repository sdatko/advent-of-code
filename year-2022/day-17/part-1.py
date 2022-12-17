#!/usr/bin/env python3
#
# --- Day 17: Pyroclastic Flow ---
#
# Your handheld device has located an alternative exit from the cave for you
# and the elephants. The ground is rumbling almost continuously now, but
# the strange valves bought you some time. It's definitely getting warmer
# in here, though.
#
# The tunnels eventually open into a very tall, narrow chamber. Large,
# oddly-shaped rocks are falling into the chamber from above, presumably
# due to all the rumbling. If you can't work out where the rocks will fall
# next, you might be crushed!
#
# The five types of rocks have the following peculiar shapes, where # is rock
# and . is empty space:
#
#   ####
#
#   .#.
#   ###
#   .#.
#
#   ..#
#   ..#
#   ###
#
#   #
#   #
#   #
#   #
#
#   ##
#   ##
#
# The rocks fall in the order shown above: first the - shape, then the + shape,
# and so on. Once the end of the list is reached, the same order repeats:
# the - shape falls first, sixth, 11th, 16th, etc.
#
# The rocks don't spin, but they do get pushed around by jets of hot gas coming
# out of the walls themselves. A quick scan reveals the effect the jets of hot
# gas will have on the rocks as they fall (your puzzle input).
#
# For example, suppose this was the jet pattern in your cave:
#
#   >>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>
#
# In jet patterns, < means a push to the left, while > means a push
# to the right. The pattern above means that the jets will push a falling
# rock right, then right, then right, then left, then left, then right,
# and so on. If the end of the list is reached, it repeats.
#
# The tall, vertical chamber is exactly seven units wide. Each rock appears
# so that its left edge is two units away from the left wall and its bottom
# edge is three units above the highest rock in the room (or the floor,
# if there isn't one).
#
# After a rock appears, it alternates between being pushed by a jet of hot gas
# one unit (in the direction indicated by the next symbol in the jet pattern)
# and then falling one unit down. If any movement would cause any part
# of the rock to move into the walls, floor, or a stopped rock, the movement
# instead does not occur. If a downward movement would have caused a falling
# rock to move into the floor or an already-fallen rock, the falling rock
# stops where it is (having landed on something) and a new rock immediately
# begins falling.
#
# Drawing falling rocks with @ and stopped rocks with #, the jet pattern
# in the example above manifests as follows:
#
#   The first rock begins falling:
#   |..@@@@.|
#   |.......|
#   |.......|
#   |.......|
#   +-------+
#
#   Jet of gas pushes rock right:
#   |...@@@@|
#   |.......|
#   |.......|
#   |.......|
#   +-------+
#
#   Rock falls 1 unit:
#   |...@@@@|
#   |.......|
#   |.......|
#   +-------+
#
#   Jet of gas pushes rock right, but nothing happens:
#   |...@@@@|
#   |.......|
#   |.......|
#   +-------+
#
#   Rock falls 1 unit:
#   |...@@@@|
#   |.......|
#   +-------+
#
#   Jet of gas pushes rock right, but nothing happens:
#   |...@@@@|
#   |.......|
#   +-------+
#
#   Rock falls 1 unit:
#   |...@@@@|
#   +-------+
#
#   Jet of gas pushes rock left:
#   |..@@@@.|
#   +-------+
#
#   Rock falls 1 unit, causing it to come to rest:
#   |..####.|
#   +-------+
#
#   A new rock begins falling:
#   |...@...|
#   |..@@@..|
#   |...@...|
#   |.......|
#   |.......|
#   |.......|
#   |..####.|
#   +-------+
#
#   Jet of gas pushes rock left:
#   |..@....|
#   |.@@@...|
#   |..@....|
#   |.......|
#   |.......|
#   |.......|
#   |..####.|
#   +-------+
#
#   Rock falls 1 unit:
#   |..@....|
#   |.@@@...|
#   |..@....|
#   |.......|
#   |.......|
#   |..####.|
#   +-------+
#
#   Jet of gas pushes rock right:
#   |...@...|
#   |..@@@..|
#   |...@...|
#   |.......|
#   |.......|
#   |..####.|
#   +-------+
#
#   Rock falls 1 unit:
#   |...@...|
#   |..@@@..|
#   |...@...|
#   |.......|
#   |..####.|
#   +-------+
#
#   Jet of gas pushes rock left:
#   |..@....|
#   |.@@@...|
#   |..@....|
#   |.......|
#   |..####.|
#   +-------+
#
#   Rock falls 1 unit:
#   |..@....|
#   |.@@@...|
#   |..@....|
#   |..####.|
#   +-------+
#
#   Jet of gas pushes rock right:
#   |...@...|
#   |..@@@..|
#   |...@...|
#   |..####.|
#   +-------+
#
#   Rock falls 1 unit, causing it to come to rest:
#   |...#...|
#   |..###..|
#   |...#...|
#   |..####.|
#   +-------+
#
#   A new rock begins falling:
#   |....@..|
#   |....@..|
#   |..@@@..|
#   |.......|
#   |.......|
#   |.......|
#   |...#...|
#   |..###..|
#   |...#...|
#   |..####.|
#   +-------+
#   The moment each of the next few rocks begins falling, you would see this:
#
#   |..@....|
#   |..@....|
#   |..@....|
#   |..@....|
#   |.......|
#   |.......|
#   |.......|
#   |..#....|
#   |..#....|
#   |####...|
#   |..###..|
#   |...#...|
#   |..####.|
#   +-------+
#
#   |..@@...|
#   |..@@...|
#   |.......|
#   |.......|
#   |.......|
#   |....#..|
#   |..#.#..|
#   |..#.#..|
#   |#####..|
#   |..###..|
#   |...#...|
#   |..####.|
#   +-------+
#
#   |..@@@@.|
#   |.......|
#   |.......|
#   |.......|
#   |....##.|
#   |....##.|
#   |....#..|
#   |..#.#..|
#   |..#.#..|
#   |#####..|
#   |..###..|
#   |...#...|
#   |..####.|
#   +-------+
#
#   |...@...|
#   |..@@@..|
#   |...@...|
#   |.......|
#   |.......|
#   |.......|
#   |.####..|
#   |....##.|
#   |....##.|
#   |....#..|
#   |..#.#..|
#   |..#.#..|
#   |#####..|
#   |..###..|
#   |...#...|
#   |..####.|
#   +-------+
#
#   |....@..|
#   |....@..|
#   |..@@@..|
#   |.......|
#   |.......|
#   |.......|
#   |..#....|
#   |.###...|
#   |..#....|
#   |.####..|
#   |....##.|
#   |....##.|
#   |....#..|
#   |..#.#..|
#   |..#.#..|
#   |#####..|
#   |..###..|
#   |...#...|
#   |..####.|
#   +-------+
#
#   |..@....|
#   |..@....|
#   |..@....|
#   |..@....|
#   |.......|
#   |.......|
#   |.......|
#   |.....#.|
#   |.....#.|
#   |..####.|
#   |.###...|
#   |..#....|
#   |.####..|
#   |....##.|
#   |....##.|
#   |....#..|
#   |..#.#..|
#   |..#.#..|
#   |#####..|
#   |..###..|
#   |...#...|
#   |..####.|
#   +-------+
#
#   |..@@...|
#   |..@@...|
#   |.......|
#   |.......|
#   |.......|
#   |....#..|
#   |....#..|
#   |....##.|
#   |....##.|
#   |..####.|
#   |.###...|
#   |..#....|
#   |.####..|
#   |....##.|
#   |....##.|
#   |....#..|
#   |..#.#..|
#   |..#.#..|
#   |#####..|
#   |..###..|
#   |...#...|
#   |..####.|
#   +-------+
#
#   |..@@@@.|
#   |.......|
#   |.......|
#   |.......|
#   |....#..|
#   |....#..|
#   |....##.|
#   |##..##.|
#   |######.|
#   |.###...|
#   |..#....|
#   |.####..|
#   |....##.|
#   |....##.|
#   |....#..|
#   |..#.#..|
#   |..#.#..|
#   |#####..|
#   |..###..|
#   |...#...|
#   |..####.|
#   +-------+
#
# To prove to the elephants your simulation is accurate, they want to know
# how tall the tower will get after 2022 rocks have stopped (but before
# the 2023rd rock begins falling). In this example, the tower of rocks
# will be 3068 units tall.
#
# How many units tall will the tower of rocks be after 2022 rocks
# have stopped falling?
#
#
# --- Solution ---
#
# We start by reading the input as a list of characters, each indicating
# the wind direction (either the '<' for left move or the '>' for right move).
# Then we define available shapes. Next we begin our Tetris-like simulation,
# spawning in a loop the blocks/rocks one by one. For each rock, we do:
# – get the next shape from the list,
# – we get the Y-position for the new shape (extend the arena's height),
# – we calculate indices for the shape elements (i.e. spawn a shape in arena),
# – in a loop we move the shape until it reaches final destination.
# The movements are about shifting the shape in arena, which effectively means
# just changing all shape's indices in relation to the direction of movement.
# Every time, first we take the next element from the list of moves and shift
# the shape horizontally, then we check whether there is an available place
# under it. If so, we move the shape vertically and we continue to perform
# the next move; otherwise the shape reached its destination – we update
# the information about current heights (if any changed) and we convert
# the shape to a rock (so it becomes a new obstacle). After than, we repeat
# everything for a next shape. After a given number of rocks are placed,
# we return the reached height as an answer.
# It is worth to note that in the code below, all operations on the arena
# are not really necessary, but I needed them for visualization to verify
# all moves were conducted correctly (just print the arena in reversed order).
# Last note is that such approach worked fine, but gave the result in about
# 20 seconds. However, I was able to reduce that time greatly (to a fraction
# around a second) by reducing the number of obstacles (rocks) stored:
# every time a rock is placed, it could fill a row, creating a new floor.
# In such case we can forget all the rocks below it as not relevant anymore.
# Originally I tried to set the cut level to be the minimum of current heights,
# but it did not work well due to formations of rocks similar to following:
#
#   #####
#   #
#   #    ##
#   #######
#
# The `min(heights) - 6` worked very well and reduced the calculations time
# further, but as this appears not very generic, I dropped this idea in favor
# of detecting floors only.
#

INPUT_FILE = 'input.txt'

WIDTH = 7
HOW_MUCH_ABOVE = 3
HOW_MUCH_FROM_LEFT = 2

NUMBER_OF_ROCKS = 2022


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

    arena = []
    rocks = []

    heights = [0] * WIDTH
    movement = 0
    cut_level = 0

    for rock in range(NUMBER_OF_ROCKS):
        # select shape
        shape = shapes[rock % len(shapes)]

        # extend the arena
        height = max(heights) + HOW_MUCH_ABOVE + len(shape)
        while len(arena) < height:
            arena.append([' '] * WIDTH)
        arena = arena[:height]

        # spawn rock
        indices = []
        for i in range(len(shape)):
            for j in range(len(shape[i])):
                arena[height - 1 - i][HOW_MUCH_FROM_LEFT + j] = shape[i][j]
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
                    for i, j in reversed(indices):
                        arena[i][j] = ' '
                        arena[i][j + 1] = '@'
                    indices = [[i, j + 1] for i, j in indices]

            # effect of wind – second case (left)
            if move == '<':
                if all(j > 0 and [i, j - 1] not in rocks
                       for i, j in indices):
                    for i, j in indices:
                        arena[i][j] = ' '
                        arena[i][j - 1] = '@'
                    indices = [[i, j - 1] for i, j in indices]

            # attempt to move down – if possible
            if all(i > 0 and [i - 1, j] not in rocks
                   for i, j in indices):
                for i, j in reversed(indices):
                    arena[i][j] = ' '
                    arena[i - 1][j] = '@'
                indices = [[i - 1, j] for i, j in indices]
                continue

            # otherwise we place the rock
            else:
                for i, j in indices:
                    arena[i][j] = '#'
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

    # for row in reversed(arena):
    #     print('|', ''.join(row), '|', sep='')

    print(max(heights))


if __name__ == '__main__':
    main()
