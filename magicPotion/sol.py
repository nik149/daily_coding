N, K = map(int, raw_input().split(' '))

arr = map(int, raw_input().split(' '))


def magicPotion(arr, i):
    if(i == 's'):
        return arr[1:]
    if(i == 'e'):
        return arr[:-1]


def countGoodArrays(arr, numMagicPotions):
    if(len(arr) == 0):
        return []

    if(sum(arr) == K):
        return [[arr, numMagicPotions]]


    if(sum(arr) < K):
        return []

    result1 = countGoodArrays(magicPotion(arr, 's'), numMagicPotions + 1)
    result2 = countGoodArrays(magicPotion(arr, 'e'), numMagicPotions + 1)

    return result1 + result2


result = countGoodArrays(arr, 0)

finalResult = []
minCount = -1
for i in range(0, len(result)):
    if(result[i][1] < minCount or minCount == -1):
        minCount = result[i][1]

print len(result), minCount
