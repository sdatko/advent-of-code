#!/usr/bin/env python3
#
# --- Day 5: If You Give A Seed A Fertilizer / Part Two ---
#
# Everyone will starve if you only plant such a small number of seeds.
# Re-reading the almanac, it looks like the seeds: line actually describes
# ranges of seed numbers.
#
# The values on the initial seeds: line come in pairs. Within each pair,
# the first value is the start of the range and the second value is the length
# of the range. So, in the first line of the example above:
#
# seeds: 79 14 55 13
#
# This line describes two ranges of seed numbers to be planted in the garden.
# The first range starts with seed number 79 and contains 14 values:
# 79, 80, ..., 91, 92. The second range starts with seed number 55
# and contains 13 values: 55, 56, ..., 66, 67.
#
# Now, rather than considering four seed numbers, you need to consider
# a total of 27 seed numbers.
#
# In the above example, the lowest location number can be obtained from
# seed number 82, which corresponds to soil 84, fertilizer 84, water 84,
# light 77, temperature 45, humidity 46, and location 46. So, the lowest
# location number is 46.
#
# Consider all of the initial seed numbers listed in the ranges on the first
# line of the almanac. What is the lowest location number that corresponds
# to any of the initial seed numbers?
#
#
# --- Solution ---
#
# The difference here is that instead of a dozen of values, we need to examine
# huge seeds ranges now (order of billions of integers). Hence, the original
# approach would be not effective enough – instead, a more effective algorithm
# that considers the ranges (pairs [start, end] instead of individual numbers)
# was prepared. The main function is similar as in previous part, though
# each transformation if performed first for all input ranges (i.e. `for` loop
# became the outer loop and we process all ranges before next transformation).
# The decode() function required a major modification, though the idea remains
# the same, now the first argument is a tuple (given range [start, end])
# instead of an integer. Because all the transformations are simple linear
# shifts of values in ranges, all we need to do is to analyse the relation
# between the given inputs range and the mappings ranges. There are a few
# possible situations:
# – the whole range falls within the mapping,
# – the range overlaps with beginning or ending of the mapping,
# – the whole range contains the whole mapping,
# – the range does not fall into any mapping (and so remains unchanged).
# For example, in the illustration below (# denotes mapping, [-] is the range),
# the original range would be split into unchanged one ([start, source - 1])
# and the one that would be translated to destination ([source, end]).
#
#              start     source      end        source + length
#                [----------##########]#################             (values)
#   ------------------------------------------------------------------------->
#                ___________:::::::::::
#                (unchanged)  (moved)
#
# In the end, we will obtain all possible ranges values for the location
# parameter – as an answer, we return the lowest number we can find there.
# Note I used the series of additional tests to verify the decode() function
# in various scenarios.
#

INPUT_FILE = 'input.txt'


def tests():
    # range is inside mapping
    actual = decode((50, 70), [(10, 40, 40)])
    expected = [(20, 40)]
    assert sorted(actual) == expected

    # range overlaps with mapping's left boundary
    actual = decode((50, 70), [(10, 40, 25)])
    expected = [(20, 34), (65, 70)]
    assert sorted(actual) == expected

    # range overlaps with mapping's right boundary
    actual = decode((50, 70), [(10, 65, 25)])
    expected = [(10, 15), (50, 64)]
    assert sorted(actual) == expected

    # range overlaps with mapping's both left and right boundaries
    actual = decode((50, 70), [(10, 55, 5)])
    expected = [(10, 14), (50, 54), (60, 70)]
    assert sorted(actual) == expected

    # range did not fall into defined mapping (range is left of mapping)
    actual = decode((50, 70), [(10, 71, 20)])
    expected = [(50, 70)]
    assert sorted(actual) == expected

    # range did not fall into defined mapping (range is right of mapping)
    actual = decode((50, 70), [(10, 30, 20)])
    expected = [(50, 70)]
    assert sorted(actual) == expected

    # range fully covers the mapping
    actual = decode([50, 70], [(10, 50, 21)])
    expected = [(10, 30)]
    assert sorted(actual) == expected

    # range overlaps only with the mapping's left boundary
    actual = decode([50, 70], [(10, 70, 20)])
    expected = [(10, 10), (50, 69)]
    assert sorted(actual) == expected

    # range overlaps only with the mapping's right boundary
    actual = decode([50, 70], [(10, 40, 11)])
    expected = [(20, 20), (51, 70)]
    assert sorted(actual) == expected

    # range of length 1 inside mapping
    actual = decode([50, 50], [(10, 50, 1)])
    expected = [(10, 10)]
    assert sorted(actual) == expected

    # multiple mappings
    actual = decode([50, 70], [(10, 55, 5), (90, 60, 5)])
    expected = [(10, 14), (50, 54), (65, 70), (90, 94)]
    assert sorted(actual) == expected


def decode(given_range, mappings):
    remainings = [given_range]
    new_ranges = []

    while remainings:
        current_range = remainings.pop()
        start, end = current_range

        for destination, source, length in mappings:
            # current range is inside mapping
            if source <= start <= end < (source + length):
                new_start = destination + (start - source)
                new_end = destination + (end - source)
                new_range = (new_start, new_end)

                # no remaining
                new_ranges.append(new_range)
                break

            # current range overlaps with mapping's left boundary
            elif start <= source <= end < (source + length):
                new_start = destination
                new_end = destination + (end - source)
                new_range = (new_start, new_end)

                remaining = (start, source - 1)

                remainings.append(remaining)
                new_ranges.append(new_range)
                break

            # current range overlaps with mapping's right boundary
            elif source <= start < (source + length) <= end:
                new_start = destination + (start - source)
                new_end = destination + (length - 1)
                new_range = (new_start, new_end)

                remaining = (source + length, end)

                remainings.append(remaining)
                new_ranges.append(new_range)
                break

            # current range overlaps with mapping's both boundaries
            elif start <= source < (source + length) < end:
                new_start = destination
                new_end = destination + (length - 1)
                new_range = (new_start, new_end)

                remaining1 = (start, source - 1)
                remaining2 = (source + length, end)

                remainings.append(remaining1)
                remainings.append(remaining2)
                new_ranges.append(new_range)
                break

        else:  # range did not fall into any defined mappings – pass it through
            new_ranges.append(current_range)

    return new_ranges


def main():
    with open(INPUT_FILE, 'r') as file:
        seeds = tuple(map(int, file.readline().replace('seeds: ', '').split()))
        maps = dict([mapping.replace(' map', '').split(':\n')
                     for mapping in file.read().strip().split('\n\n')])

        for key in maps:
            maps[key] = tuple([tuple(map(int, ranges.split()))
                               for ranges in maps[key].split('\n')])

    ranges = [(start, start + length - 1)
              for start, length in zip(seeds[::2], seeds[1::2])]

    for mapping in maps:
        outcomes = []

        while ranges:
            current_range = ranges.pop()
            new_ranges = decode(current_range, maps[mapping])
            outcomes.extend(new_ranges)

        ranges = outcomes

    closest_location = min(ranges)[0]

    print(closest_location)


if __name__ == '__main__':
    tests()
    main()
