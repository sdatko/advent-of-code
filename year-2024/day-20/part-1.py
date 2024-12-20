#!/usr/bin/env python3
#
# --- Day 20: Race Condition ---
#
# The Historians are quite pixelated again. This time, a massive,
# black building looms over you - you're right outside the CPU!
#
# While The Historians get to work, a nearby program sees that you're idle
# and challenges you to a race. Apparently, you've arrived just in time
# for the frequently-held race condition festival!
#
# The race takes place on a particularly long and twisting code path;
# programs compete to see who can finish in the fewest picoseconds.
# The winner even gets their very own mutex!
#
# They hand you a map of the racetrack (your puzzle input). For example:
#
#   ###############
#   #...#...#.....#
#   #.#.#.#.#.###.#
#   #S#...#.#.#...#
#   #######.#.#.###
#   #######.#.#...#
#   #######.#.###.#
#   ###..E#...#...#
#   ###.#######.###
#   #...###...#...#
#   #.#####.#.###.#
#   #.#...#.#.#...#
#   #.#.#.#.#.#.###
#   #...#...#...###
#   ###############
#
# The map consists of track (.) - including the start (S) and end (E) positions
# (both of which also count as track) - and walls (#).
#
# When a program runs through the racetrack, it starts at the start position.
# Then, it is allowed to move up, down, left, or right; each such move takes
# 1 picosecond. The goal is to reach the end position as quickly as possible.
# In this example racetrack, the fastest time is 84 picoseconds.
#
# Because there is only a single path from the start to the end and
# the programs all go the same speed, the races used to be pretty boring.
# To make things more interesting, they introduced a new rule to the races:
# programs are allowed to cheat.
#
# The rules for cheating are very strict. Exactly once during a race,
# a program may disable collision for up to 2 picoseconds. This allows
# the program to pass through walls as if they were regular track.
# At the end of the cheat, the program must be back on normal track again;
# otherwise, it will receive a segmentation fault and get disqualified.
#
# So, a program could complete the course in 72 picoseconds (saving
# 12 picoseconds) by cheating for the two moves marked 1 and 2:
#
#   ###############
#   #...#...12....#
#   #.#.#.#.#.###.#
#   #S#...#.#.#...#
#   #######.#.#.###
#   #######.#.#...#
#   #######.#.###.#
#   ###..E#...#...#
#   ###.#######.###
#   #...###...#...#
#   #.#####.#.###.#
#   #.#...#.#.#...#
#   #.#.#.#.#.#.###
#   #...#...#...###
#   ###############
#
# Or, a program could complete the course in 64 picoseconds (saving
# 20 picoseconds) by cheating for the two moves marked 1 and 2:
#
#   ###############
#   #...#...#.....#
#   #.#.#.#.#.###.#
#   #S#...#.#.#...#
#   #######.#.#.###
#   #######.#.#...#
#   #######.#.###.#
#   ###..E#...12..#
#   ###.#######.###
#   #...###...#...#
#   #.#####.#.###.#
#   #.#...#.#.#...#
#   #.#.#.#.#.#.###
#   #...#...#...###
#   ###############
#
# This cheat saves 38 picoseconds:
#
#   ###############
#   #...#...#.....#
#   #.#.#.#.#.###.#
#   #S#...#.#.#...#
#   #######.#.#.###
#   #######.#.#...#
#   #######.#.###.#
#   ###..E#...#...#
#   ###.####1##.###
#   #...###.2.#...#
#   #.#####.#.###.#
#   #.#...#.#.#...#
#   #.#.#.#.#.#.###
#   #...#...#...###
#   ###############
#
# This cheat saves 64 picoseconds and takes the program directly to the end:
#
#   ###############
#   #...#...#.....#
#   #.#.#.#.#.###.#
#   #S#...#.#.#...#
#   #######.#.#.###
#   #######.#.#...#
#   #######.#.###.#
#   ###..21...#...#
#   ###.#######.###
#   #...###...#...#
#   #.#####.#.###.#
#   #.#...#.#.#...#
#   #.#.#.#.#.#.###
#   #...#...#...###
#   ###############
#
# Each cheat has a distinct start position (the position where the cheat
# is activated, just before the first move that is allowed to go through
# walls) and end position; cheats are uniquely identified by their start
# position and end position.
#
# In this example, the total number of cheats (grouped by the amount of time
# they save) are as follows:
# – There are 14 cheats that save 2 picoseconds.
# – There are 14 cheats that save 4 picoseconds.
# – There are 2 cheats that save 6 picoseconds.
# – There are 4 cheats that save 8 picoseconds.
# – There are 2 cheats that save 10 picoseconds.
# – There are 3 cheats that save 12 picoseconds.
# – There is one cheat that saves 20 picoseconds.
# – There is one cheat that saves 36 picoseconds.
# – There is one cheat that saves 38 picoseconds.
# – There is one cheat that saves 40 picoseconds.
# – There is one cheat that saves 64 picoseconds.
#
# You aren't sure what the conditions of the racetrack will be like,
# so to give yourself as many options as possible, you'll need a list
# of the best cheats. How many cheats would save you at least 100 picoseconds?
#
#
# --- Solution ---
#
# We start by reading the input file into the maze definition, by splittng
# the data over newlines. Next, we identify the coordinates (x, y) of start
# and goal. Then, we browse the maze using BFS algorithm – for each position
# we find the available neighbour locations and update number of steps (time)
# to reach them. In the end, we have a collection of locations and the times
# it take to reach them. Then we browse those location for possible cheats
# – the cheat can only move us from one place in the maze to another, hence
# we can reduce the area to be searched to some range around visited positions.
# The cheat only makes sense when it provides actually a benefit from it, i.e.
# it will save some time to reach the target location, compared to how much
# time it would take to get there normally; note that the cheat itself also
# takes a few steps and this impacts the total gain. For cheats that are really
# possible and beneficial we save the detailed information (source, target and
# gain). Finally, as an answer we return the total number of cheats that allows
# saving more than given minimum steps (travel time).
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

MAX_DIST = 2
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
