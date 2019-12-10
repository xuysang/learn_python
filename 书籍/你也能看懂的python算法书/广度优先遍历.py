def bfs(numCourses,preList):
	preListCount = [0]*numCourses
	for line in preList:
		for i in range(len(line)):
			if line[i] == 1:
				preListCount[i] += 1
	canTake = []
	for i in range(len(preListCount)):
		if preListCount[i] == 0:
			canTake.append(i)
	classTake = []
	while len(canTake) != 0:
		thisClass = canTake[0]
		del canTake[0]
		classTake.append(thisClass)
		for i in range(numCourses):
			if preList[thisClass][i] == 1:  # thisClass表示以它为选修课的当前这行，遍历其他课是否需要选修
				preListCount[i] -= 1
				if preListCount[i] == 0: # 当所有待先选修的课数量为0时，加入canTake
					canTake.append(i)
	return classTake