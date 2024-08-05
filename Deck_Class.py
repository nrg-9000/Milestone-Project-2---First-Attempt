# This will contain the Deck Class
# Will contain a loop to create a Deck of cards
# Will contain a method to shuffle the cards - shuffle from random
# Will contain an all_cards variable to hold the cards
# This will also function as the computer dealer class which will the cards
# Player start function - This will deal the player's first hand (Both cards facing up)
# Dealer start function - This will deal the dealer's first hand ( One card facing up and another card facing down)
# Hit function - This will deal one card from the deck
# Stay function - Stops dealing cards and ends turn (This should also start the check function in the )
# Reset deck function - This will reset the deck to zero

import Card_Class
from random import shuffle

#creating the Deck class
class Deck:

    def __init__(self) -> None:
        self.all_cards = []  # Starts with an empty deck. 


    def init_cards(self):  # This creates a deck of 52 cards 
        
        created_card = []

        for suit in Card_Class.suit:
            for rank in Card_Class.rank:
                created_card = Card_Class.Card(suit, rank)
                self.all_cards.append(created_card)


    def shuffle(self):  # This shuffles the deck

        shuffle(self.all_cards)


    def 

    def __str__(self) -> str:  # This is to return a statement if the deck is called directly
        return f'There are {len(self.all_cards)} cards in the deck!'


if __name__ == '__main__':
    print('Please run Game_Class!')

"""
my_deck = Deck()
my_deck.add_cards()
my_deck.shuffle()
print(my_deck)
"""