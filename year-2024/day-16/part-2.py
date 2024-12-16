#!/usr/bin/env python3
#
# --- Day 16: Reindeer Maze / Part Two ---
#
# Now that you know what the best paths look like, you can figure out
# the best spot to sit.
#
# Every non-wall tile (S, ., or E) is equipped with places to sit along
# the edges of the tile. While determining which of these tiles would be
# the best spot to sit depends on a whole bunch of factors (how comfortable
# the seats are, how far away the bathrooms are, whether there's a pillar
# blocking your view, etc.), the most important factor is whether the tile
# is on one of the best paths through the maze. If you sit somewhere else,
# you'd miss all the action!
#
# So, you'll need to determine which tiles are part of any best path
# through the maze, including the S and E tiles.
#
# In the first example, there are 45 tiles (marked O) that are part of
# at least one of the various best paths through the maze:
#
#   ###############
#   #.......#....O#
#   #.#.###.#.###O#
#   #.....#.#...#O#
#   #.###.#####.#O#
#   #.#.#.......#O#
#   #.#.#####.###O#
#   #..OOOOOOOOO#O#
#   ###O#O#####O#O#
#   #OOO#O....#O#O#
#   #O#O#O###.#O#O#
#   #OOOOO#...#O#O#
#   #O###.#.#.#O#O#
#   #O..#.....#OOO#
#   ###############
#
# In the second example, there are 64 tiles that are part of at least one
# of the best paths:
#
#   #################
#   #...#...#...#..O#
#   #.#.#.#.#.#.#.#O#
#   #.#.#.#...#...#O#
#   #.#.#.#.###.#.#O#
#   #OOO#.#.#.....#O#
#   #O#O#.#.#.#####O#
#   #O#O..#.#.#OOOOO#
#   #O#O#####.#O###O#
#   #O#O#..OOOOO#OOO#
#   #O#O###O#####O###
#   #O#O#OOO#..OOO#.#
#   #O#O#O#####O###.#
#   #O#O#OOOOOOO..#.#
#   #O#O#O#########.#
#   #O#OOO..........#
#   #################
#
# Analyze your map further. How many tiles are part of at least one
# of the best paths through the maze?
#
#
# --- Solution ---
#
# The difference in this part is that we need to count tiles that are part
# of a path with the lowest score – it looks like there are multiple paths
# of the same lowest score leading to the goal. Hence, we cannot just stop
# processing, but after reaching the goal for the first time we take a note
# of what is the best score – and we can use that information to skip any path
# that at any point has already bigger score value (i.e. it will be worse when
# reaching the goal anyway). In the queue, apart of the current and previous
# positions, we need to also store the full path details (visited locations).
# For each path that reaches the goal with best score, we add the coordinates
# of visited locations to a unique set. Final modification involves checking
# of any previously visited location – it turns out that for a given position
# we should only reject it when we were there before *AND* the score we had
# there at that time was sharply lower. This preserves in simulation the paths
# that visit the same node with equal scores – consider the following map:
#
#        E
#        ^
#  ^>>>>>^
#  ^     ^
#  ^>>>>>^
#  ^
#  S
#
# Both paths leads to E with exactly the same score, however when rejecting
# path with any previously visited tile (i.e. with lower *or* equal score)
# only one of those (semi-randomly?) would be considered in previous part.
# Finally, after processing all the possibile (and reasonable) paths, we print
# the number of unique tiles visited as an answer.
#

INPUT_FILE = 'input.txt'

START = 'S'
END = 'E'
WALL = '#'

MOVES = {
    'right': (1, 0),
    'left': (-1, 0),
    'down': (0, 1),
    'up': (0, -1),
}


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
        maze = tuple(file.read().strip().split())

    start = (0, 0)
    end = (0, 0)

    for y, row in enumerate(maze):
        for x, tile in enumerate(row):
            if tile == START:
                start = (x, y)
            if tile == END:
                end = (x, y)

    # we face east, so we came from west (left)
    previous = (start[0] + MOVES['left'][0], start[1] + MOVES['left'][1])

    queue = [(0, start, previous, [start])]  # score, (start), (previous), path
    visited = dict()

    best = None
    unique = set()

    while queue:
        score, (sx, sy), (px, py), path = heap_pop(queue)

        if best and best < score:
            continue  # ignore this path

        if (sx, sy) == end:  # we reached the goal
            best = score
            unique.update(path)
            continue

        if (sx, sy, px, py) in visited and visited[(sx, sy, px, py)] < score:
            continue  # we know a path to (sx, sy) with a lower score

        visited[(sx, sy, px, py)] = score

        for (dx, dy) in MOVES.values():
            nx = sx + dx
            ny = sy + dy

            if maze[ny][nx] == WALL:
                continue  # do not hit the wall

            if nx == px and ny == py:
                continue  # never come back

            next_score = score + 1

            if nx != px and ny != py:  # there was a turn
                next_score += 1000

            heap_push(
                queue,
                (next_score, (nx, ny), (sx, sy), path + [(nx, ny)])
            )

    print(len(unique))


if __name__ == '__main__':
    main()
