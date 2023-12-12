#!/usr/bin/env python3
#
# --- Day 12: Hot Springs / Part Two ---
#
# As you look out at the field of springs, you feel like there are way more
# springs than the condition records list. When you examine the records,
# you discover that they were actually folded up this whole time!
#
# To unfold the records, on each row, replace the list of spring conditions
# with five copies of itself (separated by ?) and replace the list
# of contiguous groups of damaged springs with five copies of itself
# (separated by ,).
#
# So, this row:
#
#   .# 1
#
# Would become:
#
#   .#?.#?.#?.#?.# 1,1,1,1,1
#
# The first line of the above example would become:
#
#   ???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3
#
# In the above example, after unfolding, the number of possible arrangements
# for some rows is now much larger:
# – ???.### 1,1,3 - 1 arrangement
# – .??..??...?##. 1,1,3 - 16384 arrangements
# – ?#?#?#?#?#?#?#? 1,3,1,6 - 1 arrangement
# – ????.#...#... 4,1,1 - 16 arrangements
# – ????.######..#####. 1,6,5 - 2500 arrangements
# – ?###???????? 3,2,1 - 506250 arrangements
#
# After unfolding, adding all of the possible arrangement counts
# together produces 525152.
#
# Unfold your condition records; what is the new sum of possible
# arrangement counts?
#
#
# --- Solution ---
#
# The difference here is that each input record is ~5 times longer. While for
# the example input the code from previous part worked fast enough, my actual
# real input had some cases that made it inefficient. Surprisingly, when used
# a memoization (lru_cache), it produces the right answer in a very short time,
# which means there must be a lot of similar cases repeatedly occurring during
# calculations. Hence, I implemented my own cache decorator (for satisfying
# the no-import challenge) and I left the original code mostly unchanged.
# There are two additional checks that, after added, reduce the calculations
# by about a half: first, we can pretty much ignore all leading operational
# springs in a pattern (........#?# eventually leads directly to #?# anyway);
# second, we can fail early whenever we reach the situation where the number
# of remaining springs is lower than the sum of number of springs expected
# according to remaining groups (including at least one gap between them).
#

INPUT_FILE = 'input.txt'

OPERATIONAL = '.'
DAMAGED = '#'
UNKNOWN = '?'

CACHE = {}


def cached(function_to_call):
    def cached_decorator(*args, **kwargs):
        if args in CACHE:
            return CACHE[args]

        outcome = function_to_call(*args)

        CACHE[args] = outcome
        return outcome

    return cached_decorator


@cached
def solutions(springs, groups):
    # the operational springs do not really matter, we can omit them
    springs = springs.lstrip(OPERATIONAL)

    # fail early if there are not enough springs left
    if len(springs) < (sum(groups) + len(groups) - 1):
        return 0

    # out of springs to verify, but we still expect groups -> invalid solution
    if not springs and groups:
        return 0

    # no groups left – all remaining springs must be not damaged
    if not groups:
        # no more springs left -> valid solution
        if not springs:
            return 1

        # all remaining springs are not damaged -> valid solution
        elif all(spring != DAMAGED for spring in springs):
            return 1

        else:  # there was at least one damaged spring left -> invalid solution
            return 0

    # for damaged spring, we need to verify it matches the expected group
    if springs[0] == DAMAGED:
        length = groups[0]

        # not enough springs remain –> invalid solution
        if len(springs) < length:
            return 0

        # all next expected springs must be damaged (or unknown)
        if all(springs[i] != OPERATIONAL for i in range(length)):

            # check whether there is anything after the current group...
            if len(springs) > length:

                # if so, there cannot be a damaged spring just after group
                if springs[length] != DAMAGED:
                    return solutions(springs[length + 1:], groups[1:])

                else:  # otherwise –> invalid solution
                    return 0

            else:  # just consume group and move forward
                return solutions(springs[length:], groups[1:])

        else:  # the current group is not possible to fit there
            return 0

    # for unknown, we branch for two cases
    elif springs[0] == UNKNOWN:
        return (solutions(OPERATIONAL + springs[1:], groups)
                + solutions(DAMAGED + springs[1:], groups))

    # default case – for operational spring, we just move forward
    else:
        return solutions(springs[1:], groups)


def main():
    with open(INPUT_FILE, 'r') as file:
        records = [line.split()
                   for line in file.read().strip().split('\n')]
        records = [('?'.join([pattern] * 5),
                    tuple(map(int, groups.split(',') * 5)))
                   for (pattern, groups) in records]

    arrangements = []

    for springs, groups in records:
        number_of_arrangements = solutions(springs, groups)
        arrangements.append(number_of_arrangements)

    print(sum(arrangements))


if __name__ == '__main__':
    main()
