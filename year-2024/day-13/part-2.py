#!/usr/bin/env python3
#
# --- Day 13: Claw Contraption / Part Two ---
#
# As you go to win the first prize, you discover that the claw is nowhere
# near where you expected it would be. Due to a unit conversion error
# in your measurements, the position of every prize is actually 10000000000000
# higher on both the X and Y axis!
#
# Add 10000000000000 to the X and Y position of every prize. After making
# this change, the example above would now look like this:
#
#   Button A: X+94, Y+34
#   Button B: X+22, Y+67
#   Prize: X=10000000008400, Y=10000000005400
#
#   Button A: X+26, Y+66
#   Button B: X+67, Y+21
#   Prize: X=10000000012748, Y=10000000012176
#
#   Button A: X+17, Y+86
#   Button B: X+84, Y+37
#   Prize: X=10000000007870, Y=10000000006450
#
#   Button A: X+69, Y+23
#   Button B: X+27, Y+71
#   Prize: X=10000000018641, Y=10000000010279
#
# Now, it is only possible to win a prize on the second and fourth claw
# machines. Unfortunately, it will take many more than 100 presses to do so.
#
# Using the corrected prize coordinates, figure out how to win as many prizes
# as possible. What is the fewest tokens you would have to spend to win all
# possible prizes?
#
#
# --- Solution ---
#
# The difference in this part is that we can no longer efficiently browse
# the vectors space using naive approach, as the boundaries are too large.
# Instead, we can assume there exist a single general solution to the problem
# – the prize location can be reached as a linear combination of two vectors,
# given as some multiplication of shift vector related to button A and some
# multiplication of vector related to button B, added together:
#
#   prize = times_A * button_A + times_B * button_B
#
# This can be expressed as a system of two equations with two unknown values:
#
#   prize_X = times_A * btn_A_X + times_B * btn_B_X
#   prize_Y = times_A * btn_A_Y + times_B * btn_B_Y
#
# In short:
#
#   Cx = t1 * Ax + t2 * Bx
#   Cy = t1 * Ay + t2 * By
#
# From the second equation, we calculate the element `b`:
#
#   t2 = (Cy - t1 * Ay) / By
#
# The calculated element can t2e inserted into the first equation, so we get:
#
#   Cx = t1 * Ax + (Cy - t1 * Ay) * (Bx / By)
#
# Which can t2e now simplified to express the value of `a`:
#
#   Cx = t1 * Ax + Cy * Bx / By - t1 * Ay * Bx / By
#   Cx - Cy * Bx / By = t1 * Ax - t1 * Ay * Bx / By
#   Cx * By - Cy * Bx = t1 * (Ax * By - Ay * Bx)
#   t1 = (Cx * By - Cy * Bx) / (Ax * By - Ay * Bx)
#
# In the end, we get the solution t1s:
#
#   t1 = (Cx * By - Cy * Bx) / (Ax * By - Ay * Bx)
#   t2 = (Cy - t1 * Ay) / By
#
# Now, we accept the solution only if it is consists of integer values
# and both coefficients are positive.
#

INPUT_FILE = 'input.txt'

COST_A = 3
COST_B = 1

SHIFT = 10_000_000_000_000


def main():
    with open(INPUT_FILE, 'r') as file:
        machines = [tuple(map(int, machine.split(':')))
                    for machine in file.read().strip()
                                              .replace('\n\n', '|')
                                              .replace('\n', ':')
                                              .replace('X+', '')
                                              .replace('Y+', '')
                                              .replace('X=', '')
                                              .replace('Y=', '')
                                              .replace('Button A:', '')
                                              .replace('Button B:', '')
                                              .replace('Prize:', '')
                                              .replace(',', ':')
                                              .replace(' ', '')
                                              .split('|')]

    tokens = 0

    for machine in machines:
        btn_A = complex(*machine[0:2])
        btn_B = complex(*machine[2:4])
        prize = complex(*machine[4:6])
        prize += complex(SHIFT, SHIFT)

        Ax = btn_A.real
        Bx = btn_B.real
        Cx = prize.real
        Ay = btn_A.imag
        By = btn_B.imag
        Cy = prize.imag

        t1 = (Cx * By - Cy * Bx) / (Ax * By - Ay * Bx)
        t2 = (Cy - t1 * Ay) / By

        if any([t1 != int(t1), t2 != int(t2), t1 < 0, t2 < 0]):
            continue  # this is not a solution under given conditions

        times_A = t1
        times_B = t2

        cost = times_A * COST_A + times_B * COST_B
        tokens += int(cost)

    print(tokens)


if __name__ == '__main__':
    main()
