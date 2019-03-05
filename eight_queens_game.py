import random


def random_board(board_random):  # place a queen randomly in each  row
    for i in range(len(board_random)):
        n = random.randint(0, 7)
        board_random[i][n] = 1
    return board_random


def threat_count(board_threat):
    counter = 0
    worst_queen=0
    partial_threats=0
    worst_queen_threats=0
    for i in range(len(board_threat)):
        for j in range(len(board_threat)):
            if board_threat[i][j] == 1:
                for threat_i in range(len(board_threat)):
                    if board_threat[threat_i][j] == 1:
                        counter = counter + 1
                        partial_threats=partial_threats+1
                        # print("for",(i,j),"-->",(threat_i))
                dif = abs(i - j)
                first_i = i - min(i, j)
                first_j = j - min(i, j)
                while (first_i < 8) and (first_j < 8):
                    if board_threat[first_i][first_j] == 1:
                        counter = counter + 1
                        partial_threats = partial_threats + 1
                        # print("for ", (i, j), " -->", (first_i, first_j))
                    first_i = first_i + 1
                    first_j = first_j + 1
                first_i = i
                first_j = j
                while (first_i >= 0) and (first_j <= 7):

                    if board_threat[first_i][first_j] == 1:
                        counter = counter + 1
                        partial_threats = partial_threats + 1
                    first_i = first_i - 1
                    first_j = first_j + 1

                first_i = i
                first_j = j
                while (first_i <= 7) and (first_j >= 0):

                    if board_threat[first_i][first_j] == 1:
                        counter = counter + 1
                        partial_threats = partial_threats + 1
                    first_i = first_i + 1
                    first_j = first_j - 1

                if partial_threats>worst_queen_threats:
                    worst_queen=i
                    worst_queen_threats=partial_threats
                partial_threats=0

    return (counter - 32,worst_queen)


def moves_to_childs(board_move):
    moves = []
    for i in range(0, 8):
        for j in range(0, 8):
            #if board_move[i][j] == 0:
                moves.append((i, j))

    return moves  # it means that you can move queen in row i, to row i and and culomns 0 to 7, or side moves
