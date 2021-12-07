#!/usr/bin/env python3
#
# Task:
# The crabs don't seem interested in your proposed solution.
# Perhaps you misunderstand crab engineering?
# As it turns out, crab submarine engines don't burn fuel at a constant rate.
# Instead, each change of 1 step in horizontal position costs 1 more unit
# of fuel than the last: the first step costs 1, the second step costs 2,
# the third step costs 3, and so on.
# As each crab moves, moving further becomes more expensive.
# This changes the best horizontal position to align them all on.
# Determine the horizontal position that the crabs can align to using the least
# fuel possible so they can make you an escape route! How much fuel must they
# spend to align to that position?
#
# Solution:
# The straightforward solution works here well when we introduce here a formula
# for calculating the total fuel consumption. The formula is a sum of series
# from 1 to N, which can be expressed as N*(N+1)/2 – this is far more efficient
# than writing sum(range(n + 1)) in Python.
# Similarly to part 1, I found experimentally that the optimal position can be
# around particular value – this time it is an average of all values, expressed
# (sum(positions) // len(positions)), however I cannot justify it as well here
# and I am not sure it will work for all cases, so I am leaving the original
# approach that gave me the result.
#
# Appendix:
# The proof for average exists, although it is more complicated this time.
# We start with function f(X) = \sum_{i=0}^N g( abs(S_i - X) ), here additional
# g(n) = n * (n+1) / 2. Calculating the derivative, it gives us as follows:
# f'(X) = \sum_{i=0}^N ( 1/2 + abs(S_i - X) ) * sign(S_i - X),
# as for h(x) = g(f(x)) we have h'(x) = g'(f(x)) * f'(x). Then f'(X) can be
# rewritten to the following form of two separate sums:
# f'(X) = \sum_{i=0}^N sign(S_i - X) / 2 + \sum_{i=0}^N S_i - X,
# Here the \sum_{i=0}^N S_i - X can be written as SUM - N * X, where SUM equals
# to the sum of elements from set S and N is a number of these elements in S.
# Therefore we have:
# f'(X) = \sum_{i=0}^N sign(S_i - X) / 2 + SUM - N * X,
# Solving it for f'(X) = 0, we obtain:
# X = SUM / N + \sum_{i=0}^N sign(S_i - X) / 2N
# Here, the SUM / N is an average value of set S. The second term describes
# the boundaries for solution around the average – as sum of N values of sign()
# function lies between -N and N, the boundary limits to [-0.5; 0.5].
# In our puzzle, we need to examine two points around the average value.
#

INPUT_FILE = 'input.txt'


def sum_from_1_to_n(n):
    return n * (n + 1) // 2


def main():
    positions = [int(number)
                 for line in open(INPUT_FILE, 'r')
                 for number in line.strip().split(',')]

    fuel_cost = sum_from_1_to_n(sum(positions))

    for new_position in range(min(positions), max(positions)):
        costs = [sum_from_1_to_n(abs(current_position - new_position))
                 for current_position in positions]
        new_cost = sum(costs)

        if new_cost < fuel_cost:
            fuel_cost = new_cost

    print(fuel_cost)


if __name__ == '__main__':
    main()
