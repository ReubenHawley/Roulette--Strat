from roullette import Wallet, Bets, Roll


class Game:
    def __init__(self, placement: int = 0, wager: int = 0):
        self.Wallet = Wallet()
        self.placement = placement
        self.wager = wager
        self.bet = Bets(self.Wallet.Wallet_balance, self.placement, self.wager)
        self.rolled = Roll()

    def NewRound(self):
        print(f"Current balance is {self.Wallet.Wallet_balance}")
        self.placement = int(input("Enter a bet: "))
        self.wager = int(input("Enter an amount: "))
        self.bet = Bets(self.Wallet.Wallet_balance, self.placement, self.wager)
        self.Wallet.Realised_pnl(roll=self.rolled.Roll, bet=self.bet.Bet, amount=self.wager)


roundstart = Game()
while True:
    roundstart.NewRound()
