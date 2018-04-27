arr = map(int, raw_input().split(' '))

left = []
prod = 1

for i in range(0, len(arr)):
	left.append(prod)
	prod *= arr[i]

right = []
prod = 1
for i in range(len(arr) - 1, -1, -1):
	right.append(prod)
	prod *= arr[i]

newArr = []
for i in range(0, len(arr)):
	newArr.append(left[i] * right[len(arr) - i-1])

print newArr
