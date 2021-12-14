#!/usr/bin/env python3
#
# Task:
# The incredible pressures at this depth are starting to put a strain
# on your submarine. The submarine has polymerization equipment that
# would produce suitable materials to reinforce the submarine, and
# the nearby volcanically-active caves should even have the necessary
# input elements in sufficient quantities.
# The submarine manual contains instructions for finding the optimal polymer
# formula; specifically, it offers a polymer template and a list of pair
# insertion rules (your puzzle input). You just need to work out what
# polymer would result after repeating the pair insertion process a few times.
# The first line is the polymer template - this is the starting point
# of the process.
# The following section defines the pair insertion rules. A rule like AB -> C
# means that when elements A and B are immediately adjacent, element C should
# be inserted between them. These insertions all happen simultaneously.
# So, starting with the example polymer template NNCB, the first step
# simultaneously considers all three pairs:
# - The first pair (NN) matches the rule NN -> C, so element C is inserted
#   between the first N and the second N.
# - The second pair (NC) matches the rule NC -> B, so element B is inserted
#   between the N and the C.
# - The third pair (CB) matches the rule CB -> H, so element H is inserted
#   between the C and the B.
# Note that these pairs overlap: the second element of one pair is the
# first element of the next pair. Also, because all pairs are considered
# simultaneously, inserted elements are not considered to be part of a pair
# until the next step.
# After the first step of this process, the polymer becomes NCNBCHB.
# This polymer grows quickly.
# Apply 10 steps of pair insertion to the polymer template and find the most
# and least common elements in the result. What do you get if you take the
# quantity of the most common element and subtract the quantity of the least
# common element?
#
# Solution:
# We read the puzzle input by separating it with empty line. The first part
# then is our polymer template and the second part is a list of insertion
# rules for pairs of polymer components. For the latter we produce a dictionary
# of what letter (component) should each pair produce.
# Then we iterate in a loop on each pair of current polymer components.
# For N-long polymer, there are N-1 pairs. We find the component (letter)
# that should be inserted between current pair and we extend the polymer
# string by adding that component.
# Such operation is repeated a few times (our simulation steps).
# Finally we produce a dict of letter counts for our polymer string
# and return the difference between maximum and minimum letter occurrences
# as an answer.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        puzzle_input = file.read().split('\n\n')

    template = puzzle_input[0].strip()
    rules = {pair: insertion
             for line in puzzle_input[1].strip().split('\n')
             for pair, insertion in [line.strip().split(' -> ')]}

    steps = 10
    polymer = template

    for step in range(steps):
        pairs = len(polymer) - 1

        for index in range(pairs):
            pair = polymer[2 * index:2 * index + 2]
            insertion = rules.get(pair)
            polymer = (
                polymer[:2 * index + 1] + insertion + polymer[2 * index + 1:]
            )

    letters = {letter: polymer.count(letter) for letter in set(polymer)}

    print(max(letters.values()) - min(letters.values()))


if __name__ == '__main__':
    main()
