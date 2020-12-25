#!/usr/bin/env python3
#
# Task:
# They sent you a list of the rules valid messages should obey and a list
# of received messages they've collected so far (your puzzle input).
# The rules for valid messages (the top part of your puzzle input) are
# numbered and build upon each other. For example:
# 0: 1 2
# 1: "a"
# 2: 1 3 | 3 1
# 3: "b"
# Some rules, like 3: "b", simply match a single character (in this case, b).
# The remaining rules list the sub-rules that must be followed; for example,
# the rule 0: 1 2 means that to match rule 0, the text being checked must
# match rule 1, and the text after the part that matched rule 1 must then
# match rule 2.
# Some of the rules have multiple lists of sub-rules separated by a pipe (|).
# This means that at least one list of sub-rules must match. (The ones that
# match might be different each time the rule is encountered.) For example,
# the rule 2: 1 3 | 3 1 means that to match rule 2, the text being checked
# must match rule 1 followed by rule 3 or it must match rule 3 followed by
# rule 1.
# Fortunately, there are no loops in the rules, so the list of possible
# matches will be finite. Since rule 1 matches a and rule 3 matches b,
# rule 2 matches either ab or ba. Therefore, rule 0 matches aab or aba.
# The whole message must match all of rule 0; there can't be extra unmatched
# characters in the message.
# How many messages completely match rule 0?
#
# Solution:
#

INPUT_FILE = 'input.txt'


def inner_match(message, rules_set, rule):
    if not message:
        return False, message

    if rule.startswith('"') and rule.endswith('"') and " " not in rule:
        text = rule[1:-1]
        if message.startswith(text):
            return True, message[len(text):]
        else:
            return False, message

    elif rule.isnumeric():
        rule = rules_set[rule]
        return inner_match(message, rules_set, rule)

    elif ' | ' in rule:
        for subrule in rule.split(' | '):
            success, remaining = inner_match(message, rules_set, subrule)
            if success:
                return True, remaining
        return False, message

    elif ' ' in rule:
        for subrule in rule.split():
            success, message = inner_match(message, rules_set, subrule)
            if not success:
                break
        return success, message


def match(message, rules_set, rule):
    success, remaining = inner_match(message, rules_set, rule)

    if success and not remaining:
        return True, remaining
    else:
        return False, remaining


def main():
    data = open(INPUT_FILE, 'r').read().split('\n\n')
    messages = [line for line in data[1].strip('\n').split('\n')]
    rules = dict([line.split(': ')
                  for line in data[0].strip('\n').split('\n')])

    matched = 0
    for message in messages:
        success, remaining = match(message, rules, '0')
        if success:
            matched += 1

    print(matched)


if __name__ == '__main__':
    main()
