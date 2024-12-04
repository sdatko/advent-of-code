#!/usr/bin/env python3
#
# --- Day 4: Ceres Search / Part Two ---
#
# The Elf looks quizzically at you. Did you misunderstand the assignment?
#
# Looking for the instructions, you flip over the word search to find that
# this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're
# supposed to find two MAS in the shape of an X. One way to achieve that
# is like this:
#
#   M.S
#   .A.
#   M.S
#
# Irrelevant characters have again been replaced with . in the above diagram.
# Within the X, each MAS can be written forwards or backwards.
#
# Here's the same example from before, but this time all of the X-MASes have
# been kept instead:
#
#   .M.S......
#   ..A..MSMS.
#   .M.S.MAA..
#   ..A.ASMSM.
#   .M.S.M....
#   ..........
#   S.S.S.S.S.
#   .A.A.A.A..
#   M.M.M.M.M.
#   ..........
#
# In this example, an X-MAS appears 9 times.
#
# Flip the word search from the instructions back over to the word search
# side and try again. How many times does an X-MAS appear?
#
#
# --- Solution ---
#
# The difference in this part is in the pattern we need to consider for each
# cell in the grid. Using similar approach like before, there are just four
# possible arrangements of the text MAS MAS text in the X shape:
#   M M  M S  S S  S M
#    A    A    A    A
#   S S  M S  M M  S M
# So, only an adjustment of the directions collection (and expected string)
# was necessary in the program.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        grid = file.read().strip().split()

    max_x = len(grid[0])
    max_y = len(grid)

    directions = (
        (
            (-1, -1), (0, 0), (1, 1),  # bottom left to top right
            (-1, 1), (0, 0), (1, -1),  # top left to bottom right
        ),
        (
            (-1, 1), (0, 0), (1, -1),  # top left to bottom right
            (1, 1), (0, 0), (-1, -1),  # top right to bottom left
        ),
        (
            (1, 1), (0, 0), (-1, -1),  # top right to bottom left
            (1, -1), (0, 0), (-1, 1),  # bottom right to top left
        ),
        (
            (1, -1), (0, 0), (-1, 1),  # bottom right to top left
            (-1, -1), (0, 0), (1, 1),  # bottom left to top right
        ),
    )

    times = 0

    for y in range(0, max_y):
        for x in range(0, max_x):
            for indices in directions:
                word = ''.join(
                    grid[y + ny][x + nx]
                    for (nx, ny) in indices
                    if (0 <= x + nx < max_x) and (0 <= y + ny < max_y)
                )

                if word == 'MASMAS':
                    times += 1

    print(times)


if __name__ == '__main__':
    main()
