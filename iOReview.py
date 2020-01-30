
lineList = []
with open("simplefile.txt", 'r') as simplefile:
    for line in simplefile:
        lineList.append(line)

#wordList = lineList[0].split()



lineList.insert(0, "This is the NEW first line of the list!\n")

with open("newSimpleFile.txt", 'w') as newSimpleFile:
    newSimpleFile.writelines(lineList)



