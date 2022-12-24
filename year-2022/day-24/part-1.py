#!/usr/bin/env python3
#
# --- Day 24: Blizzard Basin ---
#
# With everything replanted for next year (and with elephants and monkeys
# to tend the grove), you and the Elves leave for the extraction point.
#
# Partway up the mountain that shields the grove is a flat, open area that
# serves as the extraction point. It's a bit of a climb, but nothing
# the expedition can't handle.
#
# At least, that would normally be true; now that the mountain is covered
# in snow, things have become more difficult than the Elves are used to.
#
# As the expedition reaches a valley that must be traversed to reach
# the extraction site, you find that strong, turbulent winds are pushing
# small blizzards of snow and sharp ice around the valley. It's a good thing
# everyone packed warm clothes! To make it across safely, you'll need to find
# a way to avoid them.
#
# Fortunately, it's easy to see all of this from the entrance to the valley,
# so you make a map of the valley and the blizzards (your puzzle input).
# For example:
#
#   #.#####
#   #.....#
#   #>....#
#   #.....#
#   #...v.#
#   #.....#
#   #####.#
#
# The walls of the valley are drawn as #; everything else is ground.
# Clear ground - where there is currently no blizzard - is drawn as `.`.
# Otherwise, blizzards are drawn with an arrow indicating their direction
# of motion: up (^), down (v), left (<), or right (>).
#
# The above map includes two blizzards, one moving right (>) and one moving
# down (v). In one minute, each blizzard moves one position in the direction
# it is pointing:
#
#   #.#####
#   #.....#
#   #.>...#
#   #.....#
#   #.....#
#   #...v.#
#   #####.#
#
# Due to conservation of blizzard energy, as a blizzard reaches the wall
# of the valley, a new blizzard forms on the opposite side of the valley
# moving in the same direction. After another minute, the bottom downward
# -moving blizzard has been replaced with a new downward-moving blizzard
# at the top of the valley instead:
#
#   #.#####
#   #...v.#
#   #..>..#
#   #.....#
#   #.....#
#   #.....#
#   #####.#
#
# Because blizzards are made of tiny snowflakes, they pass right through
# each other. After another minute, both blizzards temporarily occupy
# the same position, marked 2:
#
#   #.#####
#   #.....#
#   #...2.#
#   #.....#
#   #.....#
#   #.....#
#   #####.#
#
# After another minute, the situation resolves itself, giving each blizzard
# back its personal space:
#
#   #.#####
#   #.....#
#   #....>#
#   #...v.#
#   #.....#
#   #.....#
#   #####.#
#
# Finally, after yet another minute, the rightward-facing blizzard on the right
# is replaced with a new one on the left facing the same direction:
#
#   #.#####
#   #.....#
#   #>....#
#   #.....#
#   #...v.#
#   #.....#
#   #####.#
#
# This process repeats at least as long as you are observing it,
# but probably forever.
#
# Here is a more complex example:
#
#   #.######
#   #>>.<^<#
#   #.<..<<#
#   #>v.><>#
#   #<^v^^>#
#   ######.#
#
# Your expedition begins in the only non-wall position in the top row and
# needs to reach the only non-wall position in the bottom row. On each minute,
# you can move up, down, left, or right, or you can wait in place.
# You and the blizzards act simultaneously, and you cannot share
# a position with a blizzard.
#
# In the above example, the fastest way to reach your goal requires 18 steps.
# Drawing the position of the expedition as E, one way to achieve this is:
#
#   Initial state:
#   #E######
#   #>>.<^<#
#   #.<..<<#
#   #>v.><>#
#   #<^v^^>#
#   ######.#
#
#   Minute 1, move down:
#   #.######
#   #E>3.<.#
#   #<..<<.#
#   #>2.22.#
#   #>v..^<#
#   ######.#
#
#   Minute 2, move down:
#   #.######
#   #.2>2..#
#   #E^22^<#
#   #.>2.^>#
#   #.>..<.#
#   ######.#
#
#   Minute 3, wait:
#   #.######
#   #<^<22.#
#   #E2<.2.#
#   #><2>..#
#   #..><..#
#   ######.#
#
#   Minute 4, move up:
#   #.######
#   #E<..22#
#   #<<.<..#
#   #<2.>>.#
#   #.^22^.#
#   ######.#
#
#   Minute 5, move right:
#   #.######
#   #2Ev.<>#
#   #<.<..<#
#   #.^>^22#
#   #.2..2.#
#   ######.#
#
#   Minute 6, move right:
#   #.######
#   #>2E<.<#
#   #.2v^2<#
#   #>..>2>#
#   #<....>#
#   ######.#
#
#   Minute 7, move down:
#   #.######
#   #.22^2.#
#   #<vE<2.#
#   #>>v<>.#
#   #>....<#
#   ######.#
#
#   Minute 8, move left:
#   #.######
#   #.<>2^.#
#   #.E<<.<#
#   #.22..>#
#   #.2v^2.#
#   ######.#
#
#   Minute 9, move up:
#   #.######
#   #<E2>>.#
#   #.<<.<.#
#   #>2>2^.#
#   #.v><^.#
#   ######.#
#
#   Minute 10, move right:
#   #.######
#   #.2E.>2#
#   #<2v2^.#
#   #<>.>2.#
#   #..<>..#
#   ######.#
#
#   Minute 11, wait:
#   #.######
#   #2^E^2>#
#   #<v<.^<#
#   #..2.>2#
#   #.<..>.#
#   ######.#
#
#   Minute 12, move down:
#   #.######
#   #>>.<^<#
#   #.<E.<<#
#   #>v.><>#
#   #<^v^^>#
#   ######.#
#
#   Minute 13, move down:
#   #.######
#   #.>3.<.#
#   #<..<<.#
#   #>2E22.#
#   #>v..^<#
#   ######.#
#
#   Minute 14, move right:
#   #.######
#   #.2>2..#
#   #.^22^<#
#   #.>2E^>#
#   #.>..<.#
#   ######.#
#
#   Minute 15, move right:
#   #.######
#   #<^<22.#
#   #.2<.2.#
#   #><2>E.#
#   #..><..#
#   ######.#
#
#   Minute 16, move right:
#   #.######
#   #.<..22#
#   #<<.<..#
#   #<2.>>E#
#   #.^22^.#
#   ######.#
#
#   Minute 17, move down:
#   #.######
#   #2.v.<>#
#   #<.<..<#
#   #.^>^22#
#   #.2..2E#
#   ######.#
#
#   Minute 18, move down:
#   #.######
#   #>2.<.<#
#   #.2v^2<#
#   #>..>2>#
#   #<....>#
#   ######E#
#
# What is the fewest number of minutes required to avoid the blizzards
# and reach the goal?
#
#
# --- Solution ---
#
# We start by reading the input as a matrix of wind positions, by splitting
# the file over newlines and then each line by characters that describe the
# simulated arena. The winds are basically a movable walls that blocks some
# places in labyrinth, but they can share the same position and we still need
# to preserve information about direction of their movements in such case.
# Because of that, a bit-based encoding of arena and wind directions was used:
# – 0: free tile,
# – 1: wind up (^),
# – 2: wind down (v),
# – 4: wind left (<),
# – 8: wind right (>),
# – 16: static wall.
# This allows us to detect obstacles in each cell with a bit-wise AND operator.
# Having the arena represented as a 2-dimensional array of integers, we can
# start finding the shortest path through the maze. Starting from a given
# position, in a loop, as long as we did not reach the goal yet, we perform
# the following actions:
# – we calculate the new layout of arena, by moving each wind into a new place,
# – we find a new set of reachable positions, taking into account all currently
#   reachable positions.
# In essence this is a classical BFS algorithm (breadth-first search) that
# works, as in every outer loop iteration we check the movements for the same
# unit of time (i.e. arena/wind states). Note that we do not keep tracking
# of exact path history here, as it is not relevant for the task.
# The defined border of static walls in the input file provides a convenient
# protection for out of bounds exceptions, as with assumed encoding we can
# simply check whether a considered move (up, down, left, right) leads to
# an empty grid cell (i.e. its value is equal to zero). This way we will never
# exceed the maximum index (there is one potential place where this can happen
# – near the goal/exit position, but as we break as soon as we reach it,
# the problem does not occur here).
# Finally as an answer we return the number of loop iterations that were run
# before we reached the goal.
#

