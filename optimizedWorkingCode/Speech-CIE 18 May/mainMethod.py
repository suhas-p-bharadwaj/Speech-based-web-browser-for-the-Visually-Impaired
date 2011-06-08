from yahooEx import YahooSearchError, search
import json
import urllib
info = search('json python')
print info['totalResultsReturned']