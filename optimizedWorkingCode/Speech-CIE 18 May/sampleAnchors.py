from BeautifulSoup import BeautifulSoup
from nltk import *
import time

#Class to retrieve all the links present in a page
class getAnchors:

	#Retrieves all the links in a page
	#Appends the base url to the links if they are internal links
	#Returns the anchor dictionary obtained
	def getAllLinks(self, baseUrl):
	
	
		#Load the html content of the page
		
		f=open("htmlContent.txt")
		ss=f.read()
		f.close()

		#Format the content using Beautiful Soup
		
		soup=BeautifulSoup(ss)
		
		#Retrieve all the <a> elements
		
		anchors=soup.findAll('a')
		
		len_anchors=len(anchors)
		
		#Tokeinzer : based on <a href= ... >
		
		str_anchors = str(anchors)
		anchor_tokenizer = RegexpTokenizer('<a href=\"\/*.*>')
		tokenized_str = anchor_tokenizer.tokenize(str_anchors)
		
		
		#Split based on </a>
		
		tokenized_str = str(tokenized_str).split("</a>")
		
		#Split string based on href attribute
		
		link_title=dict()
		
		
		for l in tokenized_str:
			tokenized_str_split = l.split('">')
			tokenized_link_split = tokenized_str_split[0].split('href=\"')
			
			
			if len(tokenized_link_split)>1 and len(tokenized_str_split)>1:
				link_title[tokenized_link_split[1]] = tokenized_str_split[1]
			
		link_list = []
				
		print "link_title is"
		
		
		base_addr = baseUrl
		
		print "LENGTH OF DICT IS: " + str(len(link_title))
		
		#time.sleep(1)
		
		
		for k,v in link_title.iteritems():
			
			
			
			#check if the link starts with a "/"
			tokenize=RegexpTokenizer('^/.*')
			chk_strt_link=tokenize.tokenize(str(k))
			
			#check if the link starts with a "#"
			tokenize=RegexpTokenizer('^#.*')
			chk_strt_link1=tokenize.tokenize(str(k))
			
			#check if the link starts with http or www
			tokenize=RegexpTokenizer('^http.*')
			chk_strt_link2=tokenize.tokenize(str(k))
			
			tokenize=RegexpTokenizer('^www.*')
			chk_strt_link3=tokenize.tokenize(str(k))
			
			
			#starts with a "/" and does not start with a "#"
			if chk_strt_link and not chk_strt_link1:
				
				kk = str(k)
				kk = base_addr + kk
			
			elif chk_strt_link2 or chk_strt_link3 and not chk_strt_link1:
				
				kk = str(k)
				
			else:
				kk = str(k)
				
				
				if not chk_strt_link1 and not chk_strt_link1:
					kk=base_addr + "/" + kk
					
				elif chk_strt_link1:
					
					kk = base_addr + kk
					
			
			
			link_list.append(kk)
		

		
		title_list = []

		for v in link_title.values():
			title_list.append(v)	

		link_title_appended = dict()

		for i in range(len(link_list)):
			#different validations
			
			#check if string is empty
			strx=link_list[i]
			tokenizer=RegexpTokenizer('.*"')
			val = tokenizer.tokenize(strx)
			
			
			str1=title_list[i]
			tokenizer1=RegexpTokenizer('<.*>*')
			val1 = tokenizer1.tokenize(str1)
			
			
			len1=len(title_list[i])
			
			#check if string ends with com or org or edu
			str2=link_list[i]
			tokenizer2=RegexpTokenizer('www/..*/.(com|org|edu)#')
			val2=tokenizer2.tokenize(str2)
			
			#check if the string doesn't contain mailto attribute
			str3=link_list[i]
			tokenizer2=RegexpTokenizer('^mailto:')
			val3=tokenizer2.tokenize(str3)
			
			if val and not val1 and len1 > 5 and not val3:
				
				str1 = link_list[i]
				str2 = str1.split(" title=\"")
				
				str3=str(str2[0])
				str4=str3.split(" class=\"")
				str5 = str(str4[0])
				
				
				
				str6 = str5[:-1]
				
				
				link_title_appended[str6] = title_list[i]
				
				
			else:
				continue

			
		f=open("allAnchors.txt",'w')
		for k,v in link_title_appended.iteritems():
			f.write(k)
			f.write("\n")
			f.write(v)
			f.write("\n")
			f.write("\n")
		f.close()
		
		#Sends dictionary content in title, link form
		return link_title_appended