arr = map(int, raw_input().split(' '))
print arr

for i in range(0, len(arr)):
	if(arr[i] - 1 < len(arr) and arr[arr[i] - 1] > 0):
		arr[arr[i] - 1] = -arr[arr[i] - 1]
print arr
