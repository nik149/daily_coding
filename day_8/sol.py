arr = map(int, raw_input().split(' '))

def unadjacentArray(arr, i):
	if(len(arr) <= 2):
		return []
	if(i == 0):
		return arr[2:]
	if(i == 1):
		if(len(arr) > 3):
			return arr[3:]
		else:
			return []

	newArr = []
	for k in range(0, len(arr) - 2):
		if(k < i-1 or k > i+1):
			newArr.append(arr[k])
	return newArr

	
def subProb(arr, sum):
	if(len(arr) == 0):
		return sum;
	
	max = subProb(unadjacentArray(arr, 0), sum + arr[0])
	
	for i in range(1, len(arr)):
		max2 = subProb(unadjacentArray(arr, i), sum + arr[i])
		if(max2 > max):
			max = max2
	
	return max;

print subProb(arr, 0)

