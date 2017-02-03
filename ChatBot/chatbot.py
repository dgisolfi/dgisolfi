#Author: Daniel Gisolfi
#Date: 2/2/17
#chatbot.py
#Version 0.5

import os.path

def startup():
    #Welcome user and provide sys version
    print("Welcome to chatbot version 0.5!")

    #Provide file path, check if file exits
    if os.path.exists("/users/daniel/dgisolfi/ChatBot/chatbot_settings.txt"):
        #if file exits read it
        f = open("chatbot_settings.txt", "r")
        lines = f.readlines()
        #read line 1
        botName = lines[0]
        #read line 2
        userName = lines[1]
        #f.close()

    else:
        #if it does not write a one
        f = open("chatbot_settings.txt","w+")
        # get name of chatbot from user
        botName = input("Enter a name for the bot:\n")
        # get name of user
        userName = input("Enter the name of the user:\n")
        #write botname
        f.writelines(botName + "\n")
        #write userName
        f.writelines(userName+ "\n")
        #f.close()

    menu(botName,userName)

def menu(botName, userName):
    print("Hello " + userName + " I am " + botName)

def readInput():
    cmd = input("How Can I help you?\n")
    #"You can initialize a method by typing 'run' then the method name")
    methodController(cmd)

def methodController(cmd):
    if cmd in ["run settings"]:
        settings(cmd)

def settings(cmd):
    print("Settings:")
    f.read()


def chat(cmd):
    pass

def main():
    startup()
    readInput()

main()


