#!/usr/bin/env python3
#
# --- Day 13: Point of Incidence / Part Two ---
#
# You resume walking through the valley of mirrors and - SMACK! - run
# directly into one. Hopefully nobody was watching, because that must
# have been pretty embarrassing.
#
# Upon closer inspection, you discover that every mirror has exactly one
# smudge: exactly one . or # should be the opposite type.
#
# In each pattern, you'll need to locate and fix the smudge that causes
# a different reflection line to be valid. (The old reflection line won't
# necessarily continue being valid after the smudge is fixed.)
#
# Here's the above example again:
#
#   #.##..##.
#   ..#.##.#.
#   ##......#
#   ##......#
#   ..#.##.#.
#   ..##..##.
#   #.#.##.#.
#
#   #...##..#
#   #....#..#
#   ..##..###
#   #####.##.
#   #####.##.
#   ..##..###
#   #....#..#
#
# The first pattern's smudge is in the top-left corner. If the top-left #
# were instead ., it would have a different, horizontal line of reflection:
#
#   1 ..##..##. 1
#   2 ..#.##.#. 2
#   3v##......#v3
#   4^##......#^4
#   5 ..#.##.#. 5
#   6 ..##..##. 6
#   7 #.#.##.#. 7
#
# With the smudge in the top-left corner repaired, a new horizontal line
# of reflection between rows 3 and 4 now exists. Row 7 has no corresponding
# reflected row and can be ignored, but every other row matches exactly:
# row 1 matches row 6, row 2 matches row 5, and row 3 matches row 4.
#
# In the second pattern, the smudge can be fixed by changing the fifth symbol
# on row 2 from . to #:
#
#   1v#...##..#v1
#   2^#...##..#^2
#   3 ..##..### 3
#   4 #####.##. 4
#   5 #####.##. 5
#   6 ..##..### 6
#   7 #....#..# 7
#
# Now, the pattern has a different horizontal line of reflection
# between rows 1 and 2.
#
# Summarize your notes as before, but instead use the new different reflection
# lines. In this example, the first pattern's new horizontal line has 3 rows
# above it and the second pattern's new horizontal line has 1 row above it,
# summarizing to the value 400.
#
# In each pattern, fix the smudge and find the different line of reflection.
# What number do you get after summarizing the new reflection line in each
# pattern in your notes?
#
#
# --- Solution ---
#
# The difference here is that for each mirror we need to find a symmetry index
# that would be different from originally found one, after swapping a single
# element in the mirror image. For this, the generator function was created,
# that produces all possible variants of a given mirror – by copying original
# mirror and changing the element at any possible (x,y) position. Additionally
# the function for finding a symmetry needs now also a parameter to specify
# the forbidden index (that would be the original index found for unmodified
# mirror image; it has to be covered within that function, as for some cases
# of the real input the original symmetry was still found first even though
# some part of the original mirror was altered).
#

INPUT_FILE = 'input.txt'

SWAP = {
    '.': '#',
    '#': '.',
}


def get_col(mirror, index):
    return [row[index] for row in mirror]


def get_row(mirror, index):
    return mirror[index]


def find_symmetry(mirror, forbidden=0):
    rows = len(mirror)
    cols = len(mirror[0])

    # rows
    for index in range(rows - 1):
        for i in range(index + 1):
            if index + 1 + i >= rows:
                continue

            if get_row(mirror, index - i) != get_row(mirror, index + 1 + i):
                break

        else:  # when there was no break in a loop
            candidate = 100 * (index + 1)

            if candidate != forbidden:
                return candidate
            else:
                continue

    # columns
    for index in range(cols - 1):
        for i in range(index + 1):
            if index + 1 + i >= cols:
                continue

            if get_col(mirror, index - i) != get_col(mirror, index + 1 + i):
                break

        else:  # when there was no break in a loop
            candidate = (index + 1)

            if candidate != forbidden:
                return candidate
            else:
                continue

    # no symmetry
    return 0


def variants(mirror):
    rows = len(mirror)
    cols = len(mirror[0])

    for y in range(rows):
        for x in range(cols):
            variant = [row[:] for row in mirror]
            variant[y] = (
                variant[y][:x] + SWAP[variant[y][x]] + variant[y][x + 1:]
            )

            yield variant


def main():
    with open(INPUT_FILE, 'r') as file:
        mirrors = [mirror.split('\n')
                   for mirror in file.read().strip().split('\n\n')]

    notes = []

    for original_mirror in mirrors:
        original_index = find_symmetry(original_mirror)

        for mirror in variants(original_mirror):
            index = find_symmetry(mirror, forbidden=original_index)

            if index:
                notes.append(index)
                break

    print(sum(notes))


if __name__ == '__main__':
    main()
