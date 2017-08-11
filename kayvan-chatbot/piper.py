#Author: Daniel Gisolfi
#Date: 8/9/17
#kayvan-chatbot
#Version 1




# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer

# def main():
# 	print()
# 	methodController()

# def methodController():
# 	data = raw_input("User: ")
# 	conserve(data)


# def conserve(data):
# 	bot = ChatBot("Piper", silence_performance_warning=True)
# 	bot.set_trainer(ChatterBotCorpusTrainer)
# 	bot.train('chatterbot.corpus.english')
# 	msg = bot.get_response(data)
# 	reply(msg)





from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

from twilio.rest import Client

app = Flask(__name__)

#get authentication sid from config vars	
account_sid = os.getenv('account_sid')
#get authentication token from config vars
auth_token = os.getenv('auth_token')
#chose wich cell phone number from the list to direct the message towards
my_cell = contacts[0]
#get twilio account number from config vars
my_twilio = os.getenv('my_twilio')

#run twilio function and pass in authentication info
client = Client(account_sid,auth_token)



@app.route("/", methods=['GET', 'POST'])

def webhook():
	from_number = request.values.get('From', None)
	msg = "Hey its piper, heroku server is working"
	message = client.api.account.messages.create(to= callers[from_number],from_=my_twilio, body=msg)
	print("Message Sent")
	return msg

if __name__ == "__main__":
	app.run(debug=True)
	




