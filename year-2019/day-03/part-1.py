#!/usr/bin/env python3
#
# --- Day 3: Crossed Wires ---
#
# The gravity assist was successful, and you're well on your way to the Venus
# refuelling station. During the rush back on Earth, the fuel management system
# wasn't completely installed, so that's next on the priority list.
#
# Opening the front panel reveals a jumble of wires. Specifically, two wires
# are connected to a central port and extend outward on a grid. You trace
# the path each wire takes as it leaves the central port, one wire per line
# of text (your puzzle input).
#
# The wires twist and turn, but the two wires occasionally cross paths.
# To fix the circuit, you need to find the intersection point closest
# to the central port. Because the wires are on a grid, use the Manhattan
# distance for this measurement. While the wires do technically cross right
# at the central port where they both start, this point does not count,
# nor does a wire count as crossing with itself.
#
# For example, if the first wire's path is R8,U5,L5,D3, then starting from
# the central port (o), it goes right 8, up 5, left 5, and finally down 3:
#
#   ...........
#   ...........
#   ...........
#   ....+----+.
#   ....|....|.
#   ....|....|.
#   ....|....|.
#   .........|.
#   .o-------+.
#   ...........
#
# Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6,
# down 4, and left 4:
#
#   ...........
#   .+-----+...
#   .|.....|...
#   .|..+--X-+.
#   .|..|..|.|.
#   .|.-X--+.|.
#   .|..|....|.
#   .|.......|.
#   .o-------+.
#   ...........
#
# These wires cross at two locations (marked X), but the lower-left one
# is closer to the central port: its distance is 3 + 3 = 6.
#
# Here are a few more examples:
# – R75,D30,R83,U83,L12,D49,R71,U7,L72
#   U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
# – R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
#   U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
#
# What is the Manhattan distance from the central port
# to the closest intersection?
#
#
# --- Solution ---
#
# We start by reading the input into a list of sequences that specify the wires
# paths by splitting the file over newlines and then each line over the commas.
# Then for each wire we build a set of path coordinates by processing sequences
# from the (0, 0) position in a 2D space. Finally we find the paths crossings
# by calculating the sets intersection and for each crossing we calculate its
# distance from the origin point (0, 0). As an answer, we return the minimum
# of the all distances.
#
#

INPUT_FILE = 'input.txt'

DIRECTIONS = {
    'U': complex(0, +1),
    'D': complex(0, -1),
    'L': complex(-1, 0),
    'R': complex(+1, 0),
}


def main():
    with open(INPUT_FILE, 'r') as file:
        wires = [wire.split(',')
                 for wire in file.read().strip().split('\n')]

    paths = []

    for wire in wires:
        path = set()
        position = complex(0, 0)

        for move in wire:
            direction = move[0]
            distance = int(move[1:])

            step = DIRECTIONS[direction]

            for _ in range(distance):
                position += step
                path.add(position)

        paths.append(path)

    path1, path2 = paths
    crossings = set.intersection(path1, path2)
    distances = [int(abs(crossing.real) + abs(crossing.imag))
                 for crossing in crossings]

    print(min(distances))


if __name__ == '__main__':
    main()
