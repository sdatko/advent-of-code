#!/usr/bin/env python3
#
# --- Day 8: Haunted Wasteland ---
#
# You're still riding a camel across Desert Island when you spot a sandstorm
# quickly approaching. When you turn to warn the Elf, she disappears before
# your eyes! To be fair, she had just finished warning you about ghosts
# a few minutes ago.
#
# One of the camel's pouches is labeled "maps" - sure enough, it's full
# of documents (your puzzle input) about how to navigate the desert.
# At least, you're pretty sure that's what they are; one of the documents
# contains a list of left/right instructions, and the rest of the documents
# seem to describe some kind of network of labeled nodes.
#
# It seems like you're meant to use the left/right instructions to navigate
# the network. Perhaps if you have the camel follow the same instructions,
# you can escape the haunted wasteland!
#
# After examining the maps for a bit, two nodes stick out: AAA and ZZZ.
# You feel like AAA is where you are now, and you have to follow
# the left/right instructions until you reach ZZZ.
#
# This format defines each node of the network individually. For example:
#
#   RL
#
#   AAA = (BBB, CCC)
#   BBB = (DDD, EEE)
#   CCC = (ZZZ, GGG)
#   DDD = (DDD, DDD)
#   EEE = (EEE, EEE)
#   GGG = (GGG, GGG)
#   ZZZ = (ZZZ, ZZZ)
#
# Starting with AAA, you need to look up the next element based on the next
# left/right instruction in your input. In this example, start with AAA and
# go right (R) by choosing the right element of AAA, CCC. Then, L means
# to choose the left element of CCC, ZZZ. By following the left/right
# instructions, you reach ZZZ in 2 steps.
#
# Of course, you might not find ZZZ right away. If you run out of left/right
# instructions, repeat the whole sequence of instructions as necessary:
# RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is
# a situation that takes 6 steps to reach ZZZ:
#
#   LLR
#
#   AAA = (BBB, BBB)
#   BBB = (AAA, ZZZ)
#   ZZZ = (ZZZ, ZZZ)
#
# Starting at AAA, follow the left/right instructions.
# How many steps are required to reach ZZZ?
#
#
# --- Solution ---
#
# We start by reading the input file in two steps: first line into a list of
# moves decoded as values 0 and 1 (that would be indexes of the latter nodes),
# second the rest of the file into a map of nodes, where keys are nodes names
# and the values are tuples with next nodes names. Then we perform a loop from
# the starting position, as long as we do not reach the goal, we read the move
# from the list and switch to a new position, counting that as a step made.
# Finally, one we reached the destination (goal), we return the number of
# steps counted to do so.
#

INPUT_FILE = 'input.txt'

START = 'AAA'
GOAL = 'ZZZ'


def main():
    with open(INPUT_FILE, 'r') as file:
        moves = list(map(int, file.readline()
                                  .replace('L', '0')
                                  .replace('R', '1')
                                  .strip()))

        nodes = {line.split()[0]: tuple(line.split()[1:])
                 for line in file.read()
                                 .strip()
                                 .replace(' = (', ' ')
                                 .replace(', ', ' ')
                                 .replace(')', '')
                                 .split('\n')}

    position = START
    steps = 0

    while position != GOAL:
        index = moves[steps % len(moves)]
        position = nodes[position][index]
        steps += 1

    print(steps)


if __name__ == '__main__':
    main()
