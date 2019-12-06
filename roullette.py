from random import randint


class Bets:
    def __init__(self, bet, bet_amount:int, roll:int, wallet_balance:float):
        self.bet = bet
        self.bet_amount = bet_amount
        self.Roll = roll
        self.wallet_balance = wallet_balance
        self.Winnings = (self.bet_amount * 36)

    numbers = range(1,36)
    black = (2, 4, 6, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)
    red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
    even = range(2, 36, 2)
    odd = range(1, 35, 2)
    low = range(1, 18)
    high = range(19,36)
    Column1 = range(1, 34, 3)
    Column2 = range(2, 35, 3)
    Column3 = range(3, 36, 3)
    First12 = range(1, 12)
    Second12 = range(13, 24)
    Third12 = range(25, 36)
    Zero = (0, 'zero')

    def pnl(self):
        if self.bet == self.Roll:
            maxwin = self.bet_amount*36
            self.wallet_balance += maxwin
            balance = self.wallet_balance
            print(
                f'Roll was {self.Roll}, your bet was {self.bet},'
                f' You have won {maxwin}\n Your new balance is: {self.wallet_balance} ')
            return balance

        if self.bet == 'black' and self.Roll in Bets.black:
            blackwin = self.bet_amount * 2
            self.wallet_balance += blackwin
            balance = self.wallet_balance
            print(
                f'Roll was {self.Roll}, your bet was {self.bet},'
                f' You have won {blackwin}\n Your new balance is: {self.wallet_balance} ')
            return balance

        if self.bet == 'Red' and self.Roll in Bets.red:
            redwin = self.bet_amount * 2
            self.wallet_balance += redwin
            balance = self.wallet_balance
            print(
                f'Roll was {self.Roll}, your bet was {self.bet},'
                f' You have won {redwin}\n Your new balance is: {self.wallet_balance} ')
            return balance

        if self.bet == 'odd' and self.Roll in Bets.odd:
            oddwin = self.bet_amount * 2
            balance = self.wallet_balance + oddwin
            print(
                f'Roll was {self.Roll}, your bet was {self.bet},'
                f' You have won {oddwin}\n Your new balance is: {self.wallet_balance} ')
            return balance

        if self.bet == 'even' and self.Roll in Bets.even:
            evenwin = self.bet_amount * 2
            self.wallet_balance += evenwin
            balance = self.wallet_balance
            return balance


        else:
            balance = self.wallet_balance() - self.bet_amount()
            print(
                f'Roll was {self.Roll}, your bet was {self.bet},'
                f' You have lost {self.bet_amount}\n your new balance is {self.wallet_balance} ')
            return balance

    def Wallet_balance(self):
            if Bets.pnl(self) > 0:
                balance = self.wallet_balance + Bets.pnl(self)
                return balance
            if Bets.pnl(self)<0:
                balance = self.wallet_balance - Bets.pnl(self)
                return balance

    def outcome(self):
        if Bets.pnl(self) > 0:
            print(
                f'Roll was {self.Roll}, your bet was {self.bet},'
                f' You have won {evenwin}\n Your new balance is: {self.wallet_balance} ')

        if Bets.pnl(self) < 0:
            print(
                f'Roll was {self.Roll}, your bet was {self.bet},'
                f' You have lost {self.bet_amount}\n your new balance is {self.wallet_balance} ')




Wallet_balance =(float(input("enter starting balance")))

while Wallet_balance>0:
    bet = input("Place your bet ")
    bet_amount = (int(input("Place your bet amount ")))
    roll = randint(0, 36)
    new_bet = Bets(bet, bet_amount, roll, Bets.Wallet_balance)
    new_bet.pnl()
