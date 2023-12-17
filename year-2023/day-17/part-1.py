#!/usr/bin/env python3
#
# --- Day 17: Clumsy Crucible ---
#
# The lava starts flowing rapidly once the Lava Production Facility
# is operational. As you leave, the reindeer offers you a parachute,
# allowing you to quickly reach Gear Island.
#
# As you descend, your bird's-eye view of Gear Island reveals why you had
# trouble finding anyone on your way up: half of Gear Island is empty, but
# the half below you is a giant factory city!
#
# You land near the gradually-filling pool of lava at the base of your
# new lavafall. Lavaducts will eventually carry the lava throughout
# the city, but to make use of it immediately, Elves are loading it
# into large crucibles on wheels.
#
# The crucibles are top-heavy and pushed by hand. Unfortunately,
# the crucibles become very difficult to steer at high speeds,
# and so it can be hard to go in a straight line for very long.
#
# To get Desert Island the machine parts it needs as soon as possible,
# you'll need to find the best way to get the crucible from the lava pool
# to the machine parts factory. To do this, you need to minimize heat loss
# while choosing a route that doesn't require the crucible to go in
# a straight line for too long.
#
# Fortunately, the Elves here have a map (your puzzle input) that uses
# traffic patterns, ambient temperature, and hundreds of other parameters
# to calculate exactly how much heat loss can be expected for a crucible
# entering any particular city block.
#
# For example:
#
#   2413432311323
#   3215453535623
#   3255245654254
#   3446585845452
#   4546657867536
#   1438598798454
#   4457876987766
#   3637877979653
#   4654967986887
#   4564679986453
#   1224686865563
#   2546548887735
#   4322674655533
#
# Each city block is marked by a single digit that represents the amount
# of heat loss if the crucible enters that block. The starting point,
# the lava pool, is the top-left city block; the destination, the machine
# parts factory, is the bottom-right city block. (Because you already start
# in the top-left block, you don't incur that block's heat loss unless
# you leave that block and then return to it.)
#
# Because it is difficult to keep the top-heavy crucible going in a straight
# line for very long, it can move at most three blocks in a single direction
# before it must turn 90 degrees left or right. The crucible also can't
# reverse direction; after entering each city block, it may only turn left,
# continue straight, or turn right.
#
# One way to minimize heat loss is this path:
#
#   2>>34^>>>1323
#   32v>>>35v5623
#   32552456v>>54
#   3446585845v52
#   4546657867v>6
#   14385987984v4
#   44578769877v6
#   36378779796v>
#   465496798688v
#   456467998645v
#   12246868655<v
#   25465488877v5
#   43226746555v>
#
# This path never moves more than three consecutive blocks
# in the same direction and incurs a heat loss of only 102.
#
# Directing the crucible from the lava pool to the machine parts factory,
# but not moving more than three consecutive blocks in the same direction,
# what is the least heat loss it can incur?
#
#
# --- Solution ---
#
# We start by reading the input file into a 2D tuple of integers, by splitting
# over newlines and then each line (string) converting into list of characters
# that is mapped to integers. Then we need to solve a path finding problem
# with non-negative weights – hence, the Dijkstra's algorithm is a choice.
# I decided to reuse my previous implementation that involves heap structure
# (year-2021/day-15/part-2), after adjusting for the given task specification.
# There are two main constraints: first, we cannot revert direction (i.e. move
# immediately to previous position); second, we can move only up to 3 times
# into a given direction (i.e. we are forced to turn). Therefore, instead of
# considering only direct neighbors in algorithm, we add to the queue every
# reachable position (up to a given distance). To prevent reverting the move,
# we need to keep as part of each state the information about the direction
# from which the current position was reached – and remove that direction from
# next moves consideration. Because we already included all possible locations
# reachable in a given direction, for current state we also disallow the move
# in that direction, forcing a turn. In other words, if from a given position
# (x, y) we can move horizontally to (x + 1, y), (x + 2, y), (x + 3, y), then
# from all these positions we can only move along Y axis next. Because we use
# the ordered queue (a heap), we are guaranteed that every state currently
# considered for a given position (reached from a certain direction) comes
# from the shortest path – hence we can ignore revisiting it later. Finally,
# once we reach the first state that led us to the goal position, we return
# the answer as the shortest distance (lowest heat loss) found.
#

INPUT_FILE = 'input.txt'

MAXIMUM_STEPS = 3


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
                heap_push(Q, (next_loss, (nx, ny), (dx, dy)))

    print(current_loss)


if __name__ == '__main__':
    main()
