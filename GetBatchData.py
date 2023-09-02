
from datetime import timedelta
from datetime import date
import yfinance  as yf
from yfinance import download
import pandas as pd

def GetBatchData(symlist):
 # need this input
  #ticker_list = ['C','AAPL','ABT','ADSK','AI','ALB']
  tickers = symlist
  # todaya date and 210 days  ago

  end_date = date.today()
  start_date = end_date - timedelta(days=365)
  # Here we use yf.download function
  #Make sure to provide the dates in the "YYYY-MM-DD" format. For example, "2023-01-01" for January 1, 2023.
  data = yf.download(tickers,  threads=True, start=start_date, end=end_date, group_by='ticker',)
  df = pd.DataFrame
  df =data
# Export the DataFrame to a CSV file without repeating column names
  df.to_csv('LastRun.csv', index=False)

  #data.to_csv("LastRun.csv" )
  return(data)

