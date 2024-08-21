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


# Initialising variables
round_number = 0
game_on = True
player_choice = False
player_value = 0
inhand_aces = 0
hand_value = 0


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

    # Checking for Aces in first hand
    if player_hand[0].card_rank() == 'Ace' or player_hand[1].card_rank() == 'Ace':
        inhand_aces += 1

    print(f'Player has {player_hand[0]} and {player_hand[1]}.')
    

    # Initialising dealer hand
    dealer_hand.extend(game_deck.dealer_start())
    print(f'Dealer has {dealer_hand[0]} and *HIDDEN CARD*.')


    # Main game logic for player - player has to choose between HIT or STAY
    while True:
        try:
            player_choice = input('Do you want to Hit or Stay? (H/S): ')
            player_choice = player_choice.upper()

        except:
            print('That is not a valid choice. Please try again')

        else:
            if player_choice == 'H': 
                player_hand.extend(game_deck.hit()) # Adding another card

                print(player_hand[-1].card_rank()) ### Test


                # Keeping count of the number of Aces in the present hand
                if player_hand[-1].card_rank() == 'Ace':
                    inhand_aces += 1



                print(f'Player Hand: {player_hand}')


                if Logic_Class.values_sum(player_hand) >= 21: #Checking to see if Player is bust
                    
                    # Logic to change Aces from 11 to 1
                    hand_value = Logic_Class.values_sum(player_hand)
                    if inhand_aces != 0:
                        while hand_value >= 21 and inhand_aces != 0:
                            hand_value -= 10
                            inhand_aces -= 1
                            continue
                    
                    print(f'{player_name} is bust. Player Loses!') ### END CONDITION
                    game_on = False
                    print(inhand_aces)
                    break
                    

                else:
                    continue
            elif player_choice == 'S':        
                break
            else:
                print('That is not a valid choice. Please try again')


    # Checking flag to break outer while loop
    if not game_on: 
        break


    # Main logic for dealer - Dealer will keep hitting until win or bust

    print('Dealer will go next')
    print(f'Dealer has {dealer_hand[0]} and {dealer_hand[1]}.')
    
    if Logic_Class.values_sum(player_hand) < Logic_Class.values_sum(dealer_hand): #Checking to see if Dealer has won in first hand
        print('Dealer wins! Player Loses!') ### END CONDITION
        game_on = False
        break
    
    while True:
        if Logic_Class.values_sum(dealer_hand) >= 21: #Checking to see if Dealer is bust
            print('Dealer is bust. Player wins!!!') ### END CONDITION
            game_on = False
            break

        else:
            print('Dealer Hit!')
            dealer_hand.extend(game_deck.hit()) # Adding another card
            print(f'Dealer Hand: {dealer_hand}')

            if Logic_Class.values_sum(dealer_hand) >= 21: #Checking to see if Dealer is bust
                print('Dealer is bust. Player wins!!!') ### END CONDITION
                game_on = False
                break
            elif Logic_Class.values_sum(player_hand) < Logic_Class.values_sum(dealer_hand): #Checking to see if Dealer has won
                print('Dealer wins! Player Loses!') ### END CONDITION
                game_on = False
                break
            else:
                continue

    
