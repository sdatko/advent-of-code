#!/usr/bin/env python3
#
# --- Day 18: Snailfish ---
#
# You descend into the ocean trench and encounter some snailfish. They say
# they saw the sleigh keys! They'll even tell you which direction the keys
# went if you help one of the smaller snailfish with his math homework.
#
# Snailfish numbers aren't like regular numbers. Instead, every snailfish
# number is a pair - an ordered list of two elements. Each element of the
# pair can be either a regular number or another pair.
#
# Pairs are written as [x,y], where x and y are the elements within the pair.
# Here are some example snailfish numbers, one snailfish number per line:
#   [1,2]
#   [[1,2],3]
#   [9,[8,7]]
#   [[1,9],[8,5]]
#   [[[[1,2],[3,4]],[[5,6],[7,8]]],9]
#   [[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
#   [[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]
#
# This snailfish homework is about addition. To add two snailfish numbers,
# form a pair from the left and right parameters of the addition operator.
# For example, [1,2] + [[3,4],5] becomes [[1,2],[[3,4],5]].
#
# There's only one problem: snailfish numbers must always be reduced, and
# the process of adding two snailfish numbers can result in snailfish numbers
# that need to be reduced.
#
# To reduce a snailfish number, you must repeatedly do the first action
# in this list that applies to the snailfish number:
# - If any pair is nested inside four pairs, the leftmost such pair explodes.
# - If any regular number is >=10, the leftmost such regular number splits.
#
# Once no action in the above list applies, the snailfish number is reduced.
#
# During reduction, at most one action applies, after which the process returns
# to the top of the list of actions. For example, if split produces a pair that
# meets the explode criteria, that pair explodes before other splits occur.
#
# To explode a pair, the pair's left value is added to the first regular
# number to the left of the exploding pair (if any), and the pair's right
# value is added to the first regular number to the right of the exploding
# pair (if any). Exploding pairs will always consist of two regular numbers.
# Then, the entire exploding pair is replaced with the regular number 0.
#
# Here are some examples of a single explode action:
# - [[[[[9,8],1],2],3],4] becomes [[[[0,9],2],3],4] (the 9 has no regular
#   number to its left, so it is not added to any regular number).
# - [7,[6,[5,[4,[3,2]]]]] becomes [7,[6,[5,[7,0]]]] (the 2 has no regular
#   number to its right, and so it is not added to any regular number).
# - [[6,[5,[4,[3,2]]]],1] becomes [[6,[5,[7,0]]],3].
# - [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]] becomes
#   [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] (the pair [3,2] is unaffected because the
#   pair [7,3] is further to the left; [3,2] would explode on the next action).
# - [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]] becomes [[3,[2,[8,0]]],[9,[5,[7,0]]]].
#
# To split a regular number, replace it with a pair; the left element of the
# pair should be the regular number divided by two and rounded down, while
# the right element of the pair should be the regular number divided by two
# and rounded up. For example, 10 becomes [5,5], 11 becomes [5,6], 12 becomes
# [6,6], and so on.
#
# Here is the process of finding the reduced result of
# [[[[4,3],4],4],[7,[[8,4],9]]] + [1,1]:
# - after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
# - after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
# - after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
# - after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
# - after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
# - after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
#
# Once no reduce actions apply, the snailfish number that remains is the actual
# result of the addition operation: [[[[0,7],4],[[7,8],[6,0]]],[8,1]].
#
# The homework assignment involves adding up a list of snailfish numbers (your
# puzzle input). The snailfish numbers are each listed on a separate line.
# Add the first snailfish number and the second, then add that result and
# the third, then add that result and the fourth, and so on until all numbers
# in the list have been used once.
#
# For example, the final sum of this list is [[[[1,1],[2,2]],[3,3]],[4,4]]:
#   [1,1]
#   [2,2]
#   [3,3]
#   [4,4]
#
# The final sum of this list is [[[[3,0],[5,3]],[4,4]],[5,5]]:
#   [1,1]
#   [2,2]
#   [3,3]
#   [4,4]
#   [5,5]
#
# The final sum of this list is [[[[5,0],[7,4]],[5,5]],[6,6]]:
#   [1,1]
#   [2,2]
#   [3,3]
#   [4,4]
#   [5,5]
#   [6,6]
#
# Here's a slightly larger example:
#   [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
#   [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
#   [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
#   [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
#   [7,[5,[[3,8],[1,4]]]]
#   [[2,[2,2]],[8,[8,1]]]
#   [2,9]
#   [1,[[[9,3],9],[[9,0],[0,7]]]]
#   [[[5,[7,4]],7],1]
#   [[[[4,2],2],6],[8,7]]
#
# The final sum [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] is found
# after adding up the above snailfish numbers:
#     [[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
#   + [7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
#   = [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
#
#     [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
#   + [[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
#   = [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
#
#     [[[[6,7],[6,7]],[[7,7],[0,7]]],[[[8,7],[7,7]],[[8,8],[8,0]]]]
#   + [[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
#   = [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
#
#     [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
#   + [7,[5,[[3,8],[1,4]]]]
#   = [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
#
#     [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
#   + [[2,[2,2]],[8,[8,1]]]
#   = [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
#
#     [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
#   + [2,9]
#   = [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
#
#     [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
#   + [1,[[[9,3],9],[[9,0],[0,7]]]]
#   = [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
#
#     [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
#   + [[[5,[7,4]],7],1]
#   = [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
#
#     [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
#   + [[[[4,2],2],6],[8,7]]
#   = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
#
# To check whether it's the right answer, the snailfish teacher only checks
# the magnitude of the final sum. The magnitude of a pair is 3 times the
# magnitude of its left element plus 2 times the magnitude of its right
# element. The magnitude of a regular number is just that number.
#
# For example, the magnitude of [9,1] is 3*9 + 2*1 = 29; the magnitude of [1,9]
# is 3*1 + 2*9 = 21. Magnitude calculations are recursive: the magnitude of
# [[9,1],[1,9]] is 3*29 + 2*21 = 129.
#
# Here are a few more magnitude examples:
# - [[1,2],[[3,4],5]] becomes 143.
# - [[[[0,7],4],[[7,8],[6,0]]],[8,1]] becomes 1384.
# - [[[[1,1],[2,2]],[3,3]],[4,4]] becomes 445.
# - [[[[3,0],[5,3]],[4,4]],[5,5]] becomes 791.
# - [[[[5,0],[7,4]],[5,5]],[6,6]] becomes 1137.
# - [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]] becomes 3488.
#
# So, given this example homework assignment:
# - [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
# - [[[5,[2,8]],4],[5,[[9,9],0]]]
# - [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
# - [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
# - [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
# - [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
# - [[[[5,4],[7,7]],8],[[8,3],8]]
# - [[9,3],[[9,9],[6,[4,9]]]]
# - [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# - [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
#
# The final sum is:
#   [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
#
# The magnitude of this final sum is 4140.
#
# Add up all of the snailfish numbers from the homework assignment in the order
# they appear. What is the magnitude of the final sum?
#
#
# --- Solution ---
#
# We start by reading the input file. The syntax and description of the task
# made me think that this can be easily interpreted as lists in Python,
# so I simply treat the input as Python code after stripping the whitespaces.
# It would be safer to use json.load() call than eval(), but as I restricted
# myself to not use any import, I stick with the latter (the alternative was
# to write parsting, but well... the description is already complex enough).
# Then I started implementing the explode() function, which checks for lists
# and if we reach depth of 4 and there is another list, we replace that list
# with 0 and we attempt to add that list elements to left and right neighbor.
# As the code became overwhelming, the insertion to neighbors was implemented
# as another functions. We need to ensure we perform only one explode at time,
# so immediately there is return. In similar manner we implement the split()
# function, but this time we are looking for integers grater than 10 and when
# there is any, we replace it with and array of 2 smaller elements. After
# preparing this, the function reduce() and snailsum() is just a simple set
# of calls. For the final answer, we need to write the magnitude() function
# and this is the moment I realised I ignored the assumption that there
# are always only 2 elements in each list (pairs), so the previous code
# could be much more simplified.
# The deepcopy() function here is a legacy from part 2, where it was needed
# as all my operations were done in place, instead of producing new elements.
# However, as I felt ashamed of producing such abomination, later I figured out
# the other way to implement this whole mathematics.
#

