import pandas as pd 

def get_max_close(symbol):
	df = pd.read_csv("{}.csv".format(symbol))
	print df['Close'].max()

def test_run():
	for symbol in ['amzn','googl']:
		print "Max Close"
		print symbol,get_max_close(symbol)
	
if __name__ == "__main__":
	test_run()
