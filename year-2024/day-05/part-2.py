#!/usr/bin/env python3
#
# --- Day 5: Print Queue / Part Two ---
#
# While the Elves get to work printing the correctly-ordered updates,
# you have a little time to fix the rest of them.
#
# For each of the incorrectly-ordered updates, use the page ordering rules
# to put the page numbers in the right order. For the above example, here
# are the three incorrectly-ordered updates and their correct orderings:
# – 75,97,47,61,53 becomes 97,75,47,61,53.
# – 61,13,29 becomes 61,29,13.
# – 97,13,75,29,47 becomes 97,75,47,29,13.
#
# After taking only the incorrectly-ordered updates and ordering them
# correctly, their middle page numbers are 47, 29, and 47. Adding these
# together produces 123.
#
# Find the updates which are not in the correct order. What do you get
# if you add up the middle page numbers after correctly ordering just
# those updates?
#
#
# --- Solution ---
#
# The difference here is that we ignore the correctly arranged updates and
# instead we build a second collection of updates that needs to be fixed.
# Then we process that collection like a queue: we pick last element, verify
# all the rules and for first rule that do not apply – fix that by swapping
# the two values in place. Once no fix was necessary, we select the middle
# element from the numbers and save for an answer.
#
# Note I had an idea of identifying arbitrary order of all values defined
# in the rules set – and then to use that order to quickly sort the incorrect
# numbers. This worked well for the example data, but unfortunately the real
# input contained cycles like `a < b < c < d < a`, which made it impossible
# to solve it that way.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        rules, updates = file.read().strip().split('\n\n')
        rules = tuple(
                    tuple(map(int, rule.split('|'))) for rule in rules.split()
                )
        updates = tuple(
                    tuple(map(int, u.split(','))) for u in updates.split()
                )

    middle_numbers = []
    updates_to_fix = []

    for numbers in updates:
        for rule in rules:
            number1, number2 = rule

            try:
                before = numbers.index(number1)
                after = numbers.index(number2)

            except ValueError:  # not found – ignore the rule
                continue

            if not before < after:  # wrong order – save numbers to fix
                updates_to_fix.append(list(numbers))
                break

    while updates_to_fix:
        numbers = updates_to_fix.pop()

        for rule in rules:
            number1, number2 = rule

            try:
                before = numbers.index(number1)
                after = numbers.index(number2)

            except ValueError:  # not found – ignore the rule
                continue

            if not before < after:  # wrong order – fix and re-add to queue
                numbers[before] = number2
                numbers[after] = number1
                updates_to_fix.append(numbers)
                break

        else:  # all rules satisfied after fixing
            middle_numbers.append(numbers[len(numbers) // 2])

    print(sum(middle_numbers))


if __name__ == '__main__':
    main()
