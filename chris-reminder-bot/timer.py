# Prj: chris-reminder-bot
# Author: Daniel Gisolfi
# Date: 2.13.17
# timer.py

import time
run = raw_input("Start? > ")
mins = 0
# Only run if the user types in "start"
if run == "start":
    # Loop until we reach 20 minutes running
    while mins != 20:
        print ">>>>>>>>>>>>>>>>>>>>>", mins
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1
    # Bring up the dialog box here