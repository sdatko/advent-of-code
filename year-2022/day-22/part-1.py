#!/usr/bin/env python3
#
# --- Day 22: Monkey Map ---
#
# The monkeys take you on a surprisingly easy trail through the jungle.
# They're even going in roughly the right direction according to your handheld
# device's Grove Positioning System.
#
# As you walk, the monkeys explain that the grove is protected by a force
# field. To pass through the force field, you have to enter a password;
# doing so involves tracing a specific path on a strangely-shaped board.
#
# At least, you're pretty sure that's what you have to do; the elephants
# aren't exactly fluent in monkey.
#
# The monkeys give you notes that they took when they last saw the password
# entered (your puzzle input).
#
# For example:
#
#           ...#
#           .#..
#           #...
#           ....
#   ...#.......#
#   ........#...
#   ..#....#....
#   ..........#.
#           ...#....
#           .....#..
#           .#......
#           ......#.
#
#   10R5L5R10L4R5L5
#
# The first half of the monkeys' notes is a map of the board. It is comprised
# of a set of open tiles (on which you can move, drawn .) and solid walls
# (tiles which you cannot enter, drawn #).
#
# The second half is a description of the path you must follow. It consists
# of alternating numbers and letters:
# – A number indicates the number of tiles to move in the direction you are
#   facing. If you run into a wall, you stop moving forward and continue with
#   the next instruction.
# – A letter indicates whether to turn 90 degrees clockwise (R)
#   or counterclockwise (L). Turning happens in-place;
#   it does not change your current tile.
#
# So, a path like 10R5 means "go forward 10 tiles, then turn clockwise
# 90 degrees, then go forward 5 tiles".
#
# You begin the path in the leftmost open tile of the top row of tiles.
# Initially, you are facing to the right (from the perspective of how
# the map is drawn).
#
# If a movement instruction would take you off of the map, you wrap around
# to the other side of the board. In other words, if your next tile is off
# of the board, you should instead look in the direction opposite of your
# current facing as far as you can until you find the opposite edge of
# the board, then reappear there.
#
# For example, if you are at A and facing to the right, the tile in front
# of you is marked B; if you are at C and facing down, the tile in front
# of you is marked D:
#
#           ...#
#           .#..
#           #...
#           ....
#   ...#.D.....#
#   ........#...
#   B.#....#...A
#   .....C....#.
#           ...#....
#           .....#..
#           .#......
#           ......#.
#
# It is possible for the next tile (after wrapping around) to be a wall;
# this still counts as there being a wall in front of you, and so movement
# stops before you actually wrap to the other side of the board.
#
# By drawing the last facing you had with an arrow on each tile you visit,
# the full path taken by the above example looks like this:
#
#           >>v#
#           .#v.
#           #.v.
#           ..v.
#   ...#...v..v#
#   >>>v...>#.>>
#   ..#v...#....
#   ...>>>>v..#.
#           ...#....
#           .....#..
#           .#......
#           ......#.
#
# To finish providing the password to this strange input device, you need
# to determine numbers for your final row, column, and facing as your final
# position appears from the perspective of the original map. Rows start from 1
# at the top and count downward; columns start from 1 at the left and count
# rightward. (In the above example, row 1, column 1 refers to the empty space
# with no tile on it in the top-left corner.) Facing is 0 for right (>),
# 1 for down (v), 2 for left (<), and 3 for up (^). The final password
# is the sum of 1000 times the row, 4 times the column, and the facing.
#
# In the above example, the final row is 6,
# the final column is 8, and the final facing is 0.
# So, the final password is 1000 * 6 + 4 * 8 + 0: 6032.
#
# Follow the path given in the monkeys' notes. What is the final password?
#
#
# --- Solution ---
#
# We start by reading the input into a list of moves to perform and an arena
# where the moves are performed. For this, the file is split over empty line
# (\n\n) into two parts. First part is processed into a map of coordinates
# where the characters correspond to interesting positions or obstacles.
# Second part if split into a list of numeric values and characters `L` or `R`
# after introducing additional spaces around the letters.
# The initial position is at the first occurrence of a dot `.` character
# in the first row of input. The initial direction is a vector to the right.
# Then we conduct moves in a loop. If the next move is a letter, either L or R,
# we perform a clockwise or counter-clockwise turn of our direction vector.
# Otherwise it is a number specifying how many steps to do. For every step
# we verify if the next position is a valid point in defined arena – if so,
# then we perform it as long as the next position is not a wall (in such case
# we break the inner loop for steps and we proceed to next move). If the next
# position is not a part of our arena, i.e. we crossed the boundary, then
# we need to calculate a new position assuming the edges are teleporting us.
# In the implementation with a map of allowed coordinates, this can be achieved
# by subtracting the current direction vector from current position as long as
# it is possible; then we continue with next move from the reached location.
# Finally we translate the reached coordinates and direction using formula
# as given in the description to return the answer.
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

                # wrap if we are out of the drawing
                if new_position not in arena:
                    while (new_position - direction) in arena:
                        new_position -= direction

                # stop when the next position is a solid wall
                if arena[new_position] == '#':
                    break

                # otherwise proceed to the next position
                position = new_position

    password = 1000 * (position.imag) + 4 * (position.real)
    password += list(DIRECTIONS.values()).index(direction)

    print(int(password))


if __name__ == '__main__':
    main()
