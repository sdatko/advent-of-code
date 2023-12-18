#!/usr/bin/env python3
#
# --- Day 18: Lavaduct Lagoon / Part Two ---
#
# The Elves were right to be concerned; the planned lagoon
# would be much too small.
#
# After a few minutes, someone realizes what happened; someone swapped
# the color and instruction parameters when producing the dig plan.
# They don't have time to fix the bug; one of them asks if you can
# extract the correct instructions from the hexadecimal codes.
#
# Each hexadecimal code is six hexadecimal digits long. The first five
# hexadecimal digits encode the distance in meters as a five-digit
# hexadecimal number. The last hexadecimal digit encodes the direction
# to dig: 0 means R, 1 means D, 2 means L, and 3 means U.
#
# So, in the above example, the hexadecimal codes can be converted
# into the true instructions:
#
#   #70c710 = R 461937
#   #0dc571 = D 56407
#   #5713f0 = R 356671
#   #d2c081 = D 863240
#   #59c680 = R 367720
#   #411b91 = D 266681
#   #8ceee2 = L 577262
#   #caa173 = U 829975
#   #1b58a2 = L 112010
#   #caa171 = D 829975
#   #7807d2 = L 491645
#   #a77fa3 = U 686074
#   #015232 = L 5411
#   #7a21e3 = U 500254
#
# Digging out this loop and its interior produces a lagoon that can hold
# an impressive 952408144115 cubic meters of lava.
#
# Convert the hexadecimal color codes into the correct instructions;
# if the Elves follow this new dig plan, how many cubic meters of lava
# could the lagoon hold?
#
#
# --- Solution ---
#
# The only difference here is that instead of using first and second column
# from input data, we need to decode and use the values from the third column.
# Hence, we map the last character into a direction and all but last character
# we read as an integer of base 16. The rest of the code remains the same.
#

INPUT_FILE = 'input.txt'

DIG_TO_DIRECTION = {
    '3': 'U',
    '2': 'L',
    '1': 'D',
    '0': 'R',
}


def shoelace(vertices: list[tuple[int, int]]) -> int:
    area = 0

    for (x1, y1), (x2, y2) in zip(vertices[:-1], vertices[1:]):
        area += (x1 * y2) - (x2 * y1)  # triangle formula

    return abs(area) // 2


def main():
    with open(INPUT_FILE, 'r') as file:
        instructions = [line.split()[-1].strip('()#')
                        for line in file.read().strip().split('\n')]
        instructions = [(DIG_TO_DIRECTION[color[-1]], int(color[:-1], base=16))
                        for color in instructions]

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
