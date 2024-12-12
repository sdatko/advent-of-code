#!/usr/bin/env python3
#
# --- Day 12: Garden Groups / Part Two ---
#
# Fortunately, the Elves are trying to order so much fence
# that they qualify for a bulk discount!
#
# Under the bulk discount, instead of using the perimeter to calculate
# the price, you need to use the number of sides each region has. Each
# straight section of fence counts as a side, regardless of how long it is.
#
# Consider this example again:
#
#   AAAA
#   BBCD
#   BBCC
#   EEEC
#
# The region containing type A plants has 4 sides, as does each of the regions
# containing plants of type B, D, and E. However, the more complex region
# containing the plants of type C has 8 sides!
#
# Using the new method of calculating the per-region price by multiplying
# the region's area by its number of sides, regions A through E have prices
# 16, 16, 32, 4, and 12, respectively, for a total price of 80.
#
# The second example above (full of type X and O plants) would have a total
# price of 436.
#
# Here's a map that includes an E-shaped region full of type E plants:
#
#   EEEEE
#   EXXXX
#   EEEEE
#   EXXXX
#   EEEEE
#
# The E-shaped region has an area of 17 and 12 sides for a price of 204.
# Including the two regions full of type X plants, this map has a total
# price of 236.
#
# This map has a total price of 368:
#
#   AAAAAA
#   AAABBA
#   AAABBA
#   ABBAAA
#   ABBAAA
#   AAAAAA
#
# It includes two regions full of type B plants (each with 4 sides) and
# a single region full of type A plants (with 4 sides on the outside and
# 8 more sides on the inside, a total of 12 sides). Be especially careful
# when counting the fence around regions like the one full of type A plants;
# in particular, each section of fence has an in-side and an out-side,
# so the fence does not connect across the middle of the region (where
# the two B regions touch diagonally). (The Elves would have used the Möbius
# Fencing Company instead, but their contract terms were too one-sided.)
#
# The larger example from before now has the following updated prices:
# – A region of R plants with price 12 * 10 = 120.
# – A region of I plants with price 4 * 4 = 16.
# – A region of C plants with price 14 * 22 = 308.
# – A region of F plants with price 10 * 12 = 120.
# – A region of V plants with price 13 * 10 = 130.
# – A region of J plants with price 11 * 12 = 132.
# – A region of C plants with price 1 * 4 = 4.
# – A region of E plants with price 13 * 8 = 104.
# – A region of I plants with price 14 * 16 = 224.
# – A region of M plants with price 5 * 6 = 30.
# – A region of S plants with price 3 * 6 = 18.
#
# Adding these together produces its new total price of 1206.
#
# What is the new total price of fencing all regions on your map?
#
#
# --- Solution ---
#
# The difference in this part is that instead of a total perimeter length
# we need to find just the number of edges. While it may seem complicated,
# it is actually simple under the task conditions – it turns out that
# a region has the same number of edges as the number of it's corners.
# So, it comes down to just counting the corners – there are just 8 possible
# arrangments in the defined task:
#
#   +---------------------> X
#   |
#   |    o   o    AAAAAAA        x   x
#   |   o1---2o   A5---6A       x1   2x   5A   A6     # A – part of region
#   |    |AAA|    A|o o|A                 Ax   xA     # x – not part of region
#   |    |AAA|    A|   |A  -->
#   |    |AAA|    A|o o|A                 Ax   xA     # 1, 2, 3, 4, 5, 6, 7, 8,
#   |   o4---3o   A8---7A       x4   3x   8A   A7     # – also part of region
#   |    o   o    AAAAAAA        x   x
#   |
#   |    outter     inner        outter     inner
#   V Y
#

INPUT_FILE = 'input.txt'

VOID = '.'


def main():
    with open(INPUT_FILE, 'r') as file:
        grid = file.read().strip().split()

    prices = []

    # surround with dots to avoid boundaries check
    grid = [[VOID] * len(grid[0])] + grid + [[VOID] * len(grid[0])]
    grid = [[VOID] + list(row) + [VOID] for row in grid]

    # process the grid in a loop
    while True:
        region = None

        # find first unprocessed region
        for y, row in enumerate(grid):
            for x, field in enumerate(row):
                if field != VOID:
                    region = field
                    break
            if region:
                break

        if not region:
            break  # nothing else to process

        to_check = [(x, y)]
        coords = set()

        # find all connected neighbor fields
        while to_check:
            x, y = to_check.pop()

            if (x, y) in coords:
                continue  # we have been here already

            coords.add((x, y))

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx = x + dx
                ny = y + dy

                if grid[ny][nx] == region:
                    if (nx, ny) not in coords:
                        to_check.append((nx, ny))

        # calculate the area and the number of edges
        area = 0
        edges = 0

        for (x, y) in coords:
            area += 1

            # Outter edges
            # * case 1 – top-left
            if all([grid[y][x - 1] != region,
                    grid[y - 1][x] != region]):
                edges += 1
            # * case 2 – top-right
            if all([grid[y][x + 1] != region,
                    grid[y - 1][x] != region]):
                edges += 1
            # * case 3 – bottom-right
            if all([grid[y][x + 1] != region,
                    grid[y + 1][x] != region]):
                edges += 1
            # * case 4 – bottom-left
            if all([grid[y][x - 1] != region,
                    grid[y + 1][x] != region]):
                edges += 1

            # Inner edges
            # * case 5 – top-left
            if all([grid[y + 1][x + 1] != region,
                    (x, y + 1) in coords,
                    (x + 1, y) in coords]):
                edges += 1
            # * case 6 – top-right
            if all([grid[y + 1][x - 1] != region,
                    (x, y + 1) in coords,
                    (x - 1, y) in coords]):
                edges += 1
            # * case 7 – bottom-right
            if all([grid[y - 1][x - 1] != region,
                    (x, y - 1) in coords,
                    (x - 1, y) in coords]):
                edges += 1
            # * case 8 – bottom-left
            if all([grid[y - 1][x + 1] != region,
                    (x, y - 1) in coords,
                    (x + 1, y) in coords]):
                edges += 1

        price = area * edges
        prices.append(price)

        # clean the area from grid
        for (x, y) in coords:
            grid[y][x] = VOID

    print(sum(prices))


if __name__ == '__main__':
    main()
