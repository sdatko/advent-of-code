#!/usr/bin/env python3
#
# --- Day 6: Guard Gallivant ---
#
# The Historians use their fancy device again, this time to whisk you all away
# to the North Pole prototype suit manufacturing lab... in the year 1518!
# It turns out that having direct access to history is very convenient for
# a group of historians.
#
# You still have to be careful of time paradoxes, and so it will be important
# to avoid anyone from 1518 while The Historians search for the Chief.
# Unfortunately, a single guard is patrolling this part of the lab.
#
# Maybe you can work out where the guard will go ahead of time so that
# The Historians can search safely?
#
# You start by making a map (your puzzle input) of the situation. For example:
#
#   ....#.....
#   .........#
#   ..........
#   ..#.......
#   .......#..
#   ..........
#   .#..^.....
#   ........#.
#   #.........
#   ......#...
#
# The map shows the current position of the guard with ^ (to indicate the guard
# is currently facing up from the perspective of the map). Any obstructions
# - crates, desks, alchemical reactors, etc. - are shown as #.
#
# Lab guards in 1518 follow a very strict patrol protocol which involves
# repeatedly following these steps:
# – If there is something directly in front of you, turn right 90 degrees.
# – Otherwise, take a step forward.
#
# Following the above protocol, the guard moves up several times until
# she reaches an obstacle (in this case, a pile of failed suit prototypes):
#
#   ....#.....
#   ....^....#
#   ..........
#   ..#.......
#   .......#..
#   ..........
#   .#........
#   ........#.
#   #.........
#   ......#...
#
# Because there is now an obstacle in front of the guard, she turns right
# before continuing straight in her new facing direction:
#
#   ....#.....
#   ........>#
#   ..........
#   ..#.......
#   .......#..
#   ..........
#   .#........
#   ........#.
#   #.........
#   ......#...
#
# Reaching another obstacle (a spool of several very long polymers),
# she turns right again and continues downward:
#
#   ....#.....
#   .........#
#   ..........
#   ..#.......
#   .......#..
#   ..........
#   .#......v.
#   ........#.
#   #.........
#   ......#...
#
# This process continues for a while, but the guard eventually leaves
# the mapped area (after walking past a tank of universal solvent):
#
#   ....#.....
#   .........#
#   ..........
#   ..#.......
#   .......#..
#   ..........
#   .#........
#   ........#.
#   #.........
#   ......#v..
#
# By predicting the guard's route, you can determine which specific positions
# in the lab will be in the patrol path. Including the guard's starting
# position, the positions visited by the guard before leaving the area
# are marked with an X:
#
#   ....#.....
#   ....XXXXX#
#   ....X...X.
#   ..#.X...X.
#   ..XXXXX#X.
#   ..X.X.X.X.
#   .#XXXXXXX.
#   .XXXXXXX#.
#   #XXXXXXX..
#   ......#X..
#
# In this example, the guard will visit 41 distinct positions on your map.
#
# Predict the path of the guard. How many distinct positions will the guard
# visit before leaving the mapped area?
#
#
# --- Solution ---
#
# We start by reading the input into a 2-dimensional grid by splitting the file
# over newlines. We define helper variables to represent directions using easy
# to understand aliases (UP, instead of [0, -1]). Then, we process the grid
# to identify the locations of obstacles, as well as the starting position
# of a guard. Next, we move through positions in the grid in the semi-infinite
# loop – as long as the next position is not outside the mapped grid. In every
# iteration we record the current position in the list of unique locations
# that were visited and we check the next move – change of direction, if next
# position contains an obstacle, or moving forward otherwise. Finally, as an
# answer we count and return the number of unique locations that were visited.
#

INPUT_FILE = 'input.txt'

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

NEXT_DIRECTION = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP,
}


def main():
    with open(INPUT_FILE, 'r') as file:
        grid = file.read().strip().split()

    min_x = 0
    min_y = 0
    max_x = len(grid[0])
    max_y = len(grid)

    obstacles = set()
    position = (0, 0)
    direction = UP
    visited = set()

    for y in range(0, max_y):
        for x in range(0, max_x):
            if grid[y][x] == '#':
                obstacles.add((x, y))
            if grid[y][x] == '^':
                position = (x, y)
                direction = UP

    while True:
        visited.add(position)

        x, y = position
        nx = position[0] + direction[0]
        ny = position[1] + direction[1]

        if not (min_x <= nx < max_x and min_y <= ny < max_y):
            break  # out of mapped area

        if (nx, ny) in obstacles:
            direction = NEXT_DIRECTION[direction]

        else:
            position = (nx, ny)

    print(len(visited))


if __name__ == '__main__':
    main()
