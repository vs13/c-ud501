import pandas as pd
import matplotlib.pyplot as plt 

def test_run():
	start_date = '26-Dec-14'
	end_date = '10-May-15'
	dates = pd.date_range(start_date,end_date)
	df = pd.DataFrame(index=dates)
	for symbol in ['aapl','googl','spy','amzn']:
		dftmp = pd.read_csv("{}.csv".format(symbol),index_col=0,parse_dates=True)
		dftmp = dftmp.rename(columns={'Open':symbol,'Close':symbol,'High':symbol,'Low':symbol,'Volume':symbol})
		df = df.join(dftmp,how="inner")
	print df

if __name__ == "__main__":
	test_run()