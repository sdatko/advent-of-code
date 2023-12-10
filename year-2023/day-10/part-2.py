#!/usr/bin/env python3
#
# --- Day 10: Pipe Maze / Part Two ---
#
# You quickly reach the farthest point of the loop, but the animal never
# emerges. Maybe its nest is within the area enclosed by the loop?
#
# To determine whether it's even worth taking the time to search for such
# a nest, you should calculate how many tiles are contained within the loop.
# For example:
#
#   ...........
#   .S-------7.
#   .|F-----7|.
#   .||.....||.
#   .||.....||.
#   .|L-7.F-J|.
#   .|..|.|..|.
#   .L--J.L--J.
#   ...........
#
# The above loop encloses merely four tiles - the two pairs of . in
# the southwest and southeast (marked I below). The middle . tiles
# (marked O below) are not in the loop. Here is the same loop again
# with those regions marked:
#
#   ...........
#   .S-------7.
#   .|F-----7|.
#   .||OOOOO||.
#   .||OOOOO||.
#   .|L-7OF-J|.
#   .|II|O|II|.
#   .L--JOL--J.
#   .....O.....
#
# In fact, there doesn't even need to be a full tile path to the outside
# for tiles to count as outside the loop - squeezing between pipes is also
# allowed! Here, I is still within the loop and O is still outside the loop:
#
#   ..........
#   .S------7.
#   .|F----7|.
#   .||OOOO||.
#   .||OOOO||.
#   .|L-7F-J|.
#   .|II||II|.
#   .L--JL--J.
#   ..........
#
# In both of the above examples, 4 tiles are enclosed by the loop.
#
# Here's a larger example:
#
#   .F----7F7F7F7F-7....
#   .|F--7||||||||FJ....
#   .||.FJ||||||||L7....
#   FJL7L7LJLJ||LJ.L-7..
#   L--J.L7...LJS7F-7L7.
#   ....F-J..F7FJ|L7L7L7
#   ....L7.F7||L7|.L7L7|
#   .....|FJLJ|FJ|F7|.LJ
#   ....FJL-7.||.||||...
#   ....L---J.LJ.LJLJ...
#
# The above sketch has many random bits of ground, some of which are
# in the loop (I) and some of which are outside it (O):
#
#   OF----7F7F7F7F-7OOOO
#   O|F--7||||||||FJOOOO
#   O||OFJ||||||||L7OOOO
#   FJL7L7LJLJ||LJIL-7OO
#   L--JOL7IIILJS7F-7L7O
#   OOOOF-JIIF7FJ|L7L7L7
#   OOOOL7IF7||L7|IL7L7|
#   OOOOO|FJLJ|FJ|F7|OLJ
#   OOOOFJL-7O||O||||OOO
#   OOOOL---JOLJOLJLJOOO
#
# In this larger example, 8 tiles are enclosed by the loop.
#
# Any tile that isn't part of the main loop can count as being enclosed
# by the loop. Here's another example with many bits of junk pipe lying
# around that aren't connected to the main loop at all:
#
#   FF7FSF7F7F7F7F7F---7
#   L|LJ||||||||||||F--J
#   FL-7LJLJ||||||LJL-77
#   F--JF--7||LJLJ7F7FJ-
#   L---JF-JLJ.||-FJLJJ7
#   |F|F-JF---7F7-L7L|7|
#   |FFJF7L7F-JF7|JL---7
#   7-L-JL7||F7|L7F-7F7|
#   L.L7LFJ|||||FJL7||LJ
#   L7JLJL-JLJLJL--JLJ.L
#
# Here are just the tiles that are enclosed by the loop marked with I:
#
#   FF7FSF7F7F7F7F7F---7
#   L|LJ||||||||||||F--J
#   FL-7LJLJ||||||LJL-77
#   F--JF--7||LJLJIF7FJ-
#   L---JF-JLJIIIIFJLJJ7
#   |F|F-JF---7IIIL7L|7|
#   |FFJF7L7F-JF7IIL---7
#   7-L-JL7||F7|L7F-7F7|
#   L.L7LFJ|||||FJL7||LJ
#   L7JLJL-JLJLJL--JLJ.L
#
# In this last example, 10 tiles are enclosed by the loop.
#
# Figure out whether you have time to search for the nest by calculating
# the area within the loop. How many tiles are enclosed by the loop?
#
#
# --- Solution ---
#
# The difference here is that we need to calculate the number of tiles within
# the pipe loop – that would be the total area (all tiles enclosed in shape)
# with the number of edges (the tiles that form the loop) subtracted from it.
# The total area can be calculated using the approach similar to a scan-lines
# rendering algorithm – we process the maze line-by-line, assuming we start
# always outside of shape and we switch the state whenever we cross its side.
# In case of straight vertical tiles -> | -> we always switch inside/outside.
# In case of corners, it is a little more difficult – we need to track what
# was the opening tile and what was the closing tile; in general, if the pipe
# turns back to the same direction, i.e. it goes north -> east/west -> north
# or south -> east/west -> south, then we do not change the in/out state;
# if the pipe after turn continues to the opposite direction than previously,
# e.g. north -> east/west -> south or south -> east/west -> north, then this
# is similar to crossing a straight vertical tile and we change the state.
#
#               |        |         |        |         |        |
#               |        |         | inside |         |        |
#   outside +---+ inside | outside +--------+ outside | inside +---+ outside
#           |            |                            |            |
#           |            |                            |            |
#   outside +---+ inside | outside +--------+ outside | inside +---+ outside
#               |        |         | inside |         |        |
#               |        |         |        |         |        |
#
# Note that the horizontal tiles do not affect the inside/outside state here.
# To make this working, we also need to figure out what the starting tile is,
# which we achieve by analysing which neighbors of starting tile are connected
# to it. Last, we need to identify whether a non-ground tile is a junk or part
# of the pipe loop, which we can tell by examining the set of visited tiles
# (previous part).
#

