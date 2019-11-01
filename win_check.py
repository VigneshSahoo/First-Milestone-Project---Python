test_board = ['#','x','8','9','4','5','6','x','c','x']

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

print(win_check(test_board, 'x'))