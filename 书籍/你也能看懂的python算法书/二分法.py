numbers = [1,3,5,6,7,8,13,14,15,17,18,24,30,43,56]
head,tail = 0, len(numbers)
search = int(input("enter a number to search:"))

while tail - head > 1:
	mid = (head+tail)//2
	if search < numbers[mid]:
		tail = mid
	elif search > numbers[mid]:
		head = mid
	elif search == numbers[mid]:
		ans = mid
		break
else:
	if search == numbers[head]:
		ans = head
	else:
		ans = -1

print(ans)