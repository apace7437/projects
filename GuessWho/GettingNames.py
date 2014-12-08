def getUserName():
    check=False
    while check == False:
       name = input("What is your name?")
       correct=input("Your name is {0}, is that correct".format(name))
       if correct.lower()=="y":
           check = True
