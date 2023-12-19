#!/usr/bin/env python3
#
# --- Day 7: Handy Haversacks / Part Two ---
#
# It's getting pretty expensive to fly these days - not because of ticket
# prices, but because of the ridiculous number of bags you need to buy!
#
# Consider again your shiny gold bag and the rules from the above example:
#
# – faded blue bags contain 0 other bags.
# – dotted black bags contain 0 other bags.
# – vibrant plum bags contain 11 other bags: 5 faded blue bags
#   and 6 dotted black bags.
# – dark olive bags contain 7 other bags: 3 faded blue bags
#   and 4 dotted black bags.
#
# So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags
# within it) plus 2 vibrant plum bags (and the 11 bags within each of those):
# 1 + 1*7 + 2 + 2*11 = 32 bags!
#
# Of course, the actual rules have a small chance of going several
# levels deeper than this example; be sure to count all of the bags,
# even if the nesting becomes topologically impractical!
#
# Here's another example:
#
# – shiny gold bags contain 2 dark red bags.
# – dark red bags contain 2 dark orange bags.
# – dark orange bags contain 2 dark yellow bags.
# – dark yellow bags contain 2 dark green bags.
# – dark green bags contain 2 dark blue bags.
# – dark blue bags contain 2 dark violet bags.
# – dark violet bags contain no other bags.
#
# In this example, a single shiny gold bag must contain 126 other bags.
#
# How many individual bags are required inside your single shiny gold bag?
#
#
# --- Solution ---
#
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
