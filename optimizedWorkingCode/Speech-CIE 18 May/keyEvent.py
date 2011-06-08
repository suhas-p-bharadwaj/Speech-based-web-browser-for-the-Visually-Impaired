import Tkinter as tk
from Tkinter import *


root = tk.Tk()

def keypress(event):
	print event.keysym
	print event.char
	if event.keysym == 'Escape':
		root.destroy()

class keyEventHandler:

		
	def main():
		root.bind_all('<Key>', keypress)
		# don't show the tk window
		root.withdraw()
		root.mainloop()
		print 'Out of event handler'
		
	if __name__ == '__main__':
		main()
	