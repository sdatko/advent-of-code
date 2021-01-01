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


def inner_match(messages, rules_set, rule):
    if not messages:
        return False, messages

    if rule.startswith('"') and rule.endswith('"') and " " not in rule:
        text = rule[1:-1]
        remainings = []

        for message in messages:
            if message.startswith(text):
                remainings.append(message[len(text):])

        if remainings:
            return True, remainings
        else:
            return False, messages

    elif rule.isnumeric():
        rule = rules_set[rule]
        return inner_match(messages, rules_set, rule)

    elif ' | ' in rule:
        remainings = []

        for subrule in rule.split(' | '):
            success, remaining = inner_match(messages, rules_set, subrule)
            if success:
                remainings.extend(remaining if isinstance(remaining, list)
                                  else [remaining])

        if remainings:
            return True, remainings
        else:
            return False, messages

    elif ' ' in rule:
        remainings = messages
        for subrule in rule.split():
            success, remainings = inner_match(remainings, rules_set, subrule)
            if not success:
                break
        return success, remainings


def match(message, rules_set, rule):
    success, remainings = inner_match([message], rules_set, rule)

    if success and not all(remainings):
        return True, ""
    else:
        return False, remainings


def test(message, rules, rule):
    success, remaining = match(message, rules, rule)
    print('Message:   ', message)
    print('Rule:      ', rule)
    print('Remaining: ', remaining)
    print('Status:    ', success)
    print()
    return success, remaining


def main():
    data = """0: 4 1 | 4 1
1: 5
4: "a"
5: "b"

""".split('\n\n')
    rules = dict([line.split(': ')
                  for line in data[0].strip('\n').split('\n')])
    rules['1'] = '5 | 5 1'

    assert test('a', rules, '4') == (True, '')
    assert test('b', rules, '4') == (False, ['b'])
    assert test('a', rules, '5') == (False, ['a'])
    assert test('b', rules, '5') == (True, '')

    assert test('aa', rules, '4') == (False, ['a'])
    assert test('bb', rules, '4') == (False, ['bb'])

    assert test('a', rules, '1') == (False, ['a'])
    assert test('b', rules, '1') == (True, '')
    assert test('bb', rules, '1') == (True, '')
    assert test('bbb', rules, '1') == (True, '')
    assert test('b', rules, '1 1') == (False, [''])

    assert test('ab', rules, '4 5') == (True, '')
    assert test('abb', rules, '4 5 5') == (True, '')
    assert test('aab', rules, '4 5 5') == (False, ['ab'])

    assert test('ab', rules, '4 1') == (True, '')
    assert test('abb', rules, '4 1') == (True, '')
    assert test('abb', rules, '4 1 1') == (True, '')
    assert test('abbb', rules, '4 1 1') == (True, '')
    assert test('aab', rules, '4 1 1') == (False, ['ab'])

    assert test('ba', rules, '4 5') == (False, ['ba'])
    assert test('ba', rules, '5 4') == (True, '')
    assert test('ba', rules, '4 5 | 5 4') == (True, '')
    assert test('ba', rules, '4 1') == (False, ['ba'])
    assert test('ba', rules, '1 4') == (True, '')
    assert test('ba', rules, '4 1 | 1 4') == (True, '')

    assert test('abbb', rules, '4 5') == (False, ['bb'])
    assert test('ab', rules, '4 1') == (True, '')
    assert test('abb', rules, '4 1') == (True, '')
    assert test('abbb', rules, '4 1') == (True, '')


if __name__ == '__main__':
    main()
