#!/usr/bin/env python3
#
# --- Day 18: Boiling Boulders / Part Two ---
#
# Something seems off about your calculation. The cooling rate depends
# on exterior surface area, but your calculation also included the surface
# area of air pockets trapped in the lava droplet.
#
# Instead, consider only cube sides that could be reached by the water
# and steam as the lava droplet tumbles into the pond. The steam will expand
# to reach as much as possible, completely displacing any air on the outside
# of the lava droplet but never expanding diagonally.
#
# In the larger example above, exactly one cube of air is trapped within
# the lava droplet (at 2,2,5), so the exterior surface area of the lava
# droplet is 58.
#
# What is the exterior surface area of your scanned lava droplet?
#
#
# --- Solution ---
#
# The difference in this part is how we attempt to calculate the outer faces.
# The water/steam mentioned in the description is a good hint for that.
# First we find the minimal surrounding space around the droplet. Then we move
# through this space similar way the water would do if it pours into this space
# via a single hole (breadth-first search). From the starting point, we attempt
# to move to all adjacent positions (neighbors) that were not visited already.
# If any of such neighbors is a part of the given droplet, then we found
# an outer face to count towards an answer. Finally we just return the total
# amount of faces we encountered.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        droplet = set([tuple(map(int, cube.split(',')))
                       for cube in file.read().strip().split()])

    x_min = min([x for x, y, z in droplet]) - 1
    x_max = max([x for x, y, z in droplet]) + 1
    y_min = min([y for x, y, z in droplet]) - 1
    y_max = max([y for x, y, z in droplet]) + 1
    z_min = min([z for x, y, z in droplet]) - 1
    z_max = max([z for x, y, z in droplet]) + 1

    space = set([(x, y, z)
                 for x in range(x_min, x_max + 1)
                 for y in range(y_min, y_max + 1)
                 for z in range(z_min, z_max + 1)])

    faces = 0

    checked = set()
    to_check = set([(x_min, y_min, z_min)])

    while to_check:
        x, y, z = to_check.pop()

        checked.add((x, y, z))

        for neighbor in [(x + 1, y, z),
                         (x - 1, y, z),
                         (x, y + 1, z),
                         (x, y - 1, z),
                         (x, y, z + 1),
                         (x, y, z - 1)]:
            if neighbor in space and neighbor not in checked:
                if neighbor in droplet:
                    faces += 1
                else:
                    to_check.add(neighbor)

    print(faces)


if __name__ == '__main__':
    main()
