#1074 = 75+64+82+87+82+75+73+28+83+32+93+73+58+78+91 - figured w/pin & paper/trial & error
#Pick the highest 5 from the bottom, then pick the next highest 6 from that number

# numList[row][column]

txt = open("triangle.txt")
numList = []
total = 0

def binaryMap(toBinary):
    binaryList = []
    tempString = ""
    tempString = str(bin(toBinary))
    for x in range(2, len(tempString)):
        binaryList.append(tempString[x])
    return binaryList


def bottomUp(rowCheck, columnCheck): 
    total = 0
    tempTotal = 0
    highestList = []
    tempList = []
 
    while True: 
        for moveUp in range(rowCheck, (rowCheck - 5), -1): 
            for moveHoriz in mapper: # Working out how to itirate through each series - maybe another nested loop...
                tempList.append(numList[moveUp][moveHoriz])
                
        for x in tempList:
            tempTotal = tempTotal + x   
        if(tempTotal > total):
            total = tempTotal
            partialList = tempList
        
        tempList = []
        tempTotal = 0
    
    return highestList

numList = str(txt.read()).split("\n", 15)

for x in range(15):
    numList[x] = numList[x].split(" ", 15)
    
print len(numList[14]) # Returns how many are in row - maybe useful later - maybe easier to use a formula

print bin(1)
print binaryMap(1)
    
