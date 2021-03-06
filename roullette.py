from random import randint

import pandas as pd


class Data:
    def __init__(self):
        self.columns = ("Wallet_balance", "Placed_bid", "Bid_amount", "Roll", "PNL")
        self.Database = pd.DataFrame(columns=self.columns)

    def Add_new(self, balance, placed_bid, bid_amount, roll, pnl):
        new_data = [[balance, placed_bid, bid_amount, roll, pnl]]
        df = pd.DataFrame(new_data, columns=self.columns)
        self.Database = self.Database.append(df, ignore_index=True)

    def Print_Data(self, path_to_csv):
        self.Database.to_csv(path_to_csv)

    def __repr__(self):
        return "class Data, use method .Add_new or .Print_Data"


class Bets:
    def __init__(self, available_balance, placed_on, bet_amount: int):
        self.balance = available_balance
        self.Bet = 0
        self.amount = 0
        if placed_on > 48 or placed_on < 0:
            print(f"you have tried to enter an invalid bet, you can bet on 0-36"
                  f" for black enter #37, red #38, even #39, odd #40, low #41,"
                  f" high #42, column1 #43, column2 #44, column3 #45, First12 #46,"
                  f" Second12 #47,Third12 #48")
            self.placed_on = placed_on = input("Please input a valid bet: ")
        else:
            self.placed_on = placed_on
        self.Placed_Bet(placed_on)
        self.Bet_amount(bet_amount)

    def Placed_Bet(self, placed):
        self.Bet = placed

    def Bet_amount(self, wager):
        if wager > self.balance:
            print(f"you have tried to wager more than your balance, your current balance is {self.balance}")
            self.amount = input("please enter an amount less than or equal to your available balance: ")
        else:
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
        return "class Roll, call a .Roll method"


class Wallet:
    def __init__(self):
        self.Start_balance = float(input("Enter your starting Balance: "))
        self.Wallet_balance = self.Start_balance
        self.numbers = range(1, 36)
        self.black = (2, 4, 6, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35)  # 37
        self.red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)  # 38
        self.even = range(2, 36, 2)  # 39
        self.odd = range(1, 35, 2)  # 40
        self.low = range(1, 18)  # 41
        self.high = range(19, 36)  # 42
        self.Column1 = range(1, 34, 3)  # 43
        self.Column2 = range(2, 35, 3)  # 44
        self.Column3 = range(3, 36, 3)  # 45
        self.First12 = range(1, 12)  # 46
        self.Second12 = range(13, 24)  # 47
        self.Third12 = range(25, 36)  # 48
        self.Zero = (0, 'zero')
        self.skip_turn = (None, "skip")  # 49
        self.Roll = 0
        self.Bet = 0
        self.Amount = 0
        self.winnings = 0

    def Realised_pnl(self, roll: int, bet: int, amount: int):
        self.Bet = bet
        self.Roll = roll
        self.Amount = amount
        if self.Bet == 49:
            print(
                f'Roll was {self.Roll}, you skipped this round,'
                f'Your balance is: {self.Wallet_balance} ')

        elif self.Bet == self.Roll:
            self.winnings = self.Amount * 36
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 37 and self.Roll in self.black:
            self.winnings = self.Amount * 2
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 38 and self.Roll in self.red:
            self.winnings = self.Amount * 2
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 39 and Roll in self.even:
            self.winnings = self.Amount * 2
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 40 and self.Roll in self.odd:
            self.winnings = self.Amount * 2
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 41 and self.Roll in self.low:
            self.winnings = self.Amount * 2
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 42 and self.Roll in self.high:
            self.winnings = self.Amount * 2
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 43 and Roll in self.Column1:
            self.winnings = self.Amount * 3
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 44 and self.Roll in self.Column2:
            self.winnings = self.Amount * 3
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 45 and Roll in self.Column3:
            self.winnings = self.Amount * 3
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 46 and self.Roll in self.First12:
            self.winnings = self.Amount * 3
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 47 and self.Roll in self.Second12:
            self.winnings = self.Amount * 3
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 48 and self.Roll in self.Third12:
            self.winnings = self.Amount * 3
            self.Wallet_balance += (self.winnings - self.Amount)
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have won {self.winnings}\n Your new balance is: {self.Wallet_balance} ')

        elif self.Bet == 49:
            self.Wallet_balance *= 1
            print(
                f'Roll was {roll}, you did not place a bet,'
                f' Your new balance is: {self.Wallet_balance} ')

        else:
            self.Wallet_balance -= self.Amount
            print(
                f'Roll was {self.Roll}, your Bet was {self.Bet},'
                f' You have lost {self.Amount}\n your new balance is {self.Wallet_balance} ')
