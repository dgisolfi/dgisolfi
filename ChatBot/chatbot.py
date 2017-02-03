#Author: Daniel Gisolfi
#Date: 9/15/16
#SimpleAI
#!/usr/bin/python

copyright = 'My name is Marty. I am a Basic Hard Coded A.I. or chatbox created by Daniel\nCopyright (c) 2016 Daniel Gisolfi, Daniel.Gisolfi1@marist.edu'

def marty():
       sysName = 'Marty'
       username = input('What is the users name: \n>>>')
       print('Hello my name is Marty,')

       while True:
              userinput = input('How can I help you ' + username + '? \n>>>')
              userinput = userinput.lower()

              if userinput in ['hi','hello','hiya','ciao']:
                     print('hello',username)
              elif userinput in ['how are you?','how are you']:
                     import random
                     sysmood = ''
                     num = random.sample([1,2,3], 1)
                     if num == [1]:
                            sysmood = 'Well'
                     elif num == [2]:
                            sysmood = 'Tired'
                     elif num == [3]:
                            sysmood = 'Mad'
                     print(sysmood,', how are you?')
              elif userinput in ['what is your name', 'what is your name?','whats your name','what`s your name','name','what is my name?','what is my name', 'whats my name?','whats my name']:
                     print('My name is ' + sysName + '\nYour name is ' + username)
                     print()
              elif userinput in ['admin', 'settings','sys','system settings','system']:
                            def sys():
                                   while True:
                                          print('welcome to',sysName, 'system settings')
                                          userinput = input('Enter a subgroup of settings: \nName\nAbout\n>>>')
                                          userinput = userinput.lower()
                                          if userinput == 'name':
                                                 userinput = input('Type "sysname" to change the the name of the AI or "user" \nto change the name of the user: \n>>>')
                                                 if userinput in ['sysname']:
                                                        sysName = input('What is the systems name: \n>>>')
                                                        print('The system`s name has been changed to', sysName)
                                                        print()
                                                        break
                                                 elif userinput in ['user']:
                                                        username = input('What is the users name: \n>>>')
                                                        print('The user`s name has been changed to', username)
                                                        print()
                                                        break
                                                 elif userinput in ['quit','end','stop']:
                                                        break 
                                                 else:
                                                        print('That is not a valid command')
                                                        continue
                                          elif userinput in ['about','copyright']:
                                                 print(copyright)
                                                 print()
                                          
                            sys()
              elif userinput in ['how much change do I have', 'run change.py','change.py']:
                     def change():
                            print("change counter")
                            print()
                            print("please enter the count of each coin type")
                            quaters = int(input("quaters:  "))
                            dimes = int(input("dimes:  "))
                            nickles = int(input("nickles:  "))
                            pennies = int(input("pennies:  "))
                            total = quaters * .25 + dimes * .10 + nickles * .05 + pennies * .01
                            print()
                            print("the total value of your change is", total)

                     change()
                     continue
              elif userinput in ['run math','hep me with this math','math']:
                     def math():
                            while True:
                                   userinput = input('Enter a math operation: \n>>>')
                                   userinput = userinput.lower()
                                   print(eval(userinput))
                                   if userinput in ['exit math', 'quit','quit math']:
                                          break
                     math()
              elif userinput in ['temp','convert temp', 'run temp', 'run convert.py']:
                     def tempconvert():
                            celsius = eval(input('what is the celsius tempreature?: \n>>>'))
                            fahrenheit = 9/5 * celsius + 32
                            print('the temprature is', fahrenheit, 'degrees fahrenheit')

                     tempconvert()
              elif userinput in ['haiku', 'run haiku','write a haiku', 'tell a haiku']:
                     def haiku():
                            from random import randint

                            wordList1 = ["Enchanting", "Amazing", "Colourful", "Delightful", "Delicate"]
                            wordList2 = ["visions", "distance", "conscience", "process", "chaos"]
                            wordList3 = ["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"]
                            wordList4 = ["true", "dark", "cold", "warm", "great","wonderful", "frigid"]
                            wordList5 = ["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]
                            wordList6 = ["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]
                            wordList7 = ["inspiration", "imagination", "wisdom", "thoughts"]
                     
                            wordIndex1=randint(0, len(wordList1)-1)
                            wordIndex2=randint(0, len(wordList2)-1)
                            wordIndex3=randint(0, len(wordList3)-1)
                            wordIndex4=randint(0, len(wordList4)-1)
                            wordIndex5=randint(0, len(wordList5)-1)
                            wordIndex6=randint(0, len(wordList6)-1)
                            wordIndex7=randint(0, len(wordList7)-1)

                            haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",\n" 
                            haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",\n"
                            haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + "."

                            print(haiku)
                            print()
                     haiku()
              elif userinput in ['game','games','play a game']:
                     while True:
                            userinput = input('What game would you like to play? \nTextGame\nPong\n>>>')
                            userinput = userinput.lower()
                            if userinput in['textgame','run textgame', 'run textgame.py']:
                                   #Into to programing
                                   #Author: Daniel Gisolfi
                                   #Date: 9/22/16
                                   #TextGame.py
                                   #Version 0.3

                                   def game():
                                       #Start Game
                                       ##Game Settings
                                       title = "The Abandoned Lab:"
                                       print(title)
                                       playername = input("Enter the name of your player: ")
                                       backstory = playername + (" has arrived at a large metal door\n"
                                                    "leading to an abandoned Computer labratory, explore"
                                                    "\ninside to discover new technology")
                                       score = int(0)
                                       ##Game Locations   
                                       
                                       labentrance = "You are at the Lab entrance"
                                       servicedesk =  "You are at the Service Desk"
                                       powercenter = "You are at the Power Center"
                                       computerlab = "You are in the Computer Lab"
                                       datacenter =  "You are in the Data Center"
                                       

                                       ###Locations Visited
                                       labentranceVisited = True
                                       servicedeskVisted = False
                                       computerlabVisted = False
                                       datacenterVisted = False
                                       powercenterVisited = False
                                           
                                       #Game Start
                                       playerlocation = labentrance
                                       
                                       print()
                                       print(backstory)
                                       print()
                                       print(playerlocation)

                                       #Game loop
                                       while True:
                                           userinput = input("Which direction would you like to go?: \n")
                                           userinput = userinput.lower()

                                           if userinput == "north":
                                               if playerlocation == labentrance:
                                                   playerlocation = servicedesk
                                                   if servicedeskVisted == False:
                                                       score = score + 5
                                                       servicedeskVisted = True

                                               elif playerlocation == servicedesk:
                                                   print("there is a wall there")

                                               elif playerlocation == powercenter:
                                                   print("there is a wall there")

                                               elif playerlocation == computerlab:
                                                   playerlocation = datacenter
                                                   if datacenterVisted == False:
                                                       score = score + 5
                                                       datacenterVisted = True
                                                   break
                                               elif playerlocation == datacenter:
                                                   print("there is a wall there")
                                           elif userinput == "south":
                                               
                                               if playerlocation == labentrance:
                                                   print("there is a wall there")

                                               elif playerlocation == servicedesk:
                                                   playerlocation = labentrance
                                                   if labentranceVisited == False:
                                                       score = score + 5
                                                       labentranceVisited = True

                                               elif playerlocation == powercenter:
                                                   print("there is a wall there")
                                                   
                                               elif playerlocation == computerlab:
                                                   print("there is a wall there")
                                          
                                               elif playerlocation == datacenter:
                                                   playerlocation = computerlab
                                                   if computerlabVisted == False:
                                                       score = score + 5
                                                       computerlabVisted = True

                                           elif userinput == "east":

                                               if playerlocation == labentrance:
                                                   print("there is a wall there")
                                                   
                                               elif playerlocation == servicedesk:
                                                   playerlocation = computerlab
                                                   if computerlabVisted == False:
                                                       score = score + 5
                                                       computerlabVisted = True

                                               elif playerlocation == powercenter:
                                                   playerlocation = servicedesk
                                                   if servicedeskVisted == False:
                                                       score = score + 5
                                                       servicedeskVisted = True

                                               elif playerlocation == computerlab:
                                                   print("there is a wall there")
                                               
                                               elif playerlocation == datacenter:
                                                   print("there is a wall there")
                                                   
                                           elif userinput == "west":

                                               if playerlocation == labentrance:
                                                   print("there is a wall there")
                                                   
                                               elif playerlocation == servicedesk:
                                                   playerlocation = powercenter
                                                   if powercenterVisited == False:
                                                       score = score + 5
                                                       powercenterVisited = True

                                               elif playerlocation == powercenter:
                                                   print("there is a wall there")
                                                   
                                               elif playerlocation == computerlab:
                                                   print("there is a wall there")
                                               
                                               elif playerlocation == datacenter:
                                                   print("there is a wall there")

                                           elif userinput == "help":
                                               print("This is a list of vaid commands:"
                                                     "\nnorth"
                                                     "\nsouth"
                                                     "\neast"
                                                     "\nwest"
                                                     "\nhelp"
                                                     "\nquit\n")
                                           
                                           elif userinput == "quit":
                                               break
                                           else:
                                               print("that is not a valid command")
                                               
                                           print()
                                           print(playerlocation)
                                           print("score = ",score)
                                           
                                       #End Game
                                       conclusion = "Congratulations " + playername + ", you found the data center and new technology inside"
                                       copyright = "Copyright (c) 2016 Daniel Gisolfi, Daniel.Gisolfi1@marist.edu"
                                       print()
                                       print(conclusion)
                                       print(copyright)

                                   game()
                            elif userinput in ['pong']:
                                   break

              elif userinput in ['help','list functions','what can you help me with?', 'what can you help me with']:
                     def help():
                            functions = ['hi', 'how are you?', 'what is your name', 'system', 'run change.py', 'run math', 'run convert.py', 'haiku','game', 'quit']
                            print('The following are a list of valid commands: ')
                            print('\n'.join(functions))
                            print()
                     help()
              elif userinput in ['quit','end','stop']:
                     break
              else:
                     print("I did not understand what you said")
                     
                     
marty()