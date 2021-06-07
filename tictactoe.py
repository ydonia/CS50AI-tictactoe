"""
Tic Tac Toe Player
"""

import copy
import math

# players
X = "X"
O = "O"
EMPTY = None


# set of possible actions returned by actions method
# possible_actions = set()
# currentPlayer = X


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # make a counter for X and O players
    counterX = 0
    counterO = 0

    # count the number of X's and O's on the board
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == X:
                counterX += 1
            elif board[row][col] == O:
                counterO += 1

    # since X player starts, if X and O counters are equal, then it is X player's turn
    if counterX > counterO:
        return O
    else:
        return X

    # if terminal board is returned, game is over and accept any input

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    # iterate through the board
    for row in range(0, len(board)):
        for col in range(0, len(board[0])):
            if board[row][col] == EMPTY:
                # when an empty space is found, add to the set of possible actions
                possible_actions.add((row, col))

    # return set of possible actions
    return possible_actions

    # if terminal board is provided, accept any input
    # TODO: do i make the function return None if terminal board??

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)

    if action in possible_actions:
        # take the row and column from the action
        row = action[0]
        col = action[1]
        # make a copy of the board to modify
        board_copy = copy.deepcopy(board)
        # board_copy[action.row][action.col] = currentPlayer
        board_copy[row][col] = player(board)
        return board_copy
    else:
        raise Exception("The action is not possible.")

    # raise NotImplementedError


def areEqual(a, b, c):
    # returns true if the three squares are equal and not empty
    return a == b == c and a != EMPTY


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_player = None

    # find a way to check who is won.

    # horizontal
    for i in range(3):
        if areEqual(board[i][0], board[i][1], board[i][2]):
            winning_player = board[i][0]

    # vertical
    for i in range(3):
        if areEqual(board[0][i], board[1][i], board[2][i]):
            winning_player = board[0][i]

    # diagonal
    if areEqual(board[0][0], board[1][1], board[2][2]):
        winning_player = board[0][0]

    if areEqual(board[2][0], board[1][1], board[0][2]):
        winning_player = board[2][0]

    # TODO: check for available actions??
    # if winning_player is None:
    #     return None
    # else:
    return winning_player

    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    possible_actions = actions(board)

    if winner(board) is not None:
        return True

    # if there are no actions left, then the game is over
    if len(possible_actions) == 0:
        return True
    else:
        return False

    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # will only be called if terminal() returns true
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # recursive algorithm to check all possible moves and return which move is best for X or O depending on turn

    # if the game is over, return none
    if terminal(board):
        return None

    possible_actions = actions(board)

    if player(board) == X:
        # initialize the score and the best move
        score = -math.inf
        best_move = None

        for action in possible_actions:
            # this will actually get the maximizing score, because the minimax_O function calls the max one
            maximizing_score = minimax_O(result(board, action))

            # update the best move for X depending on the results of the minimax function
            if maximizing_score > score:
                score = maximizing_score
                best_move = action

        return best_move

    elif player(board) == O:
        # initialize the score and best move with the opposite values
        score = math.inf
        best_move = None

        for action in possible_actions:
            # this will actually get the maximizing score, because the minimax_O function calls the max one
            minimizing_score = minimax_X(result(board, action))

            # update the best move for O depending on the results of the minimax function
            if minimizing_score < score:
                score = minimizing_score
                best_move = action

        return best_move

    # raise NotImplementedError


''' the following two functions will continue to call each other recursively to find the best move for each 
    player depending on the turn, which is why each function calls the other. they will find all the possible moves 
    and choose the best move depending on whether the X or O player is playing. '''


# function for the maximizing player (X)
def minimax_X(board):
    if terminal(board):
        return utility(board)

    # to return
    possible_actions = actions(board)
    maximizing_score = -math.inf

    for action in possible_actions:
        maximizing_score = max(maximizing_score, minimax_O(result(board, action)))

    # returns the score
    return maximizing_score


# function for the minimizing player (O)
def minimax_O(board):
    if terminal(board):
        return utility(board)

    # get the lowest score out of the possible actions by calling the max function
    possible_actions = actions(board)
    minimizing_score = math.inf

    for action in possible_actions:
        minimizing_score = min(minimizing_score, minimax_X(result(board, action)))

    return minimizing_score
