


with open("testFile.txt", 'r') as fileHandler:
    fileData = fileHandler.read()
    print(fileData)



lineList = []
with open("testFile.txt", 'r') as fileHandler2:
    for line in fileHandler2:
        lineList.append(line)

#print(lineList)

print(lineList[0])

firstLine = lineList[0]


firstLineList = firstLine.split()

print(firstLineList)