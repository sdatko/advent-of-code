#!/usr/bin/env python3
#
# --- Day 14: Extended Polymerization / Part Two ---
#
# The resulting polymer isn't nearly strong enough to reinforce the submarine.
# You'll need to run more steps of the pair insertion process; a total of 40
# steps should do it.
#
# In the above example, the most common element is B (occurring 2192039569602
# times) and the least common element is H (occurring 3849876073 times);
# subtracting these produces 2188189693529.
#
# Apply 40 steps of pair insertion to the polymer template and find the most
# and least common elements in the result. What do you get if you take the
# quantity of the most common element and subtract the quantity of the least
# common element?
#
#
# --- Solution ---
#
# For this part I needed to rewrite an algorithm, as it turned to be not
# ineffective for greater number of steps. Most important was to notice that
# our dict of rules contains all pairs that are possible to obtain ever
# in our simulation. Then I realised that during the simulation, the real
# action is that each single pair produces two new pairs, e.g. for polymer
# ABC and rules AB->C, BC->A we have pair AB replaced by pair AC and CB, and
# pair BC becomes pairs BA and AC, so we get new polymer ACBAC out of it.
# However we are not interested in exact polymer string, just its components
# count, so instead of working on a string we can simply count the pairs.
# Rewriting the code to utilize that interpretation brought us to much more
# effective solution. The last deal was to count letter occurrences here.
# It can be noticed that every letter (except first and last) appears twice
# in set of pairs – e.g. C in the given example is part of pairs AC and CB
# (due to AB producing AC and CB). Therefore in a loop we just count the number
# of occurrences as first letter in each pair, then we add the last letter
# of a polymer string we will not count that way.
# The final answer is a difference between maximum and minimum counts there.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        puzzle_input = file.read().split('\n\n')

    template = puzzle_input[0].strip()
    rules = {pair: insertion
             for line in puzzle_input[1].strip().split('\n')
             for pair, insertion in [line.strip().split(' -> ')]}

    steps = 40
    pairs = {pair: 0 for pair in rules.keys()}

    for index in range(len(template) - 1):
        pair = template[index:index + 2]
        pairs[pair] += 1

    for step in range(steps):
        pairs_with_inserted = pairs.copy()

        for pair in pairs:
            count = pairs[pair]
            if count:
                new_pair_1 = pair[0] + rules[pair]
                new_pair_2 = rules[pair] + pair[1]

                pairs_with_inserted[pair] -= count
                pairs_with_inserted[new_pair_1] += count
                pairs_with_inserted[new_pair_2] += count

        pairs = pairs_with_inserted.copy()

    letters = {letter: 0 for letter in set(''.join(pairs.keys()))}

    for pair in pairs:
        letters[pair[0]] += pairs[pair]
    letters[template[-1]] += 1

    print(max(letters.values()) - min(letters.values()))


if __name__ == '__main__':
    main()
