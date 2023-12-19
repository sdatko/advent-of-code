#!/usr/bin/env python3
#
# --- Day 6: Custom Customs / Part Two ---
#
# As you finish the last group's customs declaration, you notice
# that you misread one word in the instructions:
#
# You don't need to identify the questions to which anyone answered "yes";
# you need to identify the questions to which everyone answered "yes"!
#
# Using the same example as above:
#
#   abc
#
#   a
#   b
#   c
#
#   ab
#   ac
#
#   a
#   a
#   a
#   a
#
#   b
#
# This list represents answers from five groups:
#
# – In the first group, everyone (all 1 person) answered "yes"
#   to 3 questions: a, b, and c.
# – In the second group, there is no question to which everyone
#   answered "yes".
# – In the third group, everyone answered yes to only 1 question, a.
#   Since some people did not answer "yes" to b or c, they don't count.
# – In the fourth group, everyone answered yes to only 1 question, a.
# – In the fifth group, everyone (all 1 person) answered "yes"
#   to 1 question, b.
#
# In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.
#
# For each group, count the number of questions to which
# everyone answered "yes". What is the sum of those counts?
#
#
# --- Solution ---
#
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
