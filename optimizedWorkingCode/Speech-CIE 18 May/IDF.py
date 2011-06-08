import nltk
from nltk import word_tokenize
from nltk.corpus import brown
import os, os.path
import math, time


def noOfFilesCnt():
	return totalCnt

def frequencyOfWord(word,listOfWords):
	count = 0
	for i in listOfWords:
		if word == i:
			count = count + 1
	return count


#To sort the tfidf words	
def sorter(tfidf):
	items = [(v, k) for k, v in tfidf.items()]
	items.sort()
	items.reverse()
	items = [(k, v) for v, k in items]
	return items
	

#Generate tfidf of the most frequent words	
def generateTfidf(wrdList):
	print "new idf..."
	tfidf = {}
	dictDocCount = {}
	totalCnt = 512
	
	#Create a dictionary of the words from the corpus
	print "trying to open file....."
	DocCountFl = open('newSortWords.txt','r')
	for WrdCntPair in DocCountFl.readlines():
		WrdCntPair = WrdCntPair.strip()
		if ':' in WrdCntPair:
			if WrdCntPair.count(':') == 1:
				WrdCntLst = WrdCntPair.split(':')
				dictDocCount[WrdCntLst[0]] = int(WrdCntLst[1])
	DocCountFl.close()
	
	
	#Calculate the tfidf for the 10 most frequent words in wrdLst
	for i in wrdList.keys()[:10]:
		counter = 0	
		if dictDocCount.has_key(i):
			counter = dictDocCount[i]
		else:
			counter = 0
		
		#TFIDF[i] = frequency of the word * log(1 + (total no of documents/no of documents the word occurs))
		if(counter != 0):
			tfidf[i] = wrdList[i] * math.log(1 + float(float(totalCnt)/float(counter))) 
		else:
			tfidf[i] = 0
	return tfidf	
		
	
		

	
	




