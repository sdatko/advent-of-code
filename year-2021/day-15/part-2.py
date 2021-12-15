#!/usr/bin/env python3
#
# Task:
# Now that you know how to find low-risk paths in the cave, you can try
# to find your way out.
# The entire cave is actually five times larger in both dimensions than you
# thought; the area you originally scanned is just one tile in a 5x5 tile area
# that forms the full map. Your original map tile repeats to the right and
# downward; each time the tile repeats to the right or downward, all of its
# risk levels are 1 higher than the tile immediately up or left of it.
# However, risk levels above 9 wrap back around to 1. So, if your original map
# had some position with a risk level of 8, then that same position on each of
# the 25 total tiles would be as follows:
#   8 9 1 2 3
#   9 1 2 3 4
#   1 2 3 4 5
#   2 3 4 5 6
#   3 4 5 6 7
# Each single digit above corresponds to the example position with a value of
# 8 on the top-left tile. Because the full map is actually five times larger
# in both dimensions, that position appears a total of 25 times, once in each
# duplicated tile, with the values shown above.
# Using the full map, what is the lowest total risk of any path from
# the top left to the bottom right?
#
# Solution:
# The biggest difference in this part was to implement the data alignment
# in a bigger grid. For such case, the originally prepared algorithm turned
# out to be non-effective, giving result in roughly about 104 minutes.
# Experimentally I found that the implementation of a finding vertex for
# current minimum distance was the bottleneck. Optimizing that part by
# introducing heap reduced the computation time to less than a second.
# Then I discovered that original implementation could be optimized and
# after introducing changes it gave result in about 11 seconds.
# Code below is using a heap implementation of my own – it is a bit slower
# than dedicated Python heapq module, but sufficient enough for my goals
# and my code can still remain import-free (which is my personal challenge).
#

INPUT_FILE = 'input.txt'


def heapify(array, index=0):
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < len(array) and array[left] < array[smallest]:
        smallest = left

    if right < len(array) and array[right] < array[smallest]:
        smallest = right

    if smallest != index:
        array[index], array[smallest] = array[smallest], array[index]
        heapify(array, smallest)


def heap_pop(array):
    root = array[0]
    array[0] = array[len(array) - 1]
    array.pop()
    heapify(array)
    return root


def heap_push(array, element):
    array.append(element)
    index = len(array) - 1
    parent = (index - 1) // 2

    while index != 0 and array[parent] > array[index]:
        array[index], array[parent] = array[parent], array[index]
        index = parent
        parent = (index - 1) // 2


def wrap(x):
    return (x % 10) + (x // 10)


def main():
    grid = [list(map(int, list(characters)))
            for line in open(INPUT_FILE, 'r')
            for characters in line.strip().split()]

    times_bigger = 5
    bigger_grid = []

    for times_y in range(times_bigger):
        for row in grid:
            new_row = []
            for times_x in range(times_bigger):
                new_row.extend(
                    [wrap(x + times_y + times_x) for x in row]
                )
            bigger_grid.append(new_row)

    grid = bigger_grid

    rows = len(grid)
    cols = len(grid[0])

    start = (0, 0)
    goal = (cols - 1, rows - 1)

    risk_level = sum(grid[0]) + sum(grid[:][-1])  # upper bound

    dist = [[risk_level for x in range(cols)] for y in range(rows)]
    prev = [[None for x in range(cols)] for y in range(rows)]

    dist[start[1]][start[0]] = 0
    Q = [(dist[start[1]][start[0]], start)]

    while Q:
        shortest, (sx, sy) = heap_pop(Q)

        if (sx, sy) == goal:
            break

        for (nx, ny) in ((sx - 1, sy), (sx + 1, sy),
                         (sx, sy - 1), (sx, sy + 1)):
            if nx < 0 or nx >= cols or ny < 0 or ny >= rows:
                continue

            alt = shortest + grid[ny][nx]
            if alt < dist[ny][nx]:
                dist[ny][nx] = alt
                prev[ny][nx] = (sx, sy)
                heap_push(Q, (alt, (nx, ny)))

    risk_level = dist[goal[1]][goal[0]]

    print(risk_level)


if __name__ == '__main__':
    main()
