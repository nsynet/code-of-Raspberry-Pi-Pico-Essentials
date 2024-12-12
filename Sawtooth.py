#----------------------------------------------------------
#		GENERATE TRIANGLE WAVEFORM
#		==========================
#
# In this project a MCP4921 type DAC chip is connected to the
# Raspberry Pi Pico.The program generates triangle waveform
# 
# Author: Dogan Ibrahim
# File  : Triangle.py
# Date  : February 2021
#------------------------------------------------------------
from machine import Pin, SPI
import utime

spi_sck = Pin(2)					# SCK pin at GP2
spi_tx = Pin(3)						# TX pin at GP3
spi_rx = Pin(0)						# RX pin at GP0 (not used)

spi = SPI(0,sck=spi_sck,mosi=spi_tx,miso=spi_rx,baudrate=100000)

CS = Pin(16, Pin.OUT)					# CS
CS.value(1)								# Disable chip

def Voltage(V):
    Amplitude = int(V * 4095 / 3300)
    return Amplitude
    
def DAC(data):
    buff = [0, 0]
    buff[0] = (data >> 8) & 0x0F		# HIGH byte
    buff[0] = buff[0] + 0x30
    buff[1] = data & 0xFF				# LOW byte
    CS.value(0)							# Enable MCP4921
    spi.write(bytearray(buff))			# Send to SPI bus
    CS.value(1)							# DIsable MCP4921

#
# Main program
#
while True:
    k = 0.0
    while k < 1.0:                      # Going up
        DAC(int(Voltage(k*3300)))
        utime.sleep_ms(1)
        k = k + 0.1
    
    k = 1.0
    while k > 0.0:                      # Going down
        DAC(int(Voltage(k*3300)))
        utime.sleep_ms(1)
        k = k - 0.1
        
        
