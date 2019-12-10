'''
# 通过循环数字筛选出来再放进列表

data = [1,5,-3,-2,6,8,9]
res = []
for x in data:
	if x>=0:
		res.append(x)
print(res)


# filter函数 filter(lambda x:x>=0,data)  py3中filter返回的对象是一个filter类，需要转换成list才能直观显示
# 列表解析  [x for x in data if X>=0]
# 字典解析  {k:v for k,v in d.iteritems() if v >90}
# 集合解析  {x for x in s if x%3 == 0}
from random import randint

data=[randint(-10,10) for _ in range(10)]
# print([x for x in data if x>=0])
# print(list(filter(lambda x :x >=0,data)))


d={x:randint(60,100) for x in range(1,21)}
t={k:v for k,v in d.items() if v>90}
print(t)


data=[2,2,-3,-5,9,6,7,5,8,7]
s=set(data)
s1={x for x in s if x>=0}
print(s1)


data = [randint(0,100) for _ in range(30)]
c=dict.fromkeys(data,0)


for x in data:
	c[x]+=1
print(c)


# collections.Counter
# 讲序列传入Counter的构造器，得到Counter对象是元素频度的字典
# Counter.most_common(n)方法得到频度最高的n个元素的列表

from collections import Counter
C2 = Counter(data)
print(C2[95])
print(C2.most_common(3))
'''


# 对字典中的项进行排序，可以参考使用元祖
from random import randint
data={x:randint(60,100) for x in 'xyzabc'}
# sorted(data)


data1=zip(data.values(),data.keys())
print(sorted(data1))

print(sorted(data.items(),key=lambda x:x[1]))