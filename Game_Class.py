# This will hold the main logic for the game
# Logic is written in the Notes.txt file
# Create a function to check bank balance for the Player [#####]

import Card_Class
import Deck_Class
import Player_Class
import Logic_Class


# Creating a new Deck and shuffling it
game_deck = Deck_Class.Deck()
game_deck.init_cards()  
game_deck.shuffle()  


# Asking the user for a player name
player_name = Logic_Class.player_name_func()


# Creating a new Player
current_player = Player_Class.Player(player_name)


# Creating hand for both player and dealer
player_hand = []
dealer_hand = []


# Creating a round number to keep track
round_number = 0
game_on = True


while game_on == True:


    # Checking if player has enough account balance to continue round
    if current_player.balance_check() <= 0:
        print(f'{player_name} does not have enough balance in their account')
        game_on = False
        break
    else:
        pass


    # Starting a new round
    round_number += 1
    print(f'Round Number {round_number}')


    # Player will make a bet
    bet_amount = current_player.place_bet()


    # Initialising player hand
    player_hand.extend(game_deck.player_start())
    print(f'Player has {player_hand[0]} and {player_hand[1]}.')


    # Initialising dealer hand
    dealer_hand.extend(game_deck.dealer_start())
    print(f'Dealer has {dealer_hand[0]} and *HIDDEN CARD*.')


    # Main game logic for player

