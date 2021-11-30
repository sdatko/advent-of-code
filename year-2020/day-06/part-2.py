#!/usr/bin/env python3
#
# Task:
# The form asks a series of 26 yes-or-no questions marked a through z.
# All you need to do is identify the questions for which anyone in group
# answers "yes". Groups are separated by empty lines and one persons answers
# are written in single line as questions marks that contained "yes".
# For each group, count the number of questions to which
# everyone answered "yes". What is the sum of those counts?
#
# Solution:
# The only difference here is that we do intersection in groups to find
# the same answers for everyone in group. Thank you Python :-)
#

INPUT_FILE = 'input.txt'


def main():
    groups = ''.join(open(INPUT_FILE, 'r').readlines()).split('\n\n')

    counts = []

    for group in groups:
        people = group.split()
        individual_answers = [set(answers) for answers in people]
        group_answers = set.intersection(*individual_answers)
        counts.append(len(group_answers))

    print(sum(counts))


if __name__ == '__main__':
    main()
