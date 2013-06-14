#Game Introduction
print ("Welcome to Intense Wizardry, courtesy of Sipsco Games.")
print ("This game is by Maria, because I am cool.")

#Name input
print ("You are a novice-level Wizard by the name of...? ")
name = input ("> ")
print ("Welcome to Sipsco Wizard Community College,", name, "!")

#Choose first lecture
lectures = ["conjuration", "alteration", "illusion", "destruction", "restoration", "alchemy"]

from lectureDefs import *

correctInput = False

while (not correctInput):
    print ("What lecture are you headed to first?")
    for lecture in lectures:
        print ("-",lecture.title())
    userInput = input("> ").lower()
    print ("You chose", userInput, ".")

    # TODO: put these literals in lower case
    
    if userInput == "conjuration":
        correctInput = True
        conjurationLecture()
    elif userInput == "alteration":
        correctInput = True
        alterationLecture()
    elif userInput == "illusion":
        correctInput = True
        illusionLecture()
    elif userInput == "destruction":
        correctInput = True
        destructionLecture()
    elif userInput == "restoration":
        correctInput = True
        restorationLecture()
    elif userInput == "alchemy":
        correctInput = True
        alchemyLecture()
    else:
        correctInput = False
        print ("I've never heard of", userInput.lower(), "before.")
    
