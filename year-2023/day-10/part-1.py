#!/usr/bin/env python3
#
# --- Day 10: Pipe Maze ---
#
# You use the hang glider to ride the hot air from Desert Island all
# the way up to the floating metal island. This island is surprisingly
# cold and there definitely aren't any thermals to glide on, so you leave
# your hang glider behind.
#
# You wander around for a while, but you don't find any people or animals.
# However, you do occasionally find signposts labeled "Hot Springs" pointing
# in a seemingly consistent direction; maybe you can find someone at the hot
# springs and ask them where the desert-machine parts are made.
#
# The landscape here is alien; even the flowers and trees are made of metal.
# As you stop to admire some metal grass, you notice something metallic scurry
# away in your peripheral vision and jump into a big pipe! It didn't look like
# any animal you've ever seen; if you want a better look, you'll need to get
# ahead of it.
#
# Scanning the area, you discover that the entire field you're standing on
# is densely packed with pipes; it was hard to tell at first because they're
# the same metallic silver color as the "ground". You make a quick sketch
# of all of the surface pipes you can see (your puzzle input).
#
# The pipes are arranged in a two-dimensional grid of tiles:
# – | is a vertical pipe connecting north and south.
# – - is a horizontal pipe connecting east and west.
# – L is a 90-degree bend connecting north and east.
# – J is a 90-degree bend connecting north and west.
# – 7 is a 90-degree bend connecting south and west.
# – F is a 90-degree bend connecting south and east.
# – . is ground; there is no pipe in this tile.
# – S is the starting position of the animal; there is a pipe on this tile,
#   but your sketch doesn't show what shape the pipe has.
#
# Based on the acoustics of the animal's scurrying, you're confident
# the pipe that contains the animal is one large, continuous loop.
#
# For example, here is a square loop of pipe:
#
#   .....
#   .F-7.
#   .|.|.
#   .L-J.
#   .....
#
# If the animal had entered this loop in the northwest corner,
# the sketch would instead look like this:
#
#   .....
#   .S-7.
#   .|.|.
#   .L-J.
#   .....
#
# In the above diagram, the S tile is still a 90-degree F bend:
# you can tell because of how the adjacent pipes connect to it.
#
# Unfortunately, there are also many pipes that aren't connected to the loop!
# This sketch shows the same loop as above:
#
#   -L|F7
#   7S-7|
#   L|7||
#   -L-J|
#   L|-JF
#
# In the above diagram, you can still figure out which pipes form the main
# loop: they're the ones connected to S, pipes those pipes connect to, pipes
# those pipes connect to, and so on. Every pipe in the main loop connects to
# its two neighbors (including S, which will have exactly two pipes connecting
# to it, and which is assumed to connect back to those two pipes).
#
# Here is a sketch that contains a slightly more complex main loop:
#
#   ..F7.
#   .FJ|.
#   SJ.L7
#   |F--J
#   LJ...
#
# Here's the same example sketch with the extra, non-main-loop pipe
# tiles also shown:
#
#   7-F7-
#   .FJ|7
#   SJLL7
#   |F--J
#   LJ.LJ
#
# If you want to get out ahead of the animal, you should find the tile
# in the loop that is farthest from the starting position. Because the animal
# is in the pipe, it doesn't make sense to measure this by direct distance.
# Instead, you need to find the tile that would take the longest number
# of steps along the loop to reach from the starting point - regardless
# of which way around the loop the animal went.
#
# In the first example with the square loop:
#
#   .....
#   .S-7.
#   .|.|.
#   .L-J.
#   .....
#
# You can count the distance each tile in the loop is from
# the starting point like this:
#
#   .....
#   .012.
#   .1.3.
#   .234.
#   .....
#
# In this example, the farthest point from the start is 4 steps away.
#
# Here's the more complex loop again:
#
#   ..F7.
#   .FJ|.
#   SJ.L7
#   |F--J
#   LJ...
#
# Here are the distances for each tile on that loop:
#
#   ..45.
#   .236.
#   01.78
#   14567
#   23...
#
# Find the single giant loop starting at S. How many steps along the loop
# does it take to get from the starting position to the point farthest
# from the starting position?
#
#
# --- Solution ---
#
# We start by reading the input file into a list of strings – maze definition.
# For convenience and to avoid out-of-bounds errors, the whole maze is padded
# with a single ground tile. Then we look through the maze to find the start,
# making it to initial queue and assigning the initial distance to it as zero.
# Next, in a loop, as long as there are positions in queue to process, we take
# the first position from queue and depending on what tile it corresponds to,
# we find the neighbors candidates. Later we check which neighbor was already
# visited – and those that were not yet visited, we add to the queue of next
# positions to process, saving also the distance to them. Finally, after going
# through all possible positions, we return the highest saved distance.
# This is in essence a Breadth-First Search (BFS) algorithm.
#

INPUT_FILE = 'input.txt'

START = 'S'
GROUND = '.'
PIPE_NS = '|'  # vertical pipe connecting north and south
PIPE_EW = '-'  # horizontal pipe connecting east and west
PIPE_NE = 'L'  # 90-degree bend connecting north and east
PIPE_NW = 'J'  # 90-degree bend connecting north and west
PIPE_SW = '7'  # 90-degree bend connecting south and west
PIPE_SE = 'F'  # 90-degree bend connecting south and east


def main():
    with open(INPUT_FILE, 'r') as file:
        maze = [GROUND + line + GROUND
                for line in file.read().strip().split('\n')]
        maze.insert(0, GROUND * len(maze[0]))
        maze.append(GROUND * len(maze[0]))

    positions = []
    visited = {}

    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == START:
                positions.append((x, y))
                visited[(x, y)] = 0

    while positions:
        x, y = positions.pop(0)
        tile = maze[y][x]
        distance = visited[(x, y)]

        if tile == START:
            neighbors = []

            if maze[y][x - 1] in [PIPE_EW, PIPE_NE, PIPE_SE]:
                neighbors.append((x - 1, y))

            if maze[y][x + 1] in [PIPE_EW, PIPE_NW, PIPE_SW]:
                neighbors.append((x + 1, y))

            if maze[y - 1][x] in [PIPE_NS, PIPE_SW, PIPE_SE]:
                neighbors.append((x, y - 1))

            if maze[y + 1][x] in [PIPE_NS, PIPE_NW, PIPE_NE]:
                neighbors.append((x, y + 1))

        elif tile == PIPE_NS:
            neighbors = [(x, y - 1), (x, y + 1)]

        elif tile == PIPE_EW:
            neighbors = [(x - 1, y), (x + 1, y)]

        elif tile == PIPE_NE:
            neighbors = [(x + 1, y), (x, y - 1)]

        elif tile == PIPE_NW:
            neighbors = [(x - 1, y), (x, y - 1)]

        elif tile == PIPE_SW:
            neighbors = [(x - 1, y), (x, y + 1)]

        elif tile == PIPE_SE:
            neighbors = [(x + 1, y), (x, y + 1)]

        else:  # ground or other non-pipe
            continue

        for neighbor in neighbors:
            if neighbor not in visited:
                visited[neighbor] = distance + 1
                positions.append(neighbor)

    farthest = max(visited.values())

    print(farthest)


if __name__ == '__main__':
    main()
