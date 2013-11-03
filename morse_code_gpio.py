import RPi.GPIO as GPIO
import string
import sys
import time

dit_time=0.15
dah_time=0.45
ditDah_space=0.15
char_space=0.3
word_space=1
phrase_space=3

code = dict (a = ".-", b = "-...", c = "-.-.", d = "-..", e = ".", f = "..-.", g = "--.", h = "....",  i = "..", j = ".---",  k = "-.-", l = ".-..", m = "--", n = "-.", o = "---", p = ".--.", q = "--.-", r = ".-.", s = "...", t = "-", u = "..-", v = "...-", w = ".--", x = "-..-", y = "-.--", z = "--..", _ = " ")

timer = { "." : dit_time, "-" : dah_time, ";" : char_space, " " : word_space }

i=0

def translator(word):
	if len(word) > 0:
		i = len(word)
		j = 0
		morseWord = [";"]
		while i > 0:
			if(word[j] == " "):
				morseWord.append(" ")
			else:
				morseWord.append(code[word[j]])
			j += 1
			morseWord.append(";")
			i -= 1
		return "".join(morseWord)
	else:
		return translator("Stupid!")

def ledBlinker(morseCode):
	if len(morseCode) > 0:
		state = False
		for character in morseCode:
			if character == ";" or character == " ":
				time.sleep(timer[character])
			else:
				GPIO.output(14,state)
				time.sleep(timer[character])
				print (character)
				state = not state
				GPIO.output(14,state)
				time.sleep(timer[character])
				state = not state
				GPIO.output(14,state)
				time.sleep(ditDah_space)

		GPIO.output(14,False)
		#time.sleep(phrase_space)
		
	else:
		ledBlinker(translator(""))

def main():
	
	if len(sys.argv) <= 1:
		print("A phrase/word was not informed!")
	else:
		# Using GPIO 14 for output
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(14, GPIO.OUT)
		j = 0
		for argument in sys.argv:
			print (argument.lower())
			if j != 0:
				print (translator(argument.lower()))
				ledBlinker(list(translator(argument.lower())))
			j += 1
	
	GPIO.cleanup()

if __name__ == '__main__':
	main()