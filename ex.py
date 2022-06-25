import serial
import sys
import time
import RPi.GPIO as gpio
import csv


ser = serial.Serial('/dev/serial0')
ser.baudrate = 921600
gpio.setwarnings(False)
gpio.setmode(gpio.BCM)

dtUpLeft = 6
sckUpLeft = 5

dtDownLeft = 19
sckDownLeft = 13

dtUpRight = 3
sckUpRight = 2

dtDownRight = 17
sckDownRight = 4

sampleUpLeft = 0
sampleDownLeft = 0
sampleUpRight = 0
sampleDownRight = 0
def readCountUpLeft():
  i=0
  Count=0
  gpio.setup(dtUpLeft, gpio.OUT)
  gpio.setup(sckUpLeft, gpio.OUT)
  gpio.output(dtUpLeft,1)
  gpio.output(sckUpLeft,0)
  gpio.setup(dtUpLeft, gpio.IN)

  while gpio.input(dtUpLeft) == 1:
      i=0
  for i in range(24):
        gpio.output(sckUpLeft,1)
        Count=Count<<1

        gpio.output(sckUpLeft,0)
        #time.sleep(0.001)
        if gpio.input(dtUpLeft) == 0:
            Count=Count+1
  gpio.output(sckUpLeft,1)
  Count=Count^0x800000
  gpio.output(sckUpLeft,0)
  return Count

def readCountDownLeft():
  i=0
  Count=0
  gpio.setup(dtDownLeft, gpio.OUT)
  gpio.setup(sckDownLeft, gpio.OUT)
  gpio.output(dtDownLeft,1)
  gpio.output(sckDownLeft,0)
  gpio.setup(dtDownLeft, gpio.IN)

  while gpio.input(dtDownLeft) == 1:
      i=0
  for i in range(24):
        gpio.output(sckDownLeft,1)
        Count=Count<<1

        gpio.output(sckDownLeft,0)
        #time.sleep(0.001)
        if gpio.input(dtDownLeft) == 0:
            Count=Count+1
  gpio.output(sckDownLeft,1)
  Count=Count^0x800000
  gpio.output(sckDownLeft,0)
  return Count
def readCountUpRight():
  i=0
  Count=0
  gpio.setup(dtUpRight, gpio.OUT)
  gpio.setup(sckUpRight, gpio.OUT)
  gpio.output(dtUpRight,1)
  gpio.output(sckUpRight,0)
  gpio.setup(dtUpRight, gpio.IN)

  while gpio.input(dtUpRight) == 1:
      i=0
  for i in range(24):
        gpio.output(sckUpRight,1)
        Count=Count<<1

        gpio.output(sckUpRight,0)
        #time.sleep(0.001)
        if gpio.input(dtUpRight) == 0:
            Count=Count+1
  gpio.output(sckUpRight,1)
  Count=Count^0x800000
  gpio.output(sckUpRight,0)
  return Count
def readCountDownRight():
  i=0
  Count=0
  gpio.setup(dtDownRight, gpio.OUT)
  gpio.setup(sckDownRight, gpio.OUT)
  gpio.output(dtDownRight,1)
  gpio.output(sckDownRight,0)
  gpio.setup(dtDownRight, gpio.IN)

  while gpio.input(dtDownRight) == 1:
      i=0
  for i in range(24):
        gpio.output(sckDownRight,1)
        Count=Count<<1

        gpio.output(sckDownRight,0)
        #time.sleep(0.001)
        if gpio.input(dtDownRight) == 0:
            Count=Count+1
  gpio.output(sckDownRight,1)
  Count=Count^0x800000
  gpio.output(sckDownRight,0)
  return Count

sampleUpLeft = readCountUpLeft()
sampleDownLeft = readCountDownLeft()
sampleUpRight = readCountUpRight()
sampleDownRight = readCountDownRight()


cuv = input()
startTime = time.time()
while True:
	countUpLeft = readCountUpLeft()
	countDownLeft = readCountDownLeft()
	countUpRight = readCountUpRight()
	countDownRight = readCountDownRight()
	
	wUpRight = 0
	wDownRight = 0
	wUpLeft = 0
	wDownLeft = 0
	
	wUpLeft = (countUpLeft-sampleUpLeft)/160
	wDownLeft = (countDownLeft-sampleDownLeft)/160
	wUpRight = (countUpRight-sampleUpRight)/160
	wDownRight = (countDownRight-sampleDownRight)/160
	t = time.time()-startTime
	print({'UpRight': wUpRight,'DownRight': wDownRight,'UpLeft': wUpLeft, 'DownLeft': wDownLeft, 'Time': t})
	with open (cuv, 'a') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow([wUpRight,wDownRight,wUpLeft,wDownLeft,t])
    
#f.close()


    
    
        
