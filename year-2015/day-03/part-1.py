#!/usr/bin/env python3
#
# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
#
# Santa is delivering presents to an infinite two-dimensional grid of houses.
#
# He begins by delivering a present to the house at his starting location,
# and then an elf at the North Pole calls him via radio and tells him where
# to move next. Moves are always exactly one house to the north (^), south (v),
# east (>), or west (<). After each move, he delivers another present
# to the house at his new location.
#
# However, the elf back at the north pole has had a little too much eggnog,
# and so his directions are a little off, and Santa ends up visiting some
# houses more than once. How many houses receive at least one present?
#
# For example:
# – > delivers presents to 2 houses: one at the starting location,
#   and one to the east.
# – ^>v< delivers presents to 4 houses in a square, including twice
#   to the house at his starting/ending location.
# – ^v^v^v^v^v delivers a bunch of presents to some very lucky children
#   at only 2 houses.
#
#
# --- Solution ---
#
# We start by reading the input file into a tuple of characters – the moves
# to perform. We create a helper mapping that translates the move characters
# to coordinates shifts in 2D grid. Then, from a starting position, we process
# the list of moves, every time calculating a new position. We use the set
# of visited positions to track the unique locations visited in the process.
# Finally, as an answer, we return the number of elements in our set.
#

INPUT_FILE = 'input.txt'

MOVE_TO_SHIFT = {
    '>': complex(1, 0),  # right
    '^': complex(0, -1),  # up
    '<': complex(-1, 0),  # left
    'v': complex(0, 1),  # down
}


def main():
    with open(INPUT_FILE, 'r') as file:
        moves = tuple(file.read().strip())

    # starting location
    position = complex(0, 0)
    visited = set([position])

    for move in moves:
        position += MOVE_TO_SHIFT[move]
        visited.add(position)

    print(len(visited))


if __name__ == '__main__':
    main()
