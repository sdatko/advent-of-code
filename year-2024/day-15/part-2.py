#!/usr/bin/env python3
#
# --- Day 15: Warehouse Woes / Part Two ---
#
# The lanternfish use your information to find a safe moment to swim in and
# turn off the malfunctioning robot! Just as they start preparing a festival
# in your honor, reports start coming in that a second warehouse's robot
# is also malfunctioning.
#
# This warehouse's layout is surprisingly similar to the one you just helped.
# There is one key difference: everything except the robot is twice as wide!
# The robot's list of movements doesn't change.
#
# To get the wider warehouse's map, start with your original map and,
# for each tile, make the following changes:
# – If the tile is #, the new map contains ## instead.
# – If the tile is O, the new map contains [] instead.
# – If the tile is ., the new map contains .. instead.
# – If the tile is @, the new map contains @. instead.
#
# This will produce a new warehouse map which is twice as wide and with
# wide boxes that are represented by []. (The robot does not change size.)
#
# The larger example from before would now look like this:
#
#   ####################
#   ##....[]....[]..[]##
#   ##............[]..##
#   ##..[][]....[]..[]##
#   ##....[]@.....[]..##
#   ##[]##....[]......##
#   ##[]....[]....[]..##
#   ##..[][]..[]..[][]##
#   ##........[]......##
#   ####################
#
# Because boxes are now twice as wide but the robot is still the same size
# and speed, boxes can be aligned such that they directly push two other boxes
# at once. For example, consider this situation:
#
#   #######
#   #...#.#
#   #.....#
#   #..OO@#
#   #..O..#
#   #.....#
#   #######
#
#   <vv<<^^<<^^
#
# After appropriately resizing this map, the robot would push around
# these boxes as follows:
#
#   Initial state:
#   ##############
#   ##......##..##
#   ##..........##
#   ##....[][]@.##
#   ##....[]....##
#   ##..........##
#   ##############
#
#   Move <:
#   ##############
#   ##......##..##
#   ##..........##
#   ##...[][]@..##
#   ##....[]....##
#   ##..........##
#   ##############
#
#   Move v:
#   ##############
#   ##......##..##
#   ##..........##
#   ##...[][]...##
#   ##....[].@..##
#   ##..........##
#   ##############
#
#   Move v:
#   ##############
#   ##......##..##
#   ##..........##
#   ##...[][]...##
#   ##....[]....##
#   ##.......@..##
#   ##############
#
#   Move <:
#   ##############
#   ##......##..##
#   ##..........##
#   ##...[][]...##
#   ##....[]....##
#   ##......@...##
#   ##############
#
#   Move <:
#   ##############
#   ##......##..##
#   ##..........##
#   ##...[][]...##
#   ##....[]....##
#   ##.....@....##
#   ##############
#
#   Move ^:
#   ##############
#   ##......##..##
#   ##...[][]...##
#   ##....[]....##
#   ##.....@....##
#   ##..........##
#   ##############
#
#   Move ^:
#   ##############
#   ##......##..##
#   ##...[][]...##
#   ##....[]....##
#   ##.....@....##
#   ##..........##
#   ##############
#
#   Move <:
#   ##############
#   ##......##..##
#   ##...[][]...##
#   ##....[]....##
#   ##....@.....##
#   ##..........##
#   ##############
#
#   Move <:
#   ##############
#   ##......##..##
#   ##...[][]...##
#   ##....[]....##
#   ##...@......##
#   ##..........##
#   ##############
#
#   Move ^:
#   ##############
#   ##......##..##
#   ##...[][]...##
#   ##...@[]....##
#   ##..........##
#   ##..........##
#   ##############
#
#   Move ^:
#   ##############
#   ##...[].##..##
#   ##...@.[]...##
#   ##....[]....##
#   ##..........##
#   ##..........##
#   ##############
#
# This warehouse also uses GPS to locate the boxes. For these larger boxes,
# distances are measured from the edge of the map to the closest edge of
# the box in question. So, the box shown below has a distance of 1 from
# the top edge of the map and 5 from the left edge of the map, resulting
# in a GPS coordinate of 100 * 1 + 5 = 105.
#
#   ##########
#   ##...[]...
#   ##........
#
# In the scaled-up version of the larger example from above, after the robot
# has finished all of its moves, the warehouse would look like this:
#
#   ####################
#   ##[].......[].[][]##
#   ##[]...........[].##
#   ##[]........[][][]##
#   ##[]......[]....[]##
#   ##..##......[]....##
#   ##..[]............##
#   ##..@......[].[][]##
#   ##......[][]..[]..##
#   ####################
#
# The sum of these boxes' GPS coordinates is 9021.
#
# Predict the motion of the robot and boxes in this new, scaled-up warehouse.
# What is the sum of all boxes' final GPS coordinates?
#
#
# --- Solution ---
#
# The difference in this part is that the grid is now expanded horizontally,
# with boxes occupying 2 slots on x-axis, while the robot remains of 1x1 size.
# So, we modify the initial data processing with additional replaces of data
# in each row. We represent the boxes as tuples of 4 values (x1, y1, x2, y2),
# to keep information about both occupied slots by each box. The processing
# of moves remain the same in idea, although the part of checking whether
# the move can be performed is now more complex. For simplicity, the case
# of horizontal move and the case of vertical move is considered separately.
# For horizontal move (along x axis, dy = 0), the code is pretty much the same
# as in previous part – we continue checking next positions and include any
# additional boxes until we eventually encounter either a wall or empty space,
# which results in either ignoring the move or shifting everything by a single
# position in a given direction, respectively. For vertical move, the idea
# remains similar, however the complication is that the move may involve
# additional boxes that are shifted to the side by a single position:
#
#  []  []    []  [][]
#  []   []  []    []
#
# So, for each box to move, instead of checking one next position in a given
# direction, we need check both positions above/below (depending on direction)
# the box before making a move. At each position: we may hit a wall, which
# prevents any change in current move; we may find another boxes, which extend
# further the number of positions to check; or we may find nothing (the empty
# space). If we found nothing (no walls or boxes) for all positions to check,
# we can safely move all the encountered boxes by a single position. Finally,
# after processing all the moves, we return the answer, which is calculated
# exactly the same as previously (using only left coordinate of each box).
#
# There are a few minor parts in the code that can still be improved/optimized,
# however it is effective enough and remains clear in current state, therefore
# I decided to keep the code as it is now.
#

