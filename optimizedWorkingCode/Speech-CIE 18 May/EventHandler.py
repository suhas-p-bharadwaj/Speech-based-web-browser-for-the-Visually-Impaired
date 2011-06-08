import Tkinter as tk
from Tkinter import *
from SpeechSynthesis import *
import msvcrt


class KeyEvents:

	def __init__(self):
		self.tts = TexttoSpeechEngine()
		
	# def keypress(self,event):
		# print event.keysym
		# if event.keysym == 'Escape':
			# self.root.destroy()
			# self.ttsEngine.stopSpeak()
		# if event.keysym == 'Right':
			# self.ttsEngine.next()
			
	# def listenforEvents(self):
		# self.root = tk.Tk()
		# print "Press a key (Escape key to exit):"
		# self.root.bind_all('<<Key>>', self.keypress)
		# #self.root.withdraw()
		# self.root.mainloop()
	
	def keypress(self):
		
		while True:
			
			key = msvcrt.getch()
			key1 = ""
			if key == u'\xe0'.encode('latin-1'):
				key1 = msvcrt.getch()
			
			
			print "Key:" + key + key1
			
			key = key + key1
			
			if key == u'\xe0M'.encode('latin-1'):
				print 'Right'
				self.tts.next()
			if key == u'\xe0K'.encode('latin-1'):
				print 'Left'
				self.tts.previous()
			if key == 'h':
				print 'Hello'
			if key == 'e':
				self.tts.stopSpeak()
				break;
		

	def speakAndListen(self,spkTxt):
		
		#txt = '''India, conventional long name Republic of India, is a country in South Asia. It is the seventh-largest country by geographical area, the second-most populous country with over 1.2 billion people, and the most populous democracy in the world. Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west; Bhutan, the People's Republic of China and Nepal to the northeast; and Bangladesh and Burma to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; in addition, India's Andaman and Nicobar Islands share a maritime border with Thailand and Indonesia.'''
		txt = spkTxt
		self.tts.speakText(txt)
		print 'After speak'
		#k = KeyEvents(tts)
		print 'After k'
		self.keypress()
		print 'After listen'
	
