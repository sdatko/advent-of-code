#!/usr/bin/env python3
#
# --- Day 3: Toboggan Trajectory ---
#
# With the toboggan login problems resolved, you set off toward the airport.
# While travel by toboggan might be easy, it's certainly not safe: there's
# very minimal steering and the area is covered in trees. You'll need to see
# which angles will take you near the fewest trees.
#
# Due to the local geology, trees in this area only grow on exact integer
# coordinates in a grid. You make a map (your puzzle input) of the open
# squares (.) and trees (#) you can see. For example:
#
#   ..##.......
#   #...#...#..
#   .#....#..#.
#   ..#.#...#.#
#   .#...##..#.
#   ..#.##.....
#   .#.#.#....#
#   .#........#
#   #.##...#...
#   #...##....#
#   .#..#...#.#
#
# These aren't the only trees, though; due to something you read about once
# involving arboreal genetics and biome stability, the same pattern repeats
# to the right many times:
#
#   ..##.........##.........##.........##.........##.........##.......  --->
#   #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
#   .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
#   ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
#   .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
#   ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
#   .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
#   .#........#.#........#.#........#.#........#.#........#.#........#
#   #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#   #...##....##...##....##...##....##...##....##...##....##...##....#
#   .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# You start on the open square (.) in the top-left corner and need to reach
# the bottom (below the bottom-most row on your map).
#
# The toboggan can only follow a few specific slopes (you opted for a cheaper
# model that prefers rational numbers); start by counting all the trees
# you would encounter for the slope right 3, down 1:
#
# From your starting position at the top-left, check the position that
# is right 3 and down 1. Then, check the position that is right 3 and down 1
# from there, and so on until you go past the bottom of the map.
#
# The locations you'd check in the above example are marked here with O where
# there was an open square and X where there was a tree:
#
#   ..##.........##.........##.........##.........##.........##.......  --->
#   #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
#   .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
#   ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
#   .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
#   ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
#   .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
#   .#........#.#........X.#........#.#........#.#........#.#........#
#   #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#   #...##....##...##....##...#X....##...##....##...##....##...##....#
#   .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# In this example, traversing the map using this slope would cause you
# to encounter 7 trees.
#
# Starting at the top-left corner of your map and following a slope
# of right 3 and down 1, how many trees would you encounter?
#
#
# --- Solution ---
#
# We simply interpret the input file as a grid with periodic boundaries.
# After each step in the grid (with modulo) we check what is the current
# symbol at given position. If it is #, we add one.
#

INPUT_FILE = 'input.txt'
TREE = '#'

MOVE_X = 3
MOVE_Y = 1


def main():
    grid = [line.strip('\n') for line in open(INPUT_FILE, 'r')]

    trees = 0

    pos_x = 0
    pos_y = 0

    size_x = len(grid[0])
    size_y = len(grid)

    while pos_y != (size_y - 1):
        pos_x += MOVE_X
        pos_x %= size_x
        pos_y += MOVE_Y

        if grid[pos_y][pos_x] == TREE:
            trees += 1

    print(trees)


if __name__ == '__main__':
    main()
