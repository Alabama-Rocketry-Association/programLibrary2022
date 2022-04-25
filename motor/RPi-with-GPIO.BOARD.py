import RPi.GPIO as GPIO
from time import sleep

DIR = 8  # PIN NUMBERS
STEP = 10  # PIN NUMBERS
ENABLE = 12  # PIN NUMBERS

CW = 1  # CW is backward
CCW = 0  # CCW is forward

GPIO.setmode(GPIO.BOARD)  # allows for the pin layout that raspi uses

# sets the pins for the different data
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(ENABLE, GPIO.OUT)

GPIO.output(DIR, CW)  # presets direction
GPIO.output(ENABLE, GPIO.HIGH)  # stops power draw

while True:
    sleep(1.0)  # unnecessary i think
    GPIO.output(DIR, CW)  # sets the direction, give it time before switching direction
    for x in range(400):  # change the range for how long it runs
        GPIO.output(STEP, GPIO.HIGH)  # alternates to allow the stepper to run
        
        sleep(.001)  # do not change
        
        GPIO.output(STEP, GPIO.LOW)  # alternates to allow the stepper to run
        
        sleep(.001)  # do not change
        GPIO.output(ENABLE, GPIO.HIGH)  # stops power draw
    sleep(1.0)
    GPIO.output(DIR, CCW)  # sets the direction, give it time before switching direction
    for x in range(400):  # change the range for how long it runs
        GPIO.output(STEP, GPIO.HIGH)  # alternates to allow the stepper to run

        sleep(.001)  # do not change

        GPIO.output(STEP, GPIO.LOW)  # alternates to allow the stepper to run

        sleep(.001)  # do not change
        GPIO.output(ENABLE, GPIO.HIGH)  # stops power draw





