import RPi.GPIO as GP,time
GP.setmode(GP.BOARD)
GP.setup(11,GP.OUT)

#defining dot
def dot():
    GP.output(11,GP.HIGH)
    time.sleep(0.5)
    GP.output(11,GP.LOW)
    time.sleep(1)

#defining dash
def dash():
    GP.output(11,GP.HIGH)
    time.sleep(1.5)
    GP.output(11,GP.LOW)
    time.sleep(1)

def Morse(letter):
  if letter=="a":
      dot()
      dash()
  elif letter=="b":
      dash()
      dot()
      dot()
      dot()
  elif letter=="c":
      dash()
      dot()
      dash()
      dot()
  elif letter=="d":
      dash()
      dot()
      dot()
  elif letter=="e":
      dot()
  elif letter=="f":
      dot()
      dot()
      dash()
      dot()
  elif letter=="g":
      dash()
      dash()
      dot()
  elif letter=="h":
      dot()
      dot()
      dot()
      dot()
  elif letter=="i":
      dot()
      dot()
  elif letter=="j":
      dot()
      dash()
      dash()
      dash()
  elif letter=="k":
      dash()
      dot()
      dash()
  elif letter=="l":
      dot()
      dash()
      dot()
      dot()
  elif letter=="m":
      dash()
      dash()
  elif letter=="n":
      dash()
      dot()
  elif letter=="o":
      dash()
      dash()
      dash()
  elif letter=="p":
      dot()
      dash()
      dash()
      dot()
  elif letter=="q":
      dash()
      dash()
      dot()
      dash()
  elif letter=="r":
      dot()
      dash()
      dot()
  elif letter=="s":
      dot()
      dot()
      dot()
  elif letter=="t":
      dash()
  elif letter=="u":
      dot()
      dot()
      dash()
  elif letter=="v":
      dot()
      dot()
      dot()
      dash()
  elif letter=="w":
      dot()
      dash()
      dash()
  elif letter=="x":
      dash()
      dot()
      dot()
      dash()
  elif letter=="y":
      dash()
      dot()
      dash()
      dash()
  elif letter=="z":
      dash()
      dash()
      dot()
      dot()

msg = input("Enter message")
for each in msg:
    Morse(each)
    print(each)

  
  
      
      
  
      
    
  




