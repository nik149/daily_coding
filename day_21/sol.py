numPairs = input('Insert num Pairs: ')

pairsArray= []
for i in range(0, numPairs):
    pairsArray.append(map(int, raw_input('Enter startTime endTime: ').split(' ')))

def doesOverlap(arr, item):
    nonOverlappingIndexes = []
    for i in range(0, len(arr)):
        if(item[0] >= arr[i][0] and item[0] <= arr[i][1]):
            continue
        else:
            nonOverlappingIndexes.append(i)

    if(len(nonOverlappingIndexes) > 0):
        return False, nonOverlappingIndexes
    else:
        return True, []

rooms = []

for i in range(0, numPairs):
    if(len(rooms) == 0):
        rooms.append(pairsArray[i])
    else:
        doesOverlapBool, nonOverlappingIndexes = doesOverlap(rooms, pairsArray[i])


        if(doesOverlapBool):
            rooms.append(pairsArray[i])
        else:
            rooms[nonOverlappingIndexes[0]] = pairsArray[i]


print len(rooms)
