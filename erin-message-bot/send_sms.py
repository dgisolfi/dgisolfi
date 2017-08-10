# Prj: ErinMessageBot
# Author: Daniel Gisolfi
# Date: 5.8.17
# send_sms.py

#import all twilio dependencies
from twilio.rest import Client
#import crednetials from seperate module
from credentials import account_sid, auth_token, my_cell, my_twilio
#import time and random modules
import time, random
from random import randint

from erinMessages import messages

def reminder():
	#run twilio function and pass in authentication info
	client = Client(account_sid,auth_token)
	#create  loop
	while True:
		#pick a random message from 'messages' list
		my_msg = random.choice(messages)#"Hey Erin! My name is Marty, as a paret of Daniel`s on going effort to make me bigger and better, he has added a erin-message-bot function to my code. From now on every once and a while I will remind you how great and wonderful you are!"#random.choice(messages)
		#send a sms from twilio number to cell with my_msg as text
		message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
		#print a conformation that the task has completed as well as what my_msg was
		print("Message sent to Erin Gisolfi, Hours until next message:")

		waitTime = randint(3600,28800)
		print(waitTime/60/60)


		#set the fucntion to sleep for 24hrs then run again, and loop
		print "Start : %s" % time.ctime()
		time.sleep(waitTime)
		print "End : %s" % time.ctime()
		

reminder()