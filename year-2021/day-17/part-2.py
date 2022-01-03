#!/usr/bin/env python3
#
# --- Day 17: Trick Shot / Part Two ---
#
# Maybe a fancy trick shot isn't the best idea; after all, you only have
# one probe, so you had better not miss.
#
# To get the best idea of what your options are for launching the probe,
# you need to find every initial velocity that causes the probe to eventually
# be within the target area after any step.
#
# In the above example, there are 112 different initial velocity values
# that meet these criteria:
#   23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
#   25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
#   8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
#   26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
#   20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
#   25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
#   25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
#   8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
#   24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
#   7,5     23,-6   28,-10  10,-2   11,-1   20,-9   14,-2   29,-7   13,-3
#   23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
#   27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
#   8,-2    27,-8   30,-5   24,-7
#
# How many distinct initial velocity values cause the probe to be within
# the target area after any step?
#
#
# --- Solution ---
#
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
