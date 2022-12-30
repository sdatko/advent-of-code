#!/usr/bin/env python3
#
# --- Day 2: Bathroom Security ---
#
# You arrive at Easter Bunny Headquarters under cover of darkness. However,
# you left in such a rush that you forgot to use the bathroom! Fancy office
# buildings like this one usually have keypad locks on their bathrooms,
# so you search the front desk for the code.
#
# "In order to improve security," the document you find says,
# "bathroom codes will no longer be written down. Instead, please
# memorize and follow the procedure below to access the bathrooms."
#
# The document goes on to explain that each button to be pressed can be
# found by starting on the previous button and moving to adjacent buttons
# on the keypad: U moves up, D moves down, L moves left, and R moves right.
# Each line of instructions corresponds to one button, starting at the previous
# button (or, for the first line, the "5" button); press whatever button you're
# on at the end of each line. If a move doesn't lead to a button, ignore it.
#
# You can't hold it much longer, so you decide to figure out the code
# as you walk to the bathroom. You picture a keypad like this:
#
#   1 2 3
#   4 5 6
#   7 8 9
#
# Suppose your instructions are:
#
#   ULL
#   RRDDD
#   LURDL
#   UUUUD
#
# – You start at "5" and move up (to "2"), left (to "1"), and left
#   (you can't, and stay on "1"), so the first button is 1.
# – Starting from the previous button ("1"), you move right twice (to "3")
#   and then down three times (stopping at "9" after two moves and ignoring
#   the third), ending up with 9.
# – Continuing from "9", you move left, up, right, down, and left,
#   ending with 8.
# – Finally, you move up four times (stopping at "2"), then down once,
#   ending with 5.
#
# So, in this example, the bathroom code is 1985.
#
# Your puzzle input is the instructions from the document you found
# at the front desk. What is the bathroom code?
#
#
# --- Solution ---
#
# We start by reading the input as the list of strings, by splitting the file
# over newlines. Then we define helper structures: for keypad and movements
# mapping to changes in 2D space (the complex type is convenient here, as it
# gives us out of the box the basic 2D arithmetics). Then for each instruction,
# we go move by move, calculating the next candidate position in 2D space
# and if it leads to a valid position in keypad space, we proceed; after all
# moves in given instruction, we save the value at current keypad position.
# Finally we just print the saved vales – our code.
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        instructions = file.read().strip().split('\n')

    code = ''

    keypad = {
        complex(1, 1): '1',
        complex(2, 1): '2',
        complex(3, 1): '3',

        complex(1, 2): '4',
        complex(2, 2): '5',
        complex(3, 2): '6',

        complex(1, 3): '7',
        complex(2, 3): '8',
        complex(3, 3): '9',
    }

    changes = {
        'U': complex(0, -1),
        'D': complex(0, +1),
        'L': complex(-1, 0),
        'R': complex(+1, 0),
    }

    position = complex(2, 2)  # we start on "5"

    for moves in instructions:
        for move in moves:
            candidate = position + changes[move]

            if candidate in keypad:
                position = candidate

        code += keypad[position]

    print(code)


if __name__ == '__main__':
    main()
