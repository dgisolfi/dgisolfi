from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

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
