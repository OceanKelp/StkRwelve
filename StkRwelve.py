
# This where the magic happens. This is the main file that will be run to
# process the data.  It will call the other files as needed.
  
# Using the special variable 
# __name__



from threading import main_thread
from ImportFiles import importmylib
from UserList import RunUserList

if __name__ == "__main__":
      
    importmylib() # import needed libraries
    print('main')
    RunUserList() # get user list of stocks
    exit()

