# Prj: 2Dspace
# Author: Daniel Gisolfi
# Date: 2.13.17
# 2DSpace.py

from Tkinter import *

root = Tk()
root.title("2D Space")
root.wm_iconbitmap("spaceIcon.ico")

canvas = Canvas(root, width=600, height=600)
canvas.configure(background="light blue")


def start():
	#||||||||||||||||||||||(x1,y1,x2,y2,)
	global player
	player = canvas.create_rectangle(290,290,310,310, fill="black")
	


#create player object
def move(direct):
	x = 0
	y = 0
	if direct == "up":
		y = -20
	elif direct == "down":
		y = 20
	elif direct == "left":
		x = -20
	elif direct == "right":
		x = 20
	canvas.move(player, x, y)	

def gameLoop():
	
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

		#bind keys to there corosponding methods
	root.bind("<q>", quit)
	root.bind("<Up>", upKey)
	root.bind("<Down>", downKey)
	root.bind("<Left>", leftKey)
	root.bind("<Right>", rightKey)

	#Pack canvas and call root
	canvas.pack()
	root.mainloop()


def main():
	start()
	gameLoop()
main()




