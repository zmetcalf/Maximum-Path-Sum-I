# numList[row][column]

txt = open("triangle.txt")
numList = []
total = 0

def binaryMap(toBinary):
    binaryList = []
    tempString = ""
    tempString = str(bin(toBinary))
    for i in range(12 - len(tempString)):
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

    for i in range(1024):
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
        
        for moveUp in range(rowCheck, (rowCheck - 10), -1): 
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
    
# Finds where last iterations went through
def findInRow(num, row): # Needs reworked
    results = map(int, numList[row -1])
    return results.index(num)
# ----------------------------------------

numList = str(txt.read()).split("\n", 100)

for x in range(100):
    numList[x] = numList[x].split(" ", 100)

highNum = 0
highList = []
highestList = []

for x in range(100):
    tempNum = 0
    tempList = bottomUp(99, x)
    for i in tempList:
        tempNum += int(i)
    if(tempNum > highNum):
        highNum = tempNum
        highList = tempList

test = highList.pop()
highestList += highList


tempLocator = findInRow(int(test), 91)
print tempLocator
tempList = bottomUp((89), tempLocator)
highestList.append(test)
highestList += tempList
test = highestList.pop()

tempLocator = findInRow(int(test), 81)
print tempLocator
tempList = bottomUp((79), tempLocator)
highestList.append(test)
highestList += tempList
highestList += numList[0][0]
        
#test = highList.pop()
#highestList += highList

print highestList
print test
print highList
print tempList
