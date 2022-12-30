#!/usr/bin/env python3
#
# --- Day 2: I Was Told There Would Be No Math ---
#
# The elves are running low on wrapping paper, and so they need to submit
# an order for more. They have a list of the dimensions (length l, width w,
# and height h) of each present, and only want to order exactly as much
# as they need.
#
# Fortunately, every present is a box (a perfect right rectangular prism),
# which makes calculating the required wrapping paper for each gift a little
# easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l.
# The elves also need a little extra paper for each present:
# the area of the smallest side.
#
# For example:
# – A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52
#   square feet of wrapping paper plus 6 square feet of slack,
#   for a total of 58 square feet.
# – A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42
#   square feet of wrapping paper plus 1 square foot of slack,
#   for a total of 43 square feet.
#
# All numbers in the elves' list are in feet. How many total square feet
# of wrapping paper should they order?
#
#
# --- Solution ---
#
# We start by reading the input into a list of boxes dimensions (3 integers),
# by splitting the file over newlines and then each line over the `x` character
# with mapping the results to integers. Then for each box we calculate areas
# of each unique rectangular cuboid's faces (there are 3 of such) and we add
# the cuboid area and area of the smallest side to the total sum. Finally
# we just return the total sum of calculated areas.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        boxes = [list(map(int, box.split('x')))
                 for box in file.read().strip().split('\n')]
    area = 0

    for box in boxes:
        side1 = box[0] * box[1]
        side2 = box[1] * box[2]
        side3 = box[0] * box[2]

        area += 2 * side1 + 2 * side2 + 2 * side3 + min(side1, side2, side3)

    print(area)


if __name__ == '__main__':
    main()
