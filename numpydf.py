import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
def test_run():
	start_date = '26-Dec-14'
	end_date = '10-May-15'
	dates = pd.date_range(start_date,end_date)
	df = pd.DataFrame(index=dates)
	for symbol in ['aapl','googl','spy','amzn']:
		dftmp = pd.read_csv("{}.csv".format(symbol),index_col=0,parse_dates=True)
		#dftmp = dftmp.rename(columns={'Open':symbol,'Close':symbol,'High':symbol,'Low':symbol,'Volume':symbol})
		dftmp.columns = ['Open'+symbol,'Close'+symbol,'High'+symbol,'Low'+symbol,'Volume'+symbol]
		df = df.join(dftmp,how="inner")
	#print df
	#plot_df(normalized_data(df.ix['2015-01-30':'2015-01-01',['Closeamzn','Closegoogl','Closeaapl']]))
	#Slice Rows
	dftest = df.ix['2015-01-30':'2015-01-01',['Closeamzn']]
	print dftest
	print np.array([2,3,4])

def plot_df(df,title="Stock Prices"):
	ax = df.plot(title=title)
	ax.set_xlabel("Date")
	ax.set_ylabel("Price")
	plt.show()

def normalized_data(df):
	print df/df.ix[0,:]
	return df/df.ix[0,:]

if __name__ == "__main__":
	test_run()