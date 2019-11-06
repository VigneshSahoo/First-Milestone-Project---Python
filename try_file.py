board = ['X', 'O', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X', 'O']


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

print(full_board_check(board))
