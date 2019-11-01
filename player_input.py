
def player_input():
    player1 = ''
    player2 = ''
    while player1 != 'X' and player1 != 'O':
        player1 = (input('Enter chars: ')).upper()
        if player1 == 'X':
            player2 = 'O'
        elif player1 == 'O':
            player2 = 'X'

