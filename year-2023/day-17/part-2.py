#!/usr/bin/env python3
#
# --- Day 17: Clumsy Crucible / Part Two ---
#
# The crucibles of lava simply aren't large enough to provide an adequate
# supply of lava to the machine parts factory. Instead, the Elves are going
# to upgrade to ultra crucibles.
#
# Ultra crucibles are even more difficult to steer than normal crucibles.
# Not only do they have trouble going in a straight line, but they also
# have trouble turning!
#
# Once an ultra crucible starts moving in a direction, it needs to move
# a minimum of four blocks in that direction before it can turn (or even
# before it can stop at the end). However, it will eventually start
# to get wobbly: an ultra crucible can move a maximum of ten consecutive
# blocks without turning.
#
# In the above example, an ultra crucible could follow this path
# to minimize heat loss:
#
#   2>>>>>>>>1323
#   32154535v5623
#   32552456v4254
#   34465858v5452
#   45466578v>>>>
#   143859879845v
#   445787698776v
#   363787797965v
#   465496798688v
#   456467998645v
#   122468686556v
#   254654888773v
#   432267465553v
#
# In the above example, an ultra crucible would incur the minimum
# possible heat loss of 94.
#
# Here's another example:
#
#   111111111111
#   999999999991
#   999999999991
#   999999999991
#   999999999991
#
# Sadly, an ultra crucible would need to take an unfortunate
# path like this one:
#
#   1>>>>>>>1111
#   9999999v9991
#   9999999v9991
#   9999999v9991
#   9999999v>>>>
#
# This route causes the ultra crucible to incur the minimum
# possible heat loss of 71.
#
# Directing the ultra crucible from the lava pool to the machine parts
# factory, what is the least heat loss it can incur?
#
#
# --- Solution ---
#
# The difference here is that instead of moving between 1 and 3 steps into
# a given direction, we need to analyze only the positions that are between
# 4 and 10 steps away. Hence, we add to the queue only the states that are
# located at least given 4 units away, but we have to include the contribution
# to the distance (heat loss) from the neighbors 1, 2 and 3 units away still
# (we do not teleport, we move but we cannot stop at these positions).
#

INPUT_FILE = 'input.txt'

MINIMUM_STEPS = 4
MAXIMUM_STEPS = 10


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


def main():
    with open(INPUT_FILE, 'r') as file:
        grid = tuple(tuple(map(int, list(line)))
                     for line in file.read().strip().split('\n'))

    rows = len(grid)
    cols = len(grid[0])

    start = (0, 0)
    goal = (cols - 1, rows - 1)

    Q = [(0, start, start)]  # loss, (start), (previous)
    visited = set()

    while Q:
        current_loss, (sx, sy), (px, py) = heap_pop(Q)

        if (sx, sy) == goal:
            break

        if (sx, sy, px, py) in visited:
            continue
        visited.add((sx, sy, px, py))

        next_moves = {
            (1, 0),  # right
            (-1, 0),  # left
            (0, 1),  # down
            (0, -1),  # up
        }
        forbidden_moves = {
            (-px, -py),  # can't reverse direction – never go back
            (px, py),  # do not continue current direction – force turning
        }

        for (dx, dy) in (next_moves - forbidden_moves):
            next_loss = current_loss

            for i in range(1, MAXIMUM_STEPS + 1):
                nx = sx + dx * i
                ny = sy + dy * i

                if nx < 0 or nx >= cols or ny < 0 or ny >= rows:
                    continue

                next_loss += grid[ny][nx]

                if i >= MINIMUM_STEPS:
                    heap_push(Q, (next_loss, (nx, ny), (dx, dy)))

    print(current_loss)


if __name__ == '__main__':
    main()
