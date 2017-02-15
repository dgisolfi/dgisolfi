# Prj: 2Dspace
# Author: Daniel Gisolfi
# Date: 2.13.17
# 2DSpace.py

from Tkinter import *

root = Tk()
root.title("2D Space")
root.wm_iconbitmap("spaceIcon.ico")
canvas = Canvas(root, width=300, height=200)
canvas.configure(background="black")

#create player object

canvas.create_rectangle(0,0,20,20, fill="white")



def move():
	x = 150
	y = 100
	canvas.create_rectangle(x,y,20,20, fill="white")
	root.update()


def quit(event):
	#quit program
	root.quit()

def upKey(event):
	print("uppy")
	move()

def downKey(event):
	print "down key pressed"

def leftKey(event):
    print "Left key pressed"

def rightKey(event):
    print "Right key pressed"

#frame = Frame(root, width=300, height=200)
#bind keys to there corosponding methods
root.bind("<q>", quit)
root.bind("<Up>", upKey)
root.bind("<Down>", downKey)
root.bind("<Left>", leftKey)
root.bind("<Right>", rightKey)



#canvas.create_rectangle(0,0,150,150, fill="yellow")



#Pack Frame and call root
#frame.pack()
canvas.pack()
root.mainloop()



def main():
	move()


