#!/usr/bin/env python3
#
# --- Day 22: Monkey Map / Part Two ---
#
# As you reach the force field, you think you hear some Elves in the distance.
# Perhaps they've already arrived?
#
# You approach the strange input device, but it isn't quite what the monkeys
# drew in their notes. Instead, you are met with a large cube; each of its six
# faces is a square of 50x50 tiles.
#
# To be fair, the monkeys' map does have six 50x50 regions on it. If you were
# to carefully fold the map, you should be able to shape it into a cube!
#
# In the example above, the six (smaller, 4x4) faces of the cube are:
#
#           1111
#           1111
#           1111
#           1111
#   222233334444
#   222233334444
#   222233334444
#   222233334444
#           55556666
#           55556666
#           55556666
#           55556666
#
# You still start in the same position and with the same facing as before,
# but the wrapping rules are different. Now, if you would walk off the board,
# you instead proceed around the cube. From the perspective of the map, this
# can look a little strange. In the above example, if you are at A and move
# to the right, you would arrive at B facing down; if you are at C and move
# down, you would arrive at D facing up:
#
#           ...#
#           .#..
#           #...
#           ....
#   ...#.......#
#   ........#..A
#   ..#....#....
#   .D........#.
#           ...#..B.
#           .....#..
#           .#......
#           ..C...#.
#
# Walls still block your path, even if they are on a different face
# of the cube. If you are at E facing up, your movement is blocked
# by the wall marked by the arrow:
#
#           ...#
#           .#..
#        -->#...
#           ....
#   ...#..E....#
#   ........#...
#   ..#....#....
#   ..........#.
#           ...#....
#           .....#..
#           .#......
#           ......#.
#
# Using the same method of drawing the last facing you had with an arrow
# on each tile you visit, the full path taken by the above example now looks
# like this:
#
#           >>v#
#           .#v.
#           #.v.
#           ..v.
#   ...#..^...v#
#   .>>>>>^.#.>>
#   .^#....#....
#   .^........#.
#           ...#..v.
#           .....#v.
#           .#v<<<<.
#           ..v...#.
#
# The final password is still calculated from your final position and facing
# from the perspective of the map. In this example, the final row is 5,
# the final column is 7, and the final facing is 3, so the final password
# is 1000 * 5 + 4 * 7 + 3 = 5031.
#
# Fold the map into a cube, then follow the path given in the monkeys' notes.
# What is the final password?
#
#
# --- Solution ---
#
# The difference here is that when stepping out of arena, the calculation
# of next point is much more complicated, because of our map being a 2D image
# of the unfolded 3D cube surface. The easiest approach here is to visualize
# the original shape using for example a Rubik's Cube or paper-cut model
# and then discovering the transitions. Below is a helper drawing.
#
#       1   50  100  150
#      +--------------->
#     1|
#      |     +---+---+
#      |     |AAA|BBB|
#      |     |AAA|BBB|
#      |     |AAA|BBB|
#    50|     +---+---+
#      |     |CCC|
#      |     |CCC|
#      |     |CCC|
#   100| +---+---+
#      | |EEE|DDD|
#      | |EEE|DDD|
#      | |EEE|DDD|
#   150| +---+---+
#      | |FFF|
#      | |FFF|
#      | |FFF|
#   200| +---+
#      |
#      v
#
# It is important to notice that when moving around the drawing, everything
# is exactly like the previous example. However, when stepping out of arena,
# not only the reached face is different, but also the direction vector shall
# change in effect: for example, when moving from face B down, on a folded
# cube, we would end on face C, moving from its right edge to the left.
# As seen above, there are 14 edges (3 from faces F and B; 2 from faces E, D,
# C, A) and probably the easiest approach is to consider all of the cases
# separately and write appropriate conditionals for moves. All possible paths
# are illustrated below.
#
#   +----------+     +------+
#   |          |     |      |
#   |         +---+---+     |
#   |         |AAA|BBB|     |
#   |  +------|AAA|BBB|--+  |
#   |  |      |AAA|BBB|  |  |
#   |  |      +---+---+  |  |
#   |  |   +--|CCC|  |   |  |
#   |  |   |  |CCC|  |   |  |
#   |  |   |  |CCC|--+   |  |
#   |  |  +---+---+      |  |
#   |  |  |EEE|DDD|      |  |
#   |  +--|EEE|DDD|------+  |
#   |     |EEE|DDD|         |
#   |     +---+---+         |
#   +-----|FFF|  |          |
#         |FFF|  |          |
#         |FFF|--+          |
#         +---+             |
#            |              |
#            +--------------+
#
# Note that the transitions are reversible, i.e. going right form B moves us
# into D with left direction – and going right from D moves us into B with
# the same left direction in the end.
# The code below only works for the given layout of map. A general solution
# should be possible, as from what I checked for every edge there would be
# up to 6 possible transitions to analyse (e.g. for move towards right edge
# we could end on a face that is 1, 2 or 3 faces below – or up – in drawing).
#
#   +---+
#   |AAA|
#   |AAA|---------+
#   |AAA|         |
#   +---+         |
#   |BBB|         |
#   |BBB|------+  |
#   |BBB|      |  |
#   +---+      |  |
#   |CCC|--+   |  |
#   |CCC|  |   |  |
#   |CCC|  |   |  |
#   +---+---+  |  |
#   |DDD|EEE|  |  |
#   |DDD|EEE|--+  |
#   |DDD|EEE|     |
#   +---+---+     |
#         |       |
#         +-------+
#
# The other option would be to translate the map into a 3D grid and consider
# all moves in that space. However, considering lack of time before Christmas
# I did not implemented it yet. Maybe at some point in the future...
#

