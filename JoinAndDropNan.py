import pandas as pd
import matplotlib.pyplot as plt 

def test_run():
	start_date = '26-Dec-14'
	end_date = '10-May-15'
	dates = pd.date_range(start_date,end_date)
	df = pd.DataFrame(index=dates)
	dfspy = pd.read_csv("spy.csv",index_col=0,parse_dates=True)
	df = df.join(dfspy)
	df = df.dropna()
	print df

if __name__ == "__main__":
	test_run()