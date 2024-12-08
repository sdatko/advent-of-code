#!/usr/bin/env python3
#
# --- Day 8: Resonant Collinearity / Part Two ---
#
# Watching over your shoulder as you work, one of The Historians asks
# if you took the effects of resonant harmonics into your calculations.
#
# Whoops!
#
# After updating your model, it turns out that an antinode occurs at any
# grid position exactly in line with at least two antennas of the same
# frequency, regardless of distance. This means that some of the new antinodes
# will occur at the position of each antenna (unless that antenna is the only
# one of its frequency).
#
# So, these three T-frequency antennas now create many antinodes:
#
#   T....#....
#   ...T......
#   .T....#...
#   .........#
#   ..#.......
#   ..........
#   ...#......
#   ..........
#   ....#.....
#   ..........
#
# In fact, the three T-frequency antennas are all exactly in line with
# two antennas, so they are all also antinodes! This brings the total number
# of antinodes in the above example to 9.
#
# The original example now has 34 antinodes, including the antinodes
# that appear on every antenna:
#
#   ##....#....#
#   .#.#....0...
#   ..#.#0....#.
#   ..##...0....
#   ....0....#..
#   .#...#A....#
#   ...#..#.....
#   #....#.#....
#   ..#.....A...
#   ....#....A..
#   .#........#.
#   ...#......##
#
# Calculate the impact of the signal using this updated model.
# How many unique locations within the bounds of the map contain an antinode?
#
#
# --- Solution ---
#
# The difference in this part is that we do not consider just 2 antinodes for
# each pair, but all possible resonant resonant harmonic locations before and
# after the pair – which means that from antennas locations we consider all
# positions that can be reached with calculated positions differences (dx, dy),
# including also the original antennas locations (as B=A+dx and A=B-dx are
# antoniodes as well!).
#
#   ------#-------#-------A-------B-------#-------#-------#-------#-------#->
#           A-2dx   A-dx    (B-A)    B+dx                               x axis
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        grid = file.read().strip().split()

    min_x = 0
    min_y = 0
    max_x = len(grid[0])
    max_y = len(grid)

    frequencies = set(list(''.join(grid).replace('.', '')))
    antennas = {frequency: [] for frequency in frequencies}

    for y in range(0, max_y):
        for x in range(0, max_x):
            if grid[y][x] in antennas:
                frequency = grid[y][x]
                location = (x, y)
                antennas[frequency].append(location)

    antinodes = set()

    for frequency, locations in antennas.items():
        while locations:
            location1 = locations.pop()

            for location2 in locations:
                dx = location2[0] - location1[0]
                dy = location2[1] - location1[1]

                # all resonant harmonic locations before the pair
                antinode_x, antinode_y = location1
                while all((min_x <= antinode_x < max_x,
                           min_y <= antinode_y < max_y)):
                    antinodes.add((antinode_x, antinode_y))
                    antinode_x -= dx
                    antinode_y -= dy

                # all resonant harmonic locations after the pair
                antinode_x, antinode_y = location2
                while all((min_x <= antinode_x < max_x,
                           min_y <= antinode_y < max_y)):
                    antinodes.add((antinode_x, antinode_y))
                    antinode_x += dx
                    antinode_y += dy

    print(len(antinodes))


if __name__ == '__main__':
    main()
