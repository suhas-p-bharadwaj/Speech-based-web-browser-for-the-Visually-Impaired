import pyTTS

class TexttoSpeechEngine:

	
	def __init__(self):
		self.tts = pyTTS.Create()
	
	def speakText(self,text):
		self.tts.Speak(text,pyTTS.tts_async)
		#print self.tts.last_speech
		
	def stopSpeak(self):
		print "In stop speak."
		if self.tts.IsSpeaking():
			self.tts.Stop()
		print "After if in stop speak"
		
	def previous(self):
		print "In repeat:"
		
		if self.tts.IsSpeaking():
			self.tts.Skip(-1)
			
		print "After Previous"
	
	def isSpeaking(self):
		return self.tts.IsSpeaking()
	
	def next(self):
	
		print "In next"
		
		if self.tts.IsSpeaking():
			self.tts.Skip(1)
			
		print "After next"
	
	def speakTextSync(self,text):
		self.tts.Speak(text)