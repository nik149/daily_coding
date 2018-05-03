sentence = raw_input()

words = sentence.split(' ')

k = input() #desired line length

def addSpaces(line):
    if(len(line) == 1):
        totalSpacesRequired = k - len(line[0])
        lineString = line[0] + ' ' * totalSpacesRequired
        return lineString

    lineString = ''.join(line)
    spacesArray = [0 for x in range(0, len(line) - 1)]
    totalSpacesRequired = k - len(lineString)

    i = 0
    while totalSpacesRequired != 0:
        spacesArray[i] += 1
        i+=1
        totalSpacesRequired -= 1
        if(i == len(spacesArray)):
            i = 0

    lineString = ''
    for i in range(0, len(line)):
        lineString += line[i]
        if(i < len(spacesArray)):
            lineString += ' ' * spacesArray[i]

    return lineString

linesArray = []
line = []
currentLineCount = 0

for i in range(0, len(words)):
    if(currentLineCount + len(words[i]) > k):
        linesArray.append(line);
        line = []
        currentLineCount = 0

    currentLineCount += 1 + len(words[i]) #add 1 for space
    line.append(words[i])

if(len(line) > 0):
    linesArray.append(line)

print linesArray


##padding
for i in range(0, len(linesArray)):
    lineLength = len(' '.join(linesArray[i]))
    if(lineLength < k):
        print addSpaces(linesArray[i])
    else:
        print ' '.join(linesArray[i])
