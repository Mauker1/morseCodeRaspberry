import piface.pfio as pfio
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
                                pfio.digital_write(0,state)
                                time.sleep(timer[character])
                                print (character)
                                state = not state
                                pfio.digital_write(0,state)
                                time.sleep(timer[character])
                                state = not state
                                pfio.digital_write(0,state)
                                time.sleep(ditDah_space)

                pfio.digital_write(0,False)
                #time.sleep(phrase_space) - Use on future release...

        else:
                ledBlinker(translator(""))

def main():

        if len(sys.argv) <= 1:
                print("A phrase/word was not informed!!")
        else:
                pfio.init()
                j = 0
                for argument in sys.argv:
                        print (argument.lower())
                        if j != 0:
                                print (translator(argument.lower()))
                                ledBlinker(list(translator(argument.lower())))
                        j += 1
                pfio.deinit()

if __name__ == '__main__':
        main()
