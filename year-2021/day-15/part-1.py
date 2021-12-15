#!/usr/bin/env python3
#
# Task:
# You've almost reached the exit of the cave, but the walls are getting
# closer together. Your submarine can barely still fit, though; the main
# problem is that the walls of the cave are covered in chitons, and it would
# be best not to bump any of them.
# The cavern is large, but has a very low ceiling, restricting your motion
# to two dimensions. The shape of the cavern resembles a square; a quick scan
# of chiton density produces a map of risk level throughout the cave (your
# puzzle input).
# You start in the top left position, your destination is the bottom right
# position, and you cannot move diagonally. The number at each position is
# its risk level; to determine the total risk of an entire path, add up the
# risk levels of each position you enter (that is, don't count the risk level
# of your starting position unless you enter it; leaving it adds no risk
# to your total).
# Your goal is to find a path with the lowest total risk.
# What is the lowest total risk of any path from the top left
# to the bottom right?
#
# Solution:
# We start by reading the input file as matrix (list of lists) of integers.
# To find the shortest path we can interpret the numbers in our grid as edges
# weights in graph, so then the Dijkstra's algorithm is an obvious choice.
# I implemented the algorithm according to Wikipedia's pseudocode and it gave
# me the correct answer. Long story short, we start with a set of vertices,
# we take the one with shortest path for now (minimum value) and we see how
# long distance it will take to go from this vertex to its neighbors;
# if the new distance will be shorter than one we currently know, we update
# the distance and store the information from which vertex we got there.
# We break once the smallest road value in vertices to consider corresponds
# to our target (goal) position.
# Then our answer is the last element in produced distances matrix.
# Two end notices:
# – in our task we do not really need the `prev` array, as we are only
#   interested in the distance, but not the path itself, however I left
#   it in the code as it was in original implementation I followed,
# – original implementation assumed first the creation of set of all possible
#   vertices to consider, which worked fine, but then in part 2 I realised
#   it is not really necessary and we can build a set of interesting points
#   on demand, whenever there was any change in our distances array we may
#   want to try new paths – this resulted in much greater performance,
#   however I left the original parts as commented code for legacy reasons.
#

INPUT_FILE = 'input.txt'


def main():
    grid = [list(map(int, list(characters)))
            for line in open(INPUT_FILE, 'r')
            for characters in line.strip().split()]

    rows = len(grid)
    cols = len(grid[0])

    start = (0, 0)
    goal = (cols - 1, rows - 1)

    risk_level = sum(grid[0]) + sum(grid[:][-1])  # upper bound

    # Q = set([(x, y) for y in range(rows) for x in range(cols)])
    dist = [[risk_level for x in range(cols)] for y in range(rows)]
    prev = [[None for x in range(cols)] for y in range(rows)]

    dist[start[1]][start[0]] = 0
    Q = set([(start)])  # inspired by Part 2

    while Q:
        shortest = risk_level + 1
        sx, sy = 0, 0

        for (x, y) in Q:
            if dist[y][x] < shortest:
                shortest = dist[y][x]
                sy = y
                sx = x

        Q.remove((sx, sy))

        if (sx, sy) == goal:
            break

        for (nx, ny) in ((sx - 1, sy), (sx + 1, sy),
                         (sx, sy - 1), (sx, sy + 1)):
            # if (nx, ny) not in Q:
            #     continue
            if nx < 0 or nx >= cols or ny < 0 or ny >= rows:
                continue

            alt = dist[sy][sx] + grid[ny][nx]
            if alt < dist[ny][nx]:
                dist[ny][nx] = alt
                prev[ny][nx] = (sx, sy)
                Q.add((nx, ny))  # inspired by Part 2

    risk_level = dist[goal[1]][goal[0]]

    print(risk_level)


if __name__ == '__main__':
    main()
