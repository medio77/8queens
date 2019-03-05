import eight_queens_game as game
from random import shuffle
import copy
import matplotlib.pyplot as plt


# Artificial Intelligence/A Modern Approach/Third Edition/Stuart J. Russell and Peter Norvig

def hill_climbing(board):  # heuristic is on moving the queen who's making more threats
    hill_game = game
    # accountings:
    local_optimum_counter = 0
    up_steps_counter = 0
    # -------------
    board = hill_game.random_board(board)
    while (hill_game.threat_count(board)[0] != 0):
        moves = hill_game.moves_to_childs(board)
        worst_queen=hill_game.threat_count(board)[1]
        shuffle(moves)
        for i in range(len(moves)):
            if moves[i][0]==worst_queen:
                temp_move=moves[0]
                moves[0]=moves[i]
                moves[i]=temp_move

        for move in moves:

            # the successors of a state are all possible states
            # generated by moving a single queen to another square in the same row
            # each row has 8*8=64 successors
            child = copy.deepcopy(board)

            for j in range(0, 8):  # to clear a row
                child[move[0]][j] = 0
            child[move[0]][move[1]] = 1  # to set one child

            if hill_game.threat_count(child)[0] < hill_game.threat_count(board)[0]:
                up_steps_counter = up_steps_counter + 1
                # print('a child born with threat count:', hill_game.threat_count(child))
                board = copy.deepcopy(child)
                break  # to move uphill when a move is good

            if move == moves[-1]:  # to set a random board when there are no more better moves
                local_optimum_counter = local_optimum_counter + 1
                board = hill_game.random_board(board)
    # for i in board:
    #     print(i)
    return local_optimum_counter, up_steps_counter


if __name__ == '__main__':
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    local_optimom_mass = 0
    up_steps_mass = 0
    how_many_times = 100
    local_optimum_list = []
    for i in range(how_many_times):
        local_optimum_counter, up_steps_counter = hill_climbing(board)
        print(i, "th board was solved!")
        local_optimum_list.append(local_optimum_counter)
        local_optimom_mass = local_optimom_mass + local_optimum_counter
        up_steps_mass = up_steps_mass + up_steps_counter

    print("average touched local optimums: ", local_optimom_mass / how_many_times)
    plt.plot(local_optimum_list, color='c', alpha=0.6)
    plt.axhline(local_optimom_mass / how_many_times, linestyle='dashed')
    plt.axis()
    plt.show()
