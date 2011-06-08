from Get_Base_Url import *
from IDF import *
import unittest
wordList = ['The','The','The']

class TestBaseUrl(unittest.TestCase):
	# Initialization method for the test case
	def setUp(self):
		self.url = "http://en.wikipedia.org/wiki/Abrham_Lincoln"
		self.wrdList = wordList
	# Test to assert if the getBaseUrl method returns the correct result
	def test_Base_Url(self):
		base_url = getBaseUrl(self.url)
		self.assertEqual("http://en.wikipedia.org",base_url)
	
	# Test case to assert if the frequency of words is returning the correct count
	def test_Freq_Of_Words(self):
		count = frequencyOfWord('The',self.wrdList)
		self.assertEqual(3,count)
		#self.assertIn(count,range(4))

		
if __name__ == '__main__':

	unittest.main()


