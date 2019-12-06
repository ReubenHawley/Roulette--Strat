import pandas as pd

colnames = [ "Roll", 'PNL', 'Wallet balance', 'Outcome', 'Bet amount' ]
df = pd.DataFrame( index=None, columns=colnames )


def Wallet_balance( Wallet_balance ):
	df = df.append( {'Wallet balance': Wallet_balance}, ignore_index=True )
	return df


def Roll_no( Roll ):
	df = df.append( {"Roll": Roll}, ignore_index=True )
	return df


def Outcome( Roll ):
	# add argument for win/lose here
	df = df.append( {"Outcome": Roll}, ignore_index=True )
	return df


def Bet_amount( bet_amount ):
	# add argument for win/lose here
	df = df.append( {"Bet amount": bet_amount}, ignore_index=True )
	return df


print( df )
