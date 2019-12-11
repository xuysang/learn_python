def bfs(set,m,n,matrix): # queue为队列
    dir = [[0,1],[0,-1],[1,0],[-1,0]] # 数组中四个元素代表四个方向
    queue = list(set)
    while len(queue) > 0:
    	x, y = queue.pop() # 取出队头的元素，由于是一个坐标，使用两个变量来接收
    	for d in dir: # 循环遍历4个方向
    		nx = x + d[0]
    		ny = y + d[1]
    		if 0 <= nx and nx < m and 0 <= ny and ny < n: # 如果新的点在二维数组内
    			if matrix[nx][ny] >= matrix[x][y]:
    				if (nx, ny) not in set:
    					queue.append((nx,ny))
    					set.add((nx, ny))
    print(set)
def solve(matrix): # matrix为存储地图的二维数组
  	if not matrix:
  		return matrix # 如果二维数组为空，那么就返回空
  	m = len(matrix) # 表示二维数组有多少行
  	n = len(matrix[0]) # 表示二位数组有多少列
  	toPoint = set([(0,y) for y in range(n)]) # 上边的点的横坐标为0，纵坐标为0到n-1
  	leftPoint = set([(x,0) for x in range(m)]) # 左边的点的横坐标为0到m-1,纵坐标为0
  	bottomPoint = set([(m-1,y) for y in range(n)]) # 下边的点的横坐标为m-2,纵坐标为0到n-1
  	rightPoint = set([(x,n-1) for x in range(m)]) # 右边的点的横坐标为0到m-1，纵坐标为n-1
  	a = bfs(toPoint,m,n,matrix) # 依次调用4次bfs
  	bfs(leftPoint,m,n,matrix)
  	bfs(bottomPoint,m,n,matrix)
  	bfs(rightPoint,m,n,matrix)
  	result = toPoint & leftPoint & bottomPoint & rightPoint # 求集合的交集
  	return result
matrix = [[1,3,2,3,5],[3,4,5,6,3],[2,7,4,3,3],[5,2,2,3,1]]
s = solve(matrix)
print(s)