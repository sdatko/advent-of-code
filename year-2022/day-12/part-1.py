#!/usr/bin/env python3
#
# --- Day 12: Hill Climbing Algorithm ---
#
# You try contacting the Elves using your handheld device, but the river
# you're following must be too low to get a decent signal.
#
# You ask the device for a heightmap of the surrounding area (your puzzle
# input). The heightmap shows the local area from above broken into a grid;
# the elevation of each square of the grid is given by a single lowercase
# letter, where `a` is the lowest elevation, `b` is the next-lowest,
# and so on up to the highest elevation, `z`.
#
# Also included on the heightmap are marks for your current position (S)
# and the location that should get the best signal (E). Your current position
# (S) has elevation `a`, and the location that should get the best signal (E)
# has elevation `z`.
#
# You'd like to reach E, but to save energy, you should do it in as few
# steps as possible. During each step, you can move exactly one square up,
# down, left, or right. To avoid needing to get out your climbing gear,
# the elevation of the destination square can be at most one higher than
# the elevation of your current square; that is, if your current elevation
# is `m`, you could step to elevation `n`, but not to elevation `o`.
# (This also means that the elevation of the destination square can be
# much lower than the elevation of your current square.)
#
# For example:
#
#   Sabqponm
#   abcryxxl
#   accszExk
#   acctuvwj
#   abdefghi
#
# Here, you start in the top-left corner; your goal is near the middle.
# You could start by moving down or right, but eventually you'll need
# to head toward the e at the bottom. From there, you can spiral around
# to the goal:
#
#   v..v<<<<
#   >v.vv<<^
#   .>vv>E^^
#   ..v>>>^^
#   ..>>>>>^
#
# In the above diagram, the symbols indicate whether the path exits each
# square moving up (^), down (v), left (<), or right (>). The location that
# should get the best signal is still E, and . marks unvisited squares.
#
# This path reaches the goal in 31 steps, the fewest possible.
#
# What is the fewest steps required to move from your current position
# to the location that should get the best signal?
#
#
# --- Solution ---
#
# We start by reading the input file as a matrix of numbers, where each number
# corresponds to the character's ASCII code (to make finding the difference
# in elevation easier) – so we split by newlines and then to each character,
# converting it with ord() function.
# Then we find the starting point (S) and the destination (E) in our input,
# replacing at the same time to the lowest `a` and highest `z` elevation.
# After that we are able to start finding the shortest path from start to goal.
# For that, we implement part of the BFS algorithm (breadth-first search).
# We take the coordinates of the starting point (S) as first position in graph
# to go through (distance: 0). Then, as long as there are still positions
# to process, we perform the following actions:
# – we take the first element from the list of positions to process,
# – we check whether the current element is our goal: if so, then we finish
#   (the algorithm found the path that took the least *steps* to reach it),
# – otherwise we examine the surrounding nodes, provided that they exist
#   (next element is in bounds of grid) and we did not visit it yet (unknown
#   distance / number of steps to reach it), we add them to the end of list
#   of positions still to process, additionally recording the distance to them
#   as current number of steps plus 1.
# Note that in this implementation we do not record the information about
# the source node that led us to given node – we only store the number
# of steps it took to reach it (as this is the task). This algorithm works
# as long as we only count steps (i.e. graphs edges have weight of 0 or 1).
# Last point worth to note is the additional condition on which we discard
# the potential neighbor point – the task assumes the difference in elevation
# must not be greater than 1, meaning we accept paths like `a -> b -> c -> d`,
# but not `a -> d` directly, however going down and staying on the same level
# is also possible, i.e. `a -> b -> c -> a -> a -> a -> b -> c` is also valid.
# Finally, we print the number of steps it took to reach the goal as an answer.
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
        for i, row in enumerate(matrix):
            if element in row:
                return (i, row.index(element))
        return (-1, -1)  # Not found

    start = find(ord('S'), grid)
    goal = find(ord('E'), grid)

    grid[start[0]][start[1]] = ord('a')
    grid[goal[0]][goal[1]] = ord('z')

    positions = [start]
    steps[start] = 0

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
