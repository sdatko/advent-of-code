#!/usr/bin/env python3
#
# --- Day 3: Squares With Three Sides ---
#
# Now that you can think clearly, you move deeper into the labyrinth
# of hallways and office furniture that makes up this part of Easter
# Bunny HQ. This must be a graphic design department; the walls are
# covered in specifications for triangles.
#
# Or are they?
#
# The design document gives the side lengths of each triangle it describes,
# but... 5 10 25? Some of these aren't triangles. You can't help but mark
# the impossible ones.
#
# In a valid triangle, the sum of any two sides must be larger than
# the remaining side. For example, the "triangle" given above is impossible,
# because 5 + 10 is not larger than 25.
#
# In your puzzle input, how many of the listed triangles are possible?
#
#
# --- Solution ---
#
# We read the input file into a list of triangles (three integers), first
# by splitting over newlines into list of lines and then by splitting each
# line over spaces and mapping the outcome into sorted tuple of integers.
# Then we iterate over list of triangles, counting as possible every such
# that has the sum of shortest sides (`a` and `b`) larger than the last
# longest side (`c`). Finally, we return the number of possible triangles.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        triangles = [tuple(sorted(map(int, line.strip().split())))
                     for line in file.read().strip().split('\n')]

    possible = 0

    for a, b, c in triangles:
        if (a + b) > c:
            possible += 1

    print(possible)


if __name__ == '__main__':
    main()