INPUT_FILE = 'input.txt'


def deepcopy(deeplist):
    new_list = []
    for row in deeplist:
        new_list.append(row.copy())
    return new_list


def main():
    with open(INPUT_FILE, 'r') as file:
        grid = [list(map(int, row.strip().split()))
                for row in file.read()
                               .replace('.', '0 ')
                               .replace('^', '1 ')
                               .replace('v', '2 ')
                               .replace('<', '4 ')
                               .replace('>', '8 ')
                               .replace('#', '16 ')
                               .strip()
                               .split('\n')]

    clean_grid = deepcopy(grid)
    for y, row in enumerate(grid[1:-1], start=1):
        for x, tile in enumerate(row[1:-1], start=1):
            clean_grid[y][x] = 0

    min_x = 1
    min_y = 1
    max_x = len(grid[0]) - 2
    max_y = len(grid) - 2

    start = (0, grid[0].index(0))
    goal = (len(grid) - 1, grid[-1].index(0))

    reached_positions = {start}
    time = 0

    while goal not in reached_positions:
        time += 1

        # move winds
        new_grid = deepcopy(clean_grid)

        for y, row in enumerate(grid[1:-1], start=1):
            for x, tile in enumerate(row[1:-1], start=1):
                # up
                if grid[y][x] & 1:
                    if y > min_y:
                        ny = y - 1
                    else:
                        ny = max_y
                    new_grid[ny][x] += 1

                # down
                if grid[y][x] & 2:
                    if y < max_y:
                        ny = y + 1
                    else:
                        ny = min_y
                    new_grid[ny][x] += 2

                # left
                if grid[y][x] & 4:
                    if x > min_x:
                        nx = x - 1
                    else:
                        nx = max_x
                    new_grid[y][nx] += 4

                # right
                if grid[y][x] & 8:
                    if x < max_x:
                        nx = x + 1
                    else:
                        nx = min_y
                    new_grid[y][nx] += 8

        grid = new_grid

        # find reachable positions
        new_positions = set()

        for y, x in reached_positions:
            for ny, nx in ((y - 1, x),  # up
                           (y + 1, x),  # down
                           (y, x - 1),  # left
                           (y, x + 1),  # right
                           (y, x)):  # wait in place
                if new_grid[ny][nx] != 0:
                    continue

                new_positions.add((ny, nx))

        reached_positions = new_positions

    print(time)


if __name__ == '__main__':
    main()
