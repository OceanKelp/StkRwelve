# get file from user driv#e and returns a sring of symbols
import pandas as pd
def GetUserList():
  # read file from user
  #userfile = pd.read_csv("C:\\Users\herb\VS23\StockTwelve\symbolsSmall.csv") # No header
  userfile = pd.read_csv("C:\\Users\herb\VS23\StockTwelve\ABC.csv")
  #print('userfile')
  stksym = userfile['Symbol'].tolist()
  #print(stksym)
  return(stksym)


