# This will contain the Player Class
# Player does not need to hold any cards
# Player will have a bank account
# Player will be able to place bets
# Once bank account is empty, Player will not be able to plave any bets
# Player class needs to have a method to get back the money the bet and won from the round

class Player:

    def __init__(self, name) -> None:
        self.name = name
        self.bank = 10000
        print(f'Hi {self.name}!')

    def place_bet(self):
        print(f'You have {self.bank} in your account')
        
        while True:
            
            try:
                amount = int(input('Enter the amount you would like to bet: '))
            
            except:
                print('That is not a valid input')
                continue

            else:
                if amount > self.bank:
                    print(f'You do not have enough balance in your account. Present balance is {self.bank}')
                else:
                    print('Bet accepted!')
                    return amount
                    break

    def bet_back(self, bet):  # This is to get back the original bet amount
        self.bank = self.bank + bet  
        
        
    def win_back(self, bet):  # This is to get back twice the win amount after winning the round
        self.bank = self.bank + (2 * bet)
    

    def __str__(self) -> str:
        return f'{self.name} has {self.bank} in their account!'


if __name__ == '__main__':
    print('Please run Game_Class!')


'''
player_one = Player('One')
player_one.place_bet()
'''


