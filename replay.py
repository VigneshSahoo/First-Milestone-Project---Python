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

print(replay())