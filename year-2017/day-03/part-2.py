#!/usr/bin/env python3
#
# --- Day 3: Spiral Memory / Part Two ---
#
# As a stress test on the system, the programs here clear the grid
# and then store the value 1 in square 1. Then, in the same allocation
# order as shown above, they store the sum of the values in all adjacent
# squares, including diagonals.
#
# So, the first few squares' values are chosen as follows:
# – Square 1 starts with the value 1.
# – Square 2 has only one adjacent filled square (with value 1),
#   so it also stores 1.
# – Square 3 has both of the above squares as neighbors
#   and stores the sum of their values, 2.
# – Square 4 has all three of the aforementioned squares as neighbors
#   and stores the sum of their values, 4.
# – Square 5 only has the first and fourth squares as neighbors,
#   so it gets the value 5.
#
# Once a square is written, its value does not change.
# Therefore, the first few squares would receive the following values:
#
#   147  142  133  122   59
#   304    5    4    2   57
#   330   10    1    1   54
#   351   11   23   25   26
#   362  747  806--->   ...
#
# What is the first value written that is larger than your puzzle input?
#
#
# --- Solution ---
#
# The difference here is that after each step we need to calculate the value
# for a given position, defined as sum of all neighbor position values
# (assuming there are such values, otherwise it is zero). The stop condition
# is also different here – we want the calculated values to exceed the given
# input number. Once we find first such number, we return it as an answer.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        data = int(file.read().strip())

    move = [
        complex(1, 0),  # right
        complex(0, -1),  # up
        complex(-1, 0),  # left
        complex(0, 1),  # down
    ]
    position = complex(0, 0)

    distance_to_turn = 1
    steps_in_direction = 0
    times_turned = 0

    values = {position: 1}
    while values[position] < data:
        position += move[0]
        steps_in_direction += 1

        x = int(position.real)
        y = int(position.imag)
        values[position] = sum([
            values[complex(nx, ny)]
            for nx in (x - 1, x, x + 1)
            for ny in (y - 1, y, y + 1)
            if complex(nx, ny) in values
        ])

        if steps_in_direction == distance_to_turn:  # turn
            move.append(move.pop(0))
            steps_in_direction = 0
            times_turned += 1

            if times_turned == 2:  # increase distance_to_turn to turn
                distance_to_turn += 1
                times_turned = 0

    print(values[position])


if __name__ == '__main__':
    main()
