import nltk
from nltk import word_tokenize
from nltk.corpus import brown
import os, os.path
import math, time
#count = 0
#str = nltk.corpus.brown.words()
#tfidf = {}
#wrdlist = ["Lincoln","news","Gandhi","bird","house","computer","television","book","library","satellite"]
#fileCnt = os.listdir("C:/CORPORA/brown/")
totalCnt = 0
#for i in str:
#	for j in wrdlist:
#		if j ==i:
#			count = count + 1
#	tfidf[j] = count
#	count = 0

def noOfFilesCnt():
	return totalCnt

def frequencyOfWord(word,listOfWords):
	count = 0
	for i in listOfWords:
		if word == i:
			count = count + 1
	return count


def sorter(tfidf):
	items = [(v, k) for k, v in tfidf.items()]
	items.sort()
	items.reverse()
	items = [(k, v) for v, k in items]
	return items
	
	
def generateTfidf(wrdList):
	print "new idf..."
	tfidf = {}
	dictDocCount = {}
	totalCnt = 512
	DocCountFl = open('C:\WordsDocCnt.txt','r')
	for WrdCntPair in DocCountFl.readlines():
		WrdCntPair = WrdCntPair.strip()
		if ':' in WrdCntPair:
			if WrdCntPair.count(':') == 1:
				WrdCntLst = WrdCntPair.split(':')
				dictDocCount[WrdCntLst[0]] = int(WrdCntLst[1])
	DocCountFl.close()
	for i in wrdList.keys()[:10]:
		counter = 0	
		if dictDocCount.has_key(i):
			counter = dictDocCount[i]
		else:
			counter = 0
		if(counter != 0):
			tfidf[i] = wrdList[i] * math.log(1 + float(float(totalCnt)/float(counter))) 
		else:
			tfidf[i] = 0
	return tfidf	
		
	
		

	
	




