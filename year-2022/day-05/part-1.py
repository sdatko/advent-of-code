#!/usr/bin/env python3
#
# --- Day 5: Supply Stacks ---
#
# The expedition can depart as soon as the final supplies have been unloaded
# from the ships. Supplies are stored in stacks of marked crates, but because
# the needed supplies are buried under many other crates, the crates need
# to be rearranged.
#
# The ship has a giant cargo crane capable of moving crates between stacks.
# To ensure none of the crates get crushed or fall over, the crane operator
# will rearrange them in a series of carefully-planned steps. After the crates
# are rearranged, the desired crates will be at the top of each stack.
#
# The Elves don't want to interrupt the crane operator during this delicate
# procedure, but they forgot to ask her which crate will end up where,
# and they want to be ready to unload them as soon as possible so they
# can embark.
#
# They do, however, have a drawing of the starting stacks of crates
# and the rearrangement procedure (your puzzle input). For example:
#
#       [D]
#   [N] [C]
#   [Z] [M] [P]
#    1   2   3
#
#   move 1 from 2 to 1
#   move 3 from 1 to 3
#   move 2 from 2 to 1
#   move 1 from 1 to 2
#
# In this example, there are three stacks of crates. Stack 1 contains two
# crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains
# three crates; from bottom to top, they are crates M, C, and D. Finally,
# stack 3 contains a single crate, P.
#
# Then, the rearrangement procedure is given. In each step of the procedure,
# a quantity of crates is moved from one stack to a different stack. In the
# first step of the above rearrangement procedure, one crate is moved from
# stack 2 to stack 1, resulting in this configuration:
#
#   [D]
#   [N] [C]
#   [Z] [M] [P]
#    1   2   3
#
# In the second step, three crates are moved from stack 1 to stack 3. Crates
# are moved one at a time, so the first crate to be moved (D) ends up below
# the second and third crates:
#
#           [Z]
#           [N]
#       [C] [D]
#       [M] [P]
#    1   2   3
#
# Then, both crates are moved from stack 2 to stack 1. Again, because crates
# are moved one at a time, crate C ends up below crate M:
#
#           [Z]
#           [N]
#   [M]     [D]
#   [C]     [P]
#    1   2   3
#
# Finally, one crate is moved from stack 1 to stack 2:
#
#           [Z]
#           [N]
#           [D]
#   [C] [M] [P]
#    1   2   3
#
# The Elves just need to know which crate will end up on top of each stack;
# in this example, the top crates are C in stack 1, M in stack 2, and
# Z in stack 3, so you should combine these together and give the Elves
# the message CMZ.
#
# After the rearrangement procedure completes, what crate ends up on top
# of each stack?
#
#
# --- Solution ---
#
# We start by reading the input file into two parts – the definition of moves
# and the definition of crates. Then we process both definitions independently.
# For list of moves, it is simple – we just remove unnecessary words and map
# what remains to integers, resulting in a list of tuples (3 elements),
# each specifying the number of crates to move (1), the source (2) and
# the destination (3) stack.
# The processing of creates definition is a bit more tricky. The obvious
# solution involves finding the indices of numbers in text where the columns
# are given (last row of the definition) and reading the letters at those
# indices from the rest of crates definition (other rows). However, it would
# work well only for up to 9/10 columns (depending if we start with 0 or 1).
# Instead, the approach I like more is to assume any number of columns, but
# that requires processing of the input to a different form.
# Nevertheless, what we produce in the end, is a list of stacks contents,
# represented as list of lists.
# Finally we process the list of moves: for each entry we remove last element
# from the source stack and we append it to the destination stack, repeating
# if necessary for a given number of times.
# Then we read the last element of every stack and return as the answer.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        crates, moves = file.read().split('\n\n')

        moves = [tuple(map(int, move.strip().split()))
                 for move in moves.replace('move ', '')
                                  .replace('from ', '')
                                  .replace('to ', ' ')
                                  .strip()
                                  .split('\n')]

        #
        # The obvious solution, but it only works well for up to 9 columns;
        # the indices should be found with an additional loop for automation
        #
        # crates = [[row[col] for col in (1, 5, 9, 13, 17, 21, 25, 29, 33)]
        #           for row in crates.split('\n')]

        #
        # My final solution, should work for any number of columns
        #
        crates = [row.strip().split('|')
                  for row in (crates.replace('[', ' ')
                                    .replace(']', ' ')
                                    .replace('    ', '|')
                                    .replace('   ', '|')
                                    .split('\n'))]

        crates.pop()  # Remove last row – the useless indices

        n_stacks = len(crates[0])
        stacks = [[] for _ in range(n_stacks)]

        for row in reversed(crates):
            for col, letter in enumerate(row):
                if letter.strip():
                    stacks[col].append(letter)

    for move in moves:
        count, source, destination = move
        for _ in range(count):
            letter = stacks[source - 1].pop()
            stacks[destination - 1].append(letter)

    top_letters = ''.join([stack[-1] for stack in stacks])
    print(top_letters)


if __name__ == '__main__':
    main()
