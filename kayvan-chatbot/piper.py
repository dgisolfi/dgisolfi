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

callers = {
    "8452044105": "Daniel",
    "5166408305": "kayvan"
    
}

account_sid = "AC2c6c007c9e84c808e82e8ed6e48bdce3"
auth_token = "5a443b9bf4a00a376d8a4588eef1d7f3"
client = Client(account_sid, auth_token)


@app.route("/", methods=['GET', 'POST'])

def webhook():
	msg = "Hey its piper, heroku server is working"
	message = client.api.account.messages.create(to= callers[from_number],from_="+18456704028", body=msg)
	print("Message Sent")
#   print(message)
	return msg

if __name__ == "__main__":
	app.run(debug=True)
	




