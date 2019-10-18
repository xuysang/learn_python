from array import array
import math
class Vector2d:
	typecode = 'd'
	def __init__(self,x,y):
		self.__x = float(x) #使用两个前导下划线，把属性标记为私有的
		self.__y = float(y)
	@property   #装饰器把读值方法标记为特性
	def x(self):  #读值方法与公开属性同名，都是x
		return self.__x  #直接返回self.__x
	@property
	def y(self):
		return self.__y
	def __iter__(self):
		return (i for i in (self.x,self.y))
	def __hash__(self):
		return hash(self.x)^hash(self.y)
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(*memv)