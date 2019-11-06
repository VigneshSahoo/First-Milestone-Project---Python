import random
board = ['#','7','8','9','4','5','6','1','2','3']

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
#step 5
def choose_first():
    markers = ['X', 'O']
    random_selection = random.randint(markers.index('X'), markers.index('O'))
    return markers[random_selection]
#step 6
def space_check(board, position):
    if board[position] != 'X' and board[position] != 'O':
        # True = 1
        return 1
    else:
        # False = 0
        return 0
# step 7
def full_board_check(board):
    space_list = []
    space_available = True
    for i in range(len(board)):
        space_list.append(space_check(board, i))
    if 1 not in space_list:
        space_available = False
    if 1 in space_list:
        space_available = True
    return space_available
#step 8
def player_choice(board):
    position = ''
    while position not in board:
        position = input('\nPlease select your position i.e., (1-9): ')
        if int(position) not in range(1, 10):
            print('\nOut of bound!\n')
        else:
            if board[int(position)] == 'X' or board[int(position)] == 'O':
                print('\nInvalid selection!. Position already taken. \n')
    return int(position)
#step 9:
def replay():
    play_again = True
    while play_again:
        player_answer = input('\nWould you like to play again?(Yes/No): ')
        if player_answer.upper() == 'YES':
            play_again = True
            break
        elif player_answer.upper() == 'NO':
            play_again = False
            break
    return play_again
# The Game
while True:
    intro_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    print('\nWelcome to Tic Tac Toe!\n')
    display_board(intro_board)
    board = ['X', '7', '8', '9', '4', '5', '6', '1', '2', '3']
    markers = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
    player_input()
    display_board(board)
    player1 = choose_first()
    print(f'\nFirst player to start: {player1}\n')
    game_on = True
    count = 0
    while game_on:
        position = player_choice(board)
        position_check = space_check(board, position)
        if player1 == 'X':
            place_marker(board, markers[0 + count], position)
        if player1 == 'O':
            place_marker(board, markers[1 + count], position)
        win = win_check(board, 'X') or win_check(board, 'O')
        draw = full_board_check(board)
        if win:
            print('\n' * 50)
            print('Congratulations! You won.\n')
            display_board(board)
            break
        print('\n' * 50)
        display_board(board)
        count += 1
        print(draw)
        if draw == False:
            replay()

    # if not replay():
    #     print('Thanks for playing! Hope you have enjoyed the game.\n')
    #     break
