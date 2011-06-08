# Say anything you type, and write anything you say.
# Stops when you say "turn off" or type "turn off".

import speech
import sys

file = open('summ.txt','r')
m = file.read()
print len(m)
print "Anything you type, speech will say back."
print "Anything you say, speech will print out."
print "Say or type 'turn off' to quit."


speech.say(m)

def callback(phrase, listener):
    print ": %s" % phrase
    if phrase == "turn off":
        speech.say("Goodbye.")
        listener.stoplistening()
        sys.exit()





listener = speech.listenforanything(callback)

while listener.islistening():
    text = raw_input("> ")
    if text == "turn off":
        listener.stoplistening()
        sys.exit()
    else:
        speech.say(text)
