#Author: Daniel Gisolfi
#Date: 8/9/17
#kayvan-chatbot
#Version 1

from twilio.rest import Client

account_sid = "AC2c6c007c9e84c808e82e8ed6e48bdce3"
auth_token = "5a443b9bf4a00a376d8a4588eef1d7f3"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="8452044105",from_="+18456704028", body="Test")

print(message.sid)