from BeautifulSoup import BeautifulSoup
import urllib2
import time


class FetchHTMLContent:
	
	#Constructor
	def __init__(self, u):
		self.url = u

	#To fetch the url contents
	def fetchUrlContents(self):
		print "enter fetch url func"
		
		
		time1 = time.time()
		
		#Request to fetch the html contents
		#User Agent : Specifies in the header as to which type of browser is making a request. This is a security feature
		#Magic Browser : This enables the anonymous mode, if this isn't enabled we can't make a request to the wikipedia servers	
		req = urllib2.Request(self.url, headers={'User-Agent' : "Magic Browser"})
		
		# ??
		con = urllib2.urlopen(req)
		con1 = urllib2.urlopen(req)
		
		time2 = time.time()
		print "Time to create first CON element:  " + str(time2-time1)
		
		time1 = time.time()
		
		#Format the html contents obtained
		html = BeautifulSoup(con)
		
		time2 = time.time()
		print "Time for BS:" + str(time2-time1)
		
		
		time1 = time.time()
		f=open('htmlContent.txt','w')			
		f.write(con1.read())
		f.close()
		time2 = time.time()
		print "Time for htmlContent:  " + str(time2-time1)
		
		
		#Return the html obtained
		return html
		
	#To fetch <p> contents from the html
	def fetchParaContent(self, html):
	
		#Get all the <p> elements from the page
		paras = html.findAll('p')			
		print 'No of paras:' + str(len(paras))
		
		s1 = ""
		
		#Iterate through the obtained <p>s		
		for p in paras:
		
			#Contents of <p>	
			cnt = p.contents
			s2 = ""
			
			#Remove ??
			for c in cnt:
				
				s2 = (str(c.string).replace("&quot","")).replace("None","").replace("var","")
				s1 = s1 + s2
		
		#Return cleaned <p> contents		
		return s1
		