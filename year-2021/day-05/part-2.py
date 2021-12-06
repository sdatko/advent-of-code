#!/usr/bin/env python3
#
# Task:
# Unfortunately, considering only horizontal and vertical lines doesn't give
# you the full picture; you need to also consider diagonal lines.
# Because of the limits of the hydrothermal vent mapping system, the lines
# in your list will only ever be horizontal, vertical, or a diagonal line
# at exactly 45 degrees. In other words:
# - An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
# - An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
# Consider all of the lines. At how many points do at least two lines overlap?
#
# Solution:
# The code prepared for previous part worked basically immediately here.
# The only difference is we removed the filter for vertical and horizontal
# lines (such ones that have x1 == x2 or y1 == y2).
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
