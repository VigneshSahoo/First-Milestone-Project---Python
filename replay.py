def replay():
    play_again = False
    while not play_again:
        player_answer = input('Would you like to play again?(Yes/No): ')
        if player_answer.upper() == 'YES':
            play_again = True
            break
        else:
            continue

replay()