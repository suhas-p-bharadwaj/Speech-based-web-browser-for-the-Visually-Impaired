import sys
from BeautifulSoup import BeautifulSoup, NavigableString

#Class to remove unwanted HTML tags.
class removeHTMLtags:

	#function to remove all the invalid tags 
	def strip_tags(self, html, invalid_tags):
		soup = BeautifulSoup(html)
		for tag in soup.findAll(True):
			if tag.name in invalid_tags:
				s = ""
				for c in tag.contents:
					if type(c) != NavigableString:
						c = strip_tags(unicode(c), invalid_tags)
					s += unicode(c)
				tag.replaceWith(s)
		return soup
	
	# function to strip tag elements in the raw html
	def StripTags(self, text): 
		finished = 0 
		while not finished: 
			finished = 1 
			start = text.find("<") 
			if start >= 0: 
				stop = text[start:].find(">") 
				if stop >= 0: 
					text = text[:start] + text[start+stop+1:] 
					finished = 0 
		return text 
 

