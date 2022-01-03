#!/usr/bin/env python3
#
# --- Day 4: Giant Squid ---
#
# You're already almost 1.5km (almost a mile) below the surface of the ocean,
# already so deep that you can't see any sunlight. What you can see, however,
# is a giant squid that has attached itself to the outside of your submarine.
#
# Maybe it wants to play bingo?
#
# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
# Numbers are chosen at random, and the chosen number is marked on all boards
# on which it appears. (Numbers may not appear on all boards.) If all numbers
# in any row or any column of a board are marked, that board wins.
# (Diagonals don't count.)
#
# The submarine has a bingo subsystem to help passengers (currently, you and
# the giant squid) pass the time. It automatically generates a random order
# in which to draw numbers and a random set of boards (your puzzle input).
# For example:
#   7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1
#
#   22 13 17 11  0
#    8  2 23  4 24
#   21  9 14 16  7
#    6 10  3 18  5
#    1 12 20 15 19
#
#    3 15  0  2 22
#    9 18 13 17  5
#   19  8  7 25 23
#   20 11 10 24  4
#   14 21 16 12  6
#
#   14 21 17 24  4
#   10 16 15  9 19
#   18  8 23 26 20
#   22 11 13  6  5
#    2  0 12  3  7
#
# After the first five numbers are drawn (7, 4, 9, 5, and 11), there are
# no winners, but the boards are marked as follows (shown here adjacent
# to each other to save space):
#   22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
#   21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
#
# After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are
# still no winners:
#   22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
#   21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
#
# Finally, 24 is drawn:
#   22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
#    8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
#   21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
#    6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
#    1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
#
# At this point, the third board wins because it has at least one complete
# row or column of marked numbers (in this case, the entire top row is marked:
# 14 21 17 24 4).
#
# The score of the winning board can now be calculated. Start by finding
# the sum of all unmarked numbers on that board; in this case, the sum is 188.
# Then, multiply that sum by the number that was just called when the board
# won, 24, to get the final score, 188 * 24 = 4512.
#
# To guarantee victory against the giant squid, figure out which board will
# win first. What will your final score be if you choose that board?
#
#
# --- Solution ---
#
# We split the input file by double newlines (\n\n). Then the first element
# is a list of numbers to check and the remaining elements are definitions
# of our bingo boards. The defintions we split by newlines and allocate
# in mermory just like matrices (list of rows).
# Then we iterate over list of our numbers to check.
# For each number, we take every board and analyze every its element (for each
# row and for each element in that row...). If element matches the called
# number, we replace that element in board with value of -1
#

INPUT_FILE = 'input.txt'


def main():
    with open(INPUT_FILE, 'r') as file:
        puzzle_input = file.read().split('\n\n')

    numbers_drown = puzzle_input[0]
    boards_definitions = puzzle_input[1:]

    numbers = [int(number) for number in numbers_drown.strip().split(',')]
    boards = []

    for board_definition in boards_definitions:
        new_board = []

        for line in board_definition.strip().split('\n'):
            board_row = [int(number) for number in line.split()]
            new_board.append(board_row)

        boards.append(new_board)

    solved = False
    sum_of_unmarked_numbers = 0
    called_number = 0

    for called_number in numbers:
        for board_index, board in enumerate(boards):
            for row_index, row in enumerate(board):
                for number_index, number in enumerate(row):
                    if number == called_number:
                        boards[board_index][row_index][number_index] = -1

                        board = boards[board_index]
                        column = [row[number_index] for row in board]
                        row = board[row_index][:]

                        if row.count(-1) == len(row) \
                           or column.count(-1) == len(column):
                            sum_of_unmarked_numbers = sum([
                                number
                                for row in board
                                for number in row
                                if number >= 0
                            ])
                            solved = True
                            break

                if solved:
                    break

            if solved:
                break

        if solved:
            break

    score = called_number * sum_of_unmarked_numbers
    print(score)


if __name__ == '__main__':
    main()
