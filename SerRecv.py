#----------------------------------------------------------
#		SERIAL LINK - READ DATA FROM ARDUINO
#		====================================
#
# This project reads data from the Arduino Uno and displays
# on the Thonny screen
#
# Author: Dogan Ibrahim
# File  : SerRecv.py
# Date  : February 2011
#------------------------------------------------------------
from machine import UART

uart = UART(0, 9600)

while True:								# Do forever
    line = uart.readline()
    enc = line.decode('utf-8')
    print(enc)