INPUT_FILE = 'input.txt'

BOX = 'O'
BOX2 = '[]'
ROBOT = '@'
ROBOT2 = '@.'
SPACE = '.'
SPACE2 = '..'
WALL = '#'
WALL2 = '##'

UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'


def main():
    with open(INPUT_FILE, 'r') as file:
        grid, moves = file.read().strip().split('\n\n')

    grid = tuple(row.replace(SPACE, SPACE2)
                    .replace(BOX, BOX2)
                    .replace(ROBOT, ROBOT2)
                    .replace(WALL, WALL2)
                 for row in grid.split('\n'))
    moves = tuple(moves.replace('\n', ''))

    walls = set()
    boxes = set()
    robot = (0, 0)

    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile == WALL:
                walls.add((x, y))
            if tile == BOX2[0]:
                boxes.add((x, y, x+1, y))
            if tile == ROBOT:
                robot = (x, y)

    for move in moves:
        if move == RIGHT:
            dx, dy = 1, 0
        elif move == LEFT:
            dx, dy = -1, 0
        elif move == UP:
            dx, dy = 0, -1
        elif move == DOWN:
            dx, dy = 0, 1

        rx, ry = robot

        nx = rx + dx
        ny = ry + dy

        if all([(nx, ny) not in walls,
                (nx, ny, nx + 1, ny) not in boxes,
                (nx - 1, ny, nx, ny) not in boxes]):
            robot = (nx, ny)

        elif (nx, ny) in walls:
            continue  # do nothing

        else:  # (nx, ny) in boxes
            if (nx, ny, nx + 1, ny) in boxes:
                to_move = [(nx, ny, nx + 1, ny)]
            else:
                to_move = [(nx - 1, ny, nx, ny)]

            # check if we can perform the move
            if move in (LEFT, RIGHT):  # horizontal move
                while True:
                    nx += dx
                    ny += dy

                    if (nx, ny) in walls:
                        to_move = []  # do nothing
                        break

                    elif (nx, ny, nx + 1, ny) in boxes:
                        if (nx, ny, nx + 1, ny) not in to_move:
                            to_move.append((nx, ny, nx + 1, ny))
                        continue

                    elif (nx - 1, ny, nx, ny) in boxes:
                        if (nx - 1, ny, nx, ny) not in to_move:
                            to_move.append((nx - 1, ny, nx, ny))
                        continue

                    else:  # found empty position
                        break

            else:  # vertical move, dx = 0
                while True:
                    possible = True
                    nextboxes = []

                    for (bx, by, _, _) in to_move:
                        if any([(bx, by + dy) in walls,
                                (bx + 1, by + dy) in walls]):
                            possible = False  # it hits the wall
                            break

                        else:  # is there a box above/below?
                            nextbox = (bx, by + dy, bx + 1, by + dy)
                            if nextbox in boxes and nextbox not in to_move:
                                nextboxes.append(nextbox)

                            nextbox = (bx - 1, by + dy, bx, by + dy)
                            if nextbox in boxes and nextbox not in to_move:
                                nextboxes.append(nextbox)

                            nextbox = (bx + 1, by + dy, bx + 2, by + dy)
                            if nextbox in boxes and nextbox not in to_move:
                                nextboxes.append(nextbox)

                    if not possible:
                        to_move = []  # do nothing
                        break

                    if not nextboxes:  # found empty position
                        break

                    for nextbox in nextboxes:
                        if nextbox not in to_move:
                            to_move.append(nextbox)

            if to_move:  # move the boxes and robot
                for (bx, by, _, _) in to_move:
                    boxes.remove((bx, by, bx + 1, by))
                for (bx, by, _, _) in to_move:
                    boxes.add((bx + dx, by + dy, bx + 1 + dx, by + dy))

                robot = (rx + dx, ry + dy)

    coords = []

    for box in boxes:
        x, y, _, _ = box
        coords.append(y * 100 + x)

    print(sum(coords))


if __name__ == '__main__':
    main()
