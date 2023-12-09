#!/usr/bin/env python3
#
# --- Day 5: Doesn't He Have Intern-Elves For This? ---
#
# Santa needs help figuring out which strings in his text file
# are naughty or nice.
#
# A nice string is one with all of the following properties:
# – It contains at least three vowels (aeiou only), like aei,
#   xazegov, or aeiouaeiouaeiou.
# – It contains at least one letter that appears twice in a row,
#   like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# – It does not contain the strings ab, cd, pq, or xy, even
#   if they are part of one of the other requirements.
#
# For example:
# – ugknbfddgicrmopn is nice because it has at least three vowels
#   (u...i...o...), a double letter (...dd...),
#   and none of the disallowed substrings.
# – aaa is nice because it has at least three vowels and a double letter,
#   even though the letters used by different rules overlap.
# – jchzalrnumimnmhp is naughty because it has no double letter.
# – haegwjzuvuyypxyu is naughty because it contains the string xy.
# – dvszwmarrgswjxmb is naughty because it contains only one vowel.
#
# How many strings are nice?
#
#
# --- Solution ---
#
# We start by reading the input file into a list of words by splitting over
# the newlines. Then, we iterate through the words, for each word checking
# whether it is nice by verifying that all three given conditions are true.
# Finally, we return the number of words satisfying all three conditions.
#

INPUT_FILE = 'input.txt'

VOWELS = set('aeiou')
DISALLOWED = ('ab', 'cd', 'pq', 'xy')


def main():
    with open(INPUT_FILE, 'r') as file:
        words = file.read().strip().split('\n')

    count = 0

    for word in words:
        condition1 = (sum(letter in VOWELS for letter in word) >= 3)
        condition2 = any(letter1 == letter2
                         for letter1, letter2 in zip(word[:-1], word[1:]))
        condition3 = not any(letter1 + letter2 in DISALLOWED
                             for letter1, letter2 in zip(word[:-1], word[1:]))

        if all([condition1, condition2, condition3]):
            count += 1

    print(count)


if __name__ == '__main__':
    main()
