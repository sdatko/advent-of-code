#!/usr/bin/env python3
#
# --- Day 12: Hill Climbing Algorithm / Part Two ---
#
# As you walk up the hill, you suspect that the Elves will want to turn this
# into a hiking trail. The beginning isn't very scenic, though; perhaps you
# can find a better starting point.
#
# To maximize exercise while hiking, the trail should start as low as possible:
# elevation a. The goal is still the square marked E. However, the trail
# should still be direct, taking the fewest steps to reach its goal.
# So, you'll need to find the shortest path from any square at elevation
# a to the square marked E.
#
# Again consider the example from above:
#
#   Sabqponm
#   abcryxxl
#   accszExk
#   acctuvwj
#   abdefghi
#
# Now, there are six choices for starting position (five marked a, plus
# the square marked S that counts as being at elevation a). If you start
# at the bottom-left square, you can reach the goal most quickly:
#
#   ...v<<<<
#   ...vv<<^
#   ...v>E^^
#   .>v>>>^^
#   >^>>>>>^
#
# This path reaches the goal in only 29 steps, the fewest possible.
#
# What is the fewest steps required to move starting from any square with
# elevation a to the location that should get the best signal?
#
#
# --- Solution ---
#
# The difference here is that we shall consider both original starting point
# `S` and any point on elevation `a` as the starting position. In this case,
# every such point we can add to the list of positions to process, all with
# known distance as 0. Then exactly the same algorithm finds the new, shortest
# path to the destination from any lowest point `a`.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        grid = [[ord(character) for character in list(line)]
                for line in file.read().strip().split()]

    cols = len(grid[0])
    rows = len(grid)
    steps = {}

    def find(element, matrix):
        indices = []
        for i, row in enumerate(matrix):
            if element in row:
                indices.append((i, row.index(element)))
        return indices

    start = find(ord('S'), grid)[0]
    goal = find(ord('E'), grid)[0]

    grid[start[0]][start[1]] = ord('a')
    grid[goal[0]][goal[1]] = ord('z')

    positions = find(ord('a'), grid)
    for position in positions:
        steps[position] = 0

    while len(positions) > 0:
        i, j = positions.pop(0)
        current = grid[i][j]

        if (i, j) == goal:
            break

        for ni, nj in [(i - 1, j), (i, j - 1),
                       (i + 1, j), (i, j + 1)]:
            if all([0 <= ni < rows,
                    0 <= nj < cols,
                    (ni, nj) not in steps]):
                neighbor = grid[ni][nj]

                if (neighbor - current) <= 1:
                    positions.append((ni, nj))
                    steps[(ni, nj)] = steps[(i, j)] + 1

    print(steps[goal])


if __name__ == '__main__':
    main()
