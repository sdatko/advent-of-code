#!/usr/bin/env python3
#
# Task:
# Now, addition and multiplication have different precedence levels, but
# they're not the ones you're familiar with. Instead, addition is evaluated
# before multiplication.
# What do you get if you add up the results of evaluating the homework
# problems using these new rules?
#
# Solution:
# The only change is in how the calculation of formula without brackets works.
# So we simply split the formula in places of multiplications, so we can first
# perform additions on parts between multiplications signs, then we do multiply
# all remaining values.
#

INPUT_FILE = 'input.txt'


def calculate(formula):
    result = 1

    for subformula in formula.split(' * '):
        subresult = 0

        for element in subformula.split(' + '):
            subresult += int(element)

        result *= subresult

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
