import serial
import time
ser = serial.Serial('/dev/ttyACM0', 38400, timeout=1) # 38400 is the baudrate, feel free to change
ser.reset_input_buffer()
while True:
  ser.write(bytes("hi", 'UTF-8')) # sends string to arduino
  time.sleep(1)

