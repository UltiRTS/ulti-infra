#!/usr/bin/python

import threading
import os
import time


# Define a functions for a subserver thread
def updaterbackend(info, info2):
    os.system("python3 ./engineupdater/runserver.py")


def main():
    print("=Check Server Integrity=")

    #Integrity check for updater backends
    new_release_path = "/opt/infra/newrelease/"

    if (os.path.exists(new_release_path) and
        os.access(new_release_path, os.R_OK|os.W_OK)):

        print("=Spawning Subservers=")
        try:
            #launch updater backend
            thr = threading.Thread(target=updaterbackend, args=(0, 0, ) )
            thr.start()
        except Exception as e:
            print("Error: unable to start updater server backend: ", e)
            while 1:
                time.sleep( 5 )
    else:
        err_msg =  ("Error: directory '{0}' does not exist or is not accessible\n"
                    "Run this command as normal user\n"
                    "\tsudo mkdir -p {0} ; sudo chown `whoami`:`whoami` {0}")
        err_msg = err_msg.format(new_release_path)
        print(err_msg)


# Threads for subserver process
if __name__== "__main__":
    main()
