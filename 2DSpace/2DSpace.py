# Prj: 2Dspace
# Author: Daniel Gisolfi
# Date: 2.13.17
# 2DSpace.py

from Tkinter import *

main = Tk()

def upKey(event):
	print('uppy')

def downKey(event):
	print "down key pressed"

def leftKey(event):
    print "Left key pressed"

def rightKey(event):
    print "Right key pressed"

frame = Frame(main, width=100, height=100)
#bind keys to there corosponding methods
main.bind('<Up>', upKey)
main.bind('<Down>', downKey)
main.bind('<Left>', leftKey)
main.bind('<Right>', rightKey)

#Pack Frame and call main
frame.pack()
main.mainloop()
		


