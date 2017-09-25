import RPi.GPIO as GPIO
import sys
from time import sleep
pin=int(sys.argv[1])

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
state = GPIO.input(pin)
#print state
if (state is 1):
#    print "Encender"
    GPIO.output(pin,False)
    sleep(1)
#    print "Apagar"
    GPIO.output(pin,True)
else:
    GPIO.output(pin,True)
exit(0)
