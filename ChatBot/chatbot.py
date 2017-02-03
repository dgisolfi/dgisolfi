#Author: Daniel Gisolfi
#Date: 2/2/17
#chatbot.py
#Version 0.5

import os.path

def menu():
    #Welcome user and provide sys version
    print("Welcome to chatbot version 0.5!")

    global f
    #Provide file path, check if file exits
    if os.path.exists("/users/daniel/python/chatbot_settings.txt"):
        #if file exits read it
        f = open("chatbot_settings.txt", "r")
        f.read("chatbot_settings.txt", "r")

    else:
        print("file doesnt exit")
        #if it does not write a one
        f = open("chatbot_settings.txt","w+")
        # get name of chatbot from user
        botName = input("Enter a name for the bot:\n")
        # get name of user
        userName = input("Enter the name of the user:\n")
        #write botname
        f.write("botname = " + botName + "\n")
        #write userName
        f.write("userName = " + userName + "\n")

    #print("Hello " + userName + " I am " + botName)


def readInput():
    cmd = input("How Can I help you?\n")
    #"You can initialize a method by typing 'run' then the method name")
    methodController(cmd)

def methodController(cmd):
    if cmd in ["run settings"]:
        settings(cmd)

def settings(cmd):
    print("Settings:")
    f.read("chatbot_settings.txt", "r")


def chat(cmd):
    pass

def main():
    menu()
    readInput()
    f.close()

main()


