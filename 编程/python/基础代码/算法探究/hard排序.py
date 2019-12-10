# 希尔排序 子列表的每个数据按照插入排序依次排序，然后减少增量再分子列表
def q_sort(list1):
	sublist_count=len(list1)//2
	while sublist_count>0:
		for start in range(sublist_count):
			insert_sort(list1,start,sublist_count)
		sublist_count=sublist_count//2
def insert_sort(list1,start_index,gap):
	for i in range(start_index+gap,len(list1),gap):
		value=list1[i]
		p=i
		while p>=gap and list1[p-gap]>value:
			list1[p]=list1[p-gap]
			p=p-gap
		list1[p]=value

list1=[23,35,14,98,43,32,21]
q_sort(list1)
print(list1)

# 归并排序
