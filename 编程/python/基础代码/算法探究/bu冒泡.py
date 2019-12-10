# 冒泡排序
def bu(list1):
	for num in range(len(list1)-1,0,-1):
		for i in range(num):
			if list1[i]>list1[i+1]:
				temp=list1[i]
				list1[i]=list1[i+1]
				list1[i+1]=temp
list1=[23,435,34,546,87]
bu(list1)
print(list1)

#短冒泡
def bu1(list2):
	exchanges=True
	num=len(list2)-1
	while num>0 and exchanges:
		exchanges=False
		for i in range(num):
			if list2[i]>list2[i+1]:
				exchanges=True
				temp=list2[i]
				list2[i]=list2[i+1]
				list2[i+1]=temp
		num=num-1
list2=[1,2,3,4,5,6]
bu1(list2)
print(list2)
# 选择排序
def sele(list3):
	for num in range(len(list3)-1,0,-1):
		numax=0
		for i in range(1,num+1):
			if list3[i]>list3[numax]:
				numax=i
		temp=list3[num]
		list3[num]=list3[numax]
		list3[numax]=temp
list3=[3,5,2,4,1]
sele(list3)
print(list3)
# 插入排序
def insr(list4):
	for num in range(1,len(list4)):
		value=list4[num]
		i=num
		while i>0 and list4[i-1]>value:
			list4[i]=list4[i-1]
			i=i-1
		list4[i]=value
list4=[2,3,6,4,1,5]
insr(list4)
print(list4)