from xgoogle.search import GoogleSearch, SearchError
from BeautifulSoup import BeautifulSoup
import urllib2


gs = GoogleSearch("Abraham Lincoln")
gs.results_per_page = 50
results = gs.get_results()

print type(results)
print len(results)
print results
i = 0
#for i in range(len(results)):
while i < len(results):
	print i
	res = results[i]
	print res.title.encode('utf-8')
	print res.desc.encode('utf-8')
	print res.url.encode('utf-8')
	print '\n'
	i = i+1