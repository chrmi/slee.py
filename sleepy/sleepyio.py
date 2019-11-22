import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

import sleepystate
import sleepyaudio

L_pin = 27 
R_pin = 23 
C_pin = 4 
U_pin = 17 
D_pin = 22 

A_pin = 5 
B_pin = 6 

GPIO.setmode(GPIO.BCM) 
GPIO.setup(A_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(B_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(L_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(R_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(U_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(D_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
GPIO.setup(C_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

def update():
    if not GPIO.input(U_pin) or not GPIO.input(L_pin): 
        sleepystate.selectPrevious()
    if not GPIO.input(D_pin) or not GPIO.input(R_pin): 
        sleepystate.selectNext()
    if not GPIO.input(C_pin) or not GPIO.input(B_pin):
        sleepystate.playSelected()
        sleepyaudio.changeTrack() 
        sleepystate.unpause()
    if not GPIO.input(A_pin):
        sleepystate.pause()

