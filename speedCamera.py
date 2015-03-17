import time, json, math, RPi.GPIO as GPIO

def saveSpeeders():
    speeders

t1 = int(input("What is the time the car enters the monitered zone (secs)?"))
t2 = int(input("What is the time the car exits the monitered zone (secs)?"))

distance = 1

speed = distance/(t2-t1)

print(str(speed) + "miles/min")
    
speeders = speed > 1
