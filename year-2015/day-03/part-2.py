#!/usr/bin/env python3
#
# --- Day 3: Perfectly Spherical Houses in a Vacuum / Part Two ---
#
# The next year, to speed up the process, Santa creates a robot version
# of himself, Robo-Santa, to deliver presents with him.
#
# Santa and Robo-Santa start at the same location (delivering two presents
# to the same starting house), then take turns moving based on instructions
# from the elf, who is eggnoggedly reading from the same script
# as the previous year.
#
# This year, how many houses receive at least one present?
#
# For example:
# – ^v delivers presents to 3 houses, because Santa goes north,
#   and then Robo-Santa goes south.
# – ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa
#   end up back where they started.
# – ^v^v^v^v^v now delivers presents to 11 houses, with Santa going
#   one direction and Robo-Santa going the other.
#
#
# --- Solution ---
#
# The difference here is that we have two agents that move alternately. Hence,
# odd moves we apply to the first agent's position and the even moves we apply
# to the second agent's position. The rest remains the same – after every move
# we update the set of visited locations.
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
    positions = [complex(0, 0)] * 2
    visited = set(positions)

    for i, move in enumerate(moves):
        index = (i % 2)
        positions[index] += MOVE_TO_SHIFT[move]
        visited.add(positions[index])

    print(len(visited))


if __name__ == '__main__':
    main()
