#Prj: MartySMS
#Author: Daniel Gisolfi
#Date: 2.6.17
#send_sms.py

from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_cell, my_twillio 
 
client = TwilioRestClient(account_sid, auth_token)

my_msg = "Hello, I`m Marty."
 
message = client.messages.create(to = my_cell, from_= my_twillio, body = my_msg)