INPUT_FILE = 'input.txt'


def insert_left(number, left, n0, n1, n2, n3):
    if n3 > 0:
        if isinstance(number[n0][n1][n2][n3 - 1], list):
            number[n0][n1][n2][n3 - 1][-1] += left
        else:
            number[n0][n1][n2][n3 - 1] += left
    elif n2 > 0:
        if isinstance(number[n0][n1][n2 - 1], list):
            if isinstance(number[n0][n1][n2 - 1][-1], list):
                number[n0][n1][n2 - 1][-1][-1] += left
            else:
                number[n0][n1][n2 - 1][-1] += left
        else:
            number[n0][n1][n2 - 1] += left
    elif n1 > 0:
        if isinstance(number[n0][n1 - 1], list):
            if isinstance(number[n0][n1 - 1][-1], list):
                if isinstance(number[n0][n1 - 1][-1][-1], list):
                    number[n0][n1 - 1][-1][-1][-1] += left
                else:
                    number[n0][n1 - 1][-1][-1] += left
            else:
                number[n0][n1 - 1][-1] += left
        else:
            number[n0][n1 - 1] += left
    elif n0 > 0:
        if isinstance(number[n0 - 1], list):
            if isinstance(number[n0 - 1][-1], list):
                if isinstance(number[n0 - 1][-1][-1], list):
                    if isinstance(number[n0 - 1][-1][-1][-1], list):
                        number[n0 - 1][-1][-1][-1][-1] += left
                    else:
                        number[n0 - 1][-1][-1][-1] += left
                else:
                    number[n0 - 1][-1][-1] += left
            else:
                number[n0 - 1][-1] += left
        else:
            number[n0 - 1] += left
    else:
        return False
    return True


