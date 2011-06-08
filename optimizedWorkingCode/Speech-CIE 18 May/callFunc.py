from shiftLinks import navigateLinks
import unicodedata

class speak_listen_summary:

	def readSummary(self,baseUrl):
		
		
		navigateLinks1 = navigateLinks()
		
		#Obtain the summary from the file
		fp=open("summary.txt","r")
		txt=fp.read()
		fp.close()
		summ_text= txt
		
		#Remove all non-ASCII characters
		for i in range(len(txt)):
			if(ord(txt[i])>127):
				#print "xx: " + txt[i] + "i: " + str(i)
				summ_text = summ_text.replace(txt[i]," ")
				
		print summ_text
		
		#Obtain the key and link dictionary
		key_dict = dict()
		anc_dict=dict()
		summ_text , key_dict, anc_dict=navigateLinks1.getSummary(summ_text,baseUrl)
		print summ_text
		print key_dict

		#Read the summary
		#Returns navFlag as 1 if a link is selected in the summary along with url and title
		navFlag, navLink, title = navigateLinks1.addKeys(summ_text,key_dict,anc_dict)
		
		return navFlag, navLink, title

