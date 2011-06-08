from BeautifulSoup import BeautifulSoup
from nltk import *
import time

class getAnchors:

	def getAllLinks(self):
	
		f=open("htmlContent.txt")
		ss=f.read()
		f.close()

		soup=BeautifulSoup(ss)
		anchors=soup.findAll('a')
		#print "anchors are"
		#print anchors
		len_anchors=len(anchors)
			
		str_anchors = str(anchors)
		anchor_tokenizer = RegexpTokenizer('<*(b|p|a)* href=\"\/*.*>')
		tokenized_str = anchor_tokenizer.tokenize(str_anchors)
		
		#str_anchors = str(tokenized_str)
		#anchor_tokenizer = RegexpTokenizer('<*(b|p|a)* href=\"^[^#]*.*>')
		#tokenized_str = anchor_tokenizer.tokenize(str_anchors)
		
		#print "tokenized_str 1 is......"
		#print tokenized_str
		tokenized_str = str(tokenized_str).split("</a>, ")
		#print "tokenized_str is......"
		#print tokenized_str
		link_title=dict()


		for l in tokenized_str:
			tokenized_str_split = l.split('">')
			tokenized_link_split = tokenized_str_split[0].split('href=\"')
			#print len(tokenized_link_split)
			#print len(tokenized_str_split)
			
			if len(tokenized_link_split)>1 and len(tokenized_str_split)>1:
				link_title[tokenized_link_split[1]] = tokenized_str_split[1]
			
		link_list = []
				
		print "link_title is"
		#print link_title
		
		# for k,v in link_title.iteritems():
			# #print str(k)
			# tokenize=RegexpTokenizer('^/.*')
			# chk_strt_link=tokenize.tokenize(str(k))
			
			# tokenize=RegexpTokenizer('^#.*')
			# chk_strt_link1=tokenize.tokenize(str(k))
			
			# if not chk_strt_link and not chk_strt_link1:
				# kk=str(k)
				# kk = "SomeBaseAdrress/" + kk
				# #print "kk is"
				# #print kk
			# else:
				# if not chk_strt_link1:
					# #print "not in loop"
					# kk = "www.wikipedia.org" + str(k)
				# else:
					# #print "in loop"
					# kk = "www.wikipedia.org/wiki/" + str(k[1:])
			# link_list.append(kk)
		
		base_addr = "www.someWebsite.com"
		
		print "LENGTH OF DICT IS: " + str(len(link_title))
		
		time.sleep(1)
		
		
		for k,v in link_title.iteritems():
			
			#print "Link is: " +str(k)
			#print "Title is: " + str(v)
			#time.sleep(0.1)
			
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
				#print "here1"
				kk = str(k)
				kk = base_addr + kk
			
			elif chk_strt_link2 or chk_strt_link3 and not chk_strt_link1:
				#print "here2"
				kk = str(k)
				
			else:
				kk = str(k)
				#print "here3"
				
				if not chk_strt_link1 and not chk_strt_link1:
					kk=base_addr + "/" + kk
					
				elif chk_strt_link1:
					#kk = str(k)
					kk = base_addr + kk
					#continue
			
			#print kk
			#time.sleep(0.1)
			link_list.append(kk)
			
		title_list = []

		for v in link_title.values():
			title_list.append(v)	

		link_title_appended = dict()

		for i in range(len(link_list)):
			#different validations
			
			strx=link_list[i]
			tokenizer=RegexpTokenizer('.*"')
			val = tokenizer.tokenize(strx)
			#print "val is: " +str(val)
			#time.sleep(0.1)
			
			str1=title_list[i]
			tokenizer1=RegexpTokenizer('<.*>*')
			val1 = tokenizer1.tokenize(str1)
			#print "str1 is: " + str(str1)
			#print "val1 is: " + str(val1)
			
			len1=len(title_list[i])
			
			str2=link_list[i]
			tokenizer2=RegexpTokenizer('www/..*/.(com|org|edu)#')
			val2=tokenizer2.tokenize(str2)
			
			str3=link_list[i]
			tokenizer2=RegexpTokenizer('^mailto:')
			val3=tokenizer2.tokenize(str3)
			
			if val and not val1 and len1 > 5 and not val3:
				link_title_appended[link_list[i]] = title_list[i]
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