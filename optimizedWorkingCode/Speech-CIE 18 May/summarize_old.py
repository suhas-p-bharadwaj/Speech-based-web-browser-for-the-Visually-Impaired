# Simple Summarizer 


"""     
In order to summarize a document this algorithm first determines the 
frequencies of the words in the document.  It then splits the document
into a series of sentences.  Then it creates a summary by including the
first sentence that includes each of the most frequent words.  Finally
summary's sentences are reordered to reflect that of those in the original 
document.
"""

##//////////////////////////////////////////////////////
##  Simple Summarizer
##//////////////////////////////////////////////////////

from nltk.probability import FreqDist 
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import nltk.data
from IDF import generateTfidf,sorter


class SimpleSummarizer:

	def reorder_sentences( self, output_sentences, input ):
		output_sentences.sort( lambda s1, s2:
			input.find(s1) - input.find(s2) )
		return output_sentences
	
	def summarize(self, input, num_sentences ):
		# TODO: allow the caller to specify the tokenizer they want
		# TODO: allow the user to specify the sentence tokenizer they want
		
		tokenizer = RegexpTokenizer('\w+')
		
		# get the frequency of each word in the input
		base_words = [word.lower() 
			for word in tokenizer.tokenize(input)]
		words = [word for word in base_words if word not in stopwords.words()]
		
		word_frequencies = FreqDist(words)
		
		# now create a set of the most frequent words
		most_frequent_words = [pair[0] for pair in 
			word_frequencies.items()[:100]]
		
		
		#making a list of the top 15 most frequently appearing words
		most_freq_w = word_frequencies.items()[:10]
		print "********************"
		print word_frequencies
		print "Most frequent words are......."
		print most_freq_w
		print "********************"
		#print most_freq_w.values()
		
		#generating a dictionary of the most frequently appearing words list
		dict_most_freq_words=dict([(k,v) for k,v in most_freq_w])
		print dict_most_freq_words
		print "KEYS are      :"
		print dict_most_freq_words.keys()
		
		# break the input up into sentences.  working_sentences is used 
		# for the analysis, but actual_sentences is used in the results
		# so capitalization will be correct.
		
		sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
		actual_sentences = sent_detector.tokenize(input)
		working_sentences = [sentence.lower() 
			for sentence in actual_sentences]

		# iterate over the most frequent words, and add the first sentence
		# that inclues each word to the result.
		output_sentences = []
		
		#generate the respective IDF of the top 15 most frequently appearing words
		TFIDF = generateTfidf(dict_most_freq_words)
		print "GENERATED WORDS AFTER IDF ARE:     "
		print TFIDF
		
		#now we need to multiply the IDF and TF to get thr TFIDF
		#TFIDF=dict()
		#TFIDF=dict([(n, dict_most_freq_words.get(n,0) * generated_words_IDF.get(n,0)) for n in set(dict_most_freq_words) | set (generated_words_IDF)])
		
		print "TFIDF is"
		print TFIDF
		
		TFIDF_after_SORT = sorter(TFIDF)
		print "TFIDF after sorting is"
		print TFIDF_after_SORT
		
		highest_ranked_words_dict = dict()
		highest_ranked_words_dict = dict([(k,v) for k,v in TFIDF_after_SORT])
		
		#TFIDF_after_SORT.keys()
		#print "highest_ranked_words are: "
		#print highest_ranked_words_dict
		
		highest_ranked_words = highest_ranked_words_dict.keys()
		#print highest_ranked_words
		
		for word in highest_ranked_words:
			for i in range(0, len(working_sentences)):
				if (word in working_sentences[i] 
				  and actual_sentences[i] not in output_sentences):
					output_sentences.append(actual_sentences[i])
					break
				if len(output_sentences) >= num_sentences: break
			if len(output_sentences) >= num_sentences: break
			
		# sort the output sentences back to their original order
		output_sentences = self.reorder_sentences(output_sentences, input)

		# concatinate the sentences into a single string
		return "  ".join(output_sentences)