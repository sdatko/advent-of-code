#!/usr/bin/env python3
#
# --- Day 23: Amphipod ---
#
# A group of amphipods notice your fancy submarine and flag you down.
# "With such an impressive shell," one amphipod says, "surely you can
# help us with a question that has stumped our best scientists."
#
# They go on to explain that a group of timid, stubborn amphipods live in
# a nearby burrow. Four types of amphipods live there: Amber (A), Bronze (B),
# Copper (C), and Desert (D). They live in a burrow that consists of a hallway
# and four side rooms. The side rooms are initially full of amphipods, and
# the hallway is initially empty.
#
# They give you a diagram of the situation (your puzzle input), including
# locations of each amphipod (A, B, C, or D, each of which is occupying
# an otherwise open space), walls (#), and open space (.).
#
# For example:
#   #############
#   #...........#
#   ###B#C#B#D###
#     #A#D#C#A#
#     #########
#
# The amphipods would like a method to organize every amphipod into side rooms
# so that each side room contains one type of amphipod and the types are sorted
# A-D going left to right, like this:
#   #############
#   #...........#
#   ###A#B#C#D###
#     #A#B#C#D#
#     #########
#
# Amphipods can move up, down, left, or right so long as they are moving into
# an unoccupied open space. Each type of amphipod requires a different amount
# of energy to move one step: Amber amphipods require 1 energy per step, Bronze
# amphipods require 10 energy, Copper amphipods require 100, and Desert ones
# require 1000. The amphipods would like you to find a way to organize the
# amphipods that requires the least total energy.
#
# However, because they are timid and stubborn, the amphipods have some
# extra rules:
# - Amphipods will never stop on the space immediately outside any room.
#   They can move into that space so long as they immediately continue moving.
#   (Specifically, this refers to the four open spaces in the hallway that are
#   directly above an amphipod starting position.)
# - Amphipods will never move from the hallway into a room unless that room
#   is their destination room and that room contains no amphipods which do not
#   also have that room as their own destination. If an amphipod's starting
#   room is not its destination room, it can stay in that room until it leaves
#   the room. (For example, an Amber amphipod will not move from the hallway
#   into the right three rooms, and will only move into the leftmost room
#   if that room is empty or if it only contains other Amber amphipods.)
# - Once an amphipod stops moving in the hallway, it will stay in that spot
#   until it can move into a room. (That is, once any amphipod starts moving,
#   any other amphipods currently in the hallway are locked in place and will
#   not move again until they can move fully into a room.)
#
# In the above example, the amphipods can be organized using a minimum of 12521
# energy. One way to do this is shown below.
#
# Starting configuration:
#   #############
#   #...........#
#   ###B#C#B#D###
#     #A#D#C#A#
#     #########
#
# One Bronze amphipod moves into the hallway, taking 4 steps and using
# 40 energy:
#   #############
#   #...B.......#
#   ###B#C#.#D###
#     #A#D#C#A#
#     #########
#
# The only Copper amphipod not in its side room moves there, taking 4 steps
# and using 400 energy:
#   #############
#   #...B.......#
#   ###B#.#C#D###
#     #A#D#C#A#
#     #########
#
# A Desert amphipod moves out of the way, taking 3 steps and using 3000 energy,
# and then the Bronze amphipod takes its place, taking 3 steps and using
# 30 energy:
#   #############
#   #.....D.....#
#   ###B#.#C#D###
#     #A#B#C#A#
#     #########
#
# The leftmost Bronze amphipod moves to its room using 40 energy:
#   #############
#   #.....D.....#
#   ###.#B#C#D###
#     #A#B#C#A#
#     #########
#
# Both amphipods in the rightmost room move into the hallway, using 2003 energy
# in total:
#   #############
#   #.....D.D.A.#
#   ###.#B#C#.###
#     #A#B#C#.#
#     #########
#
# Both Desert amphipods move into the rightmost room using 7000 energy:
#   #############
#   #.........A.#
#   ###.#B#C#D###
#     #A#B#C#D#
#     #########
#
# Finally, the last Amber amphipod moves into its room, using 8 energy:
#   #############
#   #...........#
#   ###A#B#C#D###
#     #A#B#C#D#
#     #########
#
# What is the least energy required to organize the amphipods?
#
#
# --- Solution ---
#
# I initially solved this by hand, using LibreOffice Calc to draw conveniently
# the corridor and rooms representation, as there are not really that many ways
# the problem can be solved. On my second try I got the correct answer. Below
# is the step-by-step solution. My initial puzzle input was like this:
#   #############
#   #...........#
#   ###B#B#D#D###
#     #C#A#A#C#
#     #########
# We start by extracting D and C from the last room. Total cost is 2 * 1000
# + 3 * 100 to do this.
#   #############
#   #.......D.C.#
#   ###B#B#D#.###
#     #C#A#A#.#
#     #########
# Then we can move D from corridor to its target position in room 4, and right
# after that we can move D from the room 3 to corresponding position in room 4.
# The total cost is 3 * 1000 for first amphipod and 4 * 1000 for the second.
#   #############
#   #.........C.#
#   ###B#B#.#D###
#     #C#A#A#D#
#     #########
# Now we move both B and A out of room 2, for the energy of 5 * 1 + 2 * 10.
#   #############
#   #.A...B...C.#
#   ###B#.#.#D###
#     #C#.#A#D#
#     #########
# This allows us to move B from room 1 and B from corridor to their target
# positions in room 2 for the total cost of 5 * 10 + 2 * 10.
#   #############
#   #.A.......C.#
#   ###.#B#.#D###
#     #C#B#A#D#
#     #########
# Now we move A out of room 3 to let C from room 1 go there. The cost is 3 * 1.
#   #############
#   #.A.....A.C.#
#   ###.#B#.#D###
#     #C#B#.#D#
#     #########
# So we move C from room 1 to room 3 with cost of 8 * 100.
#   #############
#   #.A.....A.C.#
#   ###.#B#.#D###
#     #.#B#C#D#
#     #########
# Then we move both A from corridor to their destination in room 1. Energy cost
# is 3 * 1 + 6 * 1.
#   #############
#   #.........C.#
#   ###A#B#.#D###
#     #A#B#C#D#
#     #########
# Finally we move C from corridor to room 3 for the energy cost 4 * 100.
# We finish with proper organisation of amphipods.
#   #############
#   #...........#
#   ###A#B#C#D###
#     #A#B#C#D#
#     #########
# As final answer we simply print the sum of all intermediate energy costs.
#

INPUT_FILE = 'input.txt'


def main():
    energy = 0
    energy += 2 * 1000 + 3 * 100
    energy += 3 * 1000 + 4 * 1000
    energy += 5 * 1 + 2 * 10
    energy += 5 * 10 + 2 * 10
    energy += 3 * 1
    energy += 8 * 100
    energy += 3 * 1 + 6 * 1
    energy += 4 * 100
    print(energy)


if __name__ == '__main__':
    main()