def insert_right(number, right, n0, n1, n2, n3):
    if n3 < len(number[n0][n1][n2]) - 1:
        if isinstance(number[n0][n1][n2][n3 + 1], list):
            number[n0][n1][n2][n3 + 1][0] += right
        else:
            number[n0][n1][n2][n3 + 1] += right
    elif n2 < len(number[n0][n1]) - 1:
        if isinstance(number[n0][n1][n2 + 1], list):
            if isinstance(number[n0][n1][n2 + 1][0], list):
                number[n0][n1][n2 + 1][0][0] += right
            else:
                number[n0][n1][n2 + 1][0] += right
        else:
            number[n0][n1][n2 + 1] += right
    elif n1 < len(number[n0]) - 1:
        if isinstance(number[n0][n1 + 1], list):
            if isinstance(number[n0][n1 + 1][0], list):
                if isinstance(number[n0][n1 + 1][0][0], list):
                    number[n0][n1 + 1][0][0][0] += right
                else:
                    number[n0][n1 + 1][0][0] += right
            else:
                number[n0][n1 + 1][0] += right
        else:
            number[n0][n1 + 1] += right
    elif n0 < len(number) - 1:
        if isinstance(number[n0 + 1], list):
            if isinstance(number[n0 + 1][0], list):
                if isinstance(number[n0 + 1][0][0], list):
                    if isinstance(number[n0 + 1][0][0][0], list):
                        number[n0 + 1][0][0][0][0] += right
                    else:
                        number[n0 + 1][0][0][0] += right
                else:
                    number[n0 + 1][0][0] += right
            else:
                number[n0 + 1][0] += right
        else:
            number[n0 + 1] += right
    else:
        return False
    return True


def explode(number):
    for n0, first in enumerate(number):
        if not isinstance(first, list):
            continue

        for n1, second in enumerate(first):
            if not isinstance(second, list):
                continue

            for n2, third in enumerate(second):
                if not isinstance(third, list):
                    continue

                for n3, fourth in enumerate(third):
                    if isinstance(fourth, list):  # We need to explode that
                        left = fourth[0]
                        right = fourth[1]

                        insert_left(number, left, n0, n1, n2, n3)
                        insert_right(number, right, n0, n1, n2, n3)

                        third[n3] = 0

                        return True

    return False


def split(number):
    for n0, first in enumerate(number):
        if isinstance(first, int):
            if first >= 10:
                left = first // 2
                right = first - left
                number[n0] = [left, right]
                return True
            continue

        for n1, second in enumerate(first):
            if isinstance(second, int):
                if second >= 10:
                    left = second // 2
                    right = second - left
                    first[n1] = [left, right]
                    return True
                continue

            for n2, third in enumerate(second):
                if isinstance(third, int):
                    if third >= 10:
                        left = third // 2
                        right = third - left
                        second[n2] = [left, right]
                        return True
                    continue

                for n3, fourth in enumerate(third):
                    if isinstance(fourth, int):
                        if fourth >= 10:
                            left = fourth // 2
                            right = fourth - left
                            third[n3] = [left, right]
                            return True
                        continue

    return False


def reduce(number):
    while True:
        if explode(number):
            continue
        if split(number):
            continue
        break
    return number


def deepcopy(number):
    number = number.copy()

    for index, element in enumerate(number):
        if isinstance(element, list):
            number[index] = deepcopy(element)
    return number


def snailsum(number1, number2):
    return reduce(deepcopy([number1, number2]))


def magnitude(number):
    if isinstance(number, int):
        return number

    left = 3 * magnitude(number[0])
    right = 2 * magnitude(number[1])
    value = left + right

    return value


def main():
    numbers = [eval(number.strip()) for number in open(INPUT_FILE, 'r')]

    number = numbers.pop(0)
    for next_number in numbers:
        number = snailsum(number, next_number)

    print(magnitude(number))


if __name__ == '__main__':
    main()
