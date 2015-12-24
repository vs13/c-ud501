import pandas as pd 

def test_run():
	df = pd.read_csv("amzn.csv")
	print df.tail()

if __name__ == "__main__":
	test_run()
