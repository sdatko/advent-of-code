#!/usr/bin/env python3
#
# --- Day 4: Ceres Search ---
#
# "Looks like the Chief's not here. Next!" One of The Historians pulls out
# a device and pushes the only button on it. After a brief flash,
# you recognize the interior of the Ceres monitoring station!
#
# As the search for the Chief continues, a small Elf who lives on the station
# tugs on your shirt; she'd like to know if you could help her with her word
# search (your puzzle input). She only has to find one word: XMAS.
#
# This word search allows words to be horizontal, vertical, diagonal, written
# backwards, or even overlapping other words. It's a little unusual, though,
# as you don't merely need to find one instance of XMAS - you need to find all
# of them. Here are a few ways XMAS might appear, where irrelevant characters
# have been replaced with .:
#
#   ..X...
#   .SAMX.
#   .A..A.
#   XMAS.S
#   .X....
#
# The actual word search will be full of letters instead. For example:
#
#   MMMSXXMASM
#   MSAMXMSMSA
#   AMXSXMAAMM
#   MSAMASMSMX
#   XMASAMXAMM
#   XXAMMXXAMA
#   SMSMSASXSS
#   SAXAMASAAA
#   MAMMMXMMMM
#   MXMXAXMASX
#
# In this word search, XMAS occurs a total of 18 times; here's the same word
# search again, but where letters not involved in any XMAS have been replaced
# with .:
#
#   ....XXMAS.
#   .SAMXMS...
#   ...S..A...
#   ..A.A.MS.X
#   XMASAMX.MM
#   X.....XA.A
#   S.S.S.S.SS
#   .A.A.A.A.A
#   ..M.M.M.MM
#   .X.X.XMASX
#
# Take a look at the little Elf's word search. How many times does XMAS appear?
#
#
# --- Solution ---
#
# We start by reading the input file into a 2D grid of characters by splitting
# the input over newlines. Then we declare the helper variables – the dimension
# of the grid and the directions in which we look for the XMAS string. Then,
# we process each cell in the grid, taking all adjacent indices for each cell
# (defined in the collection of directions) and comparing the values that are
# kept in those cells. Every time we need to check if the adjacent cells we try
# to reach are in our grid boundaries. If the read value matches the wanted
# XMAS string, we update the counter of found strings. Finally, as an answer
# we print the counter value.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        grid = file.read().strip().split()

    max_x = len(grid[0])
    max_y = len(grid)

    directions = (
        ((0, 0), (1, 0), (2, 0), (3, 0)),  # left to right
        ((0, 0), (-1, 0), (-2, 0), (-3, 0)),  # right to left
        ((0, 0), (0, 1), (0, 2), (0, 3)),  # down to up
        ((0, 0), (0, -1), (0, -2), (0, -3)),  # up to down
        ((0, 0), (1, 1), (2, 2), (3, 3)),  # diagonal – top right
        ((0, 0), (-1, -1), (-2, -2), (-3, -3)),  # diagonal – bottom left
        ((0, 0), (1, -1), (2, -2), (3, -3)),  # diagonal – bottom right
        ((0, 0), (-1, 1), (-2, 2), (-3, 3)),  # diagnola – top left
    )

    times = 0

    for y in range(0, max_y):
        for x in range(0, max_x):
            for indices in directions:
                word = ''.join(
                    grid[y + ny][x + nx]
                    for (nx, ny) in indices
                    if (0 <= x + nx < max_x) and (0 <= y + ny < max_y)
                )

                if word == 'XMAS':
                    times += 1

    print(times)


if __name__ == '__main__':
    main()
