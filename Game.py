from roullette import Wallet, Bets, Roll


class Game:
    def __init__(self, placement: int = 0, wager: int = 0):
        self.Wallet = Wallet()
        self.placement = placement
        self.wager = wager
        self.rolled = 0

    def NewRound(self):
        print(f"Current balance is {self.Wallet.Wallet_balance}")
        self.placement = int(input("Enter a bet: "))
        self.wager = int(input("Enter an amount: "))
        bet = Bets(self.Wallet.Wallet_balance, self.placement, self.wager)
        self.rolled = Roll()
        self.Wallet.Realised_pnl(roll=self.rolled.Roll, bet=bet.Bet, amount=self.wager)


roulette = Game()
while True:
    roulette.NewRound()
