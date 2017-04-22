import sys
import json




def addChampion():
    champion = raw_input("Please enter champion name:" )
    startingMMR = raw_input("What is your starting MMR: ")

    with open('data.JSON',"r") as i:
        info = json.load(i)
        info['champions'].append({champion:{"startingMMR":startingMMR,"currentMMR":""}})

    with open('data.JSON','w') as o:
              json.dump(info,o, sort_keys=True, indent=4, separators=(',', ': '))

    
    


    
def addMMR():
    champion = raw_input("Please enter your champion:")
    newMMR = str(raw_input("What is your new MMR: "))

    with open('data.JSON',"r") as i:
        info = json.load(i)
        counter = 0
        index = 0
        for x in info['champions']:
            for k in x:
                if k == champion:
                    index = counter
                else:
                    counter+=1

        x = int(newMMR) - int(info['champions'][index][champion]['currentMMR'])
        print "change is " + str(x)    
        info['champions'][index][champion]['currentMMR'] = newMMR
        
    with open('data.JSON','w') as o:
              json.dump(info,o)

        

                    
                    
                    
            


def addToMmr():
    newMMR = str(raw_input("What is your new MMR: "))

    with open('data.JSON',"r") as i:
        info = json.load(i)
        info['overallMMR'] = newMMR
    
    with open('data.JSON','w') as o:
              json.dump(info,o)





while True:
    print "What would you like to do"

    print "1 : Add a champion"
    print "2 : Add MMR to a champion"
    print "3 : Add to your overall MMR"
    print "4 : Graph your MMR"
    print "5 : Graph a champion's MMR"
    print "6 : Print your current MMR"
    print "7 : Print champion MMR"
    
    
    print "8 : Quit the program"

    option = int(raw_input("Enter a number "))

    if option == 1:
        addChampion()

    elif option == 2:
        addMMR()
    elif option ==3:
        addToMmr()

    
    if option == 8:
         sys.exit()
