'''
l=[1,2,3,4]
s='abcde'

for x in s:print(x)
print(iter(l))
print(iter(s))
# print(iter(5)) 整数是不可迭代的 iter里面是可迭代对象
t=iter(l)
print(next(t))  # 在py3里面，next用法变成next(iterator)

mylist = [x*x for x in range(3)]  # 可迭代的

mygenerator = (x*x for x in range(3)) # 生成器。生成器不储存所有的值，它们是不断被产生的

# iterable是指这个这个对象是可迭代的，例如list,set,dict
# iterator是指迭代器A，next(A)直到A没有next了   
'''
def create():
	mylist=range(3)
	for i in mylist:
		yield i*i
mygenerator=create()
print(mygenerator)
for i in mygenerator:
	print(i)