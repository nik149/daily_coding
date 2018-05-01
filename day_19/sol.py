N = input('N: ')
K = input('K: ')

costMat = [] ##K*N => K rows, N columns
for i in range(0, K):
    costMat.append(map(int, raw_input('cost for each house for k = rowNum').split(' ')))

def spliceRow(costMat, index):
    newArr = []
    for i in range(0, len(costMat)):
        if(i != index):
            newArr.append(costMat[i])
    return newArr


def subProb(arr, houses, k):
    ##something
    if(len(houses) == 0):
        return 0

    costMin = arr[0][houses[0]] + subProb(spliceRow(costMat, k), houses[1:], k)

    for i in range(1, len(arr)):
        cost = arr[i][houses[0]] + subProb(spliceRow(costMat, i), houses[1:], i)
        if(cost < costMin):
            costMin = cost

    return costMin



cost = 0
houseIndexes = [x for x in range(0, N)]
#if house 1 choses color1
cost = subProb(costMat, houseIndexes, 0)
print cost

