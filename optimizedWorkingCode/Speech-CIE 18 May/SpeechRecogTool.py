import speech		#Speech Library : Wrapper for MS Speech
import time
from xgoogle.search import GoogleSearch, SearchError
from BeautifulSoup import BeautifulSoup
import urllib2
import re
from SpeechSynthesis import *


	
class SpeechRecog:
	
	listener = None								#To listen to speech input from user
	href = {}
	ttsEngine = TexttoSpeechEngine()			#Text to speech engine
	
	#Callback function for listening to speech input
	def callback(self, phrase, listener):
		if ((phrase == "Stop") or (phrase == "STOP") or (phrase == "stop")):
			listener.stoplistening()
			
			
		self.ttsEngine.speakText(phrase)
	
	#Constructor	
	def __init__(self):
		listener = speech.listenforanything(self.callback)
	
	
	#Take query from user
	def inputSpeech(self):
		file = open("Bill.txt","w");
		
		#Variables to store recognized contents
		response = "NO"
		response1 = "Google"
		
		#Give instructions
		self.ttsEngine.speakTextSync("Getting ready to take search query")
		self.ttsEngine.speakText("Please say Yes if query is recognized")
		self.ttsEngine.speakText("Please say No if you want to re enter the query")
		
		
		#Until the desired query is recognized
		while((response == "NO") or (response == "No") or (response == "no")):
			
			self.ttsEngine.speakTextSync("Search Query?")
			response1 = speech.input("Say something, please.")						#speech.input() : Blocking call. Recognizes speech
			
			self.ttsEngine.speakTextSync("You said " + response1)
			print response1
			
			self.ttsEngine.speakText("Is this what you said?")
			response = speech.input("Please say yes or no")
			
			self.ttsEngine.stopSpeak()
			response=str(response)	
			print response
			
		#Return the recognized query					
		return response1
		
	def setHrefs(self,href_lst):
		
		self.href = href_lst 
		
		
	def getHrefs(self):
		return self.href	
	

	#Retrieve links and select a particular link	
	def searchQuery(self,query):
		try:
			
			
			gs = GoogleSearch(query)
			gs.results_per_page = 50
			results = gs.get_results()
			queryFlag = 0
			url = ""
			self.ttsEngine.speakText("Your results are:")
	  
			i = 0
			self.ttsEngine.speakTextSync("Pronounce Yes for selecting the link when it is read out. Pronounce No to move to next link.Pronounce back to move to previous link")
			previousFlag = 0
			
			#Iterate through the obtained results
			while i < len(results): 
				res = results[i]
				print "\n"
				print "Result number" 
				print i + 1
				print "Title:"
				print res.title.encode("utf8")
				print "***************************************"
				print "Description: "
				print "***************************************"
				print res.desc.encode("utf8")
				print "Link is: "
				print "***************************************"
				print res.url.encode("utf8")
				print "***************************************"
				print "\n"
				print "\n"
				j = str(i)
				
				
				#Read out the title and description corresponding to the ith link
				self.ttsEngine.speakText(j + res.title.encode("utf8") + ". And the corresponding description is: " + res.desc.encode("utf-8") + "Is this option good?")
				
				#Wait for the text-to-speech engine to start speaking
				time.sleep(3)
				queryFlag = 0
				
				#Wait until a speech command is given by user
				while self.ttsEngine.isSpeaking():
					response3 = speech.input()
					print response3
					response3 = str(response3)
					print type(response3)
					print len(response3)
					
					#if yes, link is selected
					if ((response3 == "Yes") or (response3 == "YES") or (response3 == "yes") or (response3 == "As") or (response3 == "as")):
						self.ttsEngine.stopSpeak()
						url = res.url
						queryFlag = 1
						break
					#If previous, move to the previous link	
					elif response3 == "previous" or response3 == "Previous" or response3 == "PREVIOUS" or response3 == "back" or response3 == "Back" or response3 == "BACK":
						previousFlag = 1
						self.ttsEngine.stopSpeak()
						break
					#Else move to next link	
					else:
						self.ttsEngine.stopSpeak()
						break
				
				if queryFlag == 1:
					break
					
				if previousFlag == 1:
					previousFlag = 0
					if i == 0:
						i = 0
					else:
						i = i - 1
					continue
				
				i = i + 1
				
			return url
		
		except SearchError, e:
			print "Search failed: %s" % e
			
		
		return	
	
		
	


	



	