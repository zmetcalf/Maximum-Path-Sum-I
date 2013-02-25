txt = open("triangle.txt")
numList = []
total = 0

numList = str(txt.read()).split("\n", 15)

for x in range(15):
    numList[x] = numList[x].split(" ", 15)
    
