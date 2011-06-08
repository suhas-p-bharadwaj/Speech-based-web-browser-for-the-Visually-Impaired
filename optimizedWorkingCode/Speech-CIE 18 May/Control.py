import time
import SpeechRecogTool
import speech
import time
from SpeechRecogTool import SpeechRecog
#from SpeechRecogTool1 import SpeechRecog1 #changed here 15/4/2011
from testRemove import removeHTMLtags
from summarize import SimpleSummarizer
from nltk.tokenize import *
from SpeechSynthesis import *
import Tkinter as tk
from Tkinter import *
from EventHandler import *

ttsEngine = TexttoSpeechEngine()
summFlag = 0

	

class SearchEngine(SpeechRecog): 

	
	def main():
		
		
		#Operations is the speech recognition engine
		speechRecog = SpeechRecog() 
		query = speechRecog.inputSpeech()
		
		print query
		ttsEngine.speakText("Returned query is " + query)
		speechRecog.searchQuery(query)
		ttsEngine.speakText("returned from second function!!!!")
		
		dict_hrefs = {}
		#To add the href functionality
		dict_hrefs = speechRecog.getHrefs()
		#print dict_hrefs
		
		
		#To remove the additional CSS, HTML and XML tags
		removeTags=removeHTMLtags()
		file=open("Bill.txt")
		html=file.read()
		file.close()
		print "***************************************"
		#print html
		#invalid_tags = ['p', 'i', 'u']
		#removeTags.strip_tags(html, invalid_tags)
		html = removeTags.StripTags(html)
		file=open("Bill.txt","w")
		file.write(html)
		file.close()
		print "***************************************"
		file=open('Bill.txt')
		txt=file.read()
		file.close()
		#print txt

		obj = SimpleSummarizer()
		newTxt = obj.summarize(txt,40)
		
		print "*******************************************"
	
		regExp=RegexpTokenizer('\w*;$')
		txtCleanUp=LineTokenizer().tokenize(newTxt)
		s=""
		a = ""
		for i in txtCleanUp:
			a=regExp.tokenize(i)
			if a:
				print a
			else:
				s = "" + i
		
		print s
		file1=open("newTxt.txt","w")
		file1.write(s)
		file1.close()	
		ttsEngine.speakText("The summarized contents are:  ")
		k = KeyEvents()
		k.speakAndListen(s)
		
		print 'done' 
		
	if __name__ == '__main__':
		main()
		

