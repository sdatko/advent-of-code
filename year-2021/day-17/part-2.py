#!/usr/bin/env python3
#
# Task:
# Maybe a fancy trick shot isn't the best idea; after all, you only have
# one probe, so you had better not miss.
# To get the best idea of what your options are for launching the probe,
# you need to find every initial velocity that causes the probe to eventually
# be within the target area after any step.
# How many distinct initial velocity values cause the probe to be within
# the target area after any step?
#
# Solution:
# In this part, the solution from previous part works as well. The only
# difference now is that we return the number of found heights (which
# is equal to the number of times we reached the trench).
#

INPUT_FILE = 'input.txt'


def ceil(x):
    return -(-x // 1)


def sign(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0


def sum_from_1_to_n(n):
    return n * (n + 1) // 2


def main():
    with open(INPUT_FILE, 'r') as file:
        puzzle_input = file.readline().strip().replace('target area: ', '')
        target_bounds = [values for entry in puzzle_input.split(', ')
                         for values in entry[2:].split('..')]
        target_bounds = list(map(int, target_bounds))

        x_range = target_bounds[:2]
        y_range = target_bounds[2:]

    starting_point = (0, 0)
    heights = []

    x_min = min(x_range) - starting_point[0]
    x_max = max(x_range) - starting_point[0]
    y_min = min(y_range) - starting_point[1]
    y_max = max(y_range) - starting_point[1]

    Vx_min = int(ceil(-0.5 + (1 + 8 * x_min)**0.5 / 2))
    Vx_max = x_max
    Vy_min = y_min
    Vy_max = -y_min - 1

    def simulation(x, y, Vx, Vy):
        max_height = sum_from_1_to_n(Vy)

        while x < x_min or y > y_max:
            x += Vx
            y += Vy
            Vx -= sign(Vx)
            Vy -= 1

            if x > x_max or y < y_min:
                break  # overshoot

        else:  # we hit the target
            heights.append(max_height)

    for Vx in range(Vx_min, Vx_max + 1):
        for Vy in range(Vy_min, Vy_max + 1):
            x, y = starting_point
            simulation(x, y, Vx, Vy)

    print(len(heights))


if __name__ == '__main__':
    main()
