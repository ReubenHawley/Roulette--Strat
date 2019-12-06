import pandas as pd


class Wallet:
	def __init__( self, initial_balance: float ):
		self.initial_balance = initial_balance

	def Wallet_balance( self ):
		wallet_balance = pd.DataFrame( [ 'Wallet Balance' ] )
