# This file will contain the check logic of the game to not lengthen the Game Class and increase readability

import Card_Class

def player_name_func():
    while True:
        try:
            player_name = input('Please enter your name: ')

        except:
            print('That is an incorrect entry!')
            continue

        else:
            return player_name
        
def values_sum(values):
    total_sum = 0
    for i in values:
        total_sum += i.card_value()
    return total_sum

