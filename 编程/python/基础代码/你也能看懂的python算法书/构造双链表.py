def Output(ListValue,ListRight,head):
	print(ListValue[head])
	next = ListRight[head]
	while next != -1:
		print(ListValue[next])
		next = ListRight[next]
ListValue = [1,5,6,2,7,3]
ListRight = [3,2,4,5,-1,1]
ListLeft = [-1,5,1,0,2,3]
head = 0
prepos = 5
Output(ListValue,ListRight,head)
print()
ListValue.append(4)
ListRight.append(ListRight[prepos])
ListLeft.append(prepos)
ListLeft[ListRight[prepos]] = len(ListValue) - 1
ListRight[prepos] = len(ListValue) - 1
Output(ListValue,ListRight,head)