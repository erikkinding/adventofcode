# -*- coding: utf-8 -*-
import time


class SwapBoard:
    def __init__(self):
        self.width = 3
        self.height = 3
        self.board = self.get_board()

        # set blank
        self.board[1][1] = '_'

        # set target
        self.target = (0, 0)

        # set red piece
        self.board[0][2] = 'o'

    def run(self):


        board = list(self.board)
        self.print_board(board)

        moves = self.get_moves(board)


    def possible_next(self, board):



        pass

    def print_board(self, board, current_position):
        for r in range(self.height):

            for c in board[r]:
                pass
            print(''.join(board[r]))

    def get_board(self):
        board = []
        for r in range(self.height):
            row = []

            for c in range(self.width):
                row.append('#')

            board.append(row)

        return board
