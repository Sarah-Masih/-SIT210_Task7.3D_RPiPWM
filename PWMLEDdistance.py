import RPi.GPIO as GPIO
#Reference: https://github.com/leon-anavi/rpi-examples/blob/master/HC-SR04/python/distance.py
#Reference: electronishobbyists.com

import time
import signal
import sys
GPIO.setwarnings(False)
from time import sleep
GPIO.setmode(GPIO.BCM)
pinDist_sensor=4
pinE= 18


def Light():
    print("light")
    
    led_pin=21

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)

    pwm= GPIO.PWM(led_pin, 100)
    pwm.start(0)
    
    while True:
        
        Dist=Distance()
        #distance in cm::light brightness 
        # 5..10..15..20...20+ :: 100%..75%..50%..25%....5%
        for x in range(100):
            if(Dist<=5 and Dist>0):
                pwm.ChangeDutyCycle(100)
                sleep(0.00001)
            elif(Dist<=10 and Dist >5):
                pwm.ChangeDutyCycle(75)
                sleep(0.00001)
            elif(Dist<=15 and Dist>10):
                pwm.ChangeDutyCycle(50)
                sleep(0.00001)
            elif(Dist<=20 and Dist>15):
                pwm.ChangeDutyCycle(25)
                sleep(0.00001)
            else:
                pwm.ChangeDutyCycle(5)
                


def Distance():
    
    signal.signal(signal.SIGINT, close)

    GPIO.setup(pinDist_sensor, GPIO.OUT)
    GPIO.setup(pinE, GPIO.IN)
        
    GPIO.output(pinDist_sensor, True)
    time.sleep(0.00001)
    GPIO.output(pinDist_sensor, False)
    Begin=time.time()
    End= time.time()
    while GPIO.input(pinE)==0:
        Begin=time.time()
        
    while GPIO.input(pinE)==1:
        End=time.time()
    TimeElapsed= End - Begin
    distance =(TimeElapsed *34300)/2
    print("Distance: %.1f cm" % distance)
    print("Begin: %.1f s" % Begin)
    print("End: %.1f s" % End)
    time.sleep(1)
    return distance
        
def close(signal, frame):
    pwm.stop()
    GPIO.cleanup()
    sys.exit(0)
    
#Distance()
Light()