# Prj: erin-message-bot
# Author: Daniel Gisolfi
# Date: 8.11.17
# send_sms.py

#import all twilio dependencies
from twilio.rest import Client
#import time and random modules
import time, random
from random import randint
#import module with possible messages
from erinMessages import messages
import os, sys, json


def reminder():

	#list of numbers to send messages to
	contacts = [
		8452044105,#daniel
		8452402529#Erin
	]
	
	#get authentication sid from config vars	
	account_sid = os.getenv('account_sid')
	#get authentication token from config vars
	auth_token = os.getenv('auth_token')
	#chose wich cell phone number from the list to direct the message towards
	my_cell = contacts[1]
	#get twilio account number from config vars
	my_twilio = os.getenv('my_twilio')

	#run twilio function and pass in authentication info
	client = Client(account_sid,auth_token)

	#create  loop
	while True:
		#pick a random message from 'messages' list
		my_msg = random.choice(messages)
		#send a sms from twilio number to cell with my_msg as text
		message = client.api.account.messages.create(to=my_cell, from_=my_twilio, body=my_msg)
		#print a conformation that the task has completed
		print("Message sent to Erin Gisolfi, Hours until next message:")

		#create a random interval of time between 1 - 8 hours
		waitTime = randint(10800,43200)
		#print aprox how many hours the function will sleep
		print(waitTime/60/60)


		#set the fucntion to sleep for x amount of time then run again, and loop
		print("Start : %s" % time.ctime())
		# print("Start")
		time.sleep(waitTime)
		# print("End")
		print("End : %s" % time.ctime())
		

reminder()