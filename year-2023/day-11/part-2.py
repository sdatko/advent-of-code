#!/usr/bin/env python3
#
# --- Day 11: Cosmic Expansion / Part Two ---
#
# The galaxies are much older (and thus much farther apart)
# than the researcher initially estimated.
#
# Now, instead of the expansion you did before, make each empty row
# or column one million times larger. That is, each empty row should
# be replaced with 1000000 empty rows, and each empty column should be
# replaced with 1000000 empty columns.
#
# (In the example above, if each empty row or column were merely 10 times
# larger, the sum of the shortest paths between every pair of galaxies
# would be 1030. If each empty row or column were merely 100 times larger,
# the sum of the shortest paths between every pair of galaxies would be 8410.
# However, your universe will need to expand far beyond these values.)
#
# Starting with the same initial image, expand the universe according to
# these new rules, then find the length of the shortest path between every
# pair of galaxies. What is the sum of these lengths?
#
#
# --- Solution ---
#
# The difference here is that instead of inserting a single additional row
# or colum after each empty one, we add multiple ones. The general idea is
# that we replace single row/column with N rows/columns – to make the space
# N times bigger; this corresponds to inserting additional (N-1) rows/columns.
# The rest of the code remains the same as in previous part.
#

INPUT_FILE = 'input.txt'

GALAXY = '#'
TIMES_BIGGER = 1_000_000


def main():
    with open(INPUT_FILE, 'r') as file:
        image = file.read().strip().split('\n')

    galaxies = []
    distances = []

    for y, row in enumerate(image):
        for x, col in enumerate(row):
            if col == GALAXY:
                galaxies.append((x, y))

    empty_rows = [y
                  for y, row in enumerate(image)
                  if all(pixel != GALAXY for pixel in row)]

    empty_cols = [x
                  for x, _ in enumerate(image[0])
                  if all(pixel != GALAXY
                         for pixel in [row[x] for row in image])]

    for row in reversed(empty_rows):
        for i, (x, y) in enumerate(galaxies):
            if y > row:
                galaxies[i] = (x, y + (TIMES_BIGGER - 1))

    for col in reversed(empty_cols):
        for i, (x, y) in enumerate(galaxies):
            if x > col:
                galaxies[i] = (x + (TIMES_BIGGER - 1), y)

    for i, galaxy1 in enumerate(galaxies[:-1]):
        for galaxy2 in galaxies[i + 1:]:
            x1, y1 = galaxy1
            x2, y2 = galaxy2

            distance = abs(x2 - x1) + abs(y2 - y1)
            distances.append(distance)

    print(sum(distances))


if __name__ == '__main__':
    main()
