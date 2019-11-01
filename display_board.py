def display_board(board):
    row1 = test_board[1:4]
    row2 = test_board[4:7]
    row3 = test_board[7:10]
    print(row1)
    print(row2)
    print(row3)

test_board = ['#','X','O','X','V','X','O','X','O','X']
display_board(board=test_board)