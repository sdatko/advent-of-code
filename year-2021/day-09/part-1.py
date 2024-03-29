#!/usr/bin/env python3
#
# --- Day 9: Smoke Basin ---
#
# These caves seem to be lava tubes. Parts are even still volcanically active;
# small hydrothermal vents release smoke into the caves that slowly settles
# like rain.
#
# If you can model how the smoke flows through the caves, you might be able
# to avoid it and be that much safer. The submarine generates a heightmap
# of the floor of the nearby caves for you (your puzzle input).
#
# Smoke flows to the lowest point of the area it's in.
# For example, consider the following heightmap:
#   2199943210
#   3987894921
#   9856789892
#   8767896789
#   9899965678
#
# Each number corresponds to the height of a particular location, where 9
# is the highest and 0 is the lowest a location can be.
#
# Your first goal is to find the low points - the locations that are lower than
# any of its adjacent locations. Most locations have four adjacent locations
# (up, down, left, and right); locations on the edge or corner of the map have
# three or two adjacent locations, respectively.
# (Diagonal locations do not count as adjacent.)
#
# In the above example, there are four low points, all highlighted: two are
# in the first row (a 1 and a 0), one is in the third row (a 5), and one is
# in the bottom row (also a 5). All other locations on the heightmap have some
# lower adjacent location, and so are not low points.
#
# The risk level of a low point is 1 plus its height. In the above example,
# the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk
# levels of all low points in the heightmap is therefore 15.
#
# Find all of the low points on your heightmap. What is the sum of the risk
# levels of all low points on your heightmap?
#
#
# --- Solution ---
#
# We start by reading input file as a matrix (i.e. list of lists) of integers.
# Then we browse through each row and column in the matrix, reading the current
# height and comparing it with adjacent values. When value for current position
# is lower than all adjacent ones, we add the current height value to list.
# Final answer is the sum of saved values and the number of them.
#

INPUT_FILE = 'input.txt'


def main():
    heightmap = [list(map(int, list(characters)))
                 for line in open(INPUT_FILE, 'r')
                 for characters in line.strip().split()]

    rows = len(heightmap)
    cols = len(heightmap[0])

    low_points = []

    for row in range(rows):
        for col in range(cols):
            current_height = heightmap[row][col]
            adjacent_heights = []
            if row - 1 >= 0:
                adjacent_heights.append(heightmap[row - 1][col])
            if row + 1 < rows:
                adjacent_heights.append(heightmap[row + 1][col])
            if col - 1 >= 0:
                adjacent_heights.append(heightmap[row][col - 1])
            if col + 1 < cols:
                adjacent_heights.append(heightmap[row][col + 1])

            if all(current_height < height for height in adjacent_heights):
                low_points.append(current_height)

    risk_level = sum(low_points) + len(low_points)

    print(risk_level)


if __name__ == '__main__':
    main()
