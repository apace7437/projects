#This file contains all the functions required for guess who


#Gets a picture of the user and saves it as their name
import picamera,time

def getUserImage(name):

  try:
      with picamera.PiCamera() as camera:
          check = False
          while check == False:
             camera.resolution = (1024,768)
             camera.start_preview()
             time.sleep(2)
             filename = "{0}.jpeg".format(name)
             camera.capture(filename)
             camera.stop_preview()
             if input("Are you happy with this?"):
                 check=True
#Makes sure you don't get an error
  except picamera.exc.PiCameraMMALError:
      print("Camera not detected, please connect and restart")
      filename=""
pass

def getCharProfile():
#Gets the person's name
    name = input("What is your name?")

#Gets the person's gender
    gender = ""
    while not(gender in["male","female"]):
        gender = input("Are you male or female?")

#Gets the person's hair colour
    hair = ""
    while not(hair in["black","brown","blonde","ginger"]):
        hair = input("What is your hair colour?")

#Gets the person's eye colour
    eyes = ""
    while not(eyes in["brown","blue","green"]):
        eyes = input("What is your eye colour?")

#Asks if the person is wearing glasses
    check = False
    while check == False:
        if input("Are you wearing glasses?"):
            check=True

#Asks if the person has a beard and/or moustache
    facial hair = ""
    while not(facial hair in["moustache","beard","both"]):
        eyes = input("Do you have a beard, moustache or both?")

#Asks if the person is wearing a hat
    check = False
    while check == False:
        if input("Are you wearing a hat?"):
            check=True
