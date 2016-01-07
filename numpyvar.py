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
	print np.array([(2,3,4),(5,6,7)])
	print np.ones((5,4))
	print np.zeros((5,4))
	print np.ones((5,4) , dtype=np.int_)
	print np.random.random((5,4))
	print np.random.rand(5,4)
	print np.random.normal(size=(2,3)) #Mean 0 SD = 1 
	print np.random.normal(50,10,size=(2,3)) # Mean 50 SD = 10
	print np.random.randint(10)
	print np.random.randint(0,10)
	print np.random.randint(0,10,size=3)
	print np.random.randint(0,10,size=(2,3))
	a = np.random.randint(0,10,size=(2,3))
	print a.shape
	print a.shape[0]
	print a.shape[1]
	print a.size
	print a.dtype 

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