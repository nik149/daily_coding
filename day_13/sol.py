S = raw_input()
K = input()


def subProb(s):
	max = 0
	length = 0
	substring = []
	ss = []
	ctr = 0
	i = 0
	k = 0
	while ctr < len(s) - 1:
		if(s[i] not in ss):
			ss.append(s[i])
			k+=1
			length+=1
			i+=1
		else:
			ss.append(s[i])
			length+=1
			i+=1
		if(k > K or i > len(s) - 1):
			if(length > max):
				max = length - 1
				substring = list(ss[:-1])
				ss = []
				length = 0
				k = 0
				ctr+=1
				i = ctr
			else:
				ss = []
				length = 0
				k = 0
				ctr += 1
				i = ctr

	print max, substring

subProb(S)
