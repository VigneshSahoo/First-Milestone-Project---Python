import random

board = ['#', '7', '8', '9', '4', '5', '6', '1', '2', '3']


def display_board(board):
    row_1 = print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    row_2 = print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    row_3 = print(board[7] + ' | ' + board[8] + ' | ' + board[9])


def player_input():
    player_marker = ''
    while player_marker != 'X' and player_marker != 'O':
        player_marker = (input("Please select your marker('X' or 'O'): ")).upper()
        print(f'You have selected {player_marker}')
    return player_marker


def place_marker(board, marker, position):
    for i in range(len(board)):
        if board[i] == str(position):
            board[i] = marker
    return board


def win_check(board, mark):
    if board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    if board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    if board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    if board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    if board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    if board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    if board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False


# step 5
def choose_first():
    markers = ['X', 'O']
    random_selection = random.randint(markers.index('X'), markers.index('O'))
    return markers[random_selection]


# step 6
def space_check(board, position):
    if board[position] != 'X' and board[position] != 'O':
        return True
    else:
        return False


# step 7
def full_board_check(board):
    for i in range(len(board)):
        space_check(board, i)


# step 8
def player_choice(board):
    position = ''
    while position not in board:
        position = input('Please select your position i.e., (1-9): ')
        if int(position) not in range(1, 10):
            print('Out of bound!')
        else:
            if board[int(position)] == 'X' or board[int(position)] == 'O':
                print('Invalid selection!. Position already taken. ')
    return int(position)


# step 9:
def replay():
    play_again = False
    while not play_again:
        player_answer = input('Would you like to play again?(Yes/No): ')
        if player_answer.upper() == 'YES':
            play_again = True
            break
        else:
            continue


# The Game
while True:
    intro_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    print('Welcome to Tic Tac Toe!')
    print(display_board(intro_board))
    board = ['#', '7', '8', '9', '4', '5', '6', '1', '2', '3']
    p1 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    p2 = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
    player_input()
    print(display_board(board))
    player1 = choose_first()
    print(f'First player to start: {player1}')
    game_on = True
    while game_on:
        position = player_choice(board)
        position_check = space_check(board, position)
        place_marker(board, player1, position)
        print(display_board(board))

    if not replay():
        print('Thanks for playing! Hope you have enjoyed the game.')
        break
