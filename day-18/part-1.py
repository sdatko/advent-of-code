#!/usr/bin/env python3
#
# Task:
# The homework (your puzzle input) consists of a series of expressions that
# consist of addition (+), multiplication (*), and parentheses ((...)).
# Just like normal math, parentheses indicate that the expression inside
# must be evaluated before it can be used by the surrounding expression.
# Addition still finds the sum of the numbers on both sides of the operator,
# and multiplication still finds the product.
# However, the rules of operator precedence have changed. Rather than
# evaluating multiplication before addition, the operators have the same
# precedence, and are evaluated left-to-right regardless of the order
# in which they appear.
# Before you can help with the homework, you need to understand it yourself.
# Evaluate the expression on each line of the homework; what is the sum
# of the resulting values?
#
# Solution:
# We read the input file, treating each line as a formula to calculate.
# Then we iterate over the formulas in a loop, every time doing basically
# two actions – reducing the brackets (calculating the value of sub-formula
# between brackets and inserting it instead of part of the original formula),
# then we simply do calculate what remains (additions and multiplications).
# The function that reduces the brackets goes as long as there is opening
# and closing bracket in the equation, first finding the most right opening
# bracket and then the first closing bracket after this one.
#

INPUT_FILE = 'input.txt'


def calculate(formula):
    result = 0
    operator = None  # '+' or '*'

    for element in formula.split():
        if element in ('+', '*'):
            operator = element
        elif operator is None:
            result = int(element)
        elif operator == '+':
            result += int(element)
        elif operator == '*':
            result *= int(element)
        else:
            print('SYNTAX ERROR')
            return 1

    return result


def reduce_brackets(formula):
    while True:
        if '(' not in formula and ')' not in formula:
            break

        left_bracket = formula.rfind('(')
        right_bracket = formula.find(')', left_bracket)

        subformula = formula[left_bracket + 1:right_bracket]
        subresult = calculate(subformula)

        formula = (
            formula[:left_bracket]
            + str(subresult)
            + formula[right_bracket + 1:]
        )

    return formula


def main():
    formulas = [line.strip('\n') for line in open(INPUT_FILE, 'r')]

    results = []

    for formula in formulas:
        formula = reduce_brackets(formula)
        result = calculate(formula)
        results.append(result)

    print(sum(results))


if __name__ == '__main__':
    main()
