#!/usr/bin/env python3
#
# --- Day 8: Haunted Wasteland / Part Two ---
#
# The sandstorm is upon you and you aren't any closer to escaping
# the wasteland. You had the camel follow the instructions, but
# you've barely left your starting position. It's going to take
# significantly more steps to escape!
#
# What if the map isn't for people - what if the map is for ghosts?
# Are ghosts even bound by the laws of spacetime? Only one way to find out.
#
# After examining the maps a bit longer, your attention is drawn
# to a curious fact: the number of nodes with names ending in A
# is equal to the number ending in Z! If you were a ghost, you'd probably
# just start at every node that ends with A and follow all of the paths
# at the same time until they all simultaneously end up at nodes that
# end with Z.
#
# For example:
#
#   LR
#
#   11A = (11B, XXX)
#   11B = (XXX, 11Z)
#   11Z = (11B, XXX)
#   22A = (22B, XXX)
#   22B = (22C, 22C)
#   22C = (22Z, 22Z)
#   22Z = (22B, 22B)
#   XXX = (XXX, XXX)
#
# Here, there are two starting nodes, 11A and 22A (because they both end
# with A). As you follow each left/right instruction, use that instruction
# to simultaneously navigate away from both nodes you're currently on.
# Repeat this process until all of the nodes you're currently on end with Z.
# (If only some of the nodes you're on end with Z, they act like any other
# node and you continue as normal.) In this example, you would proceed
# as follows:
# – Step 0: You are at 11A and 22A.
# – Step 1: You choose all of the left paths, leading you to 11B and 22B.
# – Step 2: You choose all of the right paths, leading you to 11Z and 22C.
# – Step 3: You choose all of the left paths, leading you to 11B and 22Z.
# – Step 4: You choose all of the right paths, leading you to 11Z and 22B.
# – Step 5: You choose all of the left paths, leading you to 11B and 22C.
# – Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
#
# So, in this example, you end up entirely on nodes that end
# in Z after 6 steps.
#
# Simultaneously start on every node that ends with A.
# How many steps does it take before you're only on nodes that end with Z?
#
#
# --- Solution ---
#
# The difference here is that instead of a single position we have now
# a list of individual positions that we move at once until all of these
# positions reach the defined goal condition. However, while the naive
# approach works for smaller example input, it is not efficient enough
# for a real input – it takes too many steps. Hence, we need a help of math
# to find the answer! We can count the number of steps needed for each
# individual position when moved separately, then finding the lowest common
# multiple of all discovered individual steps to calculate the answer.
#
# Note this is not a fully general solution – it works because of the input
# data is prepared in a way that each individual path (e.g. for the first
# position 11A) it will form a cycle of the constant length that will always
# end in the same end position (e.g. 11Z) after the same number of steps that
# it initially led from the start to end position for the first time (e.g.
# 11A -> [N steps] -> 11Z -> [N steps] -> 11Z -> [N steps] -> 11Z -> ...).
# A more generic solution would require cycle-detection and fast-forwarding
# for the case where they are not of fixed length.
#

INPUT_FILE = 'input.txt'

START = 'A'
GOAL = 'Z'


def gcd(numbers: list[int]) -> int:
    highest_candidate = min(numbers)

    for divisor in range(2, highest_candidate + 1):
        if all([(number % divisor) == 0 for number in numbers]):
            return divisor

    return 1  # not found – the numbers must be relatively prime


def lcm(numbers: list[int]) -> int:
    multipled = numbers[0]

    for number in numbers[1:]:
        multipled *= number / gcd(numbers)

    return int(multipled)


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

    positions = [key for key in nodes.keys() if key[-1] == START]
    steps = [0] * len(positions)

    for i, position in enumerate(positions):
        while position[-1] != GOAL:
            index = moves[steps[i] % len(moves)]
            position = nodes[position][index]
            steps[i] += 1

    print(lcm(steps))


if __name__ == '__main__':
    main()
