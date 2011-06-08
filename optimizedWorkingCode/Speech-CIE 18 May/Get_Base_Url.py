#Module to get the base url
def getBaseUrl(url):
	splittedUrl = url.split("/")
	if(len(splittedUrl) >= 3):
		baseUrl = splittedUrl[0] + "//" + splittedUrl[2]
	elif(len(splittedUrl) < 3):
		baseUrl = url
	return baseUrl
	

