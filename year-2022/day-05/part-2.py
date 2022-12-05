#!/usr/bin/env python3
#
# --- Day 5: Supply Stacks / Part Two ---
#
# As you watch the crane operator expertly rearrange the crates,
# you notice the process isn't following your prediction.
#
# Some mud was covering the writing on the side of the crane, and you quickly
# wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.
#
# The CrateMover 9001 is notable for many new and exciting features:
# air conditioning, leather seats, an extra cup holder, and the ability
# to pick up and move multiple crates at once.
#
# Again considering the example above, the crates begin
# in the same configuration:
#
#       [D]
#   [N] [C]
#   [Z] [M] [P]
#    1   2   3
#
# Moving a single crate from stack 2 to stack 1 behaves the same as before:
#
#   [D]
#   [N] [C]
#   [Z] [M] [P]
#    1   2   3
#
# However, the action of moving three crates from stack 1 to stack 3 means
# that those three moved crates stay in the same order, resulting in this
# new configuration:
#
#           [D]
#           [N]
#       [C] [Z]
#       [M] [P]
#    1   2   3
#
# Next, as both crates are moved from stack 2 to stack 1, they retain their
# order as well:
#
#           [D]
#           [N]
#   [C]     [Z]
#   [M]     [P]
#    1   2   3
#
# Finally, a single crate is still moved from stack 1 to stack 2,
# but now it's crate C that gets moved:
#
#           [D]
#           [N]
#           [Z]
#   [M] [C] [P]
#    1   2   3
#
# In this example, the CrateMover 9001 has put the crates in a totally
# different order: MCD.
#
# Before the rearrangement process finishes, update your simulation
# so that the Elves know where they should stand to be ready to unload
# the final supplies. After the rearrangement procedure completes, what
# crate ends up on top of each stack?
#
#
# --- Solution ---
#
# The only difference in this part is in the rearrangement (i.e. processing
# the list of moves). Here we build a list of letters to move from source
# and then we append them to the destination to maintain the order (reversed
# order from the list of letters we built with pops).
# In production-ready solution we should probably ensure that there are enough
# elements on a given stack to move, but it works well enough with the current
# task assumptions.
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
        letters = []
        for _ in range(count):
            letters.append(stacks[source - 1].pop())
        for letter in reversed(letters):
            stacks[destination - 1].append(letter)

    top_letters = ''.join([stack[-1] for stack in stacks])
    print(top_letters)


if __name__ == '__main__':
    main()
