#!/usr/bin/env python3
#
# --- Day 21: Monkey Math ---
#
# The monkeys are back! You're worried they're going to try to steal your stuff
# again, but it seems like they're just holding their ground and making various
# monkey noises at you.
#
# Eventually, one of the elephants realizes you don't speak monkey and comes
# over to interpret. As it turns out, they overheard you talking about trying
# to find the grove; they can show you a shortcut if you answer their riddle.
#
# Each monkey is given a job: either to yell a specific number or to yell
# the result of a math operation. All of the number-yelling monkeys know their
# number from the start; however, the math operation monkeys need to wait
# for two other monkeys to yell a number, and those two other monkeys might
# also be waiting on other monkeys.
#
# Your job is to work out the number the monkey named root will yell before
# the monkeys figure it out themselves.
#
# For example:
#
#   root: pppw + sjmn
#   dbpl: 5
#   cczh: sllz + lgvd
#   zczc: 2
#   ptdq: humn - dvpt
#   dvpt: 3
#   lfqf: 4
#   humn: 5
#   ljgn: 2
#   sjmn: drzm * dbpl
#   sllz: 4
#   pppw: cczh / lfqf
#   lgvd: ljgn * ptdq
#   drzm: hmdt - zczc
#   hmdt: 32
#
# Each line contains the name of a monkey, a colon,
# and then the job of that monkey:
# – A lone number means the monkey's job is simply to yell that number.
# – A job like aaaa + bbbb means the monkey waits for monkeys aaaa and bbbb
#   to yell each of their numbers; the monkey then yells the sum of those
#   two numbers.
# – aaaa - bbbb means the monkey yells aaaa's number minus bbbb's number.
# – Job aaaa * bbbb will yell aaaa's number multiplied by bbbb's number.
# – Job aaaa / bbbb will yell aaaa's number divided by bbbb's number.
#
# So, in the above example, monkey drzm has to wait for monkeys hmdt and zczc
# to yell their numbers. Fortunately, both hmdt and zczc have jobs that involve
# simply yelling a single number, so they do this immediately: 32 and 2.
# Monkey drzm can then yell its number by finding 32 minus 2: 30.
#
# Then, monkey sjmn has one of its numbers (30, from monkey drzm), and already
# has its other number, 5, from dbpl. This allows it to yell its own number
# by finding 30 multiplied by 5: 150.
#
# This process continues until root yells a number: 152.
#
# However, your actual situation involves considerably more monkeys.
# What number will the monkey named root yell?
#
#
# --- Solution ---
#
# We start by reading the input as dictionary of monkeys definitions, splitting
# the file over newlines and then each line over spaces, taking the first item
# as a key (after stripping the colon character) and the rest as a value.
# Then we run loop where we are looking for solutions. We take all monkeys
# and inspect their values – if that is a single numeric element, we remove
# it from the definitions and add to the solved values; if there are multiple
# elements (actually just three), this is an expression and we check if each
# item referenced in that expression is already known to us – if so, we compute
# it and store the result in the solved values; otherwise we continue to check
# the next monkey. This repeats as long as we did not solve our defined target.
# As an answer, we just return the calculated value for target monkey.
#

INPUT_FILE = 'input.txt'

TARGET = 'root'


def main():
    with open(INPUT_FILE, 'r') as file:
        monkeys = {line.split()[0].replace(':', ''): line.split()[1:]
                   for line in file.read().strip().split('\n')}

    solved = {}

    while TARGET not in solved:
        for key in monkeys.copy():
            value = monkeys[key]

            if len(value) == 1 and value[0].isnumeric():
                solved[key] = int(value[0])
                del monkeys[key]

            elif len(value) == 3:
                lvalue, operator, rvalue = value[0:3]

                if lvalue not in solved or rvalue not in solved:
                    continue

                if operator == '+':
                    result = solved[lvalue] + solved[rvalue]
                elif operator == '-':
                    result = solved[lvalue] - solved[rvalue]
                elif operator == '*':
                    result = solved[lvalue] * solved[rvalue]
                elif operator == '/':
                    result = solved[lvalue] / solved[rvalue]
                else:
                    print('Panic!')
                    exit(1)

                solved[key] = result
                del monkeys[key]

            else:
                print('Something is not yes')
                exit(1)

    print(int(solved[TARGET]))


if __name__ == '__main__':
    main()
