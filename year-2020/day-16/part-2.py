#!/usr/bin/env python3
#
# --- Day 16: Ticket Translation / Part Two ---
#
# Now that you've identified which tickets contain invalid values,
# discard those tickets entirely. Use the remaining valid tickets
# to determine which field is which.
#
# Using the valid ranges for each field, determine what order the fields
# appear on the tickets. The order is consistent between all tickets:
# if seat is the third field, it is the third field on every ticket,
# including your ticket.
#
# For example, suppose you have the following notes:
#
#   class: 0-1 or 4-19
#   row: 0-5 or 8-19
#   seat: 0-13 or 16-19
#
#   your ticket:
#   11,12,13
#
#   nearby tickets:
#   3,9,18
#   15,1,5
#   5,14,9
#
# Based on the nearby tickets in the above example, the first position
# must be row, the second position must be class, and the third position
# must be seat; you can conclude that in your ticket, class is 12,
# row is 11, and seat is 13.
#
# Once you work out which field is which, look for the six fields
# on your ticket that start with the word departure. What do you get
# if you multiply those six values together?
#
#
# --- Solution ---
#
# First step is to create a collection of valid tickets, which contains all
# tickets that did not have bad values, plus our own ticket. Then from each
# ticket in that collection of valid ones, we take the same field, obtaining
# list of values on the position number #i. Next we iterate over the list
# of constraints and we check whether all these values fit in given ranges.
# This way be build a collection of possible positions of fields on ticket.
# Finally the tricky part is to notice that most of the fields satisfy more
# than one constraint – so by elimination, we need to pick first the field
# which fits exactly one class' constraints, then remove it as a candidate
# from all other possible positions. By doing so for every field, eventually
# we receive set of unique positions. Then we just need to find the indexes
# of fields with names starting from `departure` and multiply values under
# given indexes on our ticket.
#

INPUT_FILE = 'input.txt'


def main():
    data = open(INPUT_FILE, 'r').read().split('\n\n')

    notes = data[0].strip().split('\n')

    constraints = {}
    constraints_indexes = {}
    constraints_possible_indexes = {}

    for note in notes:
        key, value = note.split(': ')
        range1, range2 = value.split(' or ')
        constraints[key] = [
            [int(number) for number in range1.split('-')],
            [int(number) for number in range2.split('-')],
        ]
        constraints_indexes[key] = None
        constraints_possible_indexes[key] = []

    my_ticket = [int(number) for number in data[1].split('\n')[1].split(',')]

    nearby_tickets = [list(map(int, line.split(',')))
                      for line in data[2].strip().split('\n')[1:]]

    valid_tickets = []

    for ticket in nearby_tickets:
        valid_ticket = True

        for number in ticket:
            valid_number = False

            for constraint in constraints.values():
                if constraint[0][0] <= number <= constraint[0][1] \
                   or constraint[1][0] <= number <= constraint[1][1]:
                    valid_number = True

            if not valid_number:
                valid_ticket = False

        if valid_ticket:
            valid_tickets.append(ticket)

    valid_tickets.append(my_ticket)

    for name, constraint in constraints.items():
        for i in range(len(my_ticket)):
            numbers = [ticket[i] for ticket in valid_tickets]
            valid_constraint = True

            for number in numbers:
                if not constraint[0][0] <= number <= constraint[0][1] \
                   and not constraint[1][0] <= number <= constraint[1][1]:
                    valid_constraint = False

            if valid_constraint:
                constraints_possible_indexes[name].append(i)

    while True:
        repeat = False

        for name, indexes in constraints_possible_indexes.items():
            if len(indexes) == 1:
                constraints_indexes[name] = indexes[0]
                repeat = True

        for index in constraints_indexes.values():
            for name in constraints_possible_indexes:
                if index in constraints_possible_indexes[name]:
                    constraints_possible_indexes[name].remove(index)

        if not repeat:
            break

    wanted_fields = [index
                     for name, index in constraints_indexes.items()
                     if name.startswith('departure')]

    result = 1

    for index in wanted_fields:
        result *= my_ticket[index]

    print(result)


if __name__ == '__main__':
    main()
