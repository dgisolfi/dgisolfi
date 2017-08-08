from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def webhook():
    """Respond to incoming calls with a simple text message."""

    resp = MessagingResponse().message("Hello")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

def main():
	print()
	methodController()

def methodController():
	data = raw_input("User: ")
	conserve(data)


def conserve(data):
	bot = ChatBot("Piper", silence_performance_warning=True)
	bot.set_trainer(ChatterBotCorpusTrainer)
	bot.train('chatterbot.corpus.english')
	msg = bot.get_response(data)
	reply(msg)


def reply(msg):
	print("Piper: " + msg)

main()

https://www.twilio.com/docs/quickstart/python/sms/hello-monkey
