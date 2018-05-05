# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail


# Write your code here
key1, lockKey = map(int, raw_input().split(' '))
N = input()
otherKeys = map(int, raw_input().split(' '))

desiredProductFromOtherKeys = lockKey

def product(arr):
    prod = 1
    for i in range(0, len(arr)):
        prod *= arr[i]
    return prod

def calculateArrayProduct(arr, productValue):
    arr.sort()
    productContents = []
    productPairs = []
    prod = key1
    for i in range(0, len(arr)):
        if((productValue % 100000) % (prod*arr[i] % 100000) == 0):
            productContents.append(arr[i])
            prod *= arr[i]

            if(prod % 100000 > productValue):
                prod = key1
                productContents = []
            elif(prod % 100000 == productValue):
                productPairs.append(productContents)
                prod = key1
                productContents = []

    minLen = -1
    for i in range(0, len(productPairs)):
        if(minLen == -1 or len(productPairs[i]) < minLen):
            minLen = len(productPairs[i])
    return minLen

print calculateArrayProduct(otherKeys, desiredProductFromOtherKeys)
