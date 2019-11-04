test_board = ['#', '7', '8', '9', '4', '5', '6', '1', '2', '3']

def space_check(board, position):
    if board[position] != 'X' or board[position] != 'O':
        return True

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

def player_switch():
    p1 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    p2 = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
    player1 = 'X'
    if player1 == p1[0]:
        for i in p1:
            print(i)

print(player_choice(test_board))
