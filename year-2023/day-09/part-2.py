#!/usr/bin/env python3
#
# --- Day 9: Mirage Maintenance / Part Two ---
#
# Of course, it would be nice to have even more history included in your
# report. Surely it's safe to just extrapolate backwards as well, right?
#
# For each history, repeat the process of finding differences until
# the sequence of differences is entirely zero. Then, rather than adding
# a zero to the end and filling in the next values of each previous sequence,
# you should instead add a zero to the beginning of your sequence of zeroes,
# then fill in new first values for each previous sequence.
#
# In particular, here is what the third example history looks like
# when extrapolating back in time:
#
#   5  10  13  16  21  30  45
#     5   3   3   5   9  15
#      -2   0   2   4   6
#         2   2   2   2
#           0   0   0
#
# Adding the new values on the left side of each sequence from bottom
# to top eventually reveals the new left-most history value: 5.
#
# Doing this for the remaining example data above results in previous
# values of -3 for the first history and 0 for the second history.
# Adding all three new values together produces 2.
#
# Analyze your OASIS report again, this time extrapolating the previous
# value for each history. What is the sum of these extrapolated values?
#
#
# --- Solution ---
#
# The only difference here is that instead of predicting the next value,
# we need to find the previous value for a sequence. The whole approach here
# is basically the same, except when finally processing all sub-sequences
# in reverse order, we take the first sub-sequence element and subtract
# the currently found previous value.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        sequences = tuple(tuple(map(int, line.split()))
                          for line in file.read().strip().split('\n'))

    values = []

    for sequence in sequences:
        subsequences = [sequence]
        previous_value = 0

        for _ in range(len(sequence) - 1):  # all possible levels
            subsequence = subsequences[-1]
            differences = tuple(b - a for (a, b) in zip(subsequence[:-1],
                                                        subsequence[1:]))

            if all(difference == 0 for difference in differences):
                break
            else:
                subsequences.append(differences)

        while subsequences:
            subsequence = subsequences.pop()
            previous_value = (subsequence[0] - previous_value)

        values.append(previous_value)

    print(sum(values))


if __name__ == '__main__':
    main()
