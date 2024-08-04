# This will contain the Deck Class
# Will contain a loop to create a Deck of cards
# Will contain a method to shuffle the cards - shuffle from random
# Will contain an all_cards variable to hold the cards
# Will contain a method to deal one card

import Card_Class
from random import shuffle

#creating the Deck class
class Deck:

    def __init__(self) -> None:
        self.all_cards_deck = []  # Starts with an empty deck. '_deck' to separate it from Player all_cards

    def add_cards(self):
        
        created_card = []

        for suit in Card_Class.suit:
            for rank in Card_Class.rank:
                created_card = Card_Class.Card(suit, rank)
                self.all_cards_deck.append(created_card)

    def shuffle(self):

        shuffle(self.all_cards_deck)

    def __str__(self) -> str:
        return f'There are {len(self.all_cards_deck)} cards in the deck!'


if __name__ == '__main__':
    print('Please run Game_Class!')

"""
my_deck = Deck()
my_deck.add_cards()
my_deck.shuffle()
print(my_deck)
"""