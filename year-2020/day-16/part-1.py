#!/usr/bin/env python3
#
# Task:
# You collect the rules for ticket fields, the numbers on your ticket,
# and the numbers on other nearby tickets for the same train service
# (via the airport security cameras) together into a single document
# you can reference (your puzzle input).
# The rules for ticket fields specify a list of fields that exist somewhere
# on the ticket and the valid ranges of values for each field. For example,
# a rule like class: 1-3 or 5-7 means that one of the fields in every ticket
# is named class and can be any value in the ranges 1-3 or 5-7 (inclusive,
# such that 3 and 5 are both valid in this field, but 4 is not).
# Each ticket is represented by a single line of comma-separated values.
# The values are the numbers on the ticket in the order they appear;
# every ticket has the same format. For example, consider this ticket:
# .--------------------------------------------------------.
# | ????: 101    ?????: 102   ??????????: 103     ???: 104 |
# |                                                        |
# | ??: 301  ??: 302             ???????: 303      ??????? |
# | ??: 401  ??: 402           ???? ????: 403    ????????? |
# '--------------------------------------------------------'
# Here, ? represents text in a language you don't understand. This ticket
# might be represented as 101,102,103,104,301,302,303,401,402,403; of course,
# the actual train tickets you're looking at are much more complicated.
# In any case, you've extracted just the numbers in such a way that the first
# number is always the same specific field, the second number is always
# a different specific field, and so on - you just don't know what each
# position actually means!
# Start by determining which tickets are completely invalid; these are
# tickets that contain values which aren't valid for any field. Ignore
# your ticket for now.
# Consider the validity of the nearby tickets you scanned.
# What is your ticket scanning error rate?
#
# Solution:
# We start by reading the file and dividing the input data to three groups
# that are separated by two empty lines. The first group contains information
# about constraints for the ticket fields, the second is our ticket, the third
# is a set of other tickets. The constraints are kept as dictionary, where
# the key is a constraint name and the value is a list of ranges of values
# valid for this field. Then we process the nearby tickets, assuming they
# incorrect first, we look for any constraint that would match each value
# on the ticket. If on ticket there is a value that does not satisfy any of
# the constraints, we save the value to a collection. Finally we print the sum
# of values stored in this collection.
#

INPUT_FILE = 'input.txt'


def main():
    data = open(INPUT_FILE, 'r').read().split('\n\n')

    notes = data[0].strip().split('\n')

    constraints = {}
    for note in notes:
        key, value = note.split(': ')
        range1, range2 = value.split(' or ')
        constraints[key] = [
            [int(number) for number in range1.split('-')],
            [int(number) for number in range2.split('-')],
        ]

    nearby_tickets = [list(map(int, line.split(',')))
                      for line in data[2].strip().split('\n')[1:]]

    bad_values = []

    for ticket in nearby_tickets:
        for number in ticket:
            valid = False

            for constraint in constraints.values():
                if constraint[0][0] <= number <= constraint[0][1] \
                   or constraint[1][0] <= number <= constraint[1][1]:
                    valid = True

            if not valid:
                bad_values.append(number)

    print(sum(bad_values))


if __name__ == '__main__':
    main()
