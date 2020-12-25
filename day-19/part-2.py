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
        results = []
        lengths = []
        remainings = []

        for subrule in rule.split(' | '):
            success, remaining = inner_match(message, rules_set, subrule)
            results.append(success)
            lengths.append(len(remaining))
            remainings.append(remaining)

        if any(results):
            remaining = min(
                filter(
                    lambda element: element[0] is True,
                    zip(results, lengths, remainings)
                ),
                key=lambda element: element[1]
            )[2]
            return True, remaining
        else:
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
    rules['8'] = '42 | 42 8'
    rules['11'] = '42 31 | 42 11 31'

    matched = 0
    for message in messages:
        success, remaining = match(message, rules, '0')
        if success:
            matched += 1

    print(matched)


if __name__ == '__main__':
    main()
