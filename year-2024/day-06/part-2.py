#!/usr/bin/env python3
#
# --- Day 6: Guard Gallivant / Part Two ---
#
# While The Historians begin working around the guard's patrol route,
# you borrow their fancy device and step outside the lab. From the safety
# of a supply closet, you time travel through the last few months and record
# the nightly status of the lab's guard post on the walls of the closet.
#
# Returning after what seems like only a few seconds to The Historians,
# they explain that the guard's patrol area is simply too large for them
# to safely search the lab without getting caught.
#
# Fortunately, they are pretty sure that adding a single new obstruction
# won't cause a time paradox. They'd like to place the new obstruction
# in such a way that the guard will get stuck in a loop, making the rest
# of the lab safe to search.
#
# To have the lowest chance of creating a time paradox, The Historians would
# like to know all of the possible positions for such an obstruction. The new
# obstruction can't be placed at the guard's starting position - the guard is
# there right now and would notice.
#
# In the above example, there are only 6 different positions where a new
# obstruction would cause the guard to get stuck in a loop. The diagrams
# of these six situations use O to mark the new obstruction, | to show
# a position where the guard moves up/down, - to show a position where
# the guard moves left/right, and + to show a position where the guard
# moves both up/down and left/right.
#
# Option one, put a printing press next to the guard's starting position:
#
#   ....#.....
#   ....+---+#
#   ....|...|.
#   ..#.|...|.
#   ....|..#|.
#   ....|...|.
#   .#.O^---+.
#   ........#.
#   #.........
#   ......#...
#
# Option two, put a stack of failed suit prototypes in the bottom right
# quadrant of the mapped area:
#
#   ....#.....
#   ....+---+#
#   ....|...|.
#   ..#.|...|.
#   ..+-+-+#|.
#   ..|.|.|.|.
#   .#+-^-+-+.
#   ......O.#.
#   #.........
#   ......#...
#
# Option three, put a crate of chimney-squeeze prototype fabric next to
# the standing desk in the bottom right quadrant:
#
#   ....#.....
#   ....+---+#
#   ....|...|.
#   ..#.|...|.
#   ..+-+-+#|.
#   ..|.|.|.|.
#   .#+-^-+-+.
#   .+----+O#.
#   #+----+...
#   ......#...
#
# Option four, put an alchemical retroencabulator near the bottom left corner:
#
#   ....#.....
#   ....+---+#
#   ....|...|.
#   ..#.|...|.
#   ..+-+-+#|.
#   ..|.|.|.|.
#   .#+-^-+-+.
#   ..|...|.#.
#   #O+---+...
#   ......#...
#
# Option five, put the alchemical retroencabulator a bit to the right instead:
#
#   ....#.....
#   ....+---+#
#   ....|...|.
#   ..#.|...|.
#   ..+-+-+#|.
#   ..|.|.|.|.
#   .#+-^-+-+.
#   ....|.|.#.
#   #..O+-+...
#   ......#...
#
# Option six, put a tank of sovereign glue right next to the tank
# of universal solvent:
#
#   ....#.....
#   ....+---+#
#   ....|...|.
#   ..#.|...|.
#   ..+-+-+#|.
#   ..|.|.|.|.
#   .#+-^-+-+.
#   .+----++#.
#   #+----++..
#   ......#O..
#
# It doesn't really matter what you choose to use as an obstacle so long as
# you and The Historians can put it into position without the guard noticing.
# The important thing is having enough options that you can find one that
# minimizes time paradoxes, and in this example, there are 6 different
# positions you could choose.
#
# You need to get the guard stuck in a loop by adding a single new obstruction.
# How many different positions could you choose for this obstruction?
#
#
# --- Solution ---
#
# The difference in this part is that we need to test all possible cases where
# there is one additional obstacle placed in the original grid. There is also
# additional condition – if we reach the loop, i.e. the same position and move
# direction was already seen, we break the loop and count that case. Finally,
# as an answer we return the count of cases where the loop was reached.
#
# The naive implementation (checking all positions) worked fine and provided
# a correct answer in the finite time (less than a minute), however it was
# possible to optimize the list of cases – the new obstacle only makes sense
# when it is placed on one of the originally visited locations. This greatly
# reduces the number of checks and the final execution time of the program.
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

    start = (position, direction)
    loops = 0

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

    locations_to_check = visited.copy()  # consider only visited positions
    locations_to_check.remove(start[0])  # skip initial guard location

    for (ox, oy) in locations_to_check:
        position, direction = start
        visited = set()

        if (ox, oy) in obstacles:  # there is already something
            continue

        obstacles.add((ox, oy))

        while True:
            visited.add((position, direction))

            x, y = position
            nx = position[0] + direction[0]
            ny = position[1] + direction[1]

            if not (min_x <= nx < max_x and min_y <= ny < max_y):
                break  # out of mapped area

            if ((nx, ny), direction) in visited:
                loops += 1
                break  # reached a loop

            if (nx, ny) in obstacles:
                direction = NEXT_DIRECTION[direction]

            else:
                position = (nx, ny)

        obstacles.remove((ox, oy))

    print(loops)


if __name__ == '__main__':
    main()
