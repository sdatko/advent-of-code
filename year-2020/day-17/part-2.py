#!/usr/bin/env python3
#
# --- Day 17: Conway Cubes / Part Two ---
#
# For some reason, your simulated results don't match what the experimental
# energy source engineers expected. Apparently, the pocket dimension actually
# has four spatial dimensions, not three.
#
# The pocket dimension contains an infinite 4-dimensional grid. At every
# integer 4-dimensional coordinate (x,y,z,w), there exists a single cube
# (really, a hypercube) which is still either active or inactive.
#
# Each cube only ever considers its neighbors: any of the 80 other cubes
# where any of their coordinates differ by at most 1. For example, given
# the cube at x=1,y=2,z=3,w=4, its neighbors include the cube
# at x=2,y=2,z=3,w=3, the cube at x=0,y=2,z=3,w=4, and so on.
#
# The initial state of the pocket dimension still consists of a small flat
# region of cubes. Furthermore, the same rules for cycle updating still apply:
# during each cycle, consider the number of active neighbors of each cube.
#
# For example, consider the same initial state as in the example above.
# Even though the pocket dimension is 4-dimensional, this initial state
# represents a small 2-dimensional slice of it. (In particular, this initial
# state defines a 3x3x1x1 region of the 4-dimensional space.)
#
# Simulating a few cycles from this initial state produces the following
# configurations, where the result of each cycle is shown layer-by-layer
# at each given z and w coordinate:
#
# Before any cycles:
#
#   z=0, w=0
#   .#.
#   ..#
#   ###
#
# After 1 cycle:
#
#   z=-1, w=-1
#   #..
#   ..#
#   .#.
#
#   z=0, w=-1
#   #..
#   ..#
#   .#.
#
#   z=1, w=-1
#   #..
#   ..#
#   .#.
#
#   z=-1, w=0
#   #..
#   ..#
#   .#.
#
#   z=0, w=0
#   #.#
#   .##
#   .#.
#
#   z=1, w=0
#   #..
#   ..#
#   .#.
#
#   z=-1, w=1
#   #..
#   ..#
#   .#.
#
#   z=0, w=1
#   #..
#   ..#
#   .#.
#
#   z=1, w=1
#   #..
#   ..#
#   .#.
#
# After 2 cycles:
#
#   z=-2, w=-2
#   .....
#   .....
#   ..#..
#   .....
#   .....
#
#   z=-1, w=-2
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=0, w=-2
#   ###..
#   ##.##
#   #...#
#   .#..#
#   .###.
#
#   z=1, w=-2
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=2, w=-2
#   .....
#   .....
#   ..#..
#   .....
#   .....
#
#   z=-2, w=-1
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=-1, w=-1
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=0, w=-1
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=1, w=-1
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=2, w=-1
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=-2, w=0
#   ###..
#   ##.##
#   #...#
#   .#..#
#   .###.
#
#   z=-1, w=0
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=0, w=0
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=1, w=0
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=2, w=0
#   ###..
#   ##.##
#   #...#
#   .#..#
#   .###.
#
#   z=-2, w=1
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=-1, w=1
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=0, w=1
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=1, w=1
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=2, w=1
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=-2, w=2
#   .....
#   .....
#   ..#..
#   .....
#   .....
#
#   z=-1, w=2
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=0, w=2
#   ###..
#   ##.##
#   #...#
#   .#..#
#   .###.
#
#   z=1, w=2
#   .....
#   .....
#   .....
#   .....
#   .....
#
#   z=2, w=2
#   .....
#   .....
#   ..#..
#   .....
#   .....
#
# After the full six-cycle boot process completes,
# 848 cubes are left in the active state.
#
# Starting with your given initial configuration, simulate six cycles
# in a 4-dimensional space. How many cubes are left in the active state
# after the sixth cycle?
#
#
# --- Solution ---
#
# The approach here is basically the same, we just add one more dimension w
# to the dictionary. Overall is work welly well, giving result in approximately
# 2-3 seconds. Some optimization can be done in activation and deactivation
# functions probably, but it is fine at the moment.
#

INPUT_FILE = 'input.txt'

ACTIVE = '#'
INACTIVE = '.'


def shall_deactivate(grid, x, y, z, w):
    neighbors = []
    for neighbor_x in range(x - 1, x + 1 + 1):
        for neighbor_y in range(y - 1, y + 1 + 1):
            for neighbor_z in range(z - 1, z + 1 + 1):
                for neighbor_w in range(w - 1, w + 1 + 1):
                    if not (neighbor_x == x
                            and neighbor_y == y
                            and neighbor_z == z
                            and neighbor_w == w):
                        neighbors.append(grid.get(
                            (neighbor_x, neighbor_y, neighbor_z, neighbor_w),
                            INACTIVE
                        ))

    if 2 <= neighbors.count(ACTIVE) <= 3:
        return False
    else:
        return True


def shall_activate(grid, x, y, z, w):
    neighbors = []
    for neighbor_x in range(x - 1, x + 1 + 1):
        for neighbor_y in range(y - 1, y + 1 + 1):
            for neighbor_z in range(z - 1, z + 1 + 1):
                for neighbor_w in range(w - 1, w + 1 + 1):
                    if not (neighbor_x == x
                            and neighbor_y == y
                            and neighbor_z == z
                            and neighbor_w == w):
                        neighbors.append(grid.get(
                            (neighbor_x, neighbor_y, neighbor_z, neighbor_w),
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
        w = 0
        for y, row in enumerate(initial_state.readlines()):
            for x, state in enumerate(list(row.strip())):
                if state == '#':
                    grid[(x, y, z, w)] = state

    cycle = 0
    while True:
        x_values = [coords[0] for coords in grid.keys()]
        y_values = [coords[1] for coords in grid.keys()]
        z_values = [coords[2] for coords in grid.keys()]
        w_values = [coords[3] for coords in grid.keys()]

        new_grid = dict(grid)

        for x in range(min(x_values) - 1, max(x_values) + 1 + 1):
            for y in range(min(y_values) - 1, max(y_values) + 1 + 1):
                for z in range(min(z_values) - 1, max(z_values) + 1 + 1):
                    for w in range(min(w_values) - 1, max(w_values) + 1 + 1):
                        state = grid.get((x, y, z, w), INACTIVE)
                        if state == ACTIVE and shall_deactivate(grid,
                                                                x, y, z, w):
                            del new_grid[(x, y, z, w)]
                        elif state == INACTIVE and shall_activate(grid,
                                                                  x, y, z, w):
                            new_grid[(x, y, z, w)] = ACTIVE

        grid = new_grid

        cycle += 1
        if cycle == 6:
            break

    print(len(grid))


if __name__ == '__main__':
    main()
