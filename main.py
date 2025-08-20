############################
### myServoClock Projekt ###
###      FoxBob79        ###
###        2025          ###
############################


### The Servo- and PCA9685 Setup ###

from pca9685 import PCA9685
from pca9685_b2 import PCA9685B2
from machine import I2C, Pin
from servo import Servos
from servo_b2 import ServosB2

sda = Pin(21)                                           # sda Pin ESP32
scl = Pin(22)                                           # scl Pin ESP32
id = 1
i2c = I2C(id=id, sda=sda, scl=scl)

pca = PCA9685(i2c=i2c)                                  # PCA9685 Board #1
pca2 = PCA9685B2(i2c=i2c)                               # PCA9685 Board #2
servo = Servos(i2c=i2c)                                 # Servos @ Board #1
servo2 = ServosB2(i2c=i2c)                              # Servos @ Board #2


### The Time and Clock Setup ###

import time

# Winterzeit / Sommerzeit
#GMT_OFFSET = 3600 * 1 # 3600 = 1 h (Winterzeit)
GMT_OFFSET = 3600 * 2 # 3600 = 1 h (Sommerzeit)


# NTP-Host
NTP_HOST = "pool.ntp.org"


# Funktion: Zeit per NTP holen
def getTimeNTP():
    NTP_DELTA = 2208988800
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = socket.getaddrinfo(NTP_HOST, 123)[0][-1]
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    finally:
        s.close()
    ntp_time = struct.unpack("!I", msg[40:44])[0]
    return time.gmtime(ntp_time - NTP_DELTA + GMT_OFFSET)

# Funktion: RTC-Zeit setzen
def setTimeRTC():
    # NTP-Zeit holen
    tm = getTimeNTP()
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6]+1, tm[3], tm[4], tm[5], 0))


# Zeit setzen
setTimeRTC()


# Aktuelles Datum und Uhrzeit einlesen
rtc = machine.RTC()
datetime = rtc.datetime()


# Aktuelles Datum und Uhrzeit ausgeben
print('Tuple:', datetime)
print()
print('     Jahr:', datetime[0])
print('    Monat:', datetime[1])
print('      Tag:', datetime[2])
print('Wochentag:', datetime[3])
print('   Stunde:', datetime[4])
print('   Minute:', datetime[5])
print('  Sekunde:', datetime[6])


# Aktuelle Stunden an SegAnz01 und SegAnz02 übergeben
std= datetime[4]
sz = int(std) // 10
se = int(std) % 10

SegAnz01 = int(sz)
SegAnz02 = int(se)


# Aktuelle Minuten an SegAnz03 und SegAnz04 übergeben
min = datetime[5]
mz = int(min) // 10
me = int(min) % 10

SegAnz03 = int(mz)
SegAnz04 = int(me)


### Servo Position SegmentAnzeige 01 ###

if SegAnz01 == 1:
    servo.position(index=0, degrees=180)
    servo.position(index=1, degrees=90)
    servo.position(index=2, degrees=90)
    servo.position(index=3, degrees=180)
    servo.position(index=4, degrees=0)
    servo.position(index=5, degrees=180)
    servo.position(index=6, degrees=0)
elif SegAnz01 == 2:
    servo.position(index=0, degrees=90)
    servo.position(index=1, degrees=90)
    servo.position(index=2, degrees=180)
    servo.position(index=3, degrees=90)
    servo.position(index=4, degrees=90)
    servo.position(index=5, degrees=180)
    servo.position(index=6, degrees=90)
elif SegAnz01 == 3:
    servo.position(index=0, degrees=90)
    servo.position(index=1, degrees=90)
    servo.position(index=2, degrees=90)
    servo.position(index=3, degrees=90)
    servo.position(index=4, degrees=0)
    servo.position(index=5, degrees=180)
    servo.position(index=6, degrees=90)
elif SegAnz01 == 4:
    servo.position(index=0, degrees=180)
    servo.position(index=1, degrees=90)
    servo.position(index=2, degrees=90)
    servo.position(index=3, degrees=180)
    servo.position(index=4, degrees=0)
    servo.position(index=5, degrees=90)
    servo.position(index=6, degrees=90)
elif SegAnz01 == 5:
    servo.position(index=0, degrees=90)
    servo.position(index=1, degrees=0)
    servo.position(index=2, degrees=90)
    servo.position(index=3, degrees=90)
    servo.position(index=4, degrees=0)
    servo.position(index=5, degrees=90)
    servo.position(index=6, degrees=90)
