import datetime, json, math, RPi.GPIO as GPIO

def saveSpeeders():
    speeders

t1 = datetime.datetime.utcnow()
t2 = datetime.datetime.utcnow()

distance = 1

speed = distance/abs(t2-t1)

print(str(speed) + "miles/min")

speeders = speed > 60

numPlates = ["AD54SGY","YZ76YSE","ZA90ABC","AAAAAAA","JDHVB76","AB12CIA"] 
with open("numPlates.txt","w") as numPlates_file:
    for plate in numPlates:
        numPlates_file.write(plate+"\n")