INPUT_FILE = 'input.txt'

START = 'S'
GROUND = '.'
PIPE_NS = '|'  # vertical pipe connecting north and south
PIPE_EW = '-'  # horizontal pipe connecting east and west
PIPE_NE = 'L'  # 90-degree bend connecting north and east
PIPE_NW = 'J'  # 90-degree bend connecting north and west
PIPE_SW = '7'  # 90-degree bend connecting south and west
PIPE_SE = 'F'  # 90-degree bend connecting south and east

TILES = (PIPE_NS, PIPE_EW, PIPE_NE, PIPE_NW, PIPE_SW, PIPE_SE)


def main():
    with open(INPUT_FILE, 'r') as file:
        maze = [GROUND + line + GROUND
                for line in file.read().strip().split('\n')]
        maze.insert(0, GROUND * len(maze[0]))
        maze.append(GROUND * len(maze[0]))

    positions = []
    visited = set()

    area = 0
    edges = 0

    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == START:
                positions.append((x, y))
                visited.add((x, y))

    while positions:
        x, y = positions.pop(0)
        tile = maze[y][x]
        visited.add((x, y))

        if tile == START:
            neighbors = []

            if maze[y][x - 1] in [PIPE_EW, PIPE_NE, PIPE_SE]:
                neighbors.append((x - 1, y))

            if maze[y][x + 1] in [PIPE_EW, PIPE_NW, PIPE_SW]:
                neighbors.append((x + 1, y))

            if maze[y - 1][x] in [PIPE_NS, PIPE_SW, PIPE_SE]:
                neighbors.append((x, y - 1))

            if maze[y + 1][x] in [PIPE_NS, PIPE_NW, PIPE_NE]:
                neighbors.append((x, y + 1))

        elif tile == PIPE_NS:
            neighbors = [(x, y - 1), (x, y + 1)]

        elif tile == PIPE_EW:
            neighbors = [(x - 1, y), (x + 1, y)]

        elif tile == PIPE_NE:
            neighbors = [(x + 1, y), (x, y - 1)]

        elif tile == PIPE_NW:
            neighbors = [(x - 1, y), (x, y - 1)]

        elif tile == PIPE_SW:
            neighbors = [(x - 1, y), (x, y + 1)]

        elif tile == PIPE_SE:
            neighbors = [(x + 1, y), (x, y + 1)]

        else:  # ground or other non-pipe
            continue

        for neighbor in neighbors:
            if neighbor not in visited:
                positions.append(neighbor)

    # figure out what S is
    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            if tile == 'S':
                north = False
                south = False
                east = False
                west = False

                if maze[y][x - 1] in [PIPE_EW, PIPE_NE, PIPE_SE]:
                    west = True
                if maze[y][x + 1] in [PIPE_EW, PIPE_NW, PIPE_SW]:
                    east = True
                if maze[y - 1][x] in [PIPE_NS, PIPE_SW, PIPE_SE]:
                    north = True
                if maze[y + 1][x] in [PIPE_NS, PIPE_NW, PIPE_NE]:
                    south = True

                assert sum([north, south, east, west]) == 2

                if north and south:
                    new_tile = PIPE_NS
                if north and east:
                    new_tile = PIPE_NE
                if north and west:
                    new_tile = PIPE_NW
                if east and west:
                    new_tile = PIPE_EW
                if south and east:
                    new_tile = PIPE_SE
                if south and west:
                    new_tile = PIPE_SW

                maze[y] = maze[y].replace(START, new_tile)

    # scan-line algorithm
    for y, row in enumerate(maze):
        inside = False
        opened = None

        for x, tile in enumerate(row):
            if tile in TILES and (x, y) in visited:
                area += 1
                edges += 1

                if tile == PIPE_NS:
                    inside = not inside

                if tile in (PIPE_NE, PIPE_SE):
                    opened = tile

                if tile in (PIPE_NW, PIPE_SW):
                    if any([opened == PIPE_NE and tile == PIPE_SW,
                            opened == PIPE_SE and tile == PIPE_NW]):
                        inside = not inside
                    opened = None

            elif inside:
                area += 1

    print(area - edges)


if __name__ == '__main__':
    main()
