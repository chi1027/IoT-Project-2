import time
import RPi.GPIO as GPIO
import DAI_main
import Line_notifier as notifier

f = open('a.txt', 'r')
w = f.read()
notifier.line_message(str(w))
f.close()