elif SegAnz01 == 6:
    servo.position(index=0, degrees=90)
    servo.position(index=1, degrees=0)
    servo.position(index=2, degrees=90)
    servo.position(index=3, degrees=90)
    servo.position(index=4, degrees=90)
    servo.position(index=5, degrees=90)
    servo.position(index=6, degrees=90)
elif SegAnz01 == 7:
    servo.position(index=0, degrees=90)
    servo.position(index=1, degrees=90)
    servo.position(index=2, degrees=90)
    servo.position(index=3, degrees=180)
    servo.position(index=4, degrees=0)
    servo.position(index=5, degrees=180)
    servo.position(index=6, degrees=0)
elif SegAnz01 == 8:
    servo.position(index=0, degrees=90)
    servo.position(index=1, degrees=90)
    servo.position(index=2, degrees=90)
    servo.position(index=3, degrees=90)
    servo.position(index=4, degrees=90)
    servo.position(index=5, degrees=90)
    servo.position(index=6, degrees=90)
elif SegAnz01 == 9:
    servo.position(index=0, degrees=90)
    servo.position(index=1, degrees=90)
    servo.position(index=2, degrees=90)
    servo.position(index=3, degrees=90)
    servo.position(index=4, degrees=0)
    servo.position(index=5, degrees=90)
    servo.position(index=6, degrees=90)
elif SegAnz01 == 0:
    servo.position(index=0, degrees=90)
    servo.position(index=1, degrees=90)
    servo.position(index=2, degrees=90)
    servo.position(index=3, degrees=90)
    servo.position(index=4, degrees=90)
    servo.position(index=5, degrees=90)
    servo.position(index=6, degrees=0)
else:
    servo.position(index=0, degrees=180)
    servo.position(index=1, degrees=0)
    servo.position(index=2, degrees=180)
    servo.position(index=3, degrees=180)
    servo.position(index=4, degrees=0)
    servo.position(index=5, degrees=180)
    servo.position(index=6, degrees=0)


### Servo Position SegmentAnzeige 02 ###

if SegAnz02 == 1:
    servo.position(index=8, degrees=180)
    servo.position(index=9, degrees=90)
    servo.position(index=10, degrees=90)
    servo.position(index=11, degrees=180)
    servo.position(index=12, degrees=0)
    servo.position(index=13, degrees=180)
    servo.position(index=14, degrees=0)
elif SegAnz02 == 2:
    servo.position(index=8, degrees=90)
    servo.position(index=9, degrees=90)
    servo.position(index=10, degrees=180)
    servo.position(index=11, degrees=90)
    servo.position(index=12, degrees=90)
    servo.position(index=13, degrees=180)
    servo.position(index=14, degrees=90)
elif SegAnz02 == 3:
    servo.position(index=8, degrees=90)
    servo.position(index=9, degrees=90)
    servo.position(index=10, degrees=90)
    servo.position(index=11, degrees=90)
    servo.position(index=12, degrees=0)
    servo.position(index=13, degrees=180)
    servo.position(index=14, degrees=90)
elif SegAnz02 == 4:
    servo.position(index=8, degrees=180)
    servo.position(index=9, degrees=90)
    servo.position(index=10, degrees=90)
    servo.position(index=11, degrees=180)
    servo.position(index=12, degrees=0)
    servo.position(index=13, degrees=90)
    servo.position(index=14, degrees=90)
elif SegAnz02 == 5:
    servo.position(index=8, degrees=90)
    servo.position(index=9, degrees=0)
    servo.position(index=10, degrees=90)
    servo.position(index=11, degrees=90)
    servo.position(index=12, degrees=0)
    servo.position(index=13, degrees=90)
    servo.position(index=14, degrees=90)
elif SegAnz02 == 6:
    servo.position(index=8, degrees=90)
    servo.position(index=9, degrees=0)
    servo.position(index=10, degrees=90)
    servo.position(index=11, degrees=90)
    servo.position(index=12, degrees=90)
    servo.position(index=13, degrees=90)
    servo.position(index=14, degrees=90)
elif SegAnz02 == 7:
    servo.position(index=8, degrees=90)
    servo.position(index=9, degrees=90)
    servo.position(index=10, degrees=90)
    servo.position(index=11, degrees=180)
    servo.position(index=12, degrees=0)
    servo.position(index=13, degrees=180)
    servo.position(index=14, degrees=0)
