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


# Starting a new round
player_hand.extend(game_deck.player_start())
print(f'Player has {player_hand}.')
dealer_hand = game_deck.dealer_start()


# Main game logic for player

