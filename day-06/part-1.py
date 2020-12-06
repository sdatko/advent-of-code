#!/usr/bin/env python3
#
# Task:
# The form asks a series of 26 yes-or-no questions marked a through z.
# All you need to do is identify the questions for which anyone in group
# answers "yes". Groups are separated by empty lines and one persons answers
# are written in single line as questions marks that contained "yes".
# For each group, count the number of questions to which
# anyone answered "yes". What is the sum of those counts?
#
# Solution:
# We join the whole input file as one long string and then split by double
# newlines to have list of groups. The list of groups can be split by
# newlines to get peoples answers. Individual answers we then get by passing
# the inputs to produce sets. Then all what remains is to sum the sets,
# meaning to calculate a union in terms of set. Finally we sum the lengths
# of each union.
#

INPUT_FILE = 'input.txt'


def main():
    groups = ''.join(open(INPUT_FILE, 'r').readlines()).split('\n\n')

    counts = []

    for group in groups:
        people = group.split()
        individual_answers = [set(answers) for answers in people]
        group_answers = set.union(*individual_answers)
        counts.append(len(group_answers))

    print(sum(counts))


if __name__ == '__main__':
    main()
