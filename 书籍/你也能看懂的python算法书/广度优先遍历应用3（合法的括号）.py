def isvalid(str):
	count = 0
	for c in str:
		if c == 'c':
			count += 1
		elif c == ')':
			count -= 1
			if count < 0:
				return False
return count == 0
def bfs(str):
	res = []
	queue = [str]
	while len(queue) > 0:
		for i in range(len(queue)):
			if isvalid(queue[i]):
				res.append(queue[i])
			if len(res) > 0:
				return list(set(res))
			temp = []
			for s in queue:
				for i in range(len(s)):
					if s[i]=='(' or s[i]==')':
						temp.append(s[:i]+s[i+1:])
			queue = list(set(temp))
	return list(set(res))

