arr = map(int, raw_input().split(' '))

newArr = []
k = 0
for i in range(0, len(arr)):
	if(i%2 == 0):
		newArr.append(arr[k])
		k += 1
	else:
		newArr.append(arr[len(arr) - k])

print newArr
