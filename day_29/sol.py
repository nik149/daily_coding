string = raw_input()

def encodeString(string):
    currentCharCount = 0
    currentChar = None

    encodedString = ''
    for i in range(0, len(string)):
        if(currentChar is None):
            currentChar = string[i]
            currentCharCount = 1
        #on new char
        elif(currentChar != string[i]):
            encodedString += str(currentCharCount) + currentChar
            currentCharCount = 1
            currentChar = string[i]
        else:
            currentCharCount += 1

    if(currentChar is not None):
        encodedString += str(currentCharCount) + currentChar

    return encodedString

print encodeString(string)
