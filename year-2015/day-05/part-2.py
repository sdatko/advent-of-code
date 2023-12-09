#!/usr/bin/env python3
#
# --- Day 5: Doesn't He Have Intern-Elves For This? / Part Two ---
#
# Realizing the error of his ways, Santa has switched to a better model
# of determining whether a string is naughty or nice. None of the old rules
# apply, as they are all clearly ridiculous.
#
# Now, a nice string is one with all of the following properties:
# – It contains a pair of any two letters that appears at least twice
#   in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa),
#   but not like aaa (aa, but it overlaps).
# – It contains at least one letter which repeats with exactly one letter
#   between them, like xyx, abcdefeghi (efe), or even aaa.
#
# For example:
# – qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj)
#   and a letter that repeats with exactly one letter between them (zxz).
# – xxyxx is nice because it has a pair that appears twice and a letter
#   that repeats with one between, even though the letters used by each
#   rule overlap.
# – uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat
#   with a single letter between them.
# – ieodomkazucvgmuy is naughty because it has a repeating letter with
#   one between (odo), but no pair that appears twice.
#
# How many strings are nice under these new rules?
#
#
# --- Solution ---
#
# The only difference here is that we use a different conditions for counting
# the word as nice. For checking the pairs, we find the indexes of first and
# last occurrences of a pair in a word and make sure that the distance between
# the indexes is great enough so there is no overlapping.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        words = file.read().strip().split('\n')

    count = 0

    for word in words:
        condition1 = any(word.index(''.join(pair)) + 1
                         < word.rindex(''.join(pair))
                         for pair in zip(word[:-1], word[1:]))
        condition2 = any(letter1 == letter2
                         for letter1, letter2 in zip(word[:-2], word[2:]))

        if all([condition1, condition2]):
            count += 1

    print(count)


if __name__ == '__main__':
    main()
