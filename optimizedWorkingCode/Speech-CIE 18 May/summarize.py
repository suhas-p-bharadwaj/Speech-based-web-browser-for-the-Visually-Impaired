# Simple Summarizer 


"""     
In order to summarize a document this algorithm first determines the 
frequencies of the words in the document.  It then splits the document
into a series of sentences.  Then it creates a summary by including the
first sentence that includes each of the most frequent words.  Finally
summary's sentences are reordered to reflect that of those in the original 
document.
"""

from nltk.probability import FreqDist 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import nltk.data
from IDF import generateTfidf,sorter
import time


class SimpleSummarizer:
	
	#Module to re-order sentences
	def reorder_sentences( self, output_sentences, input ):
		output_sentences.sort( lambda s1, s2:
			input.find(s1) - input.find(s2) )
		return output_sentences
	
	#Summarize main module. Takes in input sentences and number of sentences required in the output summary
	def summarize(self, input, num_sentences ):
		
		
		#Tokenize the words
		tokenizer = RegexpTokenizer('\w+')
		
		# get the frequency of each word in the input
		#Tokenize the input
		base_words = []
		time1 = time.time()
		tokenized_words = tokenizer.tokenize(input.lower())
		time2 = time.time()
		print "Total time taken for word tokenization is: " + str(time2 - time1)
		print "no of tokenized words are: " +str(len(tokenized_words))
		
		
		#Frequence of words
		time1 = time.time()
		word_frequencies = FreqDist(tokenized_words)
		time2 = time.time()
		print "Total time taken for calculating word frequencies is: " + str(time2 - time1)
		
		#baseWords = word_frequencies.keys()
		
		#Take the 10 most frequent words excluding stop words
		time1 = time.time()
		word_lst = []
		countValidWords = 0
		for word in word_frequencies.items():
			if word[0].lower() not in stopwords.words() and word[0].lower() != 'would':
				word_lst.append(word)
				countValidWords = countValidWords + 1
				if countValidWords > 10:
					break
		time2 = time.time()
		print "Total time taken for stop words is: " + str(time2 - time1)
				
		
		
		
		#generating a dictionary of the most frequently appearing words list
		dict_most_freq_words=dict([(k,v) for k,v in word_lst])
		
		
		#print dict_most_freq_words
		print "KEYS are      :"
		print dict_most_freq_words.keys()
		
		
		# break the input up into sentences.  working_sentences is used 
		# for the analysis, but actual_sentences is used in the results
		# so capitalization will be correct.
		
		time1 = time.time()
		sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		actual_sentences = sent_detector.tokenize(input)
		working_sentences = [sentence.lower() 
			for sentence in actual_sentences]
		time2 = time.time()	
		print "Time taken to tokenize sentences is: " +str(time2-time1)
		
		
		# iterate over the most frequent words, and add the first sentence
		# that inclues each word to the result.
		output_sentences = []
		
		#generate the respective IDF of the top 15 most frequently appearing words
		time1 = time.time()
		TFIDF = generateTfidf(dict_most_freq_words)
		time2 = time.time()
		print "Time taken in IDF function is: " +str(time2-time1)
		
				
		print "TFIDF is"
		print TFIDF
		
		#Sort the TFIDF words
		time1 = time.time()
		TFIDF_after_SORT = sorter(TFIDF)
		time2 = time.time()
		print "Time taken in SORT function is: " +str(time2-time1)
		
		print "TFIDF after sorting is"
		print TFIDF_after_SORT
		
		#Create a dictionary of highest ranked words
		highest_ranked_words_dict = dict()
		highest_ranked_words_dict = dict([(k,v) for k,v in TFIDF_after_SORT])
		
		
		highest_ranked_words = highest_ranked_words_dict.keys()
		
		#Collect the sentences from the input which contains the TFIDF words
		time1 = time.time()
		for word in highest_ranked_words:
			for i in range(0, len(working_sentences)):
				if (word in working_sentences[i] 
				  and actual_sentences[i] not in output_sentences):
					output_sentences.append(actual_sentences[i])
					break
				if len(output_sentences) >= num_sentences: break
			if len(output_sentences) >= num_sentences: break
		time2 = time.time()
		print "Time taken to generate OP sentences is: " +str(time2-time1)
		
		# sort the output sentences back to their original order
		time1 = time.time()
		output_sentences = self.reorder_sentences(output_sentences, input)
		time2 = time.time()
		print "Time taken to reorder OP sentences is: " +str(time2-time1)
		
		
		# concatinate the sentences into a single string
		return "  ".join(output_sentences)