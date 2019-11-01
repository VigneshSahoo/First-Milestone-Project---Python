import random
test_board = ['#','7','8','9','4','5','6','7','8','9']

def display_board(board):
    print(test_board[1] + '|' + test_board[2] + '|' + test_board[3])
    print(test_board[4] + '|' + test_board[5] + '|' + test_board[6])
    print(test_board[7] + '|' + test_board[8] + '|' + test_board[9])

def player_input():
    player_marker = ''
    while player_marker != 'X' and player_marker != 'O':
        player_marker = (input("Please select your marker('X' or 'O'): ")).upper()
    return player_marker

def place_marker(board, marker, position):
    for i in range(len(board)):
        if test_board[i] == str(position):
            test_board[i] = marker

def win_check(board, mark):
    if test_board[7] == mark and test_board[8] == mark and test_board[9] == mark:
        return True
    if test_board[4] == mark and test_board[5] == mark and test_board[6] == mark:
        return True
    if test_board[1] == mark and test_board[2] == mark and test_board[3] == mark:
        return True
    if test_board[1] == mark and test_board[4] == mark and test_board[7] == mark:
        return True
    if test_board[2] == mark and test_board[5] == mark and test_board[8] == mark:
        return True
    if test_board[3] == mark and test_board[6] == mark and test_board[9] == mark:
        return True
    if test_board[1] == mark and test_board[5] == mark and test_board[9] == mark:
        return True
    if test_board[3] == mark and test_board[5] == mark and test_board[7] == mark:
        return True
    else:
        return False

def choose_first():
    player1 = random.randint(1, 2)
    return player1

def space_check(board, position):
    if board[position] != 'X' or board[position] != 'O':
        return True

def full_board_check(board):
    for i in range(len(board)):
        space_check()