#!/usr/bin/env python3
#
# --- Day 6: Wait For It / Part Two ---
#
# As the race is about to start, you realize the piece of paper with race
# times and record distances you got earlier actually just has very bad
# kerning. There's really only one race - ignore the spaces between
# the numbers on each line.
#
# So, the example from before:
#
#   Time:      7  15   30
#   Distance:  9  40  200
#
# ...now instead means this:
#
#   Time:      71530
#   Distance:  940200
#
# Now, you have to figure out how many ways there are to win this single race.
# In this example, the race lasts for 71530 milliseconds and the record
# distance you need to beat is 940200 millimeters. You could hold
# the button anywhere from 14 to 71516 milliseconds and beat the record,
# a total of 71503 ways!
#
# How many ways can you beat the record in this one much longer race?
#
#
# --- Solution ---
#
# The difference here is that we read a single total time from the first line
# in the input file and the target distance from the second line (integers).
# Then we can apply the same solution as for part 1 just for a single race
# and this produces an answer in a finite time of a few seconds. However,
# by expanding the formula for traveled distance,
#   travelled = waiting_time * (total_time - waiting_time)
#   travelled = waiting_time * total_time - waiting_time * waiting_time,
# we can notice that this is actually a quadractic function of waiting time
# with the negative direction (coefficient `a` in `ax² + bx + c = 0` form).
# If we replace the travelled distance with the inequation, we finally get:
#   -1 * waiting_time ** 2 + total_time * waiting_time - distance > 0
# Such equation has zero or two solutions (depending on delta sign; note that
# for delta equal 0 we cannot satisfy the inequation, hence also no solution).
# Assuming we have solutions x1 and x2, such that x1 < x2, and our solutions
# space contains only Natural numbers (integers), we can count the answer
# as a differenct between floor of x2 and ceil of x1.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        total_time = int(''.join(file.readline().strip().split()[1:]))
        distance = int(''.join(file.readline().strip().split()[1:]))

    ways_to_win = 0

    # -waiting_time ** 2 + total_time * waiting_time - distance > 0
    a = -1
    b = total_time
    c = -distance

    delta = b ** 2 - 4 * a * c

    if delta <= 0:  # no solutions
        return 0

    x1 = (-b - (delta ** 0.5)) / (2 * a)
    x2 = (-b + (delta ** 0.5)) / (2 * a)

    if x1 > x2:
        x1, x2 = x2, x1

    x1 = int(-(-x1 // 1))  # ceil
    x2 = int(x2)  # floor

    ways_to_win = (x2 - x1 + 1)

    print(ways_to_win)


if __name__ == '__main__':
    main()
