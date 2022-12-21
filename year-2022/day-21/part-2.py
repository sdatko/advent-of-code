#!/usr/bin/env python3
#
# --- Day 21: Monkey Math / Part Two ---
#
# Due to some kind of monkey-elephant-human mistranslation,
# you seem to have misunderstood a few key details about the riddle.
#
# First, you got the wrong job for the monkey named root; specifically, you got
# the wrong math operation. The correct operation for monkey root should be =,
# which means that it still listens for two numbers (from the same two monkeys
# as before), but now checks that the two numbers match.
#
# Second, you got the wrong monkey for the job starting with `humn`.
# It isn't a monkey - it's you. Actually, you got the job wrong, too:
# you need to figure out what number you need to yell so that root's
# equality check passes. (The number that appears after humn:
# in your input is now irrelevant.)
#
# In the above example, the number you need to yell to pass root's
# equality test is 301. (This causes root to get the same number, 150,
# from both of its monkeys.)
#
# What number do you yell to pass root's equality test?
#
#
# --- Solution ---
#
# The difference here is that we do not know the value of a single variable,
# but we know the condition it should satisfy. The goal is to find the value.
# For this, we implement a reverse search algorithm in a tree – each monkey
# provides either a single numeric value or a formula that references two other
# monkeys / variables. All definitions and references here are unique, so this
# can be represented as a tree, where node `c` is defined by an operator `?`
# and its arguments `a` and `b` (see illustration below).
#
#     c
#    /?\   <--- ? = operator (+, -, *, /)
#   a   b
#
# The approach is as follows – when looking for a given target element
# in a tree, first we check if this element is defined directly as a node.
# If so, then this is either a numeric value or a formula depending on two
# other values we need to discover, so we recursively launch the searching
# for those two values. An alternative is that the target element we are
# looking for is a part of other definition (so elements `a` or `b` in this
# illustration above). In such case, we need to reverse the defined operation,
# considering whether we want to find the left or the right value here.
#
#   c = a + b   ->   a = c - b   or   b = c - a
#   c = a - b   ->   a = c + b   or   b = a - c
#   c = a * b   ->   a = c / b   or   b = c / a
#   c = a / b   ->   a = c * b   or   b = a / c
#
# Last addition is to support the equality operator, which in our case just
# requires us to return the other value in place of the matching operation
# (since we want `a = b` to be true in this case, we assume `c = 0`).
# Finally, after performing all the operations, we get the value of the target
# node that matches the root condition and we return it.
#


INPUT_FILE = 'input.txt'

TARGET = 'humn'

MATCHER_NODE = 'root'
MATCHER_OPERATION = '='


def search_for_value(target, tree, extra=None):
    # target is a key in tree
    if target in tree:
        value = tree[target]

        if len(value) == 1 and value[0].isnumeric():
            return int(value[0])

        elif len(value) == 3:
            lvalue, operator, rvalue = value[0:3]

            lvalue = search_for_value(lvalue, tree, extra)
            rvalue = search_for_value(rvalue, tree, extra)

            if operator == '+':
                return lvalue + rvalue
            elif operator == '-':
                return lvalue - rvalue
            elif operator == '*':
                return lvalue * rvalue
            elif operator == '/':
                return lvalue / rvalue

    # target in not in tree keys – we search in formulas
    for variable, formula in tree.items():
        if target in formula:
            lvalue, operator, rvalue = formula[0:3]
            del tree[variable]  # remove from tree to avoid infinite loop!

            if target == lvalue:
                variable = search_for_value(variable, tree, extra)
                rvalue = search_for_value(rvalue, tree, extra)

                if operator == '+':
                    return variable - rvalue
                elif operator == '-':
                    return variable + rvalue
                elif operator == '*':
                    return variable / rvalue
                elif operator == '/':
                    return variable * rvalue
                elif operator == '=':
                    return rvalue

            elif target == rvalue:
                variable = search_for_value(variable, tree, extra)
                lvalue = search_for_value(lvalue, tree, extra)

                if operator == '+':
                    return variable - lvalue
                elif operator == '-':
                    return lvalue - variable
                elif operator == '*':
                    return variable / lvalue
                elif operator == '/':
                    return lvalue / variable
                elif operator == '=':
                    return lvalue

    # last chance, check if it is a extra variable
    if extra and target in extra:
        return extra[target]


def main():
    with open(INPUT_FILE, 'r') as file:
        monkeys = {line.split()[0].replace(':', ''): line.split()[1:]
                   for line in file.read().strip().split('\n')}

    monkeys[MATCHER_NODE][1] = MATCHER_OPERATION
    del monkeys[TARGET]

    value = int(search_for_value(TARGET, monkeys))
    print(value)


if __name__ == '__main__':
    main()
