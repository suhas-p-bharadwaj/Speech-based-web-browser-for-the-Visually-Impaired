import time
import SpeechRecogTool
import speech
import time
from SpeechRecogTool import SpeechRecog
from testRemove import removeHTMLtags
from summarize import SimpleSummarizer
from nltk.tokenize import *
from SpeechSynthesis import *
from EventHandler import *
from FetchHtml import *
from Get_Base_Url import getBaseUrl
from callFunc import *

#Create an instance of the pytts speech synthesis engine
ttsEngine = TexttoSpeechEngine()


class SearchEngine(SpeechRecog): 

	
	def main():
		
		#navFlag is the flag set if 1 iteration is complete
		ttsEngine.speakTextSync("Hello!!! Welcome to speech recognition for the visually impaired")
		ttsEngine.speakTextSync("In this system, you can obtain information about your  desired topic using a speech query")
		ttsEngine.speakTextSync("Control the tool, by closely following the various instructions")
		navFlag = 0
		navLink = ""
		title = ""
		baseUrl = ""
		
		while 1:
			try:
		
				selectedLink = ""
				
				if navFlag == 0:	
					#Operations is the speech recognition engine
					speechRecog = SpeechRecog() 
					query = speechRecog.inputSpeech()
					print query
					ttsEngine.speakTextSync("Returned query is " + query)
				
					#Iterate through the links and get the selected link
					selectedLink = speechRecog.searchQuery(query)
				
				elif navFlag == 1 and navLink != "":
					ttsEngine.speakTextSync("Navigating to the requested link. Please wait.")
					navFlag = 0
					selectedLink = navLink
					navLink = ""
					
				
				baseUrl = getBaseUrl(selectedLink)
				print baseUrl
				
				time1 = time.time()
				
				#--------------------------------------------------------
				#Create an instance of the FetchHtml Class
				#--------------------------------------------------------
				fetchCntnts = FetchHTMLContent(selectedLink)
				
				#--------------------------------------------------------
				#Fetch the html contents from the selected page
				#--------------------------------------------------------
				htmlCntnt = fetchCntnts.fetchUrlContents()
				
				#--------------------------------------------------------
				#Fetch all the content embedded in the <p> tag
				#--------------------------------------------------------
				html = fetchCntnts.fetchParaContent(htmlCntnt)
				
				
				#--------------------------------------------------------
				#Remove all the invalid tags in the text
				#--------------------------------------------------------		
				removeTags=removeHTMLtags()	
				html = removeTags.StripTags(html)
				
				
				
				
				#--------------------------------------------------------
				#Fetch the valid required pure content and summarize
				#--------------------------------------------------------
				txt = html
				time2 = time.time()
				
				time3=time.time()
				obj = SimpleSummarizer()
				newTxt = obj.summarize(txt,40)
				time4=time.time()
				
				timeTaken = time4 - time3
				print "time taken for parsing raw html file is totally: " + str(time2-time1)
				print "Total time taken for summarization is: " + str(timeTaken)
				
				#--------------------------------------------------------
				#Clean up the summarized text. Remove the javascript contents and write it to a file
				#--------------------------------------------------------
				
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
				file1=open("summary.txt","w")
				file1.write(s)
				file1.close()	
				
				#---------------------------------------------------------
				#Block to control the reading of summarized contents
				#---------------------------------------------------------
				
				ttsEngine.speakText("The summarized contents are:  ")
				
				spkAndListen = speak_listen_summary()
				navFlag, navLink, title = spkAndListen.readSummary(baseUrl)
				
				if navLink == "":
					navFlag = 0
				
				print "RETURNED"
				print navFlag
				print navLink 
				print title
				
				
				#---------------------------------------------------------
			except:
				print "Some error happened"
				time.sleep(5)
				
				ttsEngine.speakText("Odd!! Thr was sm error processing this page We are trying to restart your browser Do you want to continue?")
				print "Odd!! Thr was sm error processing this page We are trying to restart your browser Do you want to continue?"
				query = speech.input()
				print query
				if(query == "yes" or query == "YES" or query == "Yes"):
					continue
				else:
					sys.exit()
			
			
	if __name__ == '__main__':
		main()