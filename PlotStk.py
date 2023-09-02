
import matplotlib.pyplot as plt

def plot(SP, sym_in, commentin): #Datalist symbol  comment

  SP[['Close','MA20','UpperBol','LowerBol','MA50','UpperminusPer' , 'lowerPlusPer' ]].plot(figsize=(25,8))
  plt.grid(True)
  plt.title(sym_in + '\n' + commentin)
  plt.axis('tight')
  plt.ylabel('Price');
  plt.show()
  return()
