from setup import Game

if __name__ == '__main__':
    response = input('Would you like to play war? ')
    play = True

    game = None

    if response.lower() == 'no':
        play = False
    else:
        game = Game()

    while play:
        game.war()
        response = input('Would you like to play again? ')
        if response.lower() == 'no':
            play = False
        else:
            game.reset()

    if game:
        print(
            f'Thanks for playing! The final win totals were '
            f'{game.player1.wins} wins for {game.player1} and '
            f'{game.player2.wins} wins for {game.player2}.'
        )
