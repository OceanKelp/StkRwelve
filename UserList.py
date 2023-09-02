#Run wihh user list

from GetUserFile import GetUserList
from GetBatchData import GetBatchData
from Parse import Parse
from Process2 import Process2

def RunUserList():
    SYMRtnx = GetUserList()                    # get user list & user key fix data
    # pass list to get history data
    DataAll = GetBatchData(SYMRtnx)   # get the batch data back
    
    # loop thru each symbol
    for SymX in SYMRtnx:
        print('SymX2',SymX)
        Smalldf = Parse(DataAll[SymX] )   # set up small dateframe
        Process2( SymX, Smalldf)
    return(print('user list done') )
