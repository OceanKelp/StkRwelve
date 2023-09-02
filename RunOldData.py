#Run all with old data
#read old data
import pandas as pd
from Parse import Parse
from Process2 import Process2
from io import StringIO
#olddf = readcsv('/content/LastRun.csv')

data = pd.read_csv('/content/LastRun.csv')
#read symbol contents of csv file
symfile = pd.read_csv("/content/YourSymbols.csv")

#x = symfile['Symbol']
#run each symbol
# for x in symfile:
#   print(Symbol)
  # Smalldf = Parse(olddf[s] )   # set up small dateframe
  # Process2( s, Smalldf)
# lines = data.strip().split("\n")

# for line in lines:
#     _, symbol = line.split()
#     print(symbol)
# for _, symbol in df.iterrows():
#     print(symbol.iloc[1])

stklist = symfile['Symbol'].tolist()
print(stklist)
for x in stklist:
   Smalldf = Parse(olddf[x] )   # set up small dateframe
  # Process2( x, Smalldf)
 # print(data)