elif SegAnz02 == 8:
    servo.position(index=8, degrees=90)
    servo.position(index=9, degrees=90)
    servo.position(index=10, degrees=90)
    servo.position(index=11, degrees=90)
    servo.position(index=12, degrees=90)
    servo.position(index=13, degrees=90)
    servo.position(index=14, degrees=90)
elif SegAnz02 == 9:
    servo.position(index=8, degrees=90)
    servo.position(index=9, degrees=90)
    servo.position(index=10, degrees=90)
    servo.position(index=11, degrees=90)
    servo.position(index=12, degrees=0)
    servo.position(index=13, degrees=90)
    servo.position(index=14, degrees=90)
elif SegAnz02 == 0:
    servo.position(index=8, degrees=90)
    servo.position(index=9, degrees=90)
    servo.position(index=10, degrees=90)
    servo.position(index=11, degrees=90)
    servo.position(index=12, degrees=90)
    servo.position(index=13, degrees=90)
    servo.position(index=14, degrees=0)
else:
    servo.position(index=8, degrees=180)
    servo.position(index=9, degrees=0)
    servo.position(index=10, degrees=180)
    servo.position(index=11, degrees=180)
    servo.position(index=12, degrees=0)
    servo.position(index=13, degrees=180)
    servo.position(index=14, degrees=0)


### Servo Position SegmentAnzeige 03 ###

if SegAnz03 == 1:
    servo2.position(index=0, degrees=180)
    servo2.position(index=1, degrees=90)
    servo2.position(index=2, degrees=90)
    servo2.position(index=3, degrees=180)
    servo2.position(index=4, degrees=0)
    servo2.position(index=5, degrees=180)
    servo2.position(index=6, degrees=0)
elif SegAnz03 == 2:
    servo2.position(index=0, degrees=90)
    servo2.position(index=1, degrees=90)
    servo2.position(index=2, degrees=180)
    servo2.position(index=3, degrees=90)
    servo2.position(index=4, degrees=90)
    servo2.position(index=5, degrees=180)
    servo2.position(index=6, degrees=90)
elif SegAnz03 == 3:
    servo2.position(index=0, degrees=90)
    servo2.position(index=1, degrees=90)
    servo2.position(index=2, degrees=90)
    servo2.position(index=3, degrees=90)
    servo2.position(index=4, degrees=0)
    servo2.position(index=5, degrees=180)
    servo2.position(index=6, degrees=90)
elif SegAnz03 == 4:
    servo2.position(index=0, degrees=180)
    servo2.position(index=1, degrees=90)
    servo2.position(index=2, degrees=90)
    servo2.position(index=3, degrees=180)
    servo2.position(index=4, degrees=0)
    servo2.position(index=5, degrees=90)
    servo2.position(index=6, degrees=90)
elif SegAnz03 == 5:
    servo2.position(index=0, degrees=90)
    servo2.position(index=1, degrees=0)
    servo2.position(index=2, degrees=90)
    servo2.position(index=3, degrees=90)
    servo2.position(index=4, degrees=0)
    servo2.position(index=5, degrees=90)
    servo2.position(index=6, degrees=90)
elif SegAnz03 == 6:
    servo2.position(index=0, degrees=90)
    servo2.position(index=1, degrees=0)
    servo2.position(index=2, degrees=90)
    servo2.position(index=3, degrees=90)
    servo2.position(index=4, degrees=90)
    servo2.position(index=5, degrees=90)
    servo2.position(index=6, degrees=90)
elif SegAnz03 == 7:
    servo2.position(index=0, degrees=90)
    servo2.position(index=1, degrees=90)
    servo2.position(index=2, degrees=90)
    servo2.position(index=3, degrees=180)
    servo2.position(index=4, degrees=0)
    servo2.position(index=5, degrees=180)
    servo2.position(index=6, degrees=0)
elif SegAnz03 == 8:
    servo2.position(index=0, degrees=90)
    servo2.position(index=1, degrees=90)
    servo2.position(index=2, degrees=90)
    servo2.position(index=3, degrees=90)
    servo2.position(index=4, degrees=90)
    servo2.position(index=5, degrees=90)
    servo2.position(index=6, degrees=90)
elif SegAnz03 == 9:
    servo2.position(index=0, degrees=90)
    servo2.position(index=1, degrees=90)
    servo2.position(index=2, degrees=90)
    servo2.position(index=3, degrees=90)
    servo2.position(index=4, degrees=0)
    servo2.position(index=5, degrees=90)
    servo2.position(index=6, degrees=90)
