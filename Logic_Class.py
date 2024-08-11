# This file will contain the check logic of the game to not lengthen the Game Class and increase readability

def player_name_func():
    while True:
        try:
            player_name = input('Please enter your name: ')

        except:
            print('That is an incorrect entry!')
            continue

        else:
            print(f'Welcome to the game {player_name}!')
            return player_name