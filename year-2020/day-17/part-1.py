#!/usr/bin/env python3
#
# --- Day 17: Conway Cubes ---
#
# As your flight slowly drifts through the sky, the Elves at the Mythical
# Information Bureau at the North Pole contact you. They'd like some help
# debugging a malfunctioning experimental energy source aboard one of their
# super-secret imaging satellites.
#
# The experimental energy source is based on cutting-edge technology:
# a set of Conway Cubes contained in a pocket dimension! When you hear
# it's having problems, you can't help but agree to take a look.
#
# The pocket dimension contains an infinite 3-dimensional grid.
# At every integer 3-dimensional coordinate (x,y,z), there exists
# a single cube which is either active or inactive.
#
# In the initial state of the pocket dimension, almost all cubes
# start inactive. The only exception to this is a small flat region
# of cubes (your puzzle input); the cubes in this region start
# in the specified active (#) or inactive (.) state.
#
# The energy source then proceeds to boot up by executing six cycles.
#
# Each cube only ever considers its neighbors: any of the 26 other cubes
# where any of their coordinates differ by at most 1. For example,
# given the cube at x=1,y=2,z=3, its neighbors include the cube
# at x=2,y=2,z=2, the cube at x=0,y=2,z=3, and so on.
#
# During a cycle, all cubes simultaneously change their state according
# to the following rules:
#
# – If a cube is active and exactly 2 or 3 of its neighbors are also active,
#   the cube remains active. Otherwise, the cube becomes inactive.
# – If a cube is inactive but exactly 3 of its neighbors are active,
#   the cube becomes active. Otherwise, the cube remains inactive.
#
# The engineers responsible for this experimental energy source would
# like you to simulate the pocket dimension and determine what
# the configuration of cubes should be at the end of the six-cycle
# boot process.
#
# For example, consider the following initial state:
#
#   .#.
#   ..#
#   ###
#
# Even though the pocket dimension is 3-dimensional, this initial state
# represents a small 2-dimensional slice of it. (In particular, this initial
# state defines a 3x3x1 region of the 3-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following
# configurations, where the result of each cycle is shown layer-by-layer
# at each given z coordinate (and the frame of view follows the active
# cells in each cycle):
#
# Before any cycles:
#
#   z=0
#   .#.
#   ..#
#   ###
#
# After 1 cycle:
#
#   z=-1
#   #..
#   ..#
#   .#.
#
#   z=0
#   #.#
#   .##
#   .#.
#
#   z=1
#   #..
#   ..#
#   .#.
#
# After 2 cycles:
#
#   z=-2
#   .....
#   .....
#   ..#..
#   .....
#   .....
#
#   z=-1
#   ..#..
#   .#..#
#   ....#
#   .#...
#   .....
#
#   z=0
#   ##...
#   ##...
#   #....
#   ....#
#   .###.
#
#   z=1
#   ..#..
#   .#..#
#   ....#
#   .#...
#   .....
#
#   z=2
#   .....
#   .....
#   ..#..
#   .....
#   .....
#
# After 3 cycles:
#
#   z=-2
#   .......
#   .......
#   ..##...
#   ..###..
#   .......
#   .......
#   .......
#
#   z=-1
#   ..#....
#   ...#...
#   #......
#   .....##
#   .#...#.
#   ..#.#..
#   ...#...
#
#   z=0
#   ...#...
#   .......
#   #......
#   .......
#   .....##
#   .##.#..
#   ...#...
#
#   z=1
#   ..#....
#   ...#...
#   #......
#   .....##
#   .#...#.
#   ..#.#..
#   ...#...
#
#   z=2
#   .......
#   .......
#   ..##...
#   ..###..
#   .......
#   .......
#   .......
#
# After the full six-cycle boot process completes,
# 112 cubes are left in the active state.
#
# Starting with your given initial configuration, simulate six cycles.
# How many cubes are left in the active state after the sixth cycle?
#
#
# --- Solution ---
#
# The problem here is that the working space is infinite – it can extend
# of shrink depending on the data. For this, we represent only the values
# corresponding to active state in dictionary, where the keys are coordinates
# of given energy cell / cube / you-name-it. Then we can iterate over the
# space, which for us is limited to the area around cuboid spanned over all
# coordinates – meaning basically we need to get min and max values on each
# axis and iterate in range for min-1 to min+1. Then we attempt to get
# an element from our dictionary with every possible coordinate in space
# we are sweeping through. If there is active cube, we analyze its neighbors
# and deactivate it, when conditions are met, which means we delete entry
# from the dictionary. If there is inactive cube, we do the same, but instead
# we attempt to create new dictionary's entry when conditions are fulfilled.
# After the wanted amount of cycles, we can then just return the length
# of our dictionary.
#

INPUT_FILE = 'input.txt'

ACTIVE = '#'
INACTIVE = '.'


def shall_deactivate(grid, x, y, z):
    neighbors = []
    for neighbor_x in range(x - 1, x + 1 + 1):
        for neighbor_y in range(y - 1, y + 1 + 1):
            for neighbor_z in range(z - 1, z + 1 + 1):
                if not (neighbor_x == x
                        and neighbor_y == y
                        and neighbor_z == z):
                    neighbors.append(grid.get(
                        (neighbor_x, neighbor_y, neighbor_z),
                        INACTIVE
                    ))

    if 2 <= neighbors.count(ACTIVE) <= 3:
        return False
    else:
        return True


def shall_activate(grid, x, y, z):
    neighbors = []
    for neighbor_x in range(x - 1, x + 1 + 1):
        for neighbor_y in range(y - 1, y + 1 + 1):
            for neighbor_z in range(z - 1, z + 1 + 1):
                if not (neighbor_x == x
                        and neighbor_y == y
                        and neighbor_z == z):
                    neighbors.append(grid.get(
                        (neighbor_x, neighbor_y, neighbor_z),
                        INACTIVE
                    ))

    if neighbors.count(ACTIVE) == 3:
        return True
    else:
        return False


def main():
    grid = {}

    with open(INPUT_FILE, 'r') as initial_state:
        z = 0
        for y, row in enumerate(initial_state.readlines()):
            for x, state in enumerate(list(row.strip())):
                if state == '#':
                    grid[(x, y, z)] = state

    cycle = 0
    while True:
        x_values = [coords[0] for coords in grid.keys()]
        y_values = [coords[1] for coords in grid.keys()]
        z_values = [coords[2] for coords in grid.keys()]

        new_grid = dict(grid)

        for x in range(min(x_values) - 1, max(x_values) + 1 + 1):
            for y in range(min(y_values) - 1, max(y_values) + 1 + 1):
                for z in range(min(z_values) - 1, max(z_values) + 1 + 1):
                    state = grid.get((x, y, z), INACTIVE)
                    if state == ACTIVE and shall_deactivate(grid, x, y, z):
                        del new_grid[(x, y, z)]
                    elif state == INACTIVE and shall_activate(grid, x, y, z):
                        new_grid[(x, y, z)] = ACTIVE

        grid = new_grid

        cycle += 1
        if cycle == 6:
            break

    print(len(grid))


if __name__ == '__main__':
    main()
