#!/usr/bin/env python3
#
# --- Day 16: The Floor Will Be Lava / Part Two ---
#
# As you try to work out what might be wrong, the reindeer tugs on your shirt
# and leads you to a nearby control panel. There, a collection of buttons lets
# you align the contraption so that the beam enters from any edge tile and
# heading away from that edge. (You can choose either of two directions for
# the beam if it starts on a corner; for instance, if the beam starts
# in the bottom-right corner, it can start heading either left or upward.)
#
# So, the beam could start on any tile in the top row (heading downward),
# any tile in the bottom row (heading upward), any tile in the leftmost column
# (heading right), or any tile in the rightmost column (heading left).
# To produce lava, you need to find the configuration that energizes
# as many tiles as possible.
#
# In the above example, this can be achieved by starting the beam
# in the fourth tile from the left in the top row:
#
#   .|<2<\....
#   |v-v\^....
#   .v.v.|->>>
#   .v.v.v^.|.
#   .v.v.v^...
#   .v.v.v^..\
#   .v.v/2\\..
#   <-2-/vv|..
#   .|<<<2-|.\
#   .v//.|.v..
#
# Using this configuration, 51 tiles are energized:
#
#   .#####....
#   .#.#.#....
#   .#.#.#####
#   .#.#.##...
#   .#.#.##...
#   .#.#.##...
#   .#.#####..
#   ########..
#   .#######..
#   .#...#.#..
#
# Find the initial beam configuration that energizes the largest number
# of tiles; how many tiles are energized in that configuration?
#
#
# --- Solution ---
#
# The only difference here is that we need to consider many starting positions.
# Hence, the whole code is wrapped in a loop that tries every possible start
# from a initial list. We store the highest number of energized tiles observed
# for all cases and return it as an answer.
#

INPUT_FILE = 'input.txt'

RIGHT = complex(1, 0)
LEFT = complex(-1, 0)
UP = complex(0, -1)
DOWN = complex(0, 1)

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

    max_energized = 0
    starts = (
        [(complex(0, y), RIGHT) for y in range(HEIGHT)]
        + [(complex(x, 0), DOWN) for x in range(WIDTH)]
        + [(complex(WIDTH - 1, y), LEFT) for y in range(HEIGHT)]
        + [(complex(x, HEIGHT - 1), UP) for x in range(WIDTH)]
    )

    for start in starts:
        beams = [start]
        energized = set()
        visited = set()

        while beams:
            beam = beams.pop(0)
            position, direction = beam
            x, y = unpack(position)

            if any([x < 0, y < 0, x >= WIDTH, y >= HEIGHT]):
                continue  # the beam went out of grid

            if beam in visited:
                continue  # we were already here

            tile = grid[y][x]
            energized.add(position)
            visited.add(beam)

            if tile == EMPTY:
                beams.append((position + direction, direction))

            elif tile in MIRRORS:
                if direction == RIGHT:
                    if tile == FORWARD_MIRROR:
                        beams.append((position + UP, UP))
                    else:  # BACKSLASH_MIRROR
                        beams.append((position + DOWN, DOWN))

                elif direction == LEFT:
                    if tile == FORWARD_MIRROR:
                        beams.append((position + DOWN, DOWN))
                    else:  # BACKSLASH_MIRROR
                        beams.append((position + UP, UP))

                elif direction == UP:
                    if tile == FORWARD_MIRROR:
                        beams.append((position + RIGHT, RIGHT))
                    else:  # BACKSLASH_MIRROR
                        beams.append((position + LEFT, LEFT))

                else:  # direction == DOWN:
                    if tile == FORWARD_MIRROR:
                        beams.append((position + LEFT, LEFT))
                    else:  # BACKSLASH_MIRROR
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
                print(f'PANIC! Unexpected tile: {tile} on {x},{y}')
                exit(1)

        if len(energized) > max_energized:
            max_energized = len(energized)

    print(max_energized)


if __name__ == '__main__':
    main()
