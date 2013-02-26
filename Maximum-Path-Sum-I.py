# numList[row][column]

txt = open("triangle.txt")
numList = []
total = 0

def binaryMap(toBinary):
    binaryList = []
    tempString = ""
    tempString = str(bin(toBinary))
    for i in range(22 - len(tempString)):
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
    highestPoint = 0

    for i in range(1048576): #Int num + 1 - must be even
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
        
        for moveUp in range(rowCheck, (rowCheck - 20), -1): #change for row checks = num of 111 in binary
            tempList.append(numList[moveUp][mapper[counter]])
            counter += 1
            
        for x in tempList:
            tempTotal += int(x)   
        if(tempTotal > total):
            total = tempTotal
            highestList = tempList
            highestPoint = mapper.pop()
        tempList = []
        tempTotal = 0
        counter = 0
        mapper = []
    highestList.append(highestPoint)
    return highestList

numList = str(txt.read()).split("\n", 100)

for x in range(100):
    numList[x] = numList[x].split(" ", 100)

highNum = 0
highList = []
highestList = []
highLocation = 0

for x in range(100):
    tempNum = 0
    tempList = bottomUp(99, x)
    tempLocation = tempList.pop()
    for i in tempList:
        tempNum += int(i)
    if(tempNum > highNum):
        highNum = tempNum
        highList = tempList
        highLocation = tempLocation

test = highList.pop()
highestList += highList

for puzzle in range(79, 19, -20):
    tempList = bottomUp(puzzle, highLocation)
    highLocation = tempList.pop()
    highestList.append(test)
    highestList += tempList
    test = highestList.pop()

tempList = bottomUp(19, highLocation)
highLocation = tempList.pop()
highestList.append(test)
highestList += tempList

print highestList

highestTotal = 0
for x in highestList:
    highestTotal += int(x)

print highestTotal