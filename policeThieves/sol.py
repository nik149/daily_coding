A =  raw_input().split(' ')
K = input()

numAllotment = 0
i = 0
j = 0
nextP = -1
nextT = -1
pFound = False
tFound = False
numT = len([x for x in A if (x == 'T')])
numP = len([x for x in A if (x == 'P')])

while i <= numP and j <= numT:
    if(A[i] == 'P' and pFound is False):
        nextP = i
        pFound = True
        i += 1
    elif(A[j] == 'T' and tFound is False):
        nextT = j
        tFound = True
        j += 1

    if(pFound and tFound):
        if(abs(nextP - nextT) <= K):
            numAllotment += 1
            pFound = False
            tFound = False
#            i = min(i, j)
#            j = i
        else:
            pFound = False
            tFound = False
 #           i = min(i, j)
 #           j = i

print numAllotment



