from roullette import Wallet, Bets, Roll, Data


class Game:
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
    roulette = Game()
    while True:
        placement = int(input("Enter a bet: "))
        wager = int(input("Enter an amount: "))
        roulette.NewRound(placement, wager)
        roulette.Display_History()


StartGame()
