# Prj: 2Dspace
# Author: Daniel Gisolfi
# Date: 2.13.17
# 2DSpace.py

from Tkinter import *
from random import*

root = Tk()
root.title("2D Space")
root.wm_iconbitmap("spaceIcon.ico")

canvas = Canvas(root, width=600, height=600)
canvas.configure(background="light blue")


def start():
	#||||||||||||||||||||||(x1,y1,x2,y2,)
	global player
	player = canvas.create_rectangle(290,290,310,310, fill="black")
	#mapRender()
start()

#create player object
def move(direct):
	global x, y
	x = 0
	y = 0
	if direct == "up":
		y += -20
	elif direct == "down":
		y += 20
	elif direct == "left":
		x += -20
	elif direct == "right":
		x += 20
	#print(x,y)
	canvas.move(player, x, y)
def shoot():
	pass

def mapRender():
	color = ["red", "orange", "yellow", "green", "blue", "violet", "gray", "firebrick", "dark turquoise"]
	global powerup
	#for i in range(25):
	x1 = random() * 580
	y1 = random() * 580
	x2 = x1 - 20
	y2 = y1 - 20

	powerup = canvas.create_rectangle(x1,y1,x2,y2, fill = choice(color))



def quit(event):
	#quit program
	root.quit()

def upKey(event):
	move("up")

def downKey(event):
	move("down")

def leftKey(event):
	move("left")

def rightKey(event):
	move("right")

def space(event):
	mapRender()

	#bind keys to there corosponding methods
root.bind("<q>", quit)
root.bind("<Up>", upKey)
root.bind("<Down>", downKey)
root.bind("<Left>", leftKey)
root.bind("<Right>", rightKey)
root.bind("<space>", space)

	#Pack canvas and call root
canvas.pack()
root.mainloop()





