#!/usr/bin/env python3
#
# Task:
# How many bag colors can eventually contain at least one shiny gold bag?
#
# Solution:
# First, we process the input file – discarding all useless data.
# Then we produce a set of bags that we will consider as our solution
# (bags colors that can contain the wanted bag) and a set of bags
# we want to look for in the input data – to find the parent bag
# that can contain it. Then in a loop, when we find the parent,
# we add the parent to the set of bags we want to look for.
# Eventually we will go over the whole tree of bags.
#

INPUT_FILE = 'input.txt'

WANTED = 'shiny gold'


def main():
    entries = (open(INPUT_FILE, 'r').read()
                                    .replace('bags', 'bag')
                                    .replace(' bag', '')
                                    .replace('.', '')
                                    .replace('1 ', '')
                                    .replace('2 ', '')
                                    .replace('3 ', '')
                                    .replace('4 ', '')
                                    .replace('5 ', '')
                                    .replace('6 ', '')
                                    .replace('7 ', '')
                                    .replace('8 ', '')
                                    .replace('9 ', '')
                                    .split('\n'))

    possible_bags = set()
    wanted_bags = set([WANTED])

    while wanted_bags:
        bag = wanted_bags.pop()

        for entry in entries:
            if not entry:
                break

            tmp = entry.split(' contain ')
            parent = tmp[0]
            childs = tmp[1].split(', ')

            if bag in childs:
                possible_bags.add(parent)
                wanted_bags.add(parent)

    print(len(possible_bags))


if __name__ == '__main__':
    main()
