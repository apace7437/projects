import RPi.GPIO as GPIO, time, math

pin = 17
count = 0

def spin(channel):
    global count
    count += 1
    print (count)

def calcspeed():
    global count
    r = 9
    t = 5
    CalcSpeed = ((math.pi*r)*count)/t
    return CalcSpeed

def KmpH():
    KmS = (CalcSpeed/100000)
    KmH = (KmS * 3600)

pin2 = 27
count2 = 0

def bucket_tipped(channel):
    global count
    count2 += 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin, bouncetime=300)

input("Press enter to begin.")
while True:
    count = 0
    time.sleep(5)
    print("Rainfall is {0}".format(count2 *0.2794))
    print("Windspeed is {0}".format(count))
