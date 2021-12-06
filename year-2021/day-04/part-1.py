#!/usr/bin/env python3
#
# Task:
# You're already almost 1.5km (almost a mile) below the surface of the ocean,
# already so deep that you can't see any sunlight. What you can see, however,
# is a giant squid that has attached itself to the outside of your submarine.
# Maybe it wants to play bingo?
# Bingo is played on a set of boards each consisting of a 5x5 grid of numbers.
# Numbers are chosen at random, and the chosen number is marked on all boards
# on which it appears. (Numbers may not appear on all boards.) If all numbers
# in any row or any column of a board are marked, that board wins.
# (Diagonals don't count.)
# The submarine has a bingo subsystem to help passengers (currently, you and
# the giant squid) pass the time. It automatically generates a random order
# in which to draw numbers and a random set of boards (your puzzle input).
# The score of the winning board can be calculated as follows:
# - start by finding the sum of all unmarked numbers on that board;
# - then, multiply that sum by the number that was just called when
#   the board won, to get the final score.
# To guarantee victory against the giant squid, figure out which board will
# win first. What will your final score be if you choose that board?
#
# Solution:
# We split the input file by double newlines (\n\n). Then the first element
# is a list of numbers to check and the remaining elements are definitions
# of our bingo boards. The defintions we split by newlines and allocate
# in mermory just like matrices (list of rows).
# Then we iterate over list of our numbers to check.
# For each number, we take every board and analyze every its element (for each
# row and for each element in that row...). If element matches the called
# number, we replace that element in board with value of -1

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
