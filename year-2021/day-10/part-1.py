#!/usr/bin/env python3
#
# Task:
# You ask the submarine to determine the best route out of the deep-sea cave,
# but it only replies:
#   Syntax error in navigation subsystem on line: all of them
# All of them?! The damage is worse than you thought. You bring up a copy
# of the navigation subsystem (your puzzle input).
# The navigation subsystem syntax is made of several lines containing chunks.
# There are one or more chunks on each line, and chunks contain zero or more
# other chunks. Adjacent chunks are not separated by any delimiter; if one
# chunk stops, the next chunk (if any) can immediately start. Every chunk must
# open and close with one of four legal pairs of matching characters:
# - If a chunk opens with (, it must close with ).
# - If a chunk opens with [, it must close with ].
# - If a chunk opens with {, it must close with }.
# - If a chunk opens with <, it must close with >.
# So, () is a legal chunk that contains no other chunks, as is [].
# More complex but valid chunks include ([]), {()()()}, <([{}])>,
# [<>({}){}[([])<>]], and even (((((((((()))))))))).
# Some lines are incomplete, but others are corrupted. Find and discard
# the corrupted lines first.
# A corrupted line is one where a chunk closes with the wrong character
# - that is, where the characters it opens and closes with do not form
# one of the four legal pairs listed above.
# Examples of corrupted chunks include (], {()()()>, (((()))},
# and <([]){()}[{}]). Such a chunk can appear anywhere within a line,
# and its presence causes the whole line to be considered corrupted.
# Stop at the first incorrect closing character on each corrupted line.
# Did you know that syntax checkers actually have contests to see who can
# get the high score for syntax errors in a file? It's true! To calculate
# the syntax error score for a line, take the first illegal character
# on the line and look it up in the following table:
# - ): 3 points.
# - ]: 57 points.
# - }: 1197 points.
# - >: 25137 points.
# Find the first illegal character in each corrupted line of the navigation
# subsystem. What is the total syntax error score for those errors?
#
# Solution:
# We read the input file as list of lines to analyze. Additionally, few helper
# variables are defined – to find easily the matching parenthesis character
# and corresponding points. Then we go through each line, processing every line
# character by character. There should be 3 possibilities:
# - the character is an opening bracket: we add matching complementary
#   character on the top of the list of expected characters and move
#   to the next loop iteration,
# - the current character matches first expected: it means we found proper
#   closing bracket, we remove it from the list of expectations and then
#   we proceed further in the loop,
# - the current character does not match expected element: it means there is
#   a syntax error in the given line, so we add the score for unexpected
#   character and break the further processing of that line.
# For the final result, we just print the calculated sum of scores.
#

INPUT_FILE = 'input.txt'


def main():
    lines = [line.strip() for line in open(INPUT_FILE, 'r')]

    matching = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    score = 0

    for line in lines:
        expected = []

        for character in line:
            if character in ['(', '[', '{', '<']:
                expected.insert(0, matching[character])
                continue

            elif character != expected[0]:
                score += points[character]
                break

            elif character == expected[0]:
                expected.pop(0)
                continue

            else:
                print('Something unpredicted!\n', line, '\n', character)

    print(score)


if __name__ == '__main__':
    main()
