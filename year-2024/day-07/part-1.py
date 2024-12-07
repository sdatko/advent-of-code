#!/usr/bin/env python3
#
# --- Day 7: Bridge Repair ---
#
# The Historians take you to a familiar rope bridge over a river in the middle
# of a jungle. The Chief isn't on this side of the bridge, though; maybe he's
# on the other side?
#
# When you go to cross the bridge, you notice a group of engineers trying
# to repair it. (Apparently, it breaks pretty frequently.) You won't be able
# to cross until it's fixed.
#
# You ask how long it'll take; the engineers tell you that it only needs
# final calibrations, but some young elephants were playing nearby and stole
# all the operators from their calibration equations! They could finish
# the calibrations if only someone could determine which test values could
# possibly be produced by placing any combination of operators into their
# calibration equations (your puzzle input).
#
# For example:
#
#   190: 10 19
#   3267: 81 40 27
#   83: 17 5
#   156: 15 6
#   7290: 6 8 6 15
#   161011: 16 10 13
#   192: 17 8 14
#   21037: 9 7 18 13
#   292: 11 6 16 20
#
# Each line represents a single equation. The test value appears before
# the colon on each line; it is your job to determine whether the remaining
# numbers can be combined with operators to produce the test value.
#
# Operators are always evaluated left-to-right, not according to precedence
# rules. Furthermore, numbers in the equations cannot be rearranged.
# Glancing into the jungle, you can see elephants holding two different types
# of operators: add (+) and multiply (*).
#
# Only three of the above equations can be made true by inserting operators:
# – 190: 10 19 has only one position that accepts an operator: between 10
#   and 19. Choosing + would give 29, but choosing * would give the test value
#   (10 * 19 = 190).
# – 3267: 81 40 27 has two positions for operators. Of the four possible
#   configurations of the operators, two cause the right side to match
#   the test value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267
#   (when evaluated left-to-right)!
# – 292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.
#
# The engineers just need the total calibration result, which is the sum
# of the test values from just the equations that could possibly be true.
# In the above example, the sum of the test values for the three equations
# listed above is 3749.
#
# Determine which equations could possibly be true.
# What is their total calibration result?
#
#
# --- Solution ---
#
# We start by reading the input into a collection of equations by splitting
# the file over newlines and each line over spaces, also discarding the first
# colon there (so we assume the first value in line to be the expected result).
# Then we process all equations in a loop – for each, we construct initial
# list of expressions (values that can either be summed or multiplied) and
# we process that list like a queue, removing last element in each iteration.
# For each expression, we check it's length – if it contains a single element,
# we verify if it is equal to expected result; if so, we found that equation
# can be solved and we save the value for an answer. Otherwise, if there are
# more elements in expression, we consider both possible operations (sum and
# multiplication) on two first elements of the expression and we insert into
# the queue two new equations to process. Finally, after processing all given
# equations and their possible sub-expressions, we return the sum of values
# for equations that are solvable.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        equations = tuple(tuple(map(int, equation.replace(': ', ' ').split()))
                          for equation in file.read().strip().split('\n'))

    test_values = []

    for equation in equations:
        result = equation[0]
        expressions = [equation[1:]]

        while expressions:
            expression = expressions.pop()

            if len(expression) == 1:
                value = expression[0]
                if result == value:  # there is a solution!
                    test_values.append(value)
                    break

            else:  # consider both possible operations
                value = expression[0] + expression[1]
                expressions.append((value, *expression[2:]))

                value = expression[0] * expression[1]
                expressions.append((value, *expression[2:]))

    print(sum(test_values))


if __name__ == '__main__':
    main()
