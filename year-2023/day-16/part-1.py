#!/usr/bin/env python3
#
# --- Day 16: The Floor Will Be Lava ---
#
# With the beam of light completely focused somewhere, the reindeer leads
# you deeper still into the Lava Production Facility. At some point,
# you realize that the steel facility walls have been replaced with cave,
# and the doorways are just cave, and the floor is cave, and you're pretty
# sure this is actually just a giant cave.
#
# Finally, as you approach what must be the heart of the mountain, you see
# a bright light in a cavern up ahead. There, you discover that the beam
# of light you so carefully focused is emerging from the cavern wall
# closest to the facility and pouring all of its energy into a contraption
# on the opposite side.
#
# Upon closer inspection, the contraption appears to be a flat,
# two-dimensional square grid containing empty space (.), mirrors (/ and \),
# and splitters (| and -).
#
# The contraption is aligned so that most of the beam bounces around the grid,
# but each tile on the grid converts some of the beam's light into heat
# to melt the rock in the cavern.
#
# You note the layout of the contraption (your puzzle input). For example:
#
#   .|...\....
#   |.-.\.....
#   .....|-...
#   ........|.
#   ..........
#   .........\
#   ..../.\\..
#   .-.-/..|..
#   .|....-|.\
#   ..//.|....
#
# The beam enters in the top-left corner from the left and heading
# to the right. Then, its behavior depends on what it encounters
# as it moves:
#
# – If the beam encounters empty space (.), it continues in the same direction.
# – If the beam encounters a mirror (/ or \), the beam is reflected 90 degrees
#   depending on the angle of the mirror. For instance, a rightward-moving
#   beam that encounters a / mirror would continue upward in the mirror's
#   column, while a rightward-moving beam that encounters a \ mirror would
#   continue downward from the mirror's column.
# – If the beam encounters the pointy end of a splitter (| or -), the beam
#   passes through the splitter as if the splitter were empty space.
#   For instance, a rightward-moving beam that encounters a - splitter would
#   continue in the same direction.
# – If the beam encounters the flat side of a splitter (| or -), the beam
#   is split into two beams going in each of the two directions the splitter's
#   pointy ends are pointing. For instance, a rightward-moving beam that
#   encounters a | splitter would split into two beams: one that continues
#   upward from the splitter's column and one that continues downward from
#   the splitter's column.
#
# Beams do not interact with other beams; a tile can have many beams passing
# through it at the same time. A tile is energized if that tile has at least
# one beam pass through it, reflect in it, or split in it.
#
# In the above example, here is how the beam of light bounces around
# the contraption:
#
#   >|<<<\....
#   |v-.\^....
#   .v...|->>>
#   .v...v^.|.
#   .v...v^...
#   .v...v^..\
#   .v../2\\..
#   <->-/vv|..
#   .|<<<2-|.\
#   .v//.|.v..
#
# Beams are only shown on empty tiles; arrows indicate the direction
# of the beams. If a tile contains beams moving in multiple directions,
# the number of distinct directions is shown instead. Here is the same
# diagram but instead only showing whether a tile is energized (#) or not (.):
#
#   ######....
#   .#...#....
#   .#...#####
#   .#...##...
#   .#...##...
#   .#...##...
#   .#..####..
#   ########..
#   .#######..
#   .#...#.#..
#
# Ultimately, in this example, 46 tiles become energized.
#
# The light isn't energizing enough tiles to produce lava; to debug
# the contraption, you need to start by analyzing the current situation.
# With the beam starting in the top-left heading right, how many tiles
# end up being energized?
#
#
# --- Solution ---
#
# We start by reading the input file into a 2D grid (using a list of strings)
# by splitting the content over newlines. Then we define the starting setup,
# defining a beam at given moment using a tuple of its position and direction.
# Next process the beams in a queue using BFS algorithm (Breadth-First Search):
# we take the first element from the queue, unpack it into current position
# and direction, then we read the tile available under current position and
# register the tile as energized. Then, depending on a tile and direction,
# we add new beams to the queue. It is also important to include two stop
# conditions while processing the beams: first, if the beam position occurs
# outside of grid, we drop it; and second, if we ever reach the same position
# with the same direction, we can drop the beam, as we most likely ended in
# a loop case. Finally, after processing all possible beams, we simply count
# the number of energized tiles and return it as an answer.
#

INPUT_FILE = 'input.txt'

RIGHT = complex(1, 0)
LEFT = complex(-1, 0)
UP = complex(0, -1)
DOWN = complex(0, 1)

START = complex(0, 0)

EMPTY = '.'
FORWARD_MIRROR = '/'
BACKSLASH_MIRROR = '\\'
HORIZONTAL = '-'
VERTICAL = '|'
MIRRORS = (FORWARD_MIRROR, BACKSLASH_MIRROR)
SPLITTERS = (HORIZONTAL, VERTICAL)


def unpack(position: complex) -> tuple[int, int]:
    return int(position.real), int(position.imag)


def main():
    with open(INPUT_FILE, 'r') as file:
        grid = file.read().strip().split('\n')
        WIDTH = len(grid[0])
        HEIGHT = len(grid)

    beams = [(START, RIGHT)]
    energized = set()
    visited = set()

    while beams:
        beam = beams.pop(0)
        position, direction = beam
        x, y = unpack(position)

        if any([x < 0, y < 0, x >= WIDTH, y >= HEIGHT]):
            continue  # the beam went out of grid

        if beam in visited:
            continue  # we were already here – this is a loop

        tile = grid[y][x]
        energized.add(position)
        visited.add(beam)

        if tile == EMPTY:
            beams.append((position + direction, direction))

        elif tile in MIRRORS:
            if direction == RIGHT:
                if tile == FORWARD_MIRROR:
                    beams.append((position + UP, UP))
                else:  # tile == BACKSLASH_MIRROR
                    beams.append((position + DOWN, DOWN))

            elif direction == LEFT:
                if tile == FORWARD_MIRROR:
                    beams.append((position + DOWN, DOWN))
                else:  # tile == BACKSLASH_MIRROR
                    beams.append((position + UP, UP))

            elif direction == UP:
                if tile == FORWARD_MIRROR:
                    beams.append((position + RIGHT, RIGHT))
                else:  # tile == BACKSLASH_MIRROR
                    beams.append((position + LEFT, LEFT))

            else:  # direction == DOWN:
                if tile == FORWARD_MIRROR:
                    beams.append((position + LEFT, LEFT))
                else:  # tile == BACKSLASH_MIRROR
                    beams.append((position + RIGHT, RIGHT))

        elif tile in SPLITTERS:
            if tile == VERTICAL and direction in (LEFT, RIGHT):
                beams.append((position + UP, UP))
                beams.append((position + DOWN, DOWN))

            elif tile == HORIZONTAL and direction in (UP, DOWN):
                beams.append((position + LEFT, LEFT))
                beams.append((position + RIGHT, RIGHT))

            else:  # we just pass through
                beams.append((position + direction, direction))

        else:
            print(f'ERROR! Unexpected tile: {tile} on {x},{y}')
            exit(1)

    print(len(energized))


if __name__ == '__main__':
    main()
