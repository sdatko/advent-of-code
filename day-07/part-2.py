#!/usr/bin/env python3
#
# Task:
# How many bag colors can eventually contain at least one shiny gold bag?
#
# Solution:
# Here we just reverse the look through the tree – we have a list of bags
# we want to find and counts its children, then in loop we go through the
# input and count the children of wanted bag, adding also these children
# as the next bags to go though in list.
#

INPUT_FILE = 'input.txt'

WANTED = 'shiny gold'


def main():
    entries = (open(INPUT_FILE, 'r').read()
                                    .replace('bags', 'bag')
                                    .replace(' bag', '')
                                    .replace('.', '')
                                    .split('\n'))

    number_of_bags = 0

    wanted_bags = [WANTED]

    while wanted_bags:
        bag = wanted_bags.pop()

        for entry in entries:
            if not entry:
                break

            tmp = entry.split(' contain ')
            parent = tmp[0]
            childs = tmp[1].split(', ')

            if parent == bag:
                for child in childs:
                    if child == 'no other':
                        break

                    number = int(child.split(' ', maxsplit=1)[0])
                    color = child.split(' ', maxsplit=1)[1]

                    number_of_bags += number
                    wanted_bags.extend([color] * number)

    print(number_of_bags)


if __name__ == '__main__':
    main()
