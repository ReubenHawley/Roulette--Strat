from roullette import Wallet, Bets, Roll, Data


class ManualGame:
    def __init__(self):
        self.Wallet = Wallet()
        self.placement = 0
        self.wager = 0
        self.rolled = 0
        self.Data = Data()

    def NewRound(self):
        print(f"Current balance is {self.Wallet.Wallet_balance}")
        self.placement = int(input("Enter a bet: "))
        self.wager = int(input("Enter an amount: "))
        bet = Bets(self.Wallet.Wallet_balance, self.placement, self.wager)
        self.rolled = Roll()
        self.Wallet.Realised_pnl(roll=self.rolled.Roll, bet=bet.Bet, amount=self.wager)
        self.Data.Add_new(self.Wallet.Wallet_balance, bet.Bet, self.wager, self.rolled.Roll, self.Wallet.winnings)
        self.Exit_game()

    def Display_History(self):
        print(self.Data.Database)

    def Exit_game(self):
        stop_game = input("do you want to continue? y/n: ")
        if stop_game == "n":
            exit()
        elif stop_game == "y":
            self.NewRound()


class AutoGame:
    def __init__(self):
        self.Wallet = Wallet()
        self.placement = 0
        self.wager = 0
        self.rolled = 0
        self.Data = Data()

    def NewRound(self, bid, bid_amount):
        print(f"Current balance is {self.Wallet.Wallet_balance}")
        self.placement = bid
        self.wager = bid_amount
        bet = Bets(self.Wallet.Wallet_balance, self.placement, self.wager)
        self.rolled = Roll()
        self.Wallet.Realised_pnl(roll=self.rolled.Roll, bet=bet.Bet, amount=self.wager)
        self.Data.Add_new(self.Wallet.Wallet_balance, bet.Bet, self.wager, self.rolled.Roll, self.Wallet.winnings)

    def Display_History(self):
        print(self.Data.Database)


def StartGame():
    roulette = ManualGame()
    while True:
        roulette.NewRound()
        roulette.Display_History()


StartGame()
