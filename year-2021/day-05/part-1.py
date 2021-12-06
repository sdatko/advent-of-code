#!/usr/bin/env python3
#
# Task:
# You come across a field of hydrothermal vents on the ocean floor!
# These vents constantly produce large, opaque clouds, so it would be
# best to avoid them if possible.
# They tend to form in lines; the submarine helpfully produces a list
# of nearby lines of vents (your puzzle input) for you to review.
# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
# where x1,y1 are the coordinates of one end the line segment and x2,y2 are
# the coordinates of the other end. These line segments include the points
# at both ends. In other words:
# - An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
# - An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
# For now, only consider horizontal and vertical lines:
# - lines where either x1 = x2 or y1 = y2.
# To avoid the most dangerous areas, you need to determine the number
# of points where at least two lines overlap.
# Consider only horizontal and vertical lines.
# At how many points do at least two lines overlap?
#
# Solution:
# We start with processing the input file – each entry there (line in file)
# contains definition of geometric line we want to consider. We replace
# the arrow with surrounding spaces ( -> ) in definitions to comma character,
# to split easier each entry and obtain 4 values (2 coordinates) for each line.
# In this part we filter and consider only horizontal and vertical lines.
# We build a list of dictionaries to store the data, so we can easier referrer
# in code to the desired value in coordinate system. We also introduce helper
# lists to find boundaries in our data – minimum and maximum range for X and Y.
# Then we allocate a variable in which we will be drawing – area – with size
# of the found boundaries. Next we go over each defined line and mark where
# exactly it goes in our area – by calculating the direction steps (dx, dy)
# and moving in a loop from the beginning (x1,y1) to the target (x2,y2).
# Note that the drawing uses minimum value of X and Y to shift the indexing
# in the area variable – so we can optimize a little its size (e.g. when all
# data are in range from 60 to 90 we will only allocate 31 indexes).
# Finally we browse the array and count how many times there was something
# drawn at least 2 times.
#

INPUT_FILE = 'input.txt'


def sign(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        return 0


def main():
    definitions = [line.strip() for line in open(INPUT_FILE, 'r')]

    lines = []
    x_values = []
    y_values = []
    for definition in definitions:
        x1, y1, x2, y2 = map(int, definition.replace(' -> ', ',').split(','))
        if x1 == x2 or y1 == y2:
            lines.append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})
            x_values.extend([x1, x2])
            y_values.extend([y1, y2])

    min_x = min(x_values)
    max_x = max(x_values)
    min_y = min(y_values)
    max_y = max(y_values)
    area = [[0] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for line in lines:
        dx = sign(line['x2'] - line['x1'])
        dy = sign(line['y2'] - line['y1'])

        while line['x1'] != line['x2'] or line['y1'] != line['y2']:
            area_x = line['x1'] - min_x
            area_y = line['y1'] - min_y

            area[area_y][area_x] += 1

            line['x1'] += dx
            line['y1'] += dy

        area_x = line['x1'] - min_x
        area_y = line['y1'] - min_y

        area[area_y][area_x] += 1

    common_points = len([number
                         for row in area
                         for number in row
                         if number >= 2])

    print(common_points)


if __name__ == '__main__':
    main()
