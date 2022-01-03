#!/usr/bin/env python3
#
# --- Day 18: Snailfish / Part Two ---
#
# You notice a second question on the back of the homework assignment:
#
# What is the largest magnitude you can get from adding only two
# of the snailfish numbers?
#
# Note that snailfish addition is not commutative - that is, x + y and
# y + x can produce different results.
#
# Again considering the last example homework assignment above:
#   [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
#   [[[5,[2,8]],4],[5,[[9,9],0]]]
#   [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
#   [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
#   [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
#   [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
#   [[[[5,4],[7,7]],8],[[8,3],8]]
#   [[9,3],[[9,9],[6,[4,9]]]]
#   [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
#   [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
#
# The largest magnitude of the sum of any two snailfish numbers in this list
# is 3993. This is the magnitude of [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
# + [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]], which reduces
# to [[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]].
#
# What is the largest magnitude of any sum of two different snailfish numbers
# from the homework assignment?
#
#
# --- Solution ---
#
# The code below is a different implementation of the same task, which I could
# achieve after completing both parts and understanding better the problem.
# Here, instead of nested lists, each number I represent as a sparse list of
# pairs: depth and actual value (for convenience, kept in memory as dicts).
# Two neighbor elements with the same depth attribute represent a pair [x, y]
# being a snailfish number. In essence, it behaves exactly like the previous
# implementation (tree?), just finding the closest left and right elements
# is much easier this way. So, example element [[9,3],[[9,9],[6,[4,9]]]] is in
# our representation: [{2: 9}, {2: 3}, {3: 9}, {3: 9}, {3: 6}, {4:, 4}, {4: 9}]
# (written as {depth: value} instead of {'depth': 2, 'value': 9} to save space;
# note that the depth is equal to number of open brackets when reading from
# the left side).
#

INPUT_FILE = 'input.txt'


def explode(number):
    for index in range(len(number) - 1):
        left = number[index]
        right = number[index + 1]

        if left['depth'] > 4 and right['depth'] > 4:
            if index > 0:
                number[index - 1]['value'] += left['value']
            if index < len(number) - 2:
                number[index + 2]['value'] += right['value']

            number[index] = {
                'depth': left['depth'] - 1,
                'value': 0
            }
            number.remove(right)

            return True

    return False


def split(number):
    for index in range(len(number)):
        value = number[index]['value']

        if value >= 10:
            left = value // 2
            right = value - left

            number[index]['depth'] += 1
            number[index]['value'] = left

            number.insert(index + 1, {
                'depth': number[index]['depth'],
                'value': right
            })

            return True

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
    new_number = []
    for element in number:
        new_number.append(element.copy())
    return new_number


def snailsum(number1, number2):
    new_number = deepcopy(number1 + number2)

    for element in new_number:
        element['depth'] += 1

    return reduce(new_number)


def magnitude(number):
    tmp_number = deepcopy(number)

    while len(tmp_number) > 1:
        for index in range(len(tmp_number) - 1):
            left = tmp_number[index]
            right = tmp_number[index + 1]

            if left['depth'] == right['depth']:
                tmp_number[index] = {
                    'depth': left['depth'] - 1,
                    'value': 3 * left['value'] + 2 * right['value'],
                }
                tmp_number.remove(right)
                break

    return tmp_number[0]['value']


def main():
    lines = [line.strip() for line in open(INPUT_FILE, 'r')]
    numbers = []

    for line in lines:
        depth = 0
        number = []
        for character in line:
            if character == '[':
                depth += 1
            elif character == ']':
                depth -= 1
            elif character == ',':
                continue
            else:
                value = int(character)
                number.append({'depth': depth, 'value': value})
        numbers.append(number)

    max_magnitude = 0

    for number1 in numbers:
        for number2 in numbers:
            if number1 == number2:
                continue

            tmp = magnitude(snailsum(number1, number2))
            if tmp > max_magnitude:
                max_magnitude = tmp

    print(max_magnitude)


if __name__ == '__main__':
    main()
