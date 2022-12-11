#!/usr/bin/env python3
#
# --- Day 11: Monkey in the Middle / Part Two ---
#
# You're worried you might not ever get your items back. So worried, in fact,
# that your relief that a monkey's inspection didn't damage an item no longer
# causes your worry level to be divided by three.
#
# Unfortunately, that relief was all that was keeping your worry levels
# from reaching ridiculous levels. You'll need to find another way to keep
# your worry levels manageable.
#
# At this rate, you might be putting up with these monkeys for a very long time
# - possibly 10000 rounds!
#
# With these new rules, you can still figure out the monkey business after
# 10000 rounds. Using the same example above:
#
#   == After round 1 ==
#   Monkey 0 inspected items 2 times.
#   Monkey 1 inspected items 4 times.
#   Monkey 2 inspected items 3 times.
#   Monkey 3 inspected items 6 times.
#
#   == After round 20 ==
#   Monkey 0 inspected items 99 times.
#   Monkey 1 inspected items 97 times.
#   Monkey 2 inspected items 8 times.
#   Monkey 3 inspected items 103 times.
#
#   == After round 1000 ==
#   Monkey 0 inspected items 5204 times.
#   Monkey 1 inspected items 4792 times.
#   Monkey 2 inspected items 199 times.
#   Monkey 3 inspected items 5192 times.
#
#   == After round 2000 ==
#   Monkey 0 inspected items 10419 times.
#   Monkey 1 inspected items 9577 times.
#   Monkey 2 inspected items 392 times.
#   Monkey 3 inspected items 10391 times.
#
#   == After round 3000 ==
#   Monkey 0 inspected items 15638 times.
#   Monkey 1 inspected items 14358 times.
#   Monkey 2 inspected items 587 times.
#   Monkey 3 inspected items 15593 times.
#
#   == After round 4000 ==
#   Monkey 0 inspected items 20858 times.
#   Monkey 1 inspected items 19138 times.
#   Monkey 2 inspected items 780 times.
#   Monkey 3 inspected items 20797 times.
#
#   == After round 5000 ==
#   Monkey 0 inspected items 26075 times.
#   Monkey 1 inspected items 23921 times.
#   Monkey 2 inspected items 974 times.
#   Monkey 3 inspected items 26000 times.
#
#   == After round 6000 ==
#   Monkey 0 inspected items 31294 times.
#   Monkey 1 inspected items 28702 times.
#   Monkey 2 inspected items 1165 times.
#   Monkey 3 inspected items 31204 times.
#
#   == After round 7000 ==
#   Monkey 0 inspected items 36508 times.
#   Monkey 1 inspected items 33488 times.
#   Monkey 2 inspected items 1360 times.
#   Monkey 3 inspected items 36400 times.
#
#   == After round 8000 ==
#   Monkey 0 inspected items 41728 times.
#   Monkey 1 inspected items 38268 times.
#   Monkey 2 inspected items 1553 times.
#   Monkey 3 inspected items 41606 times.
#
#   == After round 9000 ==
#   Monkey 0 inspected items 46945 times.
#   Monkey 1 inspected items 43051 times.
#   Monkey 2 inspected items 1746 times.
#   Monkey 3 inspected items 46807 times.
#
#   == After round 10000 ==
#   Monkey 0 inspected items 52166 times.
#   Monkey 1 inspected items 47830 times.
#   Monkey 2 inspected items 1938 times.
#   Monkey 3 inspected items 52013 times.
#
# After 10000 rounds, the two most active monkeys inspected items 52166
# and 52013 times. Multiplying these together, the level of monkey business
# in this situation is now 2713310158.
#
# Worry levels are no longer divided by three after each item is inspected;
# you'll need to find another way to keep your worry levels manageable.
# Starting again from the initial state in your puzzle input,
# what is the level of monkey business after 10000 rounds?
#
#
# --- Solution ---
#
# The difference here is that we need to consider much bigger number of rounds.
# Also the step of dividing by 3 is gone, which causes the worry level to reach
# extremely high values after just a few dozens of rounds.
# The trick is, we do not really care about the worry level values themselves,
# we just need them to append a newly calculated value into the right target
# monkey structure. The decision (selection of target monkey) is dependent
# on divisibility by a certain number (different for each monkey). Therefore
# we can reduce the range for worry levels – the biggest value needed to be
# considered is a multiplication of all individual divisors (formally called
# the LCM – lowest common multiple). This is due to the following properties
# of modulo operation:
# – (a + b) % n == ((a % n) + (b % n)) % n,
# – (a * b) % n == ((a % n) * (b % n)) % n,
# – (a + k * n) % n = m  <==>  a % n = m  (a consequence of the two above).
# In other words, we need to find a value that would not change the result
# of the divisibility tests we perform: such as for  `a % m`  and  `a % n`,
# from the last property above we can add a multiply  `m * n`  to value  `a`,
# obtaining  `(a + m * n) % n`  and  `(a + m * n) % m`  and it will not change
# the outcome as  `(m * n) % n == (n * m) % m == 0`.
# So apart from lines 148-150 and 158, the rest of the code
# is exactly the same as it was for part 1.
#

INPUT_FILE = 'input.txt'

ROUNDS = 10000


def main():
    with open(INPUT_FILE, 'r') as file:
        monkeys = dict()
        definitions = [dict(line.split(':') for line in definition.split('\n'))
                       for definition in file.read()
                                             .replace('Monkey', 'ID: monkey')
                                             .replace(':\n', '\n')
                                             .replace(': ', ':')
                                             .replace('  ', '')
                                             .strip()
                                             .split('\n\n')]

        for definition in definitions:
            items = list(map(int, definition['Starting items'].split(', ')))
            operation = eval('lambda old: '
                             + definition['Operation'].replace('new = ', ''))

            monkeys[definition['ID']] = {
                'items': items,
                'operation': operation,
                'divisible_by': int(definition['Test'].split()[-1]),
                'true': definition['If true'][-8:],
                'false': definition['If false'][-8:],
                'inspected': 0,
            }

    common_divisor = 1
    for monkey in monkeys.values():
        common_divisor *= monkey['divisible_by']

    for _ in range(ROUNDS):
        for monkey in monkeys.values():
            while len(monkey['items']) > 0:
                item = monkey['items'].pop()
                worry_level = monkey['operation'](item)

                worry_level = worry_level % common_divisor

                if worry_level % monkey['divisible_by'] == 0:
                    monkeys[monkey['true']]['items'].append(worry_level)
                else:
                    monkeys[monkey['false']]['items'].append(worry_level)

                monkey['inspected'] += 1

    top1, top2 = sorted([monkey['inspected'] for monkey in monkeys.values()],
                        reverse=True)[:2]

    print(top1 * top2)


if __name__ == '__main__':
    main()
