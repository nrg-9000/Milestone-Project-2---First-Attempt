# This file will contain all of the possible end conditions


import Deck_Class
import Player_Class
import Game_Class

def low_balance():
    while True:
        if Game_Class.current_player > 0:
            break    
        else:
            end_condition ### Player does not have enough balance