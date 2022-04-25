from time import sleep
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

motors = MotorKit(address=0x60)


while True:
    step_count = int(input("Step count: "))
    if step_count>=0:
        dir=stepper.FORWARD
    if step_count<0:
        dir=stepper.BACKWARD
    step_count=abs(step_count)
    for i in range(step_count):
        motors.stepper2.onestep(style=stepper.DOUBLE, direction=dir) #FORWARD or BACKWARD
        sleep(.001)
    
    motors.stepper2.release()
    
#200 steps = 1 rotation
