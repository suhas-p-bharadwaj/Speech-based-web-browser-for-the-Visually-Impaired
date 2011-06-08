from sampleAnchors import getAnchors
from nltk import *
import nltk.data
import re
import speech
import pyTTS
import urllib2
import winsound
import time
import msvcrt

class navigateLinks:
	
	#Reads the summary and performs actions depending on the user command
	#Input : summary, keyDictionary, AnchorDictionary
	def addKeys(self, summ_text, key_dict ,anc_dict):
	
		
		key_dict_name = key_dict
		print key_dict_name
		anc_dict_name=anc_dict
		
		
		#Tokenizer : Tokenizes based on values like key1, key2, key24, key 545 etc
		tok=RegexpTokenizer('^ *key[0-9]{1,3}')
		key_list=[]
		
		#Text to speech engine instance
		tts = pyTTS.Create()
		flag=0
		
		tts.Speak("While reading summary. Press Right arrow key for fast forward. Press Left Arrow key for Rewind. Press SPACE key to navigate to link.")
		tts.Speak("Every link is preceded by a beep")
		
		#Flags for fast forward and rewind while reading summary
		nextFlag = 0
		prevFlag = 0
		lastLink = ""
		title = ""
		url = ""
		linkKey = ""
		navLink = 0
		nextSentence = 0
		prevSentence = 0
		
		#Sound file : played to recognize a link
		soundFileName = "chime.wav"
		
		#Tokeinze sentences
		sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		
		sent_list = sent_detector.tokenize(summ_text.strip())
		print sent_list
		
		len_sent_list = len(sent_list)
		len_sentences = 0
		cur_loop = -1
		#for sent in sent_list:
		print "TOTAL LEN IS: " + str(len_sent_list)
		
		#Iterate through sentences
		while (len_sentences < len_sent_list):
		
			cur_loop = cur_loop + 1
			
			if navLink == 1 and url != "":
				print "breaking from while loop..."
				break
				
			else: 
				navLink = 0
			
			
			if (cur_loop!=0 and not nextSentence and not prevSentence):
				print 'In cur loop'
				len_sentences = len_sentences + 1
				
			if (len_sentences == len_sent_list):
				break	
				
			print "CURRENT LEN IS: " +  str(len_sentences)
			
			sent = sent_list[len_sentences]
			
			l=re.split(r"(\s*key[0-9]{1,3})",sent)	
			tok=RegexpTokenizer('^ *key[0-9]{1,3}')
			
			
			prevSentence = 0
			nextSentence = 0
			
			
			for i in l:
				res = tok.tokenize(i)
				#If not link, read the sentence and listen for keypress events for fast forward and rewind
				if not res:		
					print "in loop 1"
					flag=0
					
					#Speak asynchronous
					tts.Speak(i,pyTTS.tts_async)
					time.sleep(0.3)
					
					#While it is speaking, wait for key press commands
					while tts.IsSpeaking():
						if msvcrt.kbhit():
							key = msvcrt.getch()
							
							#Recognize SPACE keypress
							if (ord(key)==32):
								print "space 1 "
								flag=1
								tts.Stop()
								break
							key1 = ""
							
							#Recognize RIGHT ARROW keypress
							if key == u'\xe0'.encode('latin-1'):
								key1 = msvcrt.getch()
								key = key + key1
							if key == u'\xe0M'.encode('latin-1'):
								nextSentence = 1
								print 'Right:if'
								tts.Stop()
								break
							#Recognize LEFT ARROW keypress	
							if key == u'\xe0K'.encode('latin-1'):
								print 'Left:if'
								prevSentence = 1
								tts.Stop()
								break
				
								
				#Read the link	
				else:
					
					print "in loop 2"
					flag = 0
					key_dict_name = key_dict
					linkKey = i
					i = ' '.join(i.split())
					key = i
					key_list.append(key)
					sx = str(key_dict_name[key])		
					print "sx is:" + str(sx)
					
					#Play the beep sound before the link is read out					
					winsound.PlaySound(soundFileName,winsound.SND_FILENAME)
					
					#Speak asynchronous
					tts.Speak(sx,pyTTS.tts_async)
					time.sleep(0.2)
					
					#While speaking recognize keypress commands
					while tts.IsSpeaking():
						if msvcrt.kbhit():
							key = msvcrt.getch()
							if (ord(key)==32):
								print "space 2"
								tts.Stop()
								flag = 2
								break
								
							key1 = ""
							if key == u'\xe0'.encode('latin-1'):
								key1 = msvcrt.getch()
								key = key + key1
							if key == u'\xe0M'.encode('latin-1'):
								print 'Right:else'
								nextSentence = 1
								tts.Stop()
								break
								
							if key == u'\xe0K'.encode('latin-1'):
								print 'Left:else'
								prevSentence = 1
								tts.Stop()
								break
								
							if key == 'e':
								print 'e'
								
				
				
				#SPACE keypress : To navigate to link		
				if flag == 1 or flag == 2:
					navigateLinks1 = navigateLinks()
					
					#Checks if the link exists in dictionary
					title,url = navigateLinks1.checkcondition(flag,key_list,key_dict_name,anc_dict_name)
					navLink = 1
					print "title is: " + str(title)
					print "link is: " + str(url)
					print "breaking from flag loop..."
					break
				
				
					
				#Set the sentence length parameter to go to next or previous depending upon the flag				
				if (nextSentence or prevSentence):
					if(prevSentence):
						
						if len_sentences > 0:
							len_sentences = len_sentences - 1
						else:
							len_sentences = 0
					else:
						
						len_sentences = len_sentences + 1
						print "LEN after INCREMENT: " + str(len_sentences)
						
					print 'In if after for loop'
					break
					
		return navLink, url, title		
					
	
	#To check if the link is valid and exists in the anchor dictionary
	
	def checkcondition(self,flag,key_list,key_dict_name,anc_dict_name):	
		
		lenList = len(key_list)
		
		if ((flag ==1 or flag ==2) and lenList>0):
			print "\n"
			print "FLAG IS: "
			print flag
			print "KEY LIST IS: "
			print key_list
			print "Current key is: " + str(key_list[lenList-1])
			curKey = key_list[lenList-1]
			navigateLinks2 = navigateLinks()
			
			#Retrieve the title and url corresponding to the selected link.
			title,url = navigateLinks2.navigateToPage(curKey,key_dict_name,anc_dict_name)
			return title,url
		else:	
			return "",""	
	
	#Iterated through the key and anchor dictionary and returns the url corresponding to link selected
	def navigateToPage(self, i,key_dict_name,anc_dict):
		
		key_name_dict = key_dict_name
		anchorDictionary = anc_dict
		
		key= i
		url=""
		sx=""
		
		
		for key1 in key_name_dict.keys():
			if(key1 == key):
				val = ([key_name_dict[key]])
				sx=str(val)
		
		print "sx is:"
		print sx
		
		#To find the corresponding URL
		
		#First create an inverse dictionary
		ivd=dict()
		for k,v in anchorDictionary.iteritems():
			ivd[v]=k
		
		length_str= len(sx)
		#to consider string enclosed in quotes to compare with list elements
		strx=""
		strx=sx[1:(length_str-1)]
		print "strx is"
		print strx
		
		#now find the corresponding url
		for k in ivd.keys():
			#converting key to comparable form
			kk="'" + k + "'"
			#print kk
			if(kk==strx):
				url = ivd[k]
				break
		
		print url
		
		return sx, url
	
	#function to append key values in the summary
	#if the phrase in the summary, matches the list of link attributes, replace that attribute with key value
	def getSummary(self, summ, baseUrl):
		
		summ_text = summ			
		anchorDict = getAnchors()
		anchorDictionary = dict()
		anchorDictionary = anchorDict.getAllLinks(baseUrl)
		

		all_words=[]
		dict_words=[]

		word_tokenized = word_tokenize(summ_text)
		for i in word_tokenized:
			all_words.append(i)

		for v in anchorDictionary.values():
			dict_words.append(v)

		i=0
		key_name_dict=dict()	
		for w in dict_words:
			if w in summ_text:
				key = "key" + str(i)
				key_name_dict[key] = w
				summ_text=summ_text.replace(w,key)
				i = i + 1
				
		
		return summ_text,key_name_dict,anchorDictionary


		

			


