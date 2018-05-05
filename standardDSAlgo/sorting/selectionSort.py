def selectionSort(A):
    n = len(A)

    for i in range(0, n-1):
        minimum = i

        for j in range(i, n):
            if(A[j] < A[minimum]):
                minimum = j

        A[minimum], A[i] = A[i], A[minimum]

    return A

arr = map(int, raw_input().split(' '))

print selectionSort(arr)
