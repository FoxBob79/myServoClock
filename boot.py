### The BASIC BOOT SETUP ###

try:
  import usocket as socket
except:
  import socket

import machine
import esp
esp.osdebug(None)
#import esp32
#import webrepl
#webrepl.start()

import gc
gc.collect()

### WLAN-Setup ###

import network

ssid = "yourWLANname"
password = "xxxxxxxxxxxx"

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print("Connection successful")
print(station.ifconfig())

### I2C Bus Setup ###
from machine import Pin, PWM, I2C

i2c = I2C(0)
i2c = I2C(1, scl=Pin(22), sda=Pin(21), freq=400000)
