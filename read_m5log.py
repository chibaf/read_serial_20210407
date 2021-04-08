import serial, sys, queue
from collections import deque
import re
import time

strPort = sys.argv[1]
ser=serial.Serial(strPort, sys.argv[2])
ser.send_break()
ser.reset_input_buffer
ser.reset_input_buffer
ser.reset_input_buffer
ser.reset_input_buffer
line_byte = ser.readline()

while True:
  line = ser.readline()
  line = line.decode(encoding='utf-8')
  nums=line.split()
  print(nums)

ser.close()
