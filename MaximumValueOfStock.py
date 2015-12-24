import pandas as pd 

def get_max_close(symbol):
	df = pd.read_csv("{}.csv".format(symbol))
	print df['Close'].max()

def test_run():
	get_max_close('amzn')
	
if __name__ == "__main__":
	test_run()
