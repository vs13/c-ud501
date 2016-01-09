import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from util import get_data,plot_data
def test_run():
	start_date = '26-Dec-14'
	end_date = '10-May-15'
	dates = pd.date_range(start_date,end_date)
	df = pd.DataFrame(index=dates)
	#print df
	for symbol in ['aapl','googl','spy','amzn']:
		dftmp = pd.read_csv("{}.csv".format(symbol),index_col=0,parse_dates=True)
		#dftmp = dftmp.rename(columns={'Open':symbol,'Close':symbol,'High':symbol,'Low':symbol,'Volume':symbol})
		dftmp.columns = ['Open'+symbol,'Close'+symbol,'High'+symbol,'Low'+symbol,'Volume'+symbol]
		df = df.join(dftmp,how="inner")
	#df['Date'] =pd.to_datetime(df.Date)
	#print df.columns
	df = df.sort_index()
	#print df
	plot_df(normalized_data(df.ix['2015-01-01':'2015-01-30',['Closeamzn','Closegoogl','Closeaapl']]))
	#Slice Rows
	dftest = df.ix['2015-01-01':'2015-03-30',['Closeamzn','Closegoogl','Closeaapl']]
	
	rm_amzn = get_rolling_mean(dftest['Closeamzn'],window=20)
	rstd_amzn = get_rolling_std(dftest['Closeamzn'],window=20)
	upper_band,lower_band = get_bollinger_bands(rm_amzn,rstd_amzn)
	ax = dftest['Closeamzn'].plot(title="Bollinger Bands",label='AMZN')
	rm_amzn.plot(label="Rolling Mean",ax=ax)
	upper_band.plot(label="Upper Band",ax=ax)
	lower_band.plot(label="Lower Band",ax=ax)
	ax.legend(loc='upper left')
	ax.set_xlabel
	#plt.show()
	dfreturn = compute_daily_returns(dftest['Closeamzn'])
	plot_data(daily_returns,title="Histogram Daily Returns",ylabel="Daily Returns")
	plt.show()

def plot_df(df,title="Stock Prices"):
	ax = df.plot(title=title)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	plt.show()

def normalized_data(df):
	print df/df.ix[0,:]
	return df/df.ix[0,:]

def compute_daily_returns(df):
	daily_returns = df.copy()
	#daily_returns[1:] = (df[1:]/df[:-1].values) - 1
	daily_returns  = (df/df.shift(1)) - 1 # Alteranate Method
	daily_returns.iloc[0] = 0 # Set values at 0th row to zero
	return daily_returns

def get_rolling_mean(values,window):
	return pd.rolling_mean(values,window=window)

def get_rolling_std(values,window):
	return pd.rolling_std(values,window=window)

def get_bollinger_bands(rm,rstd):
	upper_band = rm + rstd*2
	lower_band = rm - rstd*2
	return upper_band,lower_band

if __name__ == "__main__":
	test_run()