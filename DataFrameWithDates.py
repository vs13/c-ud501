import pandas as pd
import matplotlib.pyplot as plt 

def test_run():
	start_date = '26-Dec-14'
	end_date = '10-May-15'
	dates = pd.date_range(start_date,end_date)
	df = pd.DataFrame(index=dates)
	print df

if __name__ == "__main__":
	test_run()