INPUT_FILE = 'input.txt'

DIRECTIONS = {
    'right': complex(1, 0),
    'down': complex(0, 1),
    'left': complex(-1, 0),
    'up': complex(0, -1),
}


def main():
    with open(INPUT_FILE, 'r') as file:
        data = file.read().split('\n\n')
        arena = {complex(x + 1, y + 1): character
                 for y, row in enumerate(data[0].splitlines())
                 for x, character in enumerate(row)
                 if character in ('.', '#')}
        moves = [int(move) if move.isnumeric() else move
                 for move in data[1].replace('L', ' L ')
                                    .replace('R', ' R ')
                                    .strip()
                                    .split()]

    position = complex(data[0].index('.') + 1, 1)
    direction = DIRECTIONS['right']

    for move in moves:
        # we turn
        if isinstance(move, str):
            if move == 'L':
                direction *= -1j
            else:
                direction *= 1j

        # we move forward
        else:
            for step in range(move):
                # calculate the next position
                new_position = position + direction

                # the new position is in the drawing
                if new_position in arena:
                    # stop when the next position is a solid wall
                    if arena[new_position] == '#':
                        break

                    # otherwise proceed to the next position
                    position = new_position

                # we are out of the drawing
                else:
                    x = int(position.real)
                    y = int(position.imag)

                    if direction == DIRECTIONS['right']:
                        if x == 150:  # from B to D
                            new_position = complex(100, 151 - y)
                            new_direction = DIRECTIONS['left']

                        elif x == 100:
                            if 51 <= y <= 100:  # from C to B
                                new_position = complex(100 + (y - 50), 50)
                                new_direction = DIRECTIONS['up']

                            elif 101 <= y <= 150:  # from D to to B
                                new_position = complex(150, 51 - (y - 100))
                                new_direction = DIRECTIONS['left']

                        elif x == 50:  # from F to D
                            new_position = complex(50 + (y - 150), 150)
                            new_direction = DIRECTIONS['up']

                    elif direction == DIRECTIONS['left']:
                        if x == 51:
                            if 1 <= y <= 50:  # from A to E
                                new_position = complex(1, 151 - y)
                                new_direction = DIRECTIONS['right']

                            elif 51 <= y <= 100:  # from C to E
                                new_position = complex(y - 50, 101)
                                new_direction = DIRECTIONS['down']

                        elif x == 1:
                            if 101 <= y <= 150:  # from E to A
                                new_position = complex(51, 1 + (150 - y))
                                new_direction = DIRECTIONS['right']

                            elif 151 <= y <= 200:  # from F to A
                                new_position = complex(y - 150 + 50, 1)
                                new_direction = DIRECTIONS['down']

                    elif direction == DIRECTIONS['up']:
                        if y == 1:
                            if 51 <= x <= 100:  # from A to F
                                new_position = complex(1, x + 100)
                                new_direction = DIRECTIONS['right']

                            elif 101 <= x <= 150:  # from B to F
                                new_position = complex(x - 100, 200)
                                new_direction = DIRECTIONS['up']

                        elif y == 101:  # from E to C
                            new_position = complex(51, x + 50)
                            new_direction = DIRECTIONS['right']

                    elif direction == DIRECTIONS['down']:
                        if y == 50:  # from B to C
                            new_position = complex(100, x - 50)
                            new_direction = DIRECTIONS['left']

                        elif y == 150:  # from D to F
                            new_position = complex(50, x + 100)
                            new_direction = DIRECTIONS['left']

                        elif y == 200:  # from F to B
                            new_position = complex(x + 100, 1)
                            new_direction = DIRECTIONS['down']

                    # stop when the next position is a solid wall
                    if arena[new_position] == '#':
                        break

                    # otherwise proceed to the next position
                    position = new_position
                    direction = new_direction

    password = 1000 * (position.imag) + 4 * (position.real)
    password += list(DIRECTIONS.values()).index(direction)

    print(int(password))


if __name__ == '__main__':
    main()
