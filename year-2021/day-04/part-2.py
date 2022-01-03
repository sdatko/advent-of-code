#!/usr/bin/env python3
#
# --- Day 4: Giant Squid / Part Two ---
#
# On the other hand, it might be wise to try a different strategy:
# let the giant squid win.
#
# You aren't sure how many bingo boards a giant squid could play at once,
# so rather than waste time counting its arms, the safe thing to do is
# to figure out which board will win last and choose that one. That way,
# no matter which boards it picks, it will win for sure.
#
# In the above example, the second board is the last to win, which happens
# after 13 is eventually called and its middle column is completely marked.
# If you were to keep playing until this point, the second board would have
# a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.
#
# Figure out which board will win last.
# Once it wins, what would its final score be?
#
#
# --- Solution ---
#
# The only difference in this part is the stop condition. Instead of breaking
# everything after finding first winning board, we save index of that board
# to remove it from further iterations (to check for next called number).
# Note we need to finish iterating over the list of boards first and delete
# them in proper order to not miss anything. We finish when there are no more
# elements in the boards list.
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

    sum_of_unmarked_numbers = 0
    called_number = 0

    for called_number in numbers:
        to_delete = []
        for board_index, board in enumerate(boards):
            solved = False
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
                            to_delete.append(board_index)
                            break

                if solved:
                    break

        for board_index in sorted(to_delete, reverse=True):
            boards.pop(board_index)

        if len(boards) == 0:
            break

    score = called_number * sum_of_unmarked_numbers
    print(score)


if __name__ == '__main__':
    main()
