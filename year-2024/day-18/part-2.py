#!/usr/bin/env python3
#
# --- Day 18: RAM Run / Part Two ---
#
# The Historians aren't as used to moving around in this pixelated universe
# as you are. You're afraid they're not going to be fast enough to make it
# to the exit before the path is completely blocked.
#
# To determine how fast everyone needs to go, you need to determine the first
# byte that will cut off the path to the exit.
#
# In the above example, after the byte at 1,1 falls, there is still a path
# to the exit:
#
#   O..#OOO
#   O##OO#O
#   O#OO#OO
#   OOO#OO#
#   ###OO##
#   .##O###
#   #.#OOOO
#
# However, after adding the very next byte (at 6,1), there is no longer
# a path to the exit:
#
#   ...#...
#   .##..##
#   .#..#..
#   ...#..#
#   ###..##
#   .##.###
#   #.#....
#
# So, in this example, the coordinates of the first byte that prevents
# the exit from being reachable are 6,1.
#
# Simulate more of the bytes that are about to corrupt your memory space.
# What are the coordinates of the first byte that will prevent the exit
# from being reachable from your starting position? (Provide the answer
# as two integers separated by a comma with no other characters.)
#
#
# --- Solution ---
#
# The difference in this part is that we need to find element from the list
# (collection of failures addresses), that after being added to our memory map
# makes no possible paths from start to goal (i.e. effectively blocks the way).
# For this, we can simply check all the possibilities (there is about 3500
# elements in the input data), each time re-running the original program from
# previous part with different SIZE variable - it is efficient enough to finish
# in reasonable finite time. However, I decided to implement smarter search
# for that parameter, based on the bisection search. We start by defining
# the lower bound and the upper bound – the index from the memory failures
# list that allow finding the path from start to goal and the index for which
# this task is impossible already; the easiest, is to pick the index of first
# and last element there. The index for which the path finding task becomes
# impossible must lie somewhere between. Hence, we take the candidate index,
# being around the middle between lower and upper bound, and we run the path
# finding algorithm from previous part. If there is a possible path found,
# we know that there desired element must be somewhere closer to the upper
# bound, so we replace original lower bound with that middle index; contrary,
# when there is no path already, we know the element we look for was earlier,
# so we replace the upper bound with the middle index. Then we calculate a new
# candidate index, from the new lower and upper bound and repeat the analysis.
# Effectively, each time we divide the range of indexes by half, so after first
# iteration there is only 1/2 of possible indexes, after second iteration there
# is just 1/4 of possible indexes left to check, next there is just 1/8, 1/16,
# and so on. After a few iterations, we end with lower bound as the last index
# where the path finding is possible and upper bound as the first index where
# the task is impossible. Finally, as an answer we return the value related
# to the upper bound index.
#

INPUT_FILE = 'input.txt'

MIN = 0
MAX = 70


def main():
    with open(INPUT_FILE, 'r') as file:
        failures = tuple(tuple(map(int, line.split(',')))
                         for line in file.read().strip().split())

    lower = 0  # here it works
    upper = len(failures) - 1  # here there is no path

    while upper - lower > 1:
        index = (upper + lower) // 2
        failed = set(failures[:index + 1])

        start = (MIN, MIN)
        end = (MAX, MAX)

        queue = [(start, )]  # path
        visited = set()

        while queue:
            path = queue.pop(0)
            x, y = path[-1]  # current position

            if (x, y) == end:  # we reached the goal
                break

            if (x, y) in visited:  # considered by another path already
                continue

            visited.add((x, y))

            for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx = x + dx
                ny = y + dy

                if not (MIN <= nx <= MAX and MIN <= ny <= MAX):
                    continue  # out of bounds

                if (nx, ny) in failed:
                    continue  # avoid corrupted memory

                queue.append(path + ((nx, ny), ))

        else:  # there was no break – impossible to reach the goal
            path = ()

        # move the upper or lower bound
        if not path:
            upper = index
        else:
            lower = index

    # the anwer is the lowest possible upper bound
    print(','.join(str(value) for value in failures[upper]))


if __name__ == '__main__':
    main()
