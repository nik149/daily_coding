encoding = raw_input()

singleAcceptable = 1
for i in range(0, len(encoding)):
	if(int(encoding[i]) <= 1):
		singleAcceptable = 0

if(singleAcceptable):
	ways = 1
else:
	ways = 0

for i in range(0, len(encoding) - 1):
	if(int(encoding[i]) <= 2 and int(encoding[i]) > 0 and int(encoding[i+1]) <= 6 and (i < len(encoding) - 2 and int(encoding[i+2]) > 0)):
		ways += 1

print ways 
