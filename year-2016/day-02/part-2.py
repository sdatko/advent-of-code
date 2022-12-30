#!/usr/bin/env python3
#
# --- Day 2: Bathroom Security / Part Two ---
#
# You finally arrive at the bathroom (it's a several minute walk from the lobby
# so visitors can behold the many fancy conference rooms and water coolers
# on this floor) and go to punch in the code. Much to your bladder's dismay,
# the keypad is not at all like you imagined it. Instead, you are confronted
# with the result of hundreds of man-hours of bathroom-keypad-design meetings:
#
#       1
#     2 3 4
#   5 6 7 8 9
#     A B C
#       D
#
# You still start at "5" and stop when you're at an edge, but given the same
# instructions as above, the outcome is very different:
# – You start at "5" and don't move at all (up and left are both edges),
#   ending at 5.
# – Continuing from "5", you move right twice and down three times
#   (through "6", "7", "B", "D", "D"), ending at D.
# – Then, from "D", you move five more times (through "D", "B", "C", "C", "B"),
#   ending at B.
# – Finally, after five more moves, you end at 3.
#
# So, given the actual keypad layout, the code would be 5DB3.
#
# Using the same instructions in your puzzle input,
# what is the correct bathroom code?
#
#
# --- Solution ---
#
# The only difference here is the layout of the keypad. Thanks to the approach
# of representing it as map of valid positions in 2D space, the already created
# algorithm works well here after just adjusting the map to a new shape.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        instructions = file.read().strip().split('\n')

    code = ''

    keypad = {
        complex(3, 1): '1',

        complex(2, 2): '2',
        complex(3, 2): '3',
        complex(4, 2): '4',

        complex(1, 3): '5',
        complex(2, 3): '6',
        complex(3, 3): '7',
        complex(4, 3): '8',
        complex(5, 3): '9',

        complex(2, 4): 'A',
        complex(3, 4): 'B',
        complex(4, 4): 'C',

        complex(3, 5): 'D',
    }

    changes = {
        'U': complex(0, -1),
        'D': complex(0, +1),
        'L': complex(-1, 0),
        'R': complex(+1, 0),
    }

    position = complex(1, 3)  # we start on "5"

    for moves in instructions:
        for move in moves:
            candidate = position + changes[move]

            if candidate in keypad:
                position = candidate

        code += keypad[position]

    print(code)


if __name__ == '__main__':
    main()
