#Author: Daniel Gisolfi
#Date: 6/11/17
#kayvan-chatbot
#Version 1




from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# from flask import Flask, request, redirect
# from twilio.twiml.messaging_response import MessagingResponse

# app = Flask(__name__)

# @app.route("/", methods=['GET', 'POST'])
# def webhook():
#     """Respond to incoming calls with a simple text message."""

#     resp = MessagingResponse().message("Hello")
#     return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)

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





from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

callers = {
    "8452044105": "Daniel",
    "5166408305": "kayvan"
    
}

@app.route("/", methods=['GET', 'POST'])
def reply():
    """Respond and greet the caller by name."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        message = "Hey" callers[from_number] + ", my name is Piper! I`m a bot created by Daniel, I live in a server on the internet:)"
    else:
        message = "I dont know you -_- go away."

    resp = MessagingResponse()
    resp.message(message)
    print(message)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)