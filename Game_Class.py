# This will hold the main logic for the game
# Logic is written in the Notes.txt file

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
print(current_player)

# Take a bet amount from the Player
bet_amount = current_player.place_bet()

# Starting a new round


