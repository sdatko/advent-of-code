#!/usr/bin/env python3
#
# --- Day 14: Parabolic Reflector Dish / Part Two ---
#
# The parabolic reflector dish deforms, but not in a way that focuses
# the beam. To do that, you'll need to move the rocks to the edges of
# the platform. Fortunately, a button on the side of the control panel
# labeled "spin cycle" attempts to do just that!
#
# Each cycle tilts the platform four times so that the rounded rocks
# roll north, then west, then south, then east. After each tilt,
# the rounded rocks roll as far as they can before the platform tilts
# in the next direction. After one cycle, the platform will have finished
# rolling the rounded rocks in those four directions in that order.
#
# Here's what happens in the example above after each of the first few cycles:
#
# – After 1 cycle:
#
#   .....#....
#   ....#...O#
#   ...OO##...
#   .OO#......
#   .....OOO#.
#   .O#...O#.#
#   ....O#....
#   ......OOOO
#   #...O###..
#   #..OO#....
#
# – After 2 cycles:
#
#   .....#....
#   ....#...O#
#   .....##...
#   ..O#......
#   .....OOO#.
#   .O#...O#.#
#   ....O#...O
#   .......OOO
#   #..OO###..
#   #.OOO#...O
#
# – After 3 cycles:
#
#   .....#....
#   ....#...O#
#   .....##...
#   ..O#......
#   .....OOO#.
#   .O#...O#.#
#   ....O#...O
#   .......OOO
#   #...O###.O
#   #.OOO#...O
#
# This process should work if you leave it running long enough, but you're
# still worried about the north support beams. To make sure they'll survive
# for a while, you need to calculate the total load on the north support
# beams after 1000000000 cycles.
#
# In the above example, after 1000000000 cycles,
# the total load on the north support beams is 64.
#
# Run the spin cycle for 1000000000 cycles. Afterward,
# what is the total load on the north support beams?
#
#
# --- Solution ---
#
# The difference here is that we need to roll the rocks to 4 sides instead of
# just 1 side (north). Moreover, we have to perform that a bilion times until
# we can deliver an answer. Because of this, the solution from previous part
# was not efficient enough. Instead, it turned out to be much faster to work
# directly on the platform map (stored as 2D array of letters here instead).
# Four helper functions were prepared that rolls all the rocks towards given
# directions (north, west, south, east); these are very similar in definition
# – the general idea is that we iterate FROM the direction where the rocks
# should roll (so e.g. for north we go from top to down, while for east we go
# from right to left) to count and identify by how many positions we can move
# every rock (e.g. when we are moving left and the platform's row look like
# this: ...#...O.O..; we can move the first rock by 3 positions left and then
# the second rock by 4 positions left, so it becomes ...#OO...... in the end).
# It is much more effective, however not yet enough for bilion iterations,
# hence a trick is involved – we can notice that eventually we start to reach
# the same arrangements over and over in a loop; after catching such situation
# where we get the same arrangement as previously observed, we can calculate
# the loop length and fast-forward the iterations by N times the loop length,
# where N is the integer of remaining cycles divided by the loop length.
# This way we jump from iteration 100-something to about 999_999_990...
#

INPUT_FILE = 'input.txt'

OBSTACLE = '#'
ROCK = 'O'
SPACE = '.'

CYCLES_TO_DO = 1_000_000_000


def roll_north(platform: list[list[str]]) -> None:
    width = len(platform[0])
    height = len(platform)

    for x in range(width):
        dy = 0

        for y in range(height):
            position = platform[y][x]

            if position == SPACE:
                dy += 1
            elif position == OBSTACLE:
                dy = 0
            elif position == ROCK:
                platform[y][x] = SPACE
                platform[y - dy][x] = ROCK


def roll_west(platform: list[list[str]]) -> None:
    width = len(platform[0])
    height = len(platform)

    for y in range(height):
        dx = 0

        for x in range(width):
            position = platform[y][x]

            if position == SPACE:
                dx += 1
            elif position == OBSTACLE:
                dx = 0
            elif position == ROCK:
                platform[y][x] = SPACE
                platform[y][x - dx] = ROCK


def roll_south(platform: list[list[str]]) -> None:
    width = len(platform[0])
    height = len(platform)

    for x in range(width):
        dy = 0

        for y in reversed(range(height)):
            position = platform[y][x]

            if position == SPACE:
                dy -= 1
            elif position == OBSTACLE:
                dy = 0
            elif position == ROCK:
                platform[y][x] = SPACE
                platform[y - dy][x] = ROCK


def roll_east(platform: list[list[str]]) -> None:
    width = len(platform[0])
    height = len(platform)

    for y in range(height):
        dx = 0

        for x in reversed(range(width)):
            position = platform[y][x]

            if position == SPACE:
                dx -= 1
            elif position == OBSTACLE:
                dx = 0
            elif position == ROCK:
                platform[y][x] = SPACE
                platform[y][x - dx] = ROCK


def calculate_load(platform: list[list[str]]) -> int:
    width = len(platform[0])
    height = len(platform)
    total_load = 0

    for x in range(width):
        for y in range(height):
            if platform[y][x] == ROCK:
                total_load += (height - y)

    return total_load


def uuid(platform: list[list[str]]) -> int:
    return hash(tuple(''.join(row) for row in platform))


def main():
    with open(INPUT_FILE, 'r') as file:
        platform = [list(line)
                    for line in file.read().strip().split('\n')]

    cycles_done = 0
    CACHE = {}

    while cycles_done < CYCLES_TO_DO:
        roll_north(platform)
        roll_west(platform)
        roll_south(platform)
        roll_east(platform)

        cycles_done += 1
        state = uuid(platform)
        total_load = calculate_load(platform)

        if state in CACHE:
            start = CACHE[state]
            length = cycles_done - start
            remaining = CYCLES_TO_DO - cycles_done

            # fast-forward
            cycles_done += (remaining // length) * length

        else:
            CACHE[state] = cycles_done

    print(total_load)


if __name__ == '__main__':
    main()
