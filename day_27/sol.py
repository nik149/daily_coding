string = raw_input()

def isValid(string):
    if(len(string) == 0):
        return True
    elif(len(string) % 2 != 0):
        return False
    elif(len(string) == 2 and isComp(string[0],string[1])):
        return True
    else:
        ##fetch pairs
        i = 0
        j = 0
        pairs = []
        initChar = None
        while j < len(string):
            if(initChar is None):
                initChar = string[i]
            else:
                if(isComp(initChar, string[j])):
                    pairs.append(string[i+1:j])
                    i = j + 1
                    initChar = None
            j+=1

        if(len(pairs) == 0):
            return False

        for i in range(0, len(pairs)):
            if(not isValid(pairs[i])):
                return False
        return True

def isComp(s1, s2):
    if(s1 == '(' and s2 == ')'):
        return True
    if(s1 == '{' and s2 == '}'):
        return True
    if(s1 == '[' and s2 == ']'):
        return True
    return False

print isValid(string)