elif SegAnz03 == 0:
    servo2.position(index=0, degrees=90)
    servo2.position(index=1, degrees=90)
    servo2.position(index=2, degrees=90)
    servo2.position(index=3, degrees=90)
    servo2.position(index=4, degrees=90)
    servo2.position(index=5, degrees=90)
    servo2.position(index=6, degrees=0)
else:
    servo2.position(index=0, degrees=180)
    servo2.position(index=1, degrees=0)
    servo2.position(index=2, degrees=180)
    servo2.position(index=3, degrees=180)
    servo2.position(index=4, degrees=0)
    servo2.position(index=5, degrees=180)
    servo2.position(index=6, degrees=0)

### Servo Position SegmentAnzeige 04 ###

if SegAnz04 == 1:
    servo2.position(index=8, degrees=180)
    servo2.position(index=9, degrees=90)
    servo2.position(index=10, degrees=90)
    servo2.position(index=11, degrees=180)
    servo2.position(index=12, degrees=0)
    servo2.position(index=13, degrees=180)
    servo2.position(index=14, degrees=0)
elif SegAnz04 == 2:
    servo2.position(index=8, degrees=90)
    servo2.position(index=9, degrees=90)
    servo2.position(index=10, degrees=180)
    servo2.position(index=11, degrees=90)
    servo2.position(index=12, degrees=90)
    servo2.position(index=13, degrees=180)
    servo2.position(index=14, degrees=90)
elif SegAnz04 == 3:
    servo2.position(index=8, degrees=90)
    servo2.position(index=9, degrees=90)
    servo2.position(index=10, degrees=90)
    servo2.position(index=11, degrees=90)
    servo2.position(index=12, degrees=0)
    servo2.position(index=13, degrees=180)
    servo2.position(index=14, degrees=90)
elif SegAnz04 == 4:
    servo2.position(index=8, degrees=180)
    servo2.position(index=9, degrees=90)
    servo2.position(index=10, degrees=90)
    servo2.position(index=11, degrees=180)
    servo2.position(index=12, degrees=0)
    servo2.position(index=13, degrees=90)
    servo2.position(index=14, degrees=90)
elif SegAnz04 == 5:
    servo2.position(index=8, degrees=90)
    servo2.position(index=9, degrees=0)
    servo2.position(index=10, degrees=90)
    servo2.position(index=11, degrees=90)
    servo2.position(index=12, degrees=0)
    servo2.position(index=13, degrees=90)
    servo2.position(index=14, degrees=90)
elif SegAnz04 == 6:
    servo2.position(index=8, degrees=90)
    servo2.position(index=9, degrees=0)
    servo2.position(index=10, degrees=90)
    servo2.position(index=11, degrees=90)
    servo2.position(index=12, degrees=90)
    servo2.position(index=13, degrees=90)
    servo2.position(index=14, degrees=90)
elif SegAnz04 == 7:
    servo2.position(index=8, degrees=90)
    servo2.position(index=9, degrees=90)
    servo2.position(index=10, degrees=90)
    servo2.position(index=11, degrees=180)
    servo2.position(index=12, degrees=0)
    servo2.position(index=13, degrees=180)
    servo2.position(index=14, degrees=0)
elif SegAnz04 == 8:
    servo2.position(index=8, degrees=90)
    servo2.position(index=9, degrees=90)
    servo2.position(index=10, degrees=90)
    servo2.position(index=11, degrees=90)
    servo2.position(index=12, degrees=90)
    servo2.position(index=13, degrees=90)
    servo2.position(index=14, degrees=90)
elif SegAnz04 == 9:
    servo2.position(index=8, degrees=90)
    servo2.position(index=9, degrees=90)
    servo2.position(index=10, degrees=90)
    servo2.position(index=11, degrees=90)
    servo2.position(index=12, degrees=0)
    servo2.position(index=13, degrees=90)
    servo2.position(index=14, degrees=90)
elif SegAnz04 == 0:
    servo2.position(index=8, degrees=90)
    servo2.position(index=9, degrees=90)
    servo2.position(index=10, degrees=90)
    servo2.position(index=11, degrees=90)
    servo2.position(index=12, degrees=90)
    servo2.position(index=13, degrees=90)
    servo2.position(index=14, degrees=0)
else:
    servo2.position(index=8, degrees=180)
    servo2.position(index=9, degrees=0)
    servo2.position(index=10, degrees=180)
    servo2.position(index=11, degrees=180)
    servo2.position(index=12, degrees=0)
    servo2.position(index=13, degrees=180)
    servo2.position(index=14, degrees=0)
