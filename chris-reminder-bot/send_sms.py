# Prj: chris-reminder-bot
# Author: Daniel Gisolfi
# Date: 2.6.17
# send_sms.py

#import all twilio dependencies
from twilio.rest import TwilioRestClient
#import crednetials from seperate module
from credentials import account_sid, auth_token, my_cell, my_twilio
#import time and random modules
import time, random

#a list of possible messages that can be sent to users
messages = ["Chris get your fucking shit together and get them grades boi!",
			"Chris do your homework or go to the gym you fat fuck!",
			"Chris for fucks sake STUDY!",
			"I am Marty, do your homework or I will hack you biotch!",
			"Christopherrrrrrrrr, get your shit together",
			"-_- study",
			"please study sirrr",
			"boi....do ya work",
			"Matt is a bootch do your work",
			"CHRISTOPHER DO UR WURK"]

def reminder():
	#run twilio function and pass in authentication info
	client = TwilioRestClient(account_sid,auth_token)
	#create infinite loop
	while True:
		#pick a random message from 'messages' list
		my_msg = random.choice(messages)
		#send a sms from twilio number to cell with my_msg as text
		message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
		#print a conformation that the task has completed as well as what my_msg was
		print("The following reminder successfully sent to Christopher Macaroni\n" + my_msg + "\n")

		#set the fucntion to sleep for 24hrs then run again, and loop
		print "Start : %s" % time.ctime()
		time.sleep(3600)
		print "End : %s" % time.ctime()
		

reminder()