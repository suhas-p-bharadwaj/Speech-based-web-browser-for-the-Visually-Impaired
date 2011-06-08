import msvcrt
import time
def main():
	
	while True:
		print 'in while: Outside if'
		if msvcrt.kbhit():
			key = msvcrt.getch()
			print key
			print type(key)
			print len(key)
			print ord(key)
			if key == 'e':
				break
			if ord(key) == 32:
				print 'Space :)'
		time.sleep(1)
if __name__ == "__main__":
	main()