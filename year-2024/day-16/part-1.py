#!/usr/bin/env python3
#
# --- Day 16: Reindeer Maze ---
#
# It's time again for the Reindeer Olympics! This year, the big event
# is the Reindeer Maze, where the Reindeer compete for the lowest score.
#
# You and The Historians arrive to search for the Chief right as the event
# is about to start. It wouldn't hurt to watch a little, right?
#
# The Reindeer start on the Start Tile (marked S) facing East and need
# to reach the End Tile (marked E). They can move forward one tile at a time
# (increasing their score by 1 point), but never into a wall (#). They can
# also rotate clockwise or counterclockwise 90 degrees at a time (increasing
# their score by 1000 points).
#
# To figure out the best place to sit, you start by grabbing a map
# (your puzzle input) from a nearby kiosk. For example:
#
#   ###############
#   #.......#....E#
#   #.#.###.#.###.#
#   #.....#.#...#.#
#   #.###.#####.#.#
#   #.#.#.......#.#
#   #.#.#####.###.#
#   #...........#.#
#   ###.#.#####.#.#
#   #...#.....#.#.#
#   #.#.#.###.#.#.#
#   #.....#...#.#.#
#   #.###.#.#.#.#.#
#   #S..#.....#...#
#   ###############
#
# There are many paths through this maze, but taking any of the best paths
# would incur a score of only 7036. This can be achieved by taking a total
# of 36 steps forward and turning 90 degrees a total of 7 times:
#
#   ###############
#   #.......#....E#
#   #.#.###.#.###^#
#   #.....#.#...#^#
#   #.###.#####.#^#
#   #.#.#.......#^#
#   #.#.#####.###^#
#   #..>>>>>>>>v#^#
#   ###^#.#####v#^#
#   #>>^#.....#v#^#
#   #^#.#.###.#v#^#
#   #^....#...#v#^#
#   #^###.#.#.#v#^#
#   #S..#.....#>>^#
#   ###############
#
# Here's a second example:
#
#   #################
#   #...#...#...#..E#
#   #.#.#.#.#.#.#.#.#
#   #.#.#.#...#...#.#
#   #.#.#.#.###.#.#.#
#   #...#.#.#.....#.#
#   #.#.#.#.#.#####.#
#   #.#...#.#.#.....#
#   #.#.#####.#.###.#
#   #.#.#.......#...#
#   #.#.###.#####.###
#   #.#.#...#.....#.#
#   #.#.#.#####.###.#
#   #.#.#.........#.#
#   #.#.#.#########.#
#   #S#.............#
#   #################
#
# In this maze, the best paths cost 11048 points;
# following one such path would look like this:
#
#   #################
#   #...#...#...#..E#
#   #.#.#.#.#.#.#.#^#
#   #.#.#.#...#...#^#
#   #.#.#.#.###.#.#^#
#   #>>v#.#.#.....#^#
#   #^#v#.#.#.#####^#
#   #^#v..#.#.#>>>>^#
#   #^#v#####.#^###.#
#   #^#v#..>>>>^#...#
#   #^#v###^#####.###
#   #^#v#>>^#.....#.#
#   #^#v#^#####.###.#
#   #^#v#^........#.#
#   #^#v#^#########.#
#   #S#>>^..........#
#   #################
#
# Note that the path shown above includes one 90 degree turn as the very
# first move, rotating the Reindeer from facing East to facing North.
#
# Analyze your map carefully. What is the lowest score a Reindeer
# could possibly get?
#
#
# --- Solution ---
#
# We start by reading the input file into a maze definition by splitting
# the data over newlines. Then we browse the maze to find the start position
# and the desired goal (end) location. Next, we build a priority-queue,
# where as elements we store the calculated score (that we want to minimize),
# the current location and the previous location, initialized with the start
# position that we found and fake previous position that was selected in so
# that it looks like the reindeer is oriented facing east direction (right).
# In a loop, we take the element with the lowest score from the queue/heap and
# we check if the location with that score is not our goal already, or if that
# location was not already visited – if it was, it means that we were in this
# position already with a lower score (because if it was processed earlier,
# the score must have been here lower [or equal] anyway, so there is no point
# in reconsidering that position). It is important to notice that we need
# to keep the information about both the current and the previous positions
# – to a given tile we may came from two directions and one of this moves may
# involve the turn, which would make this case actually worse later (because
# of additional score for turning). Then, when we are on unique position,
# we consider all possible next steps – excluding the moves that would hit
# the wall or take us to the previous position (as there is no point in turning
# back; that would always be worse than going directly to some other position).
# Moving to a new position always adds a score of 1, but additional 1000 score
# shall be added when there was a turn. As for turn detection, we can check
# if the next position shares one of the coordinates (along x or y axis) with
# the previous position – if so, then we continue in a straight line, so there
# was no turn; otherwise, when both X and Y coordinates changed, there must
# have been a turn involved. Finally, after reaching the goal, we return
# the score value – because of priority queue involved, this one is the lowest.
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

    queue = [(0, start, previous)]  # score, (start), (previous)
    visited = set()

    while queue:
        score, (sx, sy), (px, py) = heap_pop(queue)

        if (sx, sy) == end:  # we reached the goal
            break

        if (sx, sy, px, py) in visited:  # we were here with a lower score
            continue

        visited.add((sx, sy, px, py))

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

            heap_push(queue, (next_score, (nx, ny), (sx, sy)))

    print(score)


if __name__ == '__main__':
    main()
