board = ['#', '7', '8', '9', '4', '5', '6', '1', '2', '3']

def player_switch():
    p1 = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
    p2 = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
    player1 = 'X'
    if player1 == p1[0]:
        for i in p1:
            input('select: ')

player_switch()