#!/usr/bin/env python3
#
# --- Day 7: Bridge Repair / Part Two ---
#
# The engineers seem concerned; the total calibration result you gave them is
# nowhere close to being within safety tolerances. Just then, you spot your
# mistake: some well-hidden elephants are holding a third type of operator.
#
# The concatenation operator (||) combines the digits from its left and right
# inputs into a single number. For example, 12 || 345 would become 12345.
# All operators are still evaluated left-to-right.
#
# Now, apart from the three equations that could be made true using only
# addition and multiplication, the above example has three more equations
# that can be made true by inserting operators:
# – 156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
# – 7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
# – 192: 17 8 14 can be made true using 17 || 8 + 14.
#
# Adding up all six test values (the three that could be made before using
# only + and * plus the new three that can now be made by also using ||)
# produces the new total calibration result of 11387.
#
# Using your new knowledge of elephant hiding spots, determine which equations
# could possibly be true. What is their total calibration result?
#
#
# --- Solution ---
#
# The difference here is that we need to consider one additional operation
# – the concatenation of two numbers. The original approach is efficient
# enough to produce the result in under a few seconds, however it can be
# optimized further if before adding new expression to array we verify
# if it is still possible to solve using upper-bound criterion.
# As all operations can only increase the value (there are no subtraction
# or division operations), before adding new expression to the queue we verify
# if the currently reached value is not already exceeding the expected result.
# In such case, we can skip checking huge portion of the sub-expressions.
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

            else:  # consider all possible operations
                value = expression[0] + expression[1]
                if value <= result:
                    expressions.append((value, *expression[2:]))

                value = expression[0] * expression[1]
                if value <= result:
                    expressions.append((value, *expression[2:]))

                value = int(f'{expression[0]}{expression[1]}')
                if value <= result:
                    expressions.append((value, *expression[2:]))

    print(sum(test_values))


if __name__ == '__main__':
    main()
