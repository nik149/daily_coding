numStairs = input()

def subProb(stairsLeft, ways):
	if(stairsLeft == 0):
		return 0
	if(stairsLeft == 1):
		return ways + 1
	if(stairsLeft == 2):
		return ways + 2
	
	ways += subProb(stairsLeft - 1, ways) + subProb(stairsLeft - 2, ways)
	return ways

print subProb(numStairs, 0)
