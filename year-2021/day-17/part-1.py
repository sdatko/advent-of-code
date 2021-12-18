#!/usr/bin/env python3
#
# Task:
# You finally decode the Elves' message. HI, the message says.
# You continue searching for the sleigh keys.
# Ahead of you is what appears to be a large ocean trench. Could the keys
# have fallen into it? You'd better send a probe to investigate.
# The probe launcher on your submarine can fire the probe with any integer
# velocity in the x (forward) and y (upward, or downward if negative)
# directions. For example, an initial x,y velocity like 0,10 would fire
# the probe straight up, while an initial velocity like 10,-1 would fire
# the probe forward at a slight downward angle.
# The probe's x,y position starts at 0,0. Then, it will follow some trajectory
# by moving in steps. On each step, these changes occur in the following order:
# - The probe's x position increases by its x velocity.
# - The probe's y position increases by its y velocity.
# Due to drag, the probe's x velocity changes by 1 toward the value 0; that is,
# it decreases by 1 if it is greater than 0, increases by 1 if it is less than
# 0, or does not change if it is already 0.
# Due to gravity, the probe's y velocity decreases by 1.
# For the probe to successfully make it into the trench, the probe must be
# on some trajectory that causes it to be within a target area after any step.
# The submarine computer has already calculated this target area
# (your puzzle input). For example:
#   target area: x=20..30, y=-10..-5
# This target area means that you need to find initial x,y velocity values
# such that after any step, the probe's x position is at least 20 and at most
# 30, and the probe's y position is at least -10 and at most -5.
# Given this target area, one initial velocity that causes the probe to be
# within the target area after any step is 7,2:
#   .............#....#............
#   .......#..............#........
#   ...............................
#   S........................#.....
#   ...............................
#   ...............................
#   ...........................#...
#   ...............................
#   ....................TTTTTTTTTTT
#   ....................TTTTTTTTTTT
#   ....................TTTTTTTT#TT
#   ....................TTTTTTTTTTT
#   ....................TTTTTTTTTTT
#   ....................TTTTTTTTTTT
# In this diagram, S is the probe's initial position, 0,0. The x coordinate
# increases to the right, and the y coordinate increases upward. In the bottom
# right, positions that are within the target area are shown as T. After each
# step (until the target area is reached), the position of the probe is marked
# with #. (The bottom-right # is both a position the probe reaches and
# a position in the target area.)
# If you're going to fire a highly scientific probe out of a super cool probe
# launcher, you might as well do it with style. How high can you make the probe
# go while still reaching the target area?
# Find the initial velocity that causes the probe to reach the highest y
# position and still eventually be within the target area after any step.
# What is the highest y position it reaches on this trajectory?
#
# Solution:
# We read the input file as single line, striping the whitespace characters
# and removing the meaningless part (string 'target area: '). Then we split
# what remains by comma, as well as two dots, and we save the remaining
# numerical values. The values are bounds of the trench.
# Then we can proceed with finding the answer. Originally I went here with
# approach that simulates every possible trajectory. Then I started thinking
# how we can narrow the space of arguments to try.
# It is important to notice that we consider here only the discrete space,
# where object travelling at velocity Vx can be seen at points X and X+Vx,
# but not in between. This helps us finding the boundaries, as at some values
# we will always miss the target area due to too large step.
# For X axis it was pretty straightforward – due to drag the values of velocity
# behaves like a series of numbers that goes from N to 0, meaning at some point
# we no longer move horizontally. If this movement stops before we reach the
# trench, it is impossible to hit the target. So the minimum velocity Vx is the
# value that brings us just to left border of the trench. On the other side,
# the upper bound is a value of Vx that takes us just after the right border
# of the trench.
# For Y axis it was less obvious for me at first. We need to figure out the
# lower bound first. The minimum value is such Vy that takes us already too
# far down – it is a negative number equal to the distance to lower border
# of the trench. For upper bound... we need to realise how it behaves:
# first it would be a series of numbers from N to 0, then it will grow again
# the same values but negative, from 0 to -N – so when it comes back to the
# starting level (y = 0) it has the same value, just negative. Then it
# continues falling down and from that point the bound is the same as for
# the previous case. Therefore, to have Vy_min here, we need to launch
# the probe in opposite direction with value smaller by 1, so (-Vy_min - 1).
# There are still many cases where launched probes will not hit the target,
# but it narrows the arguments space well enough for fast calculations.
# One last notice is for founding the Vx_min, we need to found argument
# such as sum our series of (1, 2, 3, .., Vx-1, Vx) equals to x_min.
# For this we solve the formula:
#       x_min = sum_from_1_to_n( Vx )
#       x_min = Vx * (Vx + 1) // 2
#   2 * x_min = Vx² + Vx
#           0 = Vx² + Vx - 2 * x_min
# Here:
#   delta = 1² - 4 * (-2) * x_min
# And so the solution is:
#   Vx = (-1 ± sqrt(delta)) / 2
# We are only interested in positive value here, so we take only one with +
# instead of ± in this formula, and then the ceil, as we are considering only
# discrete space here.
# For having the answer, we save every max height we can reach from given
# starting position and velocity (it would be sum from 1 to Vy...), provided
# that we will hit the target. Apparently this happens always for out upper
# bound, provided that there is such value of Vx that eventually reaches 0
# (the probe stops horizontally after reaching the trench). I leave the code
# with more naive analysis here though and as a result we display the max
# of saved list of heights.
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

    print(max(heights))


if __name__ == '__main__':
    main()
