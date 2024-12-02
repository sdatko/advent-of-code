#!/usr/bin/env python3
#
# --- Day 2: Red-Nosed Reports / Part Two ---
#
# The engineers are surprised by the low number of safe reports until they
# realize they forgot to tell you about the Problem Dampener.
#
# The Problem Dampener is a reactor-mounted module that lets the reactor
# safety systems tolerate a single bad level in what would otherwise be
# a safe report. It's like the bad level never happened!
#
# Now, the same rules apply as before, except if removing a single level from
# an unsafe report would make it safe, the report instead counts as safe.
#
# More of the above example's reports are now safe:
# – 7 6 4 2 1: Safe without removing any level.
# – 1 2 7 8 9: Unsafe regardless of which level is removed.
# – 9 7 6 2 1: Unsafe regardless of which level is removed.
# – 1 3 2 4 5: Safe by removing the second level, 3.
# – 8 6 4 4 1: Safe by removing the third level, 4.
# – 1 3 6 7 9: Safe without removing any level.
#
# Thanks to the Problem Dampener, 4 reports are actually safe!
#
# Update your analysis by handling situations where the Problem Dampener can
# remove a single level from unsafe reports. How many reports are now safe?
#
#
# --- Solution ---
#
# In this case we extend the verification with additional verification
# – if the report is invalid, we process every possible subreport that can be
# made by removing a single elemenent from the original report. The condition
# to check for every subreport is then exactly the same as for the full report.
# Once we found that any subreport is safe, we do not need to check further
# subreports of given original report, so we break from the processing loop.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        reports = [list(map(int, line.strip().split()))
                   for line in file.read().strip().split('\n')]

    safe = 0

    for report in reports:
        differences = tuple(report[i + 1] - report[i]
                            for i in range(len(report) - 1))

        if any([
            all(0 > difference >= -3 for difference in differences),
            all(0 < difference <= 3 for difference in differences),
           ]):
            safe += 1

        else:
            for index in range(len(report) + 1):
                subreport = report[:index] + report[(index + 1):]

                differences = tuple(subreport[i + 1] - subreport[i]
                                    for i in range(len(subreport) - 1))

                if any([
                    all(0 > difference >= -3 for difference in differences),
                    all(0 < difference <= 3 for difference in differences),
                   ]):
                    safe += 1
                    break

    print(safe)


if __name__ == '__main__':
    main()
