from random import randint
comp_guess = randint(1, 5)


while True:
    player_guess = int(input('Guess any number between 1 to 10: '))

    if player_guess > comp_guess:
        print('Your guess is too high.')
    elif player_guess < comp_guess:
        print('Your guess is too low.')
    else:
        print('You won the game')
        play_again = input('Do you want to continue (y/n): ')
                
        if play_again == 'y':
            comp_guess = randint(1, 5)
            player_guess = None
        else:
            break
        
print('Game over')


