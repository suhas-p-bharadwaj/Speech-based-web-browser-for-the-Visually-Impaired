import msvcrt

class Events:


	def keypress(self):
		
		while True:
			
			key = msvcrt.getch()
			key1 = ""
			if key == u'\xe0'.encode('latin-1'):
				key1 = msvcrt.getch()
			
			
			print "Key:" + key + key1
			
			key = key + key1
			
			if key == u'\xe0M'.encode('latin-1'):
				print 'Right'
			if key == u'\xe0K'.encode('latin-1'):
				print 'Left'
			if key == 'h':
				print 'Hello'
			if key == 'e':
				break;
				
# def main():
	# e = Events()
	# e.keypress()
	
# if __name__ == '__main__':
	# main()