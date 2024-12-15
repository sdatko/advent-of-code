#!/usr/bin/env python3
#
# --- Day 15: Warehouse Woes ---
#
# You appear back inside your own mini submarine! Each Historian drives
# their mini submarine in a different direction; maybe the Chief has his
# own submarine down here somewhere as well?
#
# You look up to see a vast school of lanternfish swimming past you.
# On closer inspection, they seem quite anxious, so you drive your mini
# submarine over to see if you can help.
#
# Because lanternfish populations grow rapidly, they need a lot of food,
# and that food needs to be stored somewhere. That's why these lanternfish
# have built elaborate warehouse complexes operated by robots!
#
# These lanternfish seem so anxious because they have lost control of the robot
# that operates one of their most important warehouses! It is currently running
# amok, pushing around boxes in the warehouse with no regard for lanternfish
# logistics or lanternfish inventory management strategies.
#
# Right now, none of the lanternfish are brave enough to swim up to
# an unpredictable robot so they could shut it off. However, if you could
# anticipate the robot's movements, maybe they could find a safe option.
#
# The lanternfish already have a map of the warehouse and a list of movements
# the robot will attempt to make (your puzzle input). The problem is that
# the movements will sometimes fail as boxes are shifted around, making
# the actual movements of the robot difficult to predict.
#
# For example:
#
#   ##########
#   #..O..O.O#
#   #......O.#
#   #.OO..O.O#
#   #..O@..O.#
#   #O#..O...#
#   #O..O..O.#
#   #.OO.O.OO#
#   #....O...#
#   ##########
#
#   <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
#   vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
#   ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
#   <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
#   ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
#   ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
#   >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
#   <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
#   ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
#   v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
#
# As the robot (@) attempts to move, if there are any boxes (O) in the way,
# the robot will also attempt to push those boxes. However, if this action
# would cause the robot or a box to move into a wall (#), nothing moves
# instead, including the robot. The initial positions of these are shown
# on the map at the top of the document the lanternfish gave you.
#
# The rest of the document describes the moves (^ for up, v for down,
# < for left, > for right) that the robot will attempt to make, in order.
# (The moves form a single giant sequence; they are broken into multiple
# lines just to make copy-pasting easier. Newlines within the move sequence
# should be ignored.)
#
# Here is a smaller example to get started:
#
#   ########
#   #..O.O.#
#   ##@.O..#
#   #...O..#
#   #.#.O..#
#   #...O..#
#   #......#
#   ########
#
#   <^^>>>vv<v>>v<<
#
# Were the robot to attempt the given sequence of moves,
# it would push around the boxes as follows:
#
#   Initial state:
#   ########
#   #..O.O.#
#   ##@.O..#
#   #...O..#
#   #.#.O..#
#   #...O..#
#   #......#
#   ########
#
#   Move <:
#   ########
#   #..O.O.#
#   ##@.O..#
#   #...O..#
#   #.#.O..#
#   #...O..#
#   #......#
#   ########
#
#   Move ^:
#   ########
#   #.@O.O.#
#   ##..O..#
#   #...O..#
#   #.#.O..#
#   #...O..#
#   #......#
#   ########
#
#   Move ^:
#   ########
#   #.@O.O.#
#   ##..O..#
#   #...O..#
#   #.#.O..#
#   #...O..#
#   #......#
#   ########
#
#   Move >:
#   ########
#   #..@OO.#
#   ##..O..#
#   #...O..#
#   #.#.O..#
#   #...O..#
#   #......#
#   ########
#
#   Move >:
#   ########
#   #...@OO#
#   ##..O..#
#   #...O..#
#   #.#.O..#
#   #...O..#
#   #......#
#   ########
#
#   Move >:
#   ########
#   #...@OO#
#   ##..O..#
#   #...O..#
#   #.#.O..#
#   #...O..#
#   #......#
#   ########
#
#   Move v:
#   ########
#   #....OO#
#   ##..@..#
#   #...O..#
#   #.#.O..#
#   #...O..#
#   #...O..#
#   ########
#
#   Move v:
#   ########
#   #....OO#
#   ##..@..#
#   #...O..#
#   #.#.O..#
#   #...O..#
#   #...O..#
#   ########
#
#   Move <:
#   ########
#   #....OO#
#   ##.@...#
#   #...O..#
#   #.#.O..#
#   #...O..#
#   #...O..#
#   ########
#
#   Move v:
#   ########
#   #....OO#
#   ##.....#
#   #..@O..#
#   #.#.O..#
#   #...O..#
#   #...O..#
#   ########
#
#   Move >:
#   ########
#   #....OO#
#   ##.....#
#   #...@O.#
#   #.#.O..#
#   #...O..#
#   #...O..#
#   ########
#
#   Move >:
#   ########
#   #....OO#
#   ##.....#
#   #....@O#
#   #.#.O..#
#   #...O..#
#   #...O..#
#   ########
#
#   Move v:
#   ########
#   #....OO#
#   ##.....#
#   #.....O#
#   #.#.O@.#
#   #...O..#
#   #...O..#
#   ########
#
#   Move <:
#   ########
#   #....OO#
#   ##.....#
#   #.....O#
#   #.#O@..#
#   #...O..#
#   #...O..#
#   ########
#
#   Move <:
#   ########
#   #....OO#
#   ##.....#
#   #.....O#
#   #.#O@..#
#   #...O..#
#   #...O..#
#   ########
#
# The larger example has many more moves; after the robot has finished
# those moves, the warehouse would look like this:
#
#   ##########
#   #.O.O.OOO#
#   #........#
#   #OO......#
#   #OO@.....#
#   #O#.....O#
#   #O.....OO#
#   #O.....OO#
#   #OO....OO#
#   ##########
#
# The lanternfish use their own custom Goods Positioning System (GPS for short)
# to track the locations of the boxes. The GPS coordinate of a box is equal to
# 100 times its distance from the top edge of the map plus its distance from
# the left edge of the map. (This process does not stop at wall tiles; measure
# all the way to the edges of the map.)
#
# So, the box shown below has a distance of 1 from the top edge of the map
# and 4 from the left edge of the map, resulting in a GPS coordinate of
# 100 * 1 + 4 = 104.
#
#   #######
#   #...O..
#   #......
#
# The lanternfish would like to know the sum of all boxes' GPS coordinates
# after the robot finishes moving. In the larger example, the sum of all
# boxes' GPS coordinates is 10092. In the smaller example, the sum is 2028.
#
# Predict the motion of the robot and boxes in the warehouse. After the robot
# is finished moving, what is the sum of all boxes' GPS coordinates?
#
#
# --- Solution ---
#
# We start by reading the input into a 2-dimensional grid and list of moves,
# by splitting the data over two newlines, then by splitting the first part
# (grid) over newlines and removing the newlines from the second part (moves).
# Next, we browse the grid to identify the (x, y) coordinates of walls, boxes
# and robot. Then, we perform moves in a loop: in each iteration we decode
# the next move to a transition vector (dx, dy) and we calculate the expected
# next position of a robot. If the next position is empty, i.e. no wall or
# or box on that position, we simply move the bot; if there is a wall, we skip
# that move; otherwise, there is a box and we need to check if we can move
# that box as well. In the last case, we build a collection of boxes to move
# and we continue checking next positions in the given direction of move:
# if there is another box, we add it to collection and continue checking;
# if there is a wall, we cannot move anything to that directions; otherwise
# we found a single empty space, so we can move a robot and all the boxes
# by a single position in the given direction (dx, dy). Finally, after all
# moves were performed, we calculate the GPS coordinates scores for all final
# boxes positions and we return the sum of the scores as an answer.
#

