from random import randint


class Bets:
    def __init__(self, placed_on, bet_amount):
        self.Bet = 0
        self.amount = 0
        self.Placed_Bet(placed_on)
        self.Bet_amount(bet_amount)

    def Placed_Bet(self, placed):
        self.Bet = placed

    def Bet_amount(self, wager):
        self.amount = wager

    def __repr__(self):
        return "class Bets, call a method"


class Roll:
    def __init__(self):
        self.Roll = 0  # call this function for the actual roll
        self.New_roll()  # initiate a new roll

    def New_roll(self):
        self.Roll = randint(0, 36)

    def __repr__(self):
        return "class Roll, call a method"


class Wallet:
    def __init__(self, initial_amount):
        self.Wallet_balance = 0  # call this for the wallet balance
        self.Start_balance(initial_amount)  # this initiates the wallet balance

    def Start_balance(self, initial_balance):
        self.Wallet_balance = initial_balance

    def Updated_balance(self, realised_pnl):  # any updates to the wallet balance require this method
        self.Wallet_balance += realised_pnl

    def __repr__(self):
        return "class Wallet, call a method"


class Pnl:
    def __init__(self, wallet_balance, roll, bet, amount):
        self.numbers = range(1, 36)
        self.black = (2, 4, 6, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
        self.red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
        self.even = range(2, 36, 2)
        self.odd = range(1, 35, 2)
        self.low = range(1, 18)
        self.high = range(19, 36)
        self.Column1 = range(1, 34, 3)
        self.Column2 = range(2, 35, 3)
        self.Column3 = range(3, 36, 3)
        self.First12 = range(1, 12)
        self.Second12 = range(13, 24)
        self.Third12 = range(25, 36)
        self.Zero = (0, 'zero', None)
        self.Wallet_balance = wallet_balance
        self.Roll = 0
        self.Bet = 0
        self.Amount = 0
        self.Realised_pnl(roll, bet, amount)

    def Realised_pnl(self, roll, bet, amount):
        if bet == roll:
            maxwin = amount * 36
            self.Wallet_balance += maxwin
            print(
                f'Roll was {roll}, your Bet was {bet},'
                f' You have won {maxwin}\n Your new balance is: {self.Wallet_balance} ')

        if bet == 'black' and roll in self.black:
            blackwin = amount * 2
            self.Wallet_balance += blackwin
            print(
                f'Roll was {roll}, your Bet was {self.Bet},'
                f' You have won {blackwin}\n Your new balance is: {self.Wallet_balance} ')

        if bet == 'Red' and roll in self.red:
            redwin = amount * 2
            self.Wallet_balance += redwin
            print(
                f'Roll was {roll}, your Bet was {bet},'
                f' You have won {redwin}\n Your new balance is: {self.Wallet_balance} ')

        if bet == 'odd' and Roll in self.odd:
            oddwin = amount * 2
            self.Wallet_balance += oddwin
            print(
                f'Roll was {roll}, your Bet was {bet},'
                f' You have won {oddwin}\n Your new balance is: {self.Wallet_balance} ')

        if self.Bet == 'even' and Roll in self.even:
            evenwin = amount * 2
            self.Wallet_balance += evenwin

        else:
            self.Wallet_balance -= amount
            print(
                f'Roll was {roll}, your Bet was {bet},'
                f' You have lost {amount}\n your new balance is {self.Wallet_balance} ')
