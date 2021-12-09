#!/usr/bin/env python3
#
# Task:
# Next, you need to find the largest basins so you know what areas are most
# important to avoid.
# A basin is all locations that eventually flow downward to a single low point.
# Therefore, every low point has a basin, although some basins are very small.
# Locations of height 9 do not count as being in any basin, and all other
# locations will always be part of exactly one basin.
# The size of a basin is the number of locations within the basin, including
# the low point. The example above has four basins.
# Find the three largest basins and multiply their sizes together.
# What do you get if you multiply together the sizes of the three
# largest basins?
#
# Solution:
# This part extends the previous solution, just instead of saving the height
# values we are interested in position (row and column) of the lowest points.
# Then for convenience I calculate the derivatives of matrix values along axes
# x and y (i.e. the differences between i-th and i+1-th elements).
# Worth to notice here is that zip(*heightmap) is a transposition of matrix
# in our current implementation (list of lists).
# Then we go through each lowest point we found – treating each one as the
# starting point for browsing the matrix. In each iteration, we build a list
# of adjacent positions to consider in browsing, taking only the positions
# with height values greater than the one in currently analyzed (considered)
# point. We omit positions that were already visited and the ones that have
# maximum value of height possible (9). Finally, when there are no more points
# to consider, we count and save the number of visited positions.
# For answer we find 3 highest saved numbers and multiply them.
#

INPUT_FILE = 'input.txt'


def main():
    heightmap = [list(map(int, list(characters)))
                 for line in open(INPUT_FILE, 'r')
                 for characters in line.strip().split()]

    rows = len(heightmap)
    cols = len(heightmap[0])

    low_points = []
    basins = []

    for row in range(rows):
        for col in range(cols):
            current_height = heightmap[row][col]
            adjacent_heights = [
                heightmap[row - 1][col] if row - 1 >= 0 else 9,
                heightmap[row + 1][col] if row + 1 < rows else 9,
                heightmap[row][col - 1] if col - 1 >= 0 else 9,
                heightmap[row][col + 1] if col + 1 < cols else 9,
            ]

            if all(current_height < height for height in adjacent_heights):
                low_points.append((row, col))

    derrivatives_x = [[x_ii - x_i for x_i, x_ii in zip(row[:-1], row[1:])]
                      for row in heightmap]
    derrivatives_y = [[y_ii - y_i for y_i, y_ii in zip(col[:-1], col[1:])]
                      for col in zip(*heightmap)]
    derrivatives_y = list(zip(*derrivatives_y))

    for row, col in low_points:
        visited = set()
        to_consider = [(row, col)]

        while len(to_consider) > 0:
            row, col = to_consider.pop(0)
            if (row, col) in visited:
                continue

            current_height = heightmap[row][col]
            if current_height >= 9:
                continue

            visited.add((row, col))

            if row - 1 >= 0 and derrivatives_y[row - 1][col] < 0:
                to_consider.append((row - 1, col))
            if row + 1 < rows and derrivatives_y[row][col] > 0:
                to_consider.append((row + 1, col))
            if col - 1 >= 0 and derrivatives_x[row][col - 1] < 0:
                to_consider.append((row, col - 1))
            if col + 1 < cols and derrivatives_x[row][col] > 0:
                to_consider.append((row, col + 1))

        basins.append(len(visited))

    answer = 1
    for number in sorted(basins, reverse=True)[:3]:
        answer *= number

    print(answer)


if __name__ == '__main__':
    main()
