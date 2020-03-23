#!/usr/bin/python

import thread
import os
import time

# Define a functions for a subserver thread
def updaterbackend(info,info):
   os.system("python3 ./engineupdater/runserver.py")

# Threads for subserver process
if __name__== "__main__":
   print("=Check Server Integrity=")
   
   if !os.path.exists("/opt/infra/newrelease/"):    #Integrity check for updater backends
      os.system("mkdir /opt/infra/newrelease")
   
   print("=Spawning Subservers=") 
   try:
      thread.start_new_thread( updaterbackend, (0, 0, ) ) #launch updater backend
   except:
      print "Error: unable to start updater server backend"
   while 1:
      time.sleep( 5 )
