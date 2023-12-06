#!/usr/bin/env python3
#
# --- Day 5: A Maze of Twisty Trampolines, All Alike / Part Two ---
#
# Now, the jumps are even stranger: after each jump, if the offset was three
# or more, instead decrease it by 1. Otherwise, increase it by 1 as before.
#
# Using this rule with the above example, the process now takes 10 steps,
# and the offset values after finding the exit are left as 2 3 2 3 -1.
#
# How many steps does it now take to reach the exit?
#
#
# --- Solution ---
#
# The only difference here is that conditionally we increment or decrement
# the current field before jumping to a new index. This still finished in
# a finite time, though much more steps are required. Additionally, it turned
# out that using try-except construction is faster than checking for the index
# being within the valid boundary every time (known as EAFP vs LBYL approiach).
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        jumps = list(map(int, file.read().strip().split()))

    index = 0
    steps = 0

    while True:
        # EAFP – Easier to Ask for Forgiveness than Permission
        try:
            offset = jumps[index]
        except IndexError:
            break

        if offset >= 3:
            jumps[index] -= 1
        else:
            jumps[index] += 1

        index += offset
        steps += 1

    print(steps)


if __name__ == '__main__':
    main()
