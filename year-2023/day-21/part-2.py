#!/usr/bin/env python3
#
# --- Day 21: Step Counter / Part Two ---
#
# The Elf seems confused by your answer until he realizes his mistake:
# he was reading from a list of his favorite numbers that are both perfect
# squares and perfect cubes, not his step counter.
#
# The actual number of steps he needs to get today is exactly 26501365.
#
# He also points out that the garden plots and rocks are set up so
# that the map repeats infinitely in every direction.
#
# So, if you were to look one additional map-width or map-height out
# from the edge of the example map above, you would find that it keeps
# repeating:
#
# .................................
# .....###.#......###.#......###.#.
# .###.##..#..###.##..#..###.##..#.
# ..#.#...#....#.#...#....#.#...#..
# ....#.#........#.#........#.#....
# .##...####..##...####..##...####.
# .##..#...#..##..#...#..##..#...#.
# .......##.........##.........##..
# .##.#.####..##.#.####..##.#.####.
# .##..##.##..##..##.##..##..##.##.
# .................................
# .................................
# .....###.#......###.#......###.#.
# .###.##..#..###.##..#..###.##..#.
# ..#.#...#....#.#...#....#.#...#..
# ....#.#........#.#........#.#....
# .##...####..##..S####..##...####.
# .##..#...#..##..#...#..##..#...#.
# .......##.........##.........##..
# .##.#.####..##.#.####..##.#.####.
# .##..##.##..##..##.##..##..##.##.
# .................................
# .................................
# .....###.#......###.#......###.#.
# .###.##..#..###.##..#..###.##..#.
# ..#.#...#....#.#...#....#.#...#..
# ....#.#........#.#........#.#....
# .##...####..##...####..##...####.
# .##..#...#..##..#...#..##..#...#.
# .......##.........##.........##..
# .##.#.####..##.#.####..##.#.####.
# .##..##.##..##..##.##..##..##.##.
# .................................
#
# This is just a tiny three-map-by-three-map slice of the inexplicably-infinite
# farm layout; garden plots and rocks repeat as far as you can see. The Elf
# still starts on the one middle tile marked S, though - every other repeated
# S is replaced with a normal garden plot (.).
#
# Here are the number of reachable garden plots in this new infinite version
# of the example map for different numbers of steps:
#
# – In exactly 6 steps, he can still reach 16 garden plots.
# – In exactly 10 steps, he can reach any of 50 garden plots.
# – In exactly 50 steps, he can reach 1594 garden plots.
# – In exactly 100 steps, he can reach 6536 garden plots.
# – In exactly 500 steps, he can reach 167004 garden plots.
# – In exactly 1000 steps, he can reach 668697 garden plots.
# – In exactly 5000 steps, he can reach 16733044 garden plots.
#
# However, the step count the Elf needs is much larger! Starting from
# the garden plot marked S on your infinite map, how many garden plots
# could the Elf reach in exactly 26501365 steps?
#
#
# --- Solution ---
#
# The difference here is that we need to perform simulation for a much larger
# number of steps. Because the area is periodic and the number of steps is
# oddly strange number, we can expect a mathematical trick there. Cache will
# not have an effect here, since the space is infinite and constantly growing.
# However, the extrapolation seems like the right approach here. It shall be
# noticed that if there were no rocks, the pattern would grow as follows:
#                                                               O
#                                               O              O.O
#                                 O            O.O            O.O.O
#                     O          O.O          O.O.O          O.O.O.O
#           O        O.O        O.O.O        O.O.O.O        O.O.O.O.O
#   O  ->  O.O  ->  O.O.O  ->  O.O.O.O  ->  O.O.O.O.O  ->  O.O.O.O.O.O
#           O        O.O        O.O.O        O.O.O.O        O.O.O.O.O
#   1                 O          O.O          O.O.O          O.O.O.O
#           4                     O            O.O            O.O.O
#                     9                         O              O.O
#                                16                             O
#                                              25
#                                                              36
#
# The rocks disturb this pattern, but we can expect quadratic-like growth.
# The given number of steps 26501365 can be expressed as 202300 * 131 + 65,
# where 131 is the width & heigh of the grid and the 65 is the start position
# as well as the initial distance to each of the edges. This suggests that
# the repeatable observation will occur every 131 steps after first 65 steps.
# I printed the numbers of positions for 500 first iterations and performed
# a curve fit with gnuplot tool to reveal a perfect alignment for given data.
# Maybe this was just a lucky guess or the data pattern is cleverly designed
# to behave that way indeed, but as it worked for my real input – I decided
# just to implement the simple polynomial fit by solving the equation system:
#   y1 = a * x1 ** 2 + b * x1 + c,
#   y2 = a * x2 ** 2 + b * x2 + c,
#   y3 = a * x3 ** 2 + b * x3 + c,
# for a first 3 occurrences matching (step % 131) == 65, so: 65, 196 and 327.
# From this, assuming f(0) = y1, f(1) = y2, f(2) = y3 we simplify to:
#   y2 = a + b + y1,
#   y3 = 4 * a + 2 * b + y1.
# Now, solving first equation for `b` and substituting to second equation:
#   b = y2 - a - y1,
#   y3 = 2 * a + 2 * y2 - y1.
# Hence, we can calculate the value of `a` and substitute it back to `b`:
#   a = (y3 - 2 * y2 + y1) / 2,
#   b = (4 * y2 - y3 - 3 * y1) / 2.
# With this, we can calculate the number of reachable tiles for any steps
# number that matches the formula N * 131 + 65 by just calculating the value
# of `a * N ** 2 + b * N + c`.
#
# Apparently this is solution specific to the real input and it works because
# the starting position is in the middle of the grid; additionally, the middle
# row and column of the grid is empty (no rocks there), hence there is a clear
# possibility for this quadratic growth to 4 directions.
#

INPUT_FILE = 'input.txt'

ROCK = '#'
START = 'S'
STEPS = 26501365


def main():
    with open(INPUT_FILE, 'r') as file:
        grid = tuple(tuple(line)
                     for line in file.read().strip().split('\n'))

        rocks = set((x, y)
                    for y, row in enumerate(grid)
                    for x, tile in enumerate(row)
                    if tile == ROCK)

    height = len(grid)
    width = len(grid[0])

    positions = set()

    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile == START:
                positions.add((x, y))

    values = []

    for step in range(1, STEPS + 1):
        next_positions = set()

        while positions:
            (x, y) = positions.pop()

            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (nx % width, ny % height) not in rocks:
                    next_positions.add((nx, ny))

        positions = next_positions

        if step % width == width // 2:
            values.append(len(positions))

        if len(values) == 3:
            break

    # extrapolate the value for target number of steps
    y0, y1, y2 = values

    a = (y2 - 2 * y1 + y0) / 2
    b = (4 * y1 - y2 - 3 * y0) / 2
    c = y0

    n = STEPS // width

    result = int(a * n ** 2 + b * n + c)
    print(result)


if __name__ == '__main__':
    main()
