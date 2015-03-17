import RPi.GPIO as GPIO, time, math

pin = 17
count = 0

def spin(channel):
    global count
    count += 1
    print (count)

def calcspeed():
    r = 9
    t = 5
    CmS = ((math.pi*r)*count)/t
    KmH = (CmS/100000)*3600
    return KmH

##pin2 = 27
##count2 = 0
##
##def bucket_tipped(channel):
##    global count
##    count2 += 1
##    print (count2 * 0.2794)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin, bouncetime=300)

while True:
    count = 0
    time.sleep(5)
    calcspeed()
    windspeed = calcspeed()
    print(windspeed)
