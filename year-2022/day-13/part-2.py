#!/usr/bin/env python3
#
# --- Day 13: Distress Signal / Part Two ---
#
# Now, you just need to put all of the packets in the right order.
# Disregard the blank lines in your list of received packets.
#
# The distress signal protocol also requires that you include
# two additional divider packets:
#
#   [[2]]
#   [[6]]
#
# Using the same rules as before, organize all packets - the ones
# in your list of received packets as well as the two divider packets
# - into the correct order.
#
# For the example above, the result of putting the packets
# in the correct order is:
#
#   []
#   [[]]
#   [[[]]]
#   [1,1,3,1,1]
#   [1,1,5,1,1]
#   [[1],[2,3,4]]
#   [1,[2,[3,[4,[5,6,0]]]],8,9]
#   [1,[2,[3,[4,[5,6,7]]]],8,9]
#   [[1],4]
#   [[2]]
#   [3]
#   [[4,4],4,4]
#   [[4,4],4,4,4]
#   [[6]]
#   [7,7,7]
#   [7,7,7,7]
#   [[8,7,6]]
#   [9]
#
# Afterward, locate the divider packets. To find the decoder key for this
# distress signal, you need to determine the indices of the two divider
# packets and multiply them together. (The first packet is at index 1,
# the second packet is at index 2, and so on.) In this example, the divider
# packets are 10th and 14th, and so the decoder key is 140.
#
# Organize all of the packets into the correct order.
# What is the decoder key for the distress signal?
#
#
# --- Solution ---
#
# The difference here is that we need to modify the input, so it is no longer
# a list of pairs, but a list of individual packets to compare. Then we simply
# use the previously defined function to perform a sorting of that list.
# For that, I introduce additional function, that translates the previous
# output (True, False, None) to the convention expected by Python's sorted()
# function (1, -1, 0). Then, to satisfy my personal challenge (no imports),
# I reuse the definition of cmp_to_key() from CPython interpreter source code
# and pass it to the standard sorted() function.
# After that, all we need is to find the new indices of two additionally
# inserted items (remembering AoC loves indexing that starts with 1...)
# and return the multiplication of those.
#

INPUT_FILE = 'input.txt'

DIVIDER_1 = [[2]]
DIVIDER_2 = [[6]]


def is_in_right_order(left, right) -> bool | None:
    if type(left) == int and type(right) == int:
        if left < right:
            return True
        elif left > right:
            return False
        else:  # equal == undecided
            return None

    else:
        if type(left) == int:
            left = [left]
        if type(right) == int:
            right = [right]

        # Prevent modifications of original lists in the loop
        left = left[:]
        right = right[:]

        while True:
            if len(left) == 0 and len(right) == 0:
                return None  # both run out of elements == undecided

            if len(left) > 0:
                element1 = left.pop(0)
            else:
                return True

            if len(right) > 0:
                element2 = right.pop(0)
            else:
                return False

            result = is_in_right_order(element1, element2)
            if result is None:
                continue
            elif result is True:
                return True
            else:
                return False


def compare_packets(left, right) -> int:
    result = is_in_right_order(left, right)

    if result is None:
        return 0
    elif result is True:
        return 1
    else:
        return -1


#
# Taken from: https://github.com/python/cpython/blob/3.11/Lib/functools.py#L206
#
# Alternative: from functools import cmp_to_key
#
# No import challenge is no import challenge... ¯\_(ツ)_/¯
#
def cmp_to_key(mycmp):
    """Convert a cmp= function into a key= function"""
    class K(object):
        __slots__ = ['obj']

        def __init__(self, obj):
            self.obj = obj

        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0

        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0

        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0

        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0

        __hash__ = None

    return K


def safe_eval(call):
    globals_dict = {"__builtins__": None}
    locals_dict = {}
    return eval(call, globals_dict, locals_dict)


def main():
    with open(INPUT_FILE, 'r') as file:
        packets = [safe_eval(packet)
                   for packet in file.read()
                                     .replace('\n\n', '\n')
                                     .strip()
                                     .split('\n')]

        packets.append(DIVIDER_1)
        packets.append(DIVIDER_2)

    packets = sorted(packets, key=cmp_to_key(compare_packets), reverse=True)

    index1 = packets.index(DIVIDER_1) + 1
    index2 = packets.index(DIVIDER_2) + 1

    print(index1 * index2)


if __name__ == '__main__':
    main()
