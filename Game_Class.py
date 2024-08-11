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


# Take a bet amount from the Player
bet_amount = current_player.place_bet()


# Creating hand for both player and dealer
player_hand = []
dealer_hand = []


# Creating a round number to keep track
round_number = 0


# Checking if player has enough account balance to continue round
while True:
    if current_player.balance_check() > 0:
        break    
    else:
        end_condition ### Player does not have enough balance



# Starting a new round
round_number += 1
print(f'Round Number {round_number}')


# Initialising player hand
player_hand.extend(game_deck.player_start())
print(f'Player has {player_hand}.')


# Initialising dealer hand
dealer_hand.extend(game_deck.dealer_start())
print(f'Dealer')


# Main game logic for player

