#This file contains all the functions required for guess who


#Gets a picture of the user and saves it as their name
import picamera,time,json

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
                valid = input("Are you happy with this?")
                if valid =="yes" or valid =="y":
                    check=True
#Makes sure you don't get an error
    except picamera.exc.PiCameraMMALError:
        print("Camera not detected, please connect and restart")
        filename=""
    return filename




#Gets the person's name
def getCharProfile():
    name = input("What is your name?")
    filename=getUserImage(name)

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
    if input("Are you wearing glasses y/n?").upper()=="y":
        glasses=True
    else:
        glasses=False

#Asks if the person has a beard and/or moustache
    facialHair = ""
    while not(facialHair in["moustache","beard","both","no"]):
        facialHair = input("Do you have a beard, moustache or both?")

#Asks if the person is wearing a hat
    if input("Are you wearing a hat y/n?").upper()=="y":
        glasses=True
    else:
        glasses=False

    return(name,gender,hair,eyes,glasses,facialHair,filename)

def loadPeople():
    try:
        with open ("person",mode="r") as file:
            people = json.load(file)
    except IOError:
        print("No people found")
        people = []
    return people

people = loadPeople()

def savePeople():
    person = getCharProfile()
    people.append(person)
    with open("person",mode="w") as file:
        json.dump(people, file)
