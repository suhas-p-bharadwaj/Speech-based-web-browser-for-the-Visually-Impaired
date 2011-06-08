# from sampleAnchors import getAnchors
# import urllib2

# anchorDict = getAnchors()
# anchorDictionary = dict()
# anchorDictionary = anchorDict.getAllLinks()

#print "dictionary is..."

# for k,v in anchorDictionary.iteritems():
	# print k
	# print v
	
# req = urllib2.Request(k, headers={'User-Agent' : "Magic Browser"}) 
# con = urllib2.urlopen( req )
# contents = con.read()


a=[]
b=[]

a.append("hi")
a.append("today")
a.append("is")
a.append("saturday")
a.append("wishing")
a.append("a")
a.append("good")
a.append("morning")

b.append("hi")
b.append("good")
b.append("morning")

i=0
j=1
for w1 in b:
	i = 0
	for w2 in a:
		print i
		if w1 == w2:
			a[i] = "key" + str(j)
			print w2
			j=j+1
		i=i+1
print a





#shift link program
from sampleAnchors import getAnchors
from nltk import *
import re
import speech
import urllib2


summ_text = "We live in a country called India. London is a five hour flight from here. It borders Ukraine. There are many universities which are\
			good in the world. Northwestern University is one of them"

			
anchorDict = getAnchors()
anchorDictionary = dict()
anchorDictionary = anchorDict.getAllLinks()
#print anchorDictionary

all_words=[]
dict_words=[]

word_tokenized = word_tokenize(summ_text)
#print word_tokenized
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
		
print summ_text
print key_name_dict

			
# strx= "what is your name? My name is key123. We live in key234"
l=re.split(r"(\s*key[0-9]{1,3})",summ_text)
tok=RegexpTokenizer('^ key[0-9]{1,3}')

def navigateToPage(i):
	
	#key = WhitespaceTokenizer().tokenize(i) 
	key= str(i[1:])
	#print "key in func is:::"
	#print key
	#print type(key)
	url=""
	sx=""
	for key1 in key_name_dict.keys():
		if(key1 == key):
			val = ([key_name_dict[key]])
			#print len(val)
			sx=str(val)
		
	#to find the corresponding URL
	#first create an inverse dictionary
	ivd=dict()
	for k,v in anchorDictionary.iteritems():
		ivd[v]=k
	
	length_str= len(sx)
	strx=""
	strx=sx[1:(length_str-1)]
	print strx
		
	#now find the corresponding url
	for k in ivd.keys():
		kk="'" + k + "'"
		if(kk==strx):
			#print "hmph"
			url = ivd[k]
			break
	
	print url
	opt=raw_input("1 or 2")
	if(opt=="1"):
		url = "http://" + url
		req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"}) 
		con = urllib2.urlopen( req )
		contents = con.read()
		print contents
	
	

for i in l:
	res = tok.tokenize(i)
	if not res:
		#speech.say(i)
		continue
	else:
		#print "zz"
		navigateToPage(i)


