import speech
import time
from xgoogle.search import GoogleSearch, SearchError
from BeautifulSoup import BeautifulSoup
import urllib2
import re


	
class SpeechRecog1:
	
	listener = None
	
	def callback(self, phrase, listener):
		if ((phrase == "Stop") or (phrase == "STOP") or (phrase == "stop")):
			listener.stoplistening()
			
		if ((phrase == "Next") or (phrase == "NEXT") or (phrase == "next")):
			listener.stoplistening()
			
		speech.say(phrase)
		
	def __init__(self):
		print 'In Constructor'
		listener = speech.listenforanything(self.callback)
		print 'In constructor 2'
	
	
	def inputSpeech(self):
		print "Hello"
		file = open("Bill.txt","w");
		response = "NO"
		response1 = "Google"
		speech.say("Hello!!! Welcome to speech recognition for the visually impaired")

		#while((response != "YES") or (response != "Yes") or (response != "yes")):
		while((response == "NO") or (response == "No") or (response == "no")):
			speech.say("Please enter your search query")
			response1 = speech.input("Say something, please.")
			speech.say("You said " + response1)
			print response1
			speech.say("Is this what you said?")
			
			response = speech.input("Is it ok?")
			response=str(response)
			
			
				
			print response
			#while((response != "No") or (response != "NO") or (response != "no") or (response != "YES") or (response != "Yes") or (response != "yes")):
				#print "Please say yes or no"
				#speech.say("Please say   yes    or   no   ")
				#response= speech.input("Please say yes or no")
				#print response
				
		return response1
		
	def searchQuery(self,query):
		try:
			file = open("Bill.txt","w")
			file1 = open("HTML.txt","w");
			#file2 = open("x.txt","w");
			#file3 = open("test.txt","w");
			gs = GoogleSearch(query)
			gs.results_per_page = 50
			results = gs.get_results()
	  
			speech.say("Yor results are:")
	  
			i = 1;
	  
			for res in results:
				print "\n"
				print "Result number" 
				print i
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
				speech.say(j + res.title.encode("utf8") + "      And the corresponding description is: " + res.desc.encode("utf-8"))
				speech.say("Is this option good?")
				response3 = speech.input("Is this option good ? ")
				print response3
				if ((response3 == "Yes") or (response3 == "YES") or (response3 == "yes")):
				#if((response3 != "No") or (response3 != "NO") or (response3 != "no")):
					req = urllib2.Request(res.url, headers={'User-Agent' : "Magic Browser"}) 
					con = urllib2.urlopen( req )
					#file.write(con)
		 
					html = BeautifulSoup(con)
					#file1.open()
					
					print "zzzzzzzzzzzzz"
					hrefs = html.findAll('a')
					paras = html.findAll('p')
					
					#body = html.findAll('body')					
					#z = str(paras[0])
					#print type(z)
					#print len(paras)
					lst = []
					#for b in body:
						#file3.write(b.renderContents());
						#tags = b.renderContents();
						#for tag in tags:
							#file3.write(tag.contents)
							
					for p in paras:
						#lst.append(re.sub("<.*span.*>","",re.sub("<a href.*>","",re.sub("<p>","",re.sub('<.*b>','',str(p))))))
						#re.sub("<p>","",str(p))
						#file2.write(p.renderContents());
						cnt = p.contents
						for c in cnt:
							file.write((str(c.string).replace("&quot","")).replace("None","").replace("var",""))
							file1.write((str(c.string).replace("&quot","")).replace("None","").replace("var",""))
			 
					#print lst
					#for l in lst:
						#file.write(l.encode("utf-8"))
						
					file.close()
					file1.close()
					#file1.close()
					#file2.close()
					#file3.close()
					print "\n";
					print hrefs[10];
		 
					print "crewhaha";
					break;
		 
		
				i = i + 1
		
		except SearchError, e:
			print "Search failed: %s" % e
			
		
		return	
	