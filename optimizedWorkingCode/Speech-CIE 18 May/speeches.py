import speech
import time
from xgoogle.search import GoogleSearch, SearchError
from BeautifulSoup import BeautifulSoup
import urllib2
import re

file = open("Bill.txt","w");
response = "NO"
response1 = "Google"
speech.say("Hello!!! Welcome to speech recognition for the visually impaired")

while((response != "YES") or (response != "Yes") or (response != "yes")):
	speech.say("Please enter your search query")
	response1 = speech.input("Say something, please.")
	speech.say("You said " + response1)
	print response1
	speech.say("Is this what you said?")
	response = speech.input("Is it ok?")
	print response

try:
  gs = GoogleSearch(response1)
  gs.results_per_page = 50
  results = gs.get_results()
  
  speech.say("Yor results are:")
  
  i = 0;
  
  for res in results:
    print res.title.encode("utf8")
  #  print res.desc.encode("utf8")
    print res.url.encode("utf8")
    j = str(i)
    speech.say(j + res.url.encode("utf-8"));
    response3 = speech.input("Is this option good ? ")
    print response3
    if ((response3 == "Yes")):
     req = urllib2.Request(res.url, headers={'User-Agent' : "Magic Browser"}) 
     con = urllib2.urlopen( req ) 
     
     html = BeautifulSoup(con)
     hrefs = html.findAll('a');
     paras = html.findAll('p');	 
     z = str(paras[0])
     print type(z)
     lst = []
     for p in paras:
      lst.append(re.sub("<.*span.*>","",re.sub("<a href.*>","",re.sub("<p>","",re.sub('<.*b>','',str(p))))))
      #re.sub("<p>","",str(p))
     	 
     print lst;
     for l in lst:
      file.write(lst[0]);
     file.close();
     print "\n";
     print hrefs[10];
	 
     print "crewhaha";
     break;
	 
	
    i = i + 1
    
except SearchError, e:
  print "Search failed: %s" % e


def callback(phrase, listener):
    if ((phrase == "Stop") or (phrase == "STOP") or (phrase == "stop")):
        listener.stoplistening()
    speech.say(phrase)

listener = speech.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)
