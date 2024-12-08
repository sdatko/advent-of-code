#!/usr/bin/env python3
#
# --- Day 8: Resonant Collinearity ---
#
# You find yourselves on the roof of a top-secret Easter Bunny installation.
#
# While The Historians do their thing, you take a look at the familiar huge
# antenna. Much to your surprise, it seems to have been reconfigured to emit
# a signal that makes people 0.1% more likely to buy Easter Bunny brand
# Imitation Mediocre Chocolate as a Christmas gift! Unthinkable!
#
# Scanning across the city, you find that there are actually many such
# antennas. Each antenna is tuned to a specific frequency indicated by
# a single lowercase letter, uppercase letter, or digit. You create a map
# (your puzzle input) of these antennas. For example:
#
#   ............
#   ........0...
#   .....0......
#   .......0....
#   ....0.......
#   ......A.....
#   ............
#   ............
#   ........A...
#   .........A..
#   ............
#   ............
#
# The signal only applies its nefarious effect at specific antinodes based
# on the resonant frequencies of the antennas. In particular, an antinode
# occurs at any point that is perfectly in line with two antennas of the same
# frequency - but only when one of the antennas is twice as far away as
# the other. This means that for any pair of antennas with the same frequency,
# there are two antinodes, one on either side of them.
#
# So, for these two antennas with frequency a, they create the two antinodes
# marked with #:
#
#   ..........
#   ...#......
#   ..........
#   ....a.....
#   ..........
#   .....a....
#   ..........
#   ......#...
#   ..........
#   ..........
#
# Adding a third antenna with the same frequency creates several more
# antinodes. It would ideally add four antinodes, but two are off the right
# side of the map, so instead it adds only two:
#
#   ..........
#   ...#......
#   #.........
#   ....a.....
#   ........a.
#   .....a....
#   ..#.......
#   ......#...
#   ..........
#   ..........
#
# Antennas with different frequencies don't create antinodes; A and a
# count as different frequencies. However, antinodes can occur at locations
# that contain antennas. In this diagram, the lone antenna with frequency
# capital A creates no antinodes but has a lowercase-a-frequency antinode
# at its location:
#
#   ..........
#   ...#......
#   #.........
#   ....a.....
#   ........a.
#   .....a....
#   ..#.......
#   ......A...
#   ..........
#   ..........
#
# The first example has antennas with two different frequencies,
# so the antinodes they create look like this, plus an antinode
# overlapping the topmost A-frequency antenna:
#
#   ......#....#
#   ...#....0...
#   ....#0....#.
#   ..#....0....
#   ....0....#..
#   .#....A.....
#   ...#........
#   #......#....
#   ........A...
#   .........A..
#   ..........#.
#   ..........#.
#
# Because the topmost A-frequency antenna overlaps with a 0-frequency
# antinode, there are 14 total unique locations that contain an antinode
# within the bounds of the map.
#
# Calculate the impact of the signal. How many unique locations within
# the bounds of the map contain an antinode?
#
#
# --- Solution ---
#
# We start by reading the input file into a 2-dimensional grid, by splitting
# the data over newlines. Next, we identify all the available frequencies
# and their related antennas locations – by finding all unique characters
# in the grid (except for the dot characters, which mark empty spaces in grid)
# and then the (x, y) positions of those characters occurrences in the grid.
# Then we identify all the antinodes locations: for each available frequency,
# we consider all the available pairs of locations; for each pair of locations,
# we calculate their positions difference and the locations of antinodes
# for that pair – there is one antinode before the pair and there is one after.
# It is important to verify if each antinode is located within the mapped grid.
# Finally, as an answer we print the number of unique locations where antinodes
# were found.
#
#   --------------#-------A-------B-------#--------------------------------->
#                   A-dx    (B-A)    B+dx                               x axis
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

                # first location – before the pair
                antinode_x = location1[0] - dx
                antinode_y = location1[1] - dy

                if all((min_x <= antinode_x < max_x,
                        min_y <= antinode_y < max_y)):
                    antinodes.add((antinode_x, antinode_y))

                # second location – after the pair
                antinode_x = location2[0] + dx
                antinode_y = location2[1] + dy

                if all((min_x <= antinode_x < max_x,
                        min_y <= antinode_y < max_y)):
                    antinodes.add((antinode_x, antinode_y))

    print(len(antinodes))


if __name__ == '__main__':
    main()
