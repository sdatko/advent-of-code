#!/usr/bin/env python3
#
# --- Day 23: Unstable Diffusion / Part Two ---
#
# It seems you're on the right track. Finish simulating the process and figure
# out where the Elves need to go. How many rounds did you save them?
#
# In the example above, the first round where no Elf moved was round 20:
#
#   .......#......
#   ....#......#..
#   ..#.....#.....
#   ......#.......
#   ...#....#.#..#
#   #.............
#   ....#.....#...
#   ..#.....#.....
#   ....#.#....#..
#   .........#....
#   ....#......#..
#   .......#......
#
# Figure out where the Elves need to go.
# What is the number of the first round where no Elf moves?
#
#
# --- Solution ---
#
# The difference in this part is that instead of a running for a fixed number
# of rounds, we launch the simulation as long as there are any moves performed.
# The final answer is a number of final round that was run.
#

INPUT_FILE = 'input.txt'

DIRECTIONS = {
    'N': complex(0, 1),
    'S': complex(0, -1),
    'E': complex(1, 0),
    'W': complex(-1, 0),
    'NE': complex(1, 1),
    'SE': complex(1, -1),
    'NW': complex(-1, 1),
    'SW': complex(-1, -1),
}

PROPOSALS = ['N', 'S', 'W', 'E']


def neighborhood(elf):
    return (
        elf + DIRECTIONS['N'],
        elf + DIRECTIONS['S'],
        elf + DIRECTIONS['E'],
        elf + DIRECTIONS['W'],
        elf + DIRECTIONS['NE'],
        elf + DIRECTIONS['SE'],
        elf + DIRECTIONS['NW'],
        elf + DIRECTIONS['SW'],
    )


def side(elf, direction):
    if direction == 'N':
        return (
            elf + DIRECTIONS['NE'],
            elf + DIRECTIONS['N'],
            elf + DIRECTIONS['NW'],
        )
    elif direction == 'S':
        return (
            elf + DIRECTIONS['SE'],
            elf + DIRECTIONS['S'],
            elf + DIRECTIONS['SW'],
        )
    elif direction == 'E':
        return (
            elf + DIRECTIONS['NE'],
            elf + DIRECTIONS['E'],
            elf + DIRECTIONS['SE'],
        )
    elif direction == 'W':
        return (
            elf + DIRECTIONS['NW'],
            elf + DIRECTIONS['W'],
            elf + DIRECTIONS['SW'],
        )


def main():
    with open(INPUT_FILE, 'r') as file:
        elves = {complex(x, -y)
                 for y, row in enumerate(file.readlines())
                 for x, character in enumerate(row)
                 if character in ('#')}

    round = 0

    while True:
        moved = False
        moves = dict()
        round += 1

        # first half
        for elf in elves:
            # if there is other elf in the neighborhood
            if any(neighbor in elves for neighbor in neighborhood(elf)):
                # find first possible move proposal
                for direction in PROPOSALS:
                    if all(pos not in elves for pos in side(elf, direction)):
                        moves[elf] = elf + DIRECTIONS[direction]
                        break

        # second half
        new_positions = list(moves.values())

        # move elves who chose unique positions
        for elf, new_position in moves.items():
            if new_positions.count(new_position) == 1:
                elves.remove(elf)
                elves.add(new_position)
                moved = True

        # end of the round – shift proposals
        PROPOSALS.append(PROPOSALS.pop(0))

        # exit condition
        if not moved:
            break

    # return the number of last round
    print(round)


if __name__ == '__main__':
    main()
