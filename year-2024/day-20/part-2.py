#!/usr/bin/env python3
#
# --- Day 20: Race Condition / Part Two ---
#
# The programs seem perplexed by your list of cheats. Apparently,
# the two-picosecond cheating rule was deprecated several milliseconds ago!
# The latest version of the cheating rule permits a single cheat that
# instead lasts at most 20 picoseconds.
#
# Now, in addition to all the cheats that were possible in just two
# picoseconds, many more cheats are possible. This six-picosecond
# cheat saves 76 picoseconds:
#
#   ###############
#   #...#...#.....#
#   #.#.#.#.#.###.#
#   #S#...#.#.#...#
#   #1#####.#.#.###
#   #2#####.#.#...#
#   #3#####.#.###.#
#   #456.E#...#...#
#   ###.#######.###
#   #...###...#...#
#   #.#####.#.###.#
#   #.#...#.#.#...#
#   #.#.#.#.#.#.###
#   #...#...#...###
#   ###############
#
# Because this cheat has the same start and end positions
# as the one above, it's the same cheat, even though the path
# taken during the cheat is different:
#
#   ###############
#   #...#...#.....#
#   #.#.#.#.#.###.#
#   #S12..#.#.#...#
#   ###3###.#.#.###
#   ###4###.#.#...#
#   ###5###.#.###.#
#   ###6.E#...#...#
#   ###.#######.###
#   #...###...#...#
#   #.#####.#.###.#
#   #.#...#.#.#...#
#   #.#.#.#.#.#.###
#   #...#...#...###
#   ###############
#
# Cheats don't need to use all 20 picoseconds; cheats can last any amount
# of time up to and including 20 picoseconds (but can still only end when
# the program is on normal track). Any cheat time not used is lost;
# it can't be saved for another cheat later.
#
# You'll still need a list of the best cheats, but now there are even more
# to choose between. Here are the quantities of cheats in this example that
# save 50 picoseconds or more:
# – There are 32 cheats that save 50 picoseconds.
# – There are 31 cheats that save 52 picoseconds.
# – There are 29 cheats that save 54 picoseconds.
# – There are 39 cheats that save 56 picoseconds.
# – There are 25 cheats that save 58 picoseconds.
# – There are 23 cheats that save 60 picoseconds.
# – There are 20 cheats that save 62 picoseconds.
# – There are 19 cheats that save 64 picoseconds.
# – There are 12 cheats that save 66 picoseconds.
# – There are 14 cheats that save 68 picoseconds.
# – There are 12 cheats that save 70 picoseconds.
# – There are 22 cheats that save 72 picoseconds.
# – There are 4 cheats that save 74 picoseconds.
# – There are 3 cheats that save 76 picoseconds.
#
# Find the best cheats using the updated cheating rules.
# How many cheats would save you at least 100 picoseconds?
#
#
# --- Solution ---
#
# The difference in this part is that we need to consider cheats that can
# take us farther na 2 positions. After cleanups and optiomization of code
# from previous part, the only change actually needed was to change the value
# of MAX_DIST parameter.
#

INPUT_FILE = 'input.txt'

START = 'S'
END = 'E'
WALL = '#'

MOVES = {
    'right': (1, 0),
    'left': (-1, 0),
    'down': (0, 1),
    'up': (0, -1),
}

MAX_DIST = 20
MIN_GAIN = 100


def main():
    with open(INPUT_FILE, 'r') as file:
        maze = tuple(file.read().strip().split())

    start = (0, 0)
    end = (0, 0)

    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            if tile == START:
                start = (x, y)
            if tile == END:
                end = (x, y)

    queue = [(0, start)]  # time, (position)
    visited = dict()

    while queue:
        time, (x, y) = queue.pop(0)

        if (x, y) in visited:  # we were already here with a lower score
            continue

        visited[(x, y)] = time

        if (x, y) == end:
            break

        for (dx, dy) in MOVES.values():
            nx = x + dx
            ny = y + dy

            if maze[ny][nx] == WALL:
                continue  # do not hit the wall

            if (nx, ny) in visited:
                continue  # ignore where we already were

            queue.append((time + 1, (nx, ny)))

    cheats = dict()

    for (x1, y1) in visited.keys():
        for dx in range(-MAX_DIST, MAX_DIST + 1):
            for dy in range(-MAX_DIST + abs(dx), MAX_DIST + 1 - abs(dx)):
                x2 = x1 + dx
                y2 = y1 + dy

                if (x2, y2) not in visited:
                    continue

                gain = visited[(x2, y2)] - visited[(x1, y1)]
                gain -= (abs(dx) + abs(dy))

                if gain > 1:
                    cheats[(x1, y1, x2, y2)] = gain

    print(sum(1 for cheat in cheats.values() if cheat >= MIN_GAIN))


if __name__ == '__main__':
    main()
