def bubbleSort(A):
    n = len(A)

    for i in range(0, n):
        for j in range(i, n):
            if(A[i] > A[j]): ##increasing order
                A[i], A[j] = A[j], A[i]

    return A

arr = map(int, raw_input().split(' '))

print bubbleSort(arr)
