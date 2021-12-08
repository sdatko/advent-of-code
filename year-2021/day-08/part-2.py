#!/usr/bin/env python3
#
# Task:
# Through a little deduction, you should now be able to determine the remaining
# digits. Consider again the first example above:
#   acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab
#   | cdfeb fcadb cdfeb cdbaf
# After some careful analysis, the mapping between signal wires and segments
# only make sense in the following configuration:
#    dddd
#   e    a
#   e    a
#    ffff
#   g    b
#   g    b
#    cccc
# So, the unique signal patterns would correspond to the following digits:
#   acedgfb: 8
#   cdfbe: 5
#   gcdfa: 2
#   fbcad: 3
#   dab: 7
#   cefabd: 9
#   cdfgeb: 6
#   eafb: 4
#   cagedb: 0
#   ab: 1
# Then, the four digits of the output value can be decoded:
#   cdfeb: 5
#   fcadb: 3
#   cdfeb: 5
#   cdbaf: 3
# Therefore, the output value for this entry is 5353.
# For each entry, determine all of the wire/segment connections and decode
# the four-digit output values. What do you get if you add up all of the
# output values?
#
# Solution:
# This part requires us to find a mapping between signals and the digits these
# signals represent. The problem is that in each entry, the signal parts
# (letters `a`, `b`, etc.) correspond to a different part of display.
# Utilizing sets in Python works here well for finding the solution,
# as the order of letters in signal seems to have no meaning.
# The mapping requires two passes on the signal – first, we need to find what
# signal (set of letters) encodes the values we can be immediately sure of,
# for example – 1 can be 'cf', then 4 is 'bcdf', 7 is 'acf' and 8 is 'abcdefg':
#     1:       4:       7:       8:
#    ....     ....     aaaa     aaaa
#   .    c   b    c   .    c   b    c
#   .    c   b    c   .    c   b    c
#    ....     dddd     ....     dddd
#   .    f   .    f   .    f   e    f
#   .    f   .    f   .    f   e    f
#    ....     ....     ....     gggg
# Knowing that, we have to find sets of letters that represents all remaining
# digits – 0, 2, 3, 5, 6 and 9.
#     0:       2:       3:       5:       6:       9:
#    aaaa     aaaa     aaaa     aaaa     aaaa     aaaa
#   b    c   .    c   .    c   b    .   b    .   b    c
#   b    c   .    c   .    c   b    .   b    .   b    c
#    ....     dddd     dddd     dddd     dddd     dddd
#   e    f   e    .   .    f   .    f   e    f   .    f
#   e    f   e    .   .    f   .    f   e    f   .    f
#    gggg     gggg     gggg     gggg     gggg     gggg
# We can notice that these letters consist of 5 or 6 elements.
# Focusing on the missing parts (1 or 2 elements) will narrow the problem
# to two smaller groups: digits 0, 6, 9 and digits 2, 3, 5.
# Then in each subgroup we do another narrowing of the problem.
# For example, from digits 0, 6 and 9, digit 9 is the only one that has
# alla 4 segments common with digit 4, while the remaining have only 3 common
# elements. At this point we are sure what digit decodes 9.
# To distinguish 0 and 6, we can count in addition the common segments with
# digit 1 – for digit 0 it is 2, for digit 6 it is 1.
# Using the same approach for digits 2, 3, 5 gives us the whole mapping
# for a particular signal.
# For convenience of use, the final mapping is reversed then, so the keys
# represent signals (set of letters) and items corresponds to their values.
# In main part we just need to iterate over the output for a given signal
# and use the prepared mapping on each part of the output to decode the number.
# For final answer, we just sum the numbers we found.
#

INPUT_FILE = 'input.txt'


def decode_signal(signal):
    digits = [set(digit) for digit in signal.split()]
    to_remove = []
    mapping = {}

    for digit in digits:
        if len(digit) == 2:
            mapping['1'] = set(digit)
            to_remove.append(digit)
        elif len(digit) == 3:
            mapping['7'] = set(digit)
            to_remove.append(digit)
        elif len(digit) == 4:
            mapping['4'] = set(digit)
            to_remove.append(digit)
        elif len(digit) == 7:
            mapping['8'] = set(digit)
            to_remove.append(digit)

    for element in to_remove:
        digits.remove(element)

    for digit in digits:
        if len(digit) == 5:
            common_with_4 = digit & mapping['4']

            if len(common_with_4) == 2:
                mapping['2'] = set(digit)

            elif len(common_with_4) == 3:
                common_with_both_4_and_1 = common_with_4 & mapping['1']

                if len(common_with_both_4_and_1) == 2:
                    mapping['3'] = set(digit)
                elif len(common_with_both_4_and_1) == 1:
                    mapping['5'] = set(digit)

        elif len(digit) == 6:
            common_with_4 = digit & mapping['4']

            if len(common_with_4) == 4:
                mapping['9'] = set(digit)

            elif len(common_with_4) == 3:
                common_with_both_4_and_1 = common_with_4 & mapping['1']

                if len(common_with_both_4_and_1) == 2:
                    mapping['0'] = set(digit)
                elif len(common_with_both_4_and_1) == 1:
                    mapping['6'] = set(digit)

    mapping = {frozenset(signal): value for value, signal in mapping.items()}

    return mapping


def main():
    entries = [line.strip() for line in open(INPUT_FILE, 'r')]
    signals = [entry.split(' | ')[0] for entry in entries]
    outputs = [entry.split(' | ')[1] for entry in entries]

    values = []

    for signal, output in zip(signals, outputs):
        mapping = decode_signal(signal)
        value_string = ''

        for digit in output.split():
            value_string += mapping[frozenset(digit)]

        values.append(int(value_string))

    print(sum(values))


if __name__ == '__main__':
    main()
