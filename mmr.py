import sys
import json




def addChampion(file):
    champion = raw_input("Please enter champion name:" )
    startingMMR = raw_input("What is your starting MMR: ")

    info = json.load(file)
    info["champions"].append({ champion :{"currentMMR": startingMMR,"pastMMR":"" } } )
    json.dumps(info,file)
    
def addMMR(file):
    champion = raw_input("Please enter your champion:")
    addToMMR = raw_input("How much did you change?")

    info = json.load(file)
    print  info['overallMMR']

def addToMmmr(file):
    return 0




f = open('data.JSON','r+')
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
        addChampion(f)

    elif option == 2:
        addMMR(f)        

    if option == 6:
         sys.exit()
