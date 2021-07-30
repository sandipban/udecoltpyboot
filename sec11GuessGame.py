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


'''Assignment Part 1 code'''

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(wrd):
    '''This function takes a word as arguement and strip all punctuations in the list punctuation_chars'''
    for pun in punctuation_chars:
        wrd = wrd.replace(pun, '')
    return wrd


def get_pos(strn_sentence):
    '''arguement strn is one or more sentences and calculate count of positive words'''
    strn_sentence = strip_punctuation(strn_sentence)
    lst_strn_sentence = strn_sentence.split()
    cont = 0
    for word in lst_strn_sentence:
        for p_word in positive_words:
            if word == p_word:
                cont += 1
    return cont