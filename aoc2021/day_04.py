import os

import numpy as np


def task_1(number_order, boards):
    drawn_numbers = set()
    bingo = False
    for number in number_order:
        drawn_numbers.add(number)
        for board in boards:
            for i in range(5):
                if not set(board[i]) - set(drawn_numbers):
                    bingo = True
                    break
            if not bingo:
                for i in range(5):
                    if not set(board[:, i]) - set(drawn_numbers):
                        bingo = True
                        break
            if bingo:
                board_numbers = set(board.ravel())
                total_undrawn = sum(board_numbers - drawn_numbers)
                return total_undrawn * number


def task_2(number_order, boards):
    drawn_numbers = set()
    bingo = False
    bingo_board_indexes = []  # list of board indexes
    for number in number_order:
        drawn_numbers.add(number)
        for b_i, board in enumerate(boards):
            if b_i in bingo_board_indexes:
                continue
            for i in range(5):
                if not set(board[i]) - set(drawn_numbers):
                    bingo = True
                    break
            for i in range(5):
                if not set(board[:, i]) - set(drawn_numbers):
                    bingo = True
                    break
            if bingo:
                bingo_board_indexes.append(b_i)
                bingo = False
        if len(boards) == len(bingo_board_indexes):
            final_board_index = bingo_board_indexes[-1]
            final_board = boards[final_board_index]
            board_numbers = set(final_board.ravel())
            total_undrawn = sum(board_numbers - drawn_numbers)
            return total_undrawn * number



def main():
    # load_data
    boards = []
    number_order = []
    current_board = None
    line_no = 1
    for line in open(os.getcwd() + '/data/day_04.txt'):
        line = line.replace('\n', '').strip()
        if line_no == 1:
            number_order = [int(x) for x in line.split(',') if x]
        elif line_no % 6 == 2:  # blank line
            if current_board is not None:
                boards.append(current_board)
            current_board = np.zeros((5, 5), dtype=int)
        else:
            index = (line_no - 3) % 6
            current_board[index] = np.array([int(x) for x in line.split(' ') if x])
        line_no += 1
    boards.append(current_board)

    # run tasks
    print(task_1(number_order, boards))
    print(task_2(number_order, boards))


if __name__ == '__main__':
    main()
