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

ttsEngine = TexttoSpeechEngine()


class SearchEngine(SpeechRecog): 

	
	def main():
		
		navFlag = 0
		navLink = ""
		title = ""
		baseUrl = ""
		
		while 1:
		
			selectedLink = ""
			

			if navFlag == 0:	
				#Operations is the speech recognition engine
				speechRecog = SpeechRecog() 
				query = speechRecog.inputSpeech()
			
				print query
			
				ttsEngine.speakText("Returned query is " + query)
			
				#Iterate through the links and get the selected link
				selectedLink = speechRecog.searchQuery(query)
			
			elif navFlag == 1 and navLink != "":
				ttsEngine.speakTextSync("Navigating to the requested link. Please wait.")
				navFlag = 0
				selectedLink = navLink
				navLink = ""
				
			
			baseUrl = getBaseUrl(selectedLink)
			print baseUrl
			
			fetchCntnts = FetchHTMLContent(selectedLink)
			
			htmlCntnt = fetchCntnts.fetchUrlContents()
			
			fetchCntnts.fetchParaContent(htmlCntnt)
			
			
			#Remove all invalid tags and write back to Bill.txt
			#--------------------------------------------------------
			
			removeTags=removeHTMLtags()
			file=open("Bill.txt")
			html=file.read()
			file.close()
			
			html = removeTags.StripTags(html)
			
			file=open("Bill.txt","w")
			file.write(html)
			file.close()
			
			#--------------------------------------------------------
			
			#Fetch the valid required pure content and summarize
			#--------------------------------------------------------
			
			file=open('Bill.txt')
			txt=file.read()
			file.close()

			obj = SimpleSummarizer()
			newTxt = obj.summarize(txt,40)
			
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
			
			ttsEngine.speakText("The summarized contents are:  ")
			
			spkAndListen = speak_listen_summary()
			navFlag, navLink, title = spkAndListen.readSummary(baseUrl)
			
			if navLink == "":
				navFlag = 0
			
			print "RETURNED"
			print navFlag
			print navLink 
			print title
		
		
	if __name__ == '__main__':
		main()