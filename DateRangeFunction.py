import pandas as pd
import matplotlib.pyplot as plt 

def test_run():
	start_date = '26-Dec-14'
	end_date = '10-May-15'
	dates = pd.date_range(start_date,end_date)
	print dates

if __name__ == "__main__":
	test_run()