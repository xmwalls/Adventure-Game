#Xavier Walls
#4/24/2020 as of now

import random
import time

#main function
def adventure():
  global name
  name = requestString("What is your name hero?")
  intro()
  

#introduction to the game and story
def intro():
  showInformation("Welcome to my castle "+name+".\nHere take this map with you, it will help you navigate.\nThank you for helping me find my treasure\nWell at the cost of the monster of course.\nOh yeah, I forgot\ndont get killed by the mosnter!\nGood luck "+name+"!")
  pictureCas = makePicture(getMediaPath("Castle.png")) 
  door1 = makeSound(getMediaPath("door1.wav"))
  play(door1)
  show(pictureCas)
  showEnt()



#Each rooms text and encounters
def showLib():
  play(makeSound(getMediaPath("door1.wav")))
  time.sleep(1)
  show(makePicture(getMediaPath("library.png")))
  time.sleep(1)
  randomEncounter()
  showInformation("You are in the Libary.\nTheir is a door to the north and to the west")
  while true:
    selection = requestString("Door selction")
    if selection == "north":
      showArm()
    if selection == "west":
      showEnt()
    else:
      showInformation("Invalid Response")

def showArm():
  play(makeSound(getMediaPath("door1.wav")))
  time.sleep(1)
  show(makePicture(getMediaPath("armory.png")))
  time.sleep(1)
  randomEncounter()
  showInformation("You are in the Armory.\nTheir is a door to the east, to the west, and to the south")
  while true:
    selection = requestString("Door selction")
    if selection == "east":
      showSpiral()
    if selection == "west":
      showNorthGH()
    if selection == "south":
      showLib()
    else:
      showInformation("Invalid Response")

def showBed():
  play(makeSound(getMediaPath("door1.wav")))
  time.sleep(1)
  show(makePicture(getMediaPath("bedroom.png")))
  time.sleep(1)
  randomEncounter()
  showInformation("You are in the Bedroom.\nTheir is a door to south and to the east")
  while true:
    selection = requestString("Door selction")
    if selection == "south":
      showDin()
    if selection == "east":
      showNorthGH()
    else:
      showInformation("Invalid Response")

def showDin():
  play(makeSound(getMediaPath("door1.wav")))
  time.sleep(1)
  show(makePicture(getMediaPath("dinHall.png")))
  time.sleep(1)
  randomEncounter()
  showInformation("You are in the Dining Hall.\nTheir is a door to north and to the east")
  while true:
    selection = requestString("Door selction")
    if selection == "north":
      showBed()
    if selection == "east":
      showEnt()
    else:
      showInformation("Invalid Response")

def showSp():
  play(makeSound(getMediaPath("door1.wav")))
  time.sleep(1)
  show(makePicture(getMediaPath("spiral.png")))
  time.sleep(1)
  randomEncounter()
  showInformation("You are in the Spiral.\nTheir is a door to the south")
  while true:
    selection = requestString("Door selction")
    if selection == "south":
      showArm()
    else:
      showInformation("Invalid Response")

def showEnt():
  show(makePicture(getMediaPath("entrance.png")))
  showInformation("You are at the entrence.\nTheir is a door to east and to the west.\n Also you may advance to the end of the hall.\nHowever if you advance the monstercan kill you")
  while true:
    selection = requestString("Door selction or advance")
    if selection == "advance":
      showNorthGH()
    if selection == "east":
      showLib()
    if selection == "west":
      showDin()
    else:
      showInformation("Invalid Response")

def showNorthGH():
  play(makeSound(getMediaPath("footsteps1.wav")))
  time.sleep(3)
  show(makePicture(getMediaPath("northGreatHall.png")))
  time.sleep(1)
  randomEncounter()
  showInformation("You are at the end of the hall.\nTheir is a door to the east and to the west\nor you can go back down the hall.")
  while true:
    selection = requestString("Door selction or go back")
    if selection == "go back":
      play(makeSound(getMediaPath("footsteps1.wav")))
      showEnt()
    if selection == "east":
      showLib()
    if selection == "west":
      showDin()
    else:
      showInformation("Invalid Response")
  
#Random encounters based on treasure:20%, no treasure:60%, death:20%
#Also the score calculation, just a simple +1, and you can find it in the console
score = 0
def randomEncounter():
    roll = random.random()        
    if roll <= 0.20:
         currentScore = score +1
         show(makePicture(getMediaPath("treasure.png")))
         play(makeSound(getMediaPath("applause7.wav")))
         showInformation("You found the Treasure!\nYou Won!!!")
         print "Current Score: "+currentScore
         
    if roll > 0.20 and roll < 0.80:
         showInformation("No treasure")
    if roll >= 0.80:
      show(makePicture(getMediaPath("monster.png")))
      play(makeSound(getMediaPath("Drone.wav")))
      showInformation("Death by unspeakable horrid monster!\nPlease play again.")
      exit() #I dont know why this exit doesnt work...
      