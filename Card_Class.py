# This will house the Card Class
# Card class should have dictionaries for suit, rank, and value
# All face cards will have value 10
# Ace can be 1 or 11 - which ever is preferable to the player at that time

# Creating the dictionaries
suit = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
rank = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Queen', ' King', 'Jack')

# The Ace card value definition has to be in the Game function depending on the player's current hand
value = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Queen': 10, ' King': 10, 'Jack': 10}

# Starting the Card Class
class Card:  # Giving () in a class definition is not mandatory but also not wrong

    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = value[rank]

    def __str__(self) -> str:
        return f'The {self.rank} of {self.suit}.'
    
if __name__ == '__main':
    print('Please run Game_Class!')    