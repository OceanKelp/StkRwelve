# calculate technical idicators to plot
# plot stock data

from Moneyflow import HerbFlow
from PlotStk import plot
from Message import StatusMessage
import pandas as pd


def Process2(symbolin, dt_Pan):
  # setup
  Symbol = symbolin
  Per = .02   # bol per for uo & low band

# calculate technical idicators to plot
  dt_Pan['MA20'] = dt_Pan['Close'].rolling(window=20).mean()
  dt_Pan['MA50'] = dt_Pan['Close'].rolling(window=50).mean()
  dt_Pan['20dSTD'] = dt_Pan['Close'].rolling(window=20).std()
  dt_Pan['UpperBol'] =  dt_Pan['MA20'] + ( dt_Pan['20dSTD'] * 2)
  dt_Pan['LowerBol'] = dt_Pan['MA20'] - (dt_Pan['20dSTD'] * 2)
  dt_Pan['UpperminusPer'] =  dt_Pan['UpperBol'] -  dt_Pan['UpperBol'] * Per
  dt_Pan['lowerPlusPer'] =  dt_Pan['LowerBol']  + ( dt_Pan['LowerBol'] * Per )
  dt_Pan['difBol'] = dt_Pan['UpperBol'] - dt_Pan['LowerBol']

 # get message & score
  pointsgood = pointsbad = 0
  messagegood, messagebad,  pointsgood, pointsbad =  StatusMessage(dt_Pan , Symbol)
  score = pointsgood -pointsbad
  # make indicator tests
  message = Symbol +  '  Score = %d  '  %score + messagegood +  'pointsgood = %d  ' %pointsgood +   messagebad + ' Bad = %d  '  %pointsbad

  # calculate money flow
  MFResult = pd.DataFrame()

  print(Symbol,'  Score  ', score, '  ', message)
  if score > 20: #10:
    Days = 50
    # SmallDataPar  = dt_Pan[['Open','Close','High','Low','Volume']].copy()
    # print(dt_Pan)
    # length = len(SmallDataPar)
    # Dayreferance = length - Days # get lenhth to end
    # stockpricesxday = SmallDataPar[Dayreferance : length]
    # print(stockpricesxday )
    # #HerbFlow(Symbol,SmallDataPar)
    # HerbFlow(Symbol, stockpricesxday )
    # # length = len(dt_Pan)
    # # Dayreferance = length - Days # get lenhth to end
    # stockpricesxday = dt_Pan[Dayreferance : length]
    # #plot(dt_Pan, Symbol, message)
    # plot(stockpricesxday, Symbol, message)
    length = len(dt_Pan)
    Dayreferance = length - Days # get lenhth to end
    shortdf = dt_Pan[Dayreferance : length]
    HerbFlow(Symbol, shortdf )
    plot(shortdf, Symbol, message)
   
