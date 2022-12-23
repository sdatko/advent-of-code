#!/usr/bin/env python3
#
# --- Day 23: Unstable Diffusion ---
#
# You enter a large crater of gray dirt where the grove is supposed to be.
# All around you, plants you imagine were expected to be full of fruit are
# instead withered and broken. A large group of Elves has formed in the middle
# of the grove.
#
# "...but this volcano has been dormant for months. Without ash, the fruit
# can't grow!"
#
# You look up to see a massive, snow-capped mountain towering above you.
#
# "It's not like there are other active volcanoes here;
# we've looked everywhere."
#
# "But our scanners show active magma flows; clearly it's going somewhere."
#
# They finally notice you at the edge of the grove, your pack almost
# overflowing from the random star fruit you've been collecting.
# Behind you, elephants and monkeys explore the grove, looking concerned.
# Then, the Elves recognize the ash cloud slowly spreading above your
# recent detour.
#
# "Why do you--" "How is--" "Did you just--"
#
# Before any of them can form a complete question, another Elf speaks up:
# "Okay, new plan. We have almost enough fruit already, and ash from the plume
# should spread here eventually. If we quickly plant new seedlings now, we can
# still make it to the extraction point. Spread out!"
#
# The Elves each reach into their pack and pull out a tiny plant. The plants
# rely on important nutrients from the ash, so they can't be planted too close
# together.
#
# There isn't enough time to let the Elves figure out where to plant
# the seedlings themselves; you quickly scan the grove (your puzzle input)
# and note their positions.
#
# For example:
#
#   ....#..
#   ..###.#
#   #...#.#
#   .#...##
#   #.###..
#   ##.#.##
#   .#..#..
#
# The scan shows Elves # and empty ground .; outside your scan, more empty
# ground extends a long way in every direction. The scan is oriented so that
# north is up; orthogonal directions are written N (north), S (south),
# W (west), and E (east), while diagonal directions are written NE, NW, SE, SW.
#
# The Elves follow a time-consuming process to figure out where they should
# each go; you can speed up this process considerably. The process consists
# of some number of rounds during which Elves alternate between considering
# where to move and actually moving.
#
# During the first half of each round, each Elf considers the eight positions
# adjacent to themself. If no other Elves are in one of those eight positions,
# the Elf does not do anything during this round. Otherwise, the Elf looks
# in each of four directions in the following order and proposes moving one
# step in the first valid direction:
# – If there is no Elf in the N, NE, or NW adjacent positions,
#   the Elf proposes moving north one step.
# – If there is no Elf in the S, SE, or SW adjacent positions,
#   the Elf proposes moving south one step.
# – If there is no Elf in the W, NW, or SW adjacent positions,
#   the Elf proposes moving west one step.
# – If there is no Elf in the E, NE, or SE adjacent positions,
#   the Elf proposes moving east one step.
#
# After each Elf has had a chance to propose a move, the second half
# of the round can begin. Simultaneously, each Elf moves to their proposed
# destination tile if they were the only Elf to propose moving to that
# position. If two or more Elves propose moving to the same position,
# none of those Elves move.
#
# Finally, at the end of the round, the first direction the Elves considered
# is moved to the end of the list of directions. For example, during the second
# round, the Elves would try proposing a move to the south first, then west,
# then east, then north. On the third round, the Elves would first consider
# west, then east, then north, then south.
#
# As a smaller example, consider just these five Elves:
#
#   .....
#   ..##.
#   ..#..
#   .....
#   ..##.
#   .....
#
# The northernmost two Elves and southernmost two Elves all propose moving
# north, while the middle Elf cannot move north and proposes moving south.
# The middle Elf proposes the same destination as the southwest Elf,
# so neither of them move, but the other three do:
#
#   ..##.
#   .....
#   ..#..
#   ...#.
#   ..#..
#   .....
#
# Next, the northernmost two Elves and the southernmost Elf all propose moving
# south. Of the remaining middle two Elves, the west one cannot move south
# and proposes moving west, while the east one cannot move south or west
# and proposes moving east. All five Elves succeed in moving to their
# proposed positions:
#
#   .....
#   ..##.
#   .#...
#   ....#
#   .....
#   ..#..
#
# Finally, the southernmost two Elves choose not to move at all.
# Of the remaining three Elves, the west one proposes moving west,
# the east one proposes moving east, and the middle one proposes
# moving north; all three succeed in moving:
#
#   ..#..
#   ....#
#   #....
#   ....#
#   .....
#   ..#..
#
# At this point, no Elves need to move, and so the process ends.
#
# The larger example above proceeds as follows:
#
#   == Initial State ==
#   ..............
#   ..............
#   .......#......
#   .....###.#....
#   ...#...#.#....
#   ....#...##....
#   ...#.###......
#   ...##.#.##....
#   ....#..#......
#   ..............
#   ..............
#   ..............
#
#   == End of Round 1 ==
#   ..............
#   .......#......
#   .....#...#....
#   ...#..#.#.....
#   .......#..#...
#   ....#.#.##....
#   ..#..#.#......
#   ..#.#.#.##....
#   ..............
#   ....#..#......
#   ..............
#   ..............
#
#   == End of Round 2 ==
#   ..............
#   .......#......
#   ....#.....#...
#   ...#..#.#.....
#   .......#...#..
#   ...#..#.#.....
#   .#...#.#.#....
#   ..............
#   ..#.#.#.##....
#   ....#..#......
#   ..............
#   ..............
#
#   == End of Round 3 ==
#   ..............
#   .......#......
#   .....#....#...
#   ..#..#...#....
#   .......#...#..
#   ...#..#.#.....
#   .#..#.....#...
#   .......##.....
#   ..##.#....#...
#   ...#..........
#   .......#......
#   ..............
#
#   == End of Round 4 ==
#   ..............
#   .......#......
#   ......#....#..
#   ..#...##......
#   ...#.....#.#..
#   .........#....
#   .#...###..#...
#   ..#......#....
#   ....##....#...
#   ....#.........
#   .......#......
#   ..............
#
#   == End of Round 5 ==
#   .......#......
#   ..............
#   ..#..#.....#..
#   .........#....
#   ......##...#..
#   .#.#.####.....
#   ...........#..
#   ....##..#.....
#   ..#...........
#   ..........#...
#   ....#..#......
#   ..............
#
# After a few more rounds...
#
#   == End of Round 10 ==
#   .......#......
#   ...........#..
#   ..#.#..#......
#   ......#.......
#   ...#.....#..#.
#   .#......##....
#   .....##.......
#   ..#........#..
#   ....#.#..#....
#   ..............
#   ....#..#..#...
#   ..............
#
# To make sure they're on the right track, the Elves like to check after
# round 10 that they're making good progress toward covering enough ground.
# To do this, count the number of empty ground tiles contained by the smallest
# rectangle that contains every Elf. (The edges of the rectangle should be
# aligned to the N/S/E/W directions; the Elves do not have the patience
# to calculate arbitrary rectangles.) In the above example, that rectangle is:
#
#   ......#.....
#   ..........#.
#   .#.#..#.....
#   .....#......
#   ..#.....#..#
#   #......##...
#   ....##......
#   .#........#.
#   ...#.#..#...
#   ............
#   ...#..#..#..
#
# In this region, the number of empty ground tiles is 110.
#
# Simulate the Elves' process and find the smallest rectangle
# that contains the Elves after 10 rounds. How many empty ground tiles
# does that rectangle contain?
#
#
# --- Solution ---
#
# We start by reading the input into a list of coordinates of elves positions,
# enumerating every character in every line of given file (note it is important
# to enumerate lines with negative numbers [-y], so first line in file is above
# the second line in file). Then we perform defined actions in a loop a given
# number of times. We browse the set of elves to find the individuals that are
# expected to move (have any neighbor around) – for each such, we determine
# the direction of movement and save that in a dictionary of pairs: from -> to
# (source position and target position). Then we process the list of moves
# and for each unique move we update the corresponding elf position in set
# (which effectively means: we remove that position and add a new one to set).
# After everything done, we find the bounding box for the final coordinates
# and we calculate its area, then we remove the number of elves in simulation
# (assuming each elf occupy single area unit) to compute the number of free
# area units – this is our answer.
#

INPUT_FILE = 'input.txt'

ROUNDS = 10

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

    for _ in range(ROUNDS):
        moves = dict()

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

        # end of the round – shift proposals
        PROPOSALS.append(PROPOSALS.pop(0))

    # calculate how big area was covered
    x_min = min([int(elf.real) for elf in elves])
    x_max = max([int(elf.real) for elf in elves])
    y_min = min([int(elf.imag) for elf in elves])
    y_max = max([int(elf.imag) for elf in elves])

    area = (y_max - y_min + 1) * (x_max - x_min + 1)
    free_units = area - len(elves)

    print(free_units)


if __name__ == '__main__':
    main()