INPUT_FILE = 'input.txt'

BOX = 'O'
ROBOT = '@'
WALL = '#'

UP = '^'
DOWN = 'v'
LEFT = '<'
RIGHT = '>'


def main():
    with open(INPUT_FILE, 'r') as file:
        grid, moves = file.read().strip().split('\n\n')

    grid = tuple(row for row in grid.split('\n'))
    moves = tuple(moves.replace('\n', ''))

    walls = set()
    boxes = set()
    robot = (0, 0)

    for y, row in enumerate(grid):
        for x, tile in enumerate(row):
            if tile == WALL:
                walls.add((x, y))
            if tile == BOX:
                boxes.add((x, y))
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

        if (nx, ny) not in walls and (nx, ny) not in boxes:
            robot = (nx, ny)

        elif (nx, ny) in walls:
            continue  # do nothing

        else:  # (nx, ny) in boxes
            to_move = [(nx, ny)]

            # check if we can perform the move
            while True:
                nx += dx
                ny += dy

                if (nx, ny) in walls:
                    to_move = []  # do nothing
                    break

                elif (nx, ny) in boxes:
                    to_move.append((nx, ny))
                    continue

                else:  # found empty position
                    break

            if to_move:  # move the boxes and robot
                for (bx, by) in to_move:
                    boxes.remove((bx, by))
                for (bx, by) in to_move:
                    boxes.add((bx + dx, by + dy))

                robot = (rx + dx, ry + dy)

    coords = []

    for box in boxes:
        x, y = box
        coords.append(y * 100 + x)

    print(sum(coords))


if __name__ == '__main__':
    main()
