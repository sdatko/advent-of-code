#!/usr/bin/env python3
#
# --- Day 18: Lavaduct Lagoon ---
#
# Thanks to your efforts, the machine parts factory is one of the first
# factories up and running since the lavafall came back. However, to catch up
# with the large backlog of parts requests, the factory will also need a large
# supply of lava for a while; the Elves have already started creating a large
# lagoon nearby for this purpose.
#
# However, they aren't sure the lagoon will be big enough; they've asked you
# to take a look at the dig plan (your puzzle input). For example:
#
#   R 6 (#70c710)
#   D 5 (#0dc571)
#   L 2 (#5713f0)
#   D 2 (#d2c081)
#   R 2 (#59c680)
#   D 2 (#411b91)
#   L 5 (#8ceee2)
#   U 2 (#caa173)
#   L 1 (#1b58a2)
#   U 2 (#caa171)
#   R 2 (#7807d2)
#   U 3 (#a77fa3)
#   L 2 (#015232)
#   U 2 (#7a21e3)
#
# The digger starts in a 1 meter cube hole in the ground. They then dig
# the specified number of meters up (U), down (D), left (L), or right (R),
# clearing full 1 meter cubes as they go. The directions are given as seen
# from above, so if "up" were north, then "right" would be east, and so on.
# Each trench is also listed with the color that the edge of the trench
# should be painted as an RGB hexadecimal color code.
#
# When viewed from above, the above example dig plan would result
# in the following loop of trench (#) having been dug out from
# otherwise ground-level terrain (.):
#
#   #######
#   #.....#
#   ###...#
#   ..#...#
#   ..#...#
#   ###.###
#   #...#..
#   ##..###
#   .#....#
#   .######
#
# At this point, the trench could contain 38 cubic meters of lava.
# However, this is just the edge of the lagoon; the next step is
# to dig out the interior so that it is one meter deep as well:
#
#   #######
#   #######
#   #######
#   ..#####
#   ..#####
#   #######
#   #####..
#   #######
#   .######
#   .######
#
# Now, the lagoon can contain a much more respectable 62 cubic meters of lava.
# While the interior is dug out, the edges are also painted according to
# the color codes in the dig plan.
#
# The Elves are concerned the lagoon won't be large enough; if they follow
# their dig plan, how many cubic meters of lava could it hold?
#
#
# --- Solution ---
#
# We start by reading the input file into a list of instructions (tuples of
# direction character and distance integer; the third column from input is not
# used within this part at all). Then we process the instructions in a loop
# to figure out the vertices of corners that define the shape. Also, during
# that, by summing the travel distances, we can also count the number of edge
# points. Then, we can find the area of the shape, using the Shoelace Formula,
# also known as the Gauss's Area Formula, which is considered a special case
# of the Green's Theorem. Then, from transforming the Pick's theorem we can
# determine the number on interior points enclosed withing the shape boundary,
# i.e. area = (number of interior points) + (number of edge points) / 2 - 1.
# Finally, as an answer we provide the sum of interior points number and
# the edge points number.
#
# Important note is that the Shoelace formula here does not return the area
# of the whole shape described in task, but of a little smaller shape – shown
# on the illustration below, the Shoelace Formula corresponds to shape defined
# by vertices (o). The whole shape consists of areas for interior points (i)
# and all edge points (e) and (o).
#
#     |  0 1 2 3 4 5 6  x
#   --+----------------->
#     | +-+-+-+-+-+-+-+
#   0 | |o|e|e|e|e|e|o|
#     | +-+-+-+-+-+-+-+
#   1 | |e|i|i|i|i|i|e|
#     | +-+-+-+-+-+-+-+
#   2 | |o|e|e|e|o|i|e|
#     | +-+-+-+-+-+-+-+
#   3 |         |e|i|e|
#     |         +-+-+-+
#   4 |         |e|i|e|
#     |         +-+-+-+
#   5 |         |o|e|o|
#     |         +-+-+-+
#   y V
#

INPUT_FILE = 'input.txt'


def shoelace(vertices: list[tuple[int, int]]) -> int:
    area = 0

    for (x1, y1), (x2, y2) in zip(vertices[:-1], vertices[1:]):
        area += (y1 + y2) * (x1 - x2)  # trapezoid formula

    return abs(area) // 2


def main():
    with open(INPUT_FILE, 'r') as file:
        instructions = [line.split()[:2]
                        for line in file.read().strip().split('\n')]
        instructions = [(direction, int(distance))
                        for direction, distance in instructions]

    x, y = (0, 0)  # starting position
    vertices = [(x, y)]
    edges = 0
    area = 0

    for direction, distance in instructions:
        if direction == 'R':
            x, y = (x + distance, y)
        elif direction == 'L':
            x, y = (x - distance, y)
        elif direction == 'U':
            x, y = (x, y + distance)
        elif direction == 'D':
            x, y = (x, y - distance)

        vertices.append((x, y))
        edges += distance

    area = shoelace(vertices)
    interior = area - edges // 2 + 1

    print(edges + interior)


if __name__ == '__main__':
    main()
