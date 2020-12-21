#!/usr/bin/env python3
#
# Task:
# As you look over the list of messages, you realize your matching rules
# aren't quite right. To fix them, completely replace rules 8 and 11
# with the following:
# 8: 42 | 42 8
# 11: 42 31 | 42 11 31
# This small change has a big impact: now, the rules do contain loops,
# and the list of messages they could hypothetically match is infinite.
# You'll need to determine how these changes affect which messages are valid.
# Fortunately, many of the rules are unaffected by this change; it might help
# to start by looking at which rules always match the same set of values
# and how those rules (especially rules 42 and 31) are used by the new versions
# of rules 8 and 11. (Remember, you only need to handle the rules you have;
# building a solution that could handle any hypothetical combination of rules
# would be significantly more difficult [Wiki -> Formal grammar].)
# After updating rules 8 and 11, how many messages completely match rule 0?
#
# Solution:
#

INPUT_FILE = 'input.txt'


def match(message, rules_set, rule):
    success = False

    if '|' in rule:
        for multi_rule in rule.split(' | '):
            success, message1 = match(message, rules_set, multi_rule)
            if success:
                return True, message1
        return False, message

    elif ' ' in rule:
        for i, subrule in enumerate(rule.split()):
            success, message = match(message, rules_set, subrule)
            if success and not message and i != len(rule.split()) - 1:
                return False, message
            if not success:
                return False, message
        if success:
            return True, message
        else:
            return False, message

    else:
        if rule.isnumeric():
            rule = rules_set[rule]
            return match(message, rules_set, rule)
        else:
            if message and message.startswith(rule):
                return True, message[len(rule):]
            return False, message



def main():
    data = open(INPUT_FILE, 'r').read().split('\n\n')
    messages = [line for line in data[1].strip('\n').split('\n')]
    rules = dict([line.split(': ')
                  for line in data[0].strip('\n').split('\n')])
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'

    matched = 0
    for message in messages:
        success, remaining = match(message, rules, '0')
        if success and not remaining:
            matched += 1

    print(matched)


if __name__ == '__main__':
    main()
