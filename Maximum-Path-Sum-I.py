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
    for i in range(6 - len(tempString)):
        binaryList.append('0')
    for x in range(2, len(tempString)):
        binaryList.append(tempString[x])
    return binaryList

def bottomUp(rowCheck, columnCheck): 
    total = 0
    tempTotal = 0
    highestList = []
    tempList = []
    mapperCount = 0
    mapper = []
    binMap = []
    counter = 0

    for i in range(16):
        currentColumn = columnCheck
        currentRow = rowCheck
        binMap = binaryMap(i) # generates map to move up or left
        mapper.append(columnCheck)
        for z in binMap:    
            currentRow -= 1 # move to row 14 - up
            currentColumn -= int(z)
            if(currentColumn >= currentRow):
                mapper.append(currentRow)
            elif(currentColumn < 0):
                mapper.append(0)
            else:
                mapper.append(currentColumn)
        
        for moveUp in range(rowCheck, (rowCheck - 5), -1): #should not be nested
            # for moveHoriz in mapper:
            tempList.append(numList[moveUp][mapper[counter]])
            counter += 1
            
        for x in tempList:
            tempTotal += int(x)   
        if(tempTotal > total):
            total = tempTotal
            highestList = tempList
        tempList = []
        tempTotal = 0
        counter = 0
        mapper = []
    
    return highestList

numList = str(txt.read()).split("\n", 15)

for x in range(15):
    numList[x] = numList[x].split(" ", 15)
# print numList[14][0]  
print bottomUp(14, 9)
    
