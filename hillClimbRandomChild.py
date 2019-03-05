import eight_queens_game as game
from random import shuffle
import copy


def hill_climbing(board):
    hill_game = game
    board = hill_game.random_board(board)
    while (hill_game.threat_count(board) != 0):
        moves = hill_game.moves_to_childs(board)
        shuffle(moves)
        for move in moves:
            child = copy.deepcopy(board)

            for j in range(0, 8):  # to clear a row
                child[move[0]][j] = 0
            child[move[0]][move[1]] = 1  # to set one child

            if hill_game.threat_count(child) < hill_game.threat_count(board):
                print('a child born with threat count:', hill_game.threat_count(child))
                board = copy.deepcopy(child)
                break   #to move uphill when a move is good
            if move==moves[-1]:     #to set a random board when there are no more better moves
                board = hill_game.random_board(board)
    for i in board:
        print(i)


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    hill_climbing(board)
