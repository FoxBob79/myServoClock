### The Servo-Setup ###

from pca9685 import PCA9685
from pca9685_b2 import PCA9685B2
from machine import I2C, Pin
from servo import Servos
from servo_b2 import ServosB2

sda = Pin(21)
scl = Pin(22)
id = 1
i2c = I2C(id=id, sda=sda, scl=scl)

pca = PCA9685(i2c=i2c)
pca2 = PCA9685B2(i2c=i2c)
servo = Servos(i2c=i2c)
servo2 = ServosB2(i2c=i2c)


### TEST: Eingabe ###

print("Bitte geben Sie eine Zahl für SegAnz01 ein:")

z = input()
SegAnz01 = int(z)

print("Bitte geben Sie eine Zahl für SegAnz02 ein:")

y = input()
SegAnz02 = int(y)

print("Bitte geben Sie eine Zahl für SegAnz03 ein:")

x = input()
SegAnz03 = int(x)



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

