import sys
import json



overall mmr = []
average mmr = 
libarary = {}

def addChampion():
    champion = raw_input("Please enter champion name:" )
    startingMMR = raw_input("What is your starting MMR")

def addMMR(file):
    champion = raw_input("Please enter your champion:")
    addToMMR = raw_input("How much did you change?")

def addToMmmr(file):
    

f = open('data.txt','r+')
while True:
    print "What would you like to do"
    print "1 : Add a champion"
    print "2 : Add MMR to a champion"
    print "3 : Add to your overall MMR"
    print "4 : Graph your MMR"
    print "5 : Graph a champion's MMR"
    print "6 : Quit the program"

    option = int(raw_input("Enter a number "))

    if option == 1:
        addChampion()

    elif option == 3:
        addMMR(f)        

    if option == 6:
         sys.exit()
