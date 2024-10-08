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
dealer_aces = 0
dealer_value = 0


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

    ''' This is not required anymore as we are counting aces everytime
    # Checking for Aces in first hand
    if str(player_hand[0].card_rank()) == 'Ace' or str(player_hand[1].card_rank()) == 'Ace':
        inhand_aces += 1
    '''

    print(inhand_aces) ### Test

    print(f'Player has {player_hand[0]} and {player_hand[1]}.')
    
    print(type(player_hand[0].card_rank())) ### TEST
    print(repr(player_hand[-1].card_rank())) ### TEST

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
                
                print(Logic_Class.values_sum(player_hand)) ###TEST

                # Checking for Aces in hand
                for i in player_hand:
                    if i.card_rank() == 'Ace':
                        inhand_aces += 1

                print(inhand_aces) ### Test


                print(f'Player Hand: {player_hand}')

                hand_value = Logic_Class.values_sum(player_hand)


                if hand_value >= 21: #Checking to see if Player is bust
                    
                    # Logic to change Aces from 11 to 1
                    if inhand_aces != 0:
                        while hand_value >= 21 and inhand_aces != 0:
                            hand_value -= 10
                            inhand_aces -= 1
                            continue
                        if hand_value < 21:
                            inhand_aces = 0
                            continue
                    
                    print(f'{player_name} is bust. Player Loses!') ### END CONDITION
                    print(Logic_Class.values_sum(player_hand)) ###TEST
                    game_on = False
                    break
                    

                else:
                    print(Logic_Class.values_sum(player_hand)) ###TEST
                    inhand_aces = 0
                    continue
            elif player_choice == 'S':

                for i in player_hand:
                    if i.card_rank() == 'Ace':
                        inhand_aces += 1

                print(inhand_aces) ### Test

                hand_value = Logic_Class.values_sum(player_hand)

                    
                # Logic to change Aces from 11 to 1
                if inhand_aces != 0:
                    while inhand_aces != 0:
                         hand_value -= 10
                         inhand_aces -= 1
                         continue
                     
                break
            elif player_choice == 'P': ###TEST
                print(Logic_Class.values_sum(player_hand))
            else:
                print('That is not a valid choice. Please try again')


    # Checking flag to break outer while loop
    if not game_on: 
        break


    # Main logic for dealer - Dealer will keep hitting until win or bust

    print('Dealer will go next')
    print(f'Dealer has {dealer_hand[0]} and {dealer_hand[1]}.')
    
    #Checking to see if Dealer has won in first hand
    if hand_value < Logic_Class.values_sum(dealer_hand): # Comparing with 'hand_value' to adjust for aces
        print('Dealer wins! Player Loses!') ### END CONDITION
        game_on = False
        break
    
    while True:
        if Logic_Class.values_sum(dealer_hand) >= 21: #Checking to see if Dealer is bust
           
            # Checking for Aces in dealer hand
            for i in dealer_hand:
                if i.card_rank() == 'Ace':
                    dealer_aces += 1

            print(dealer_aces) ### Test

            print(f'Dealer Hand: {dealer_hand}') ### TEST

            dealer_value = Logic_Class.values_sum(dealer_hand)


            if dealer_value >= 21: #Checking to see if Dealer is bust
                
                # Logic to change Aces from 11 to 1
                if dealer_aces != 0:
                    while dealer_value >= 21 and dealer_aces != 0:
                        dealer_value -= 10
                        dealer_aces -= 1
                        continue
                    if dealer_value < 21:
                        dealer_aces = 0
                        continue
            print('Dealer is bust. Player wins!!!') ### END CONDITION
            game_on = False
            break


        else:
            print('Dealer Hit!')
            dealer_hand.extend(game_deck.hit()) # Adding another card
            print(f'Dealer Hand: {dealer_hand}')

            if Logic_Class.values_sum(dealer_hand) >= 21: #Checking to see if Dealer is bust

                # Checking for Aces in dealer hand
                for i in dealer_hand:
                    if i.card_rank() == 'Ace':
                        dealer_aces += 1

                print(dealer_aces) ### Test

                print(f'Dealer Hand: {dealer_hand}') ### TEST

                dealer_value = Logic_Class.values_sum(dealer_hand)


                if dealer_value >= 21: #Checking to see if Dealer is bust
                    
                    # Logic to change Aces from 11 to 1
                    if dealer_aces != 0:
                        while dealer_value >= 21 and dealer_aces != 0:
                            dealer_value -= 10
                            dealer_aces -= 1
                            continue
                        if dealer_value < 21:
                            dealer_aces = 0
                            continue
                print('Dealer is bust. Player wins!!!') ### END CONDITION
                game_on = False
                break
            elif hand_value < Logic_Class.values_sum(dealer_hand): #Checking to see if Dealer has won
                print('Dealer wins! Player Loses!') ### END CONDITION
                game_on = False
                break
            else:
                continue

    
