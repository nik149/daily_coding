arr = map(int, raw_input().split(' '))
k = input()

pair = arr[:k]
print max(pair)
i = 1
while i < len(arr)-k + 1:
    pair = arr[i:i+k]
    print max(pair)
    i+=1

