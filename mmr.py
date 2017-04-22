import sys
import json




def addChampion():
    champion = raw_input("Please enter champion name:" )
    startingMMR = raw_input("What is your starting MMR: ")

    with open('data.JSON',"r") as i:
        info = json.load(i)
        info['champions'].append({champion:{"startingMMR":startingMMR,"currentMMR":""}})

    with open('data.JSON','w') as o:
              json.dump(info,o)

    
    


    
def addMMR():
    champion = raw_input("Please enter your champion:")
    addToMMR = raw_input("How much did you change?")

    info = json.load()
    print  info['overallMMR']

def addToMmmr(file):
    return 0







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

    elif option == 2:
        addMMR(f)        

    if option == 6:
         sys.exit()
