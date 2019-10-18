from array import array
import math
class Vector2d:  
	typecode = 'd'  # typecode是类属性，在Vector2d实例和字节序列之间转换时使用
	def __init__(self,x,y):
		self.x = float(x) # 在__init__方法中把x和y转换成浮点数，尽早捕获错误，防止传入不当参数
		self.y = float(y)
	def __iter__(self): # 定义__iter__方法，把Vector2d实例变成可迭代的对象，这样才能拆包。
		return (i for i in (self.x,self.y))  # 直接调用生成器表达式一个接一个产出分量
	def __repr__(self):
		class_name = type(self).__name__
		return '{}({!r},{!r})'.format(class_name,*self)
	def __str__(self):
		return str(tuple(self))
	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))
	def __eq__(self,other):
		return tuple(self)==tuple(other)
	def __abs__(self):
		return math.hypot(self.x,self.y)
	def __bool__(self):
		return bool(abs(self))
	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(*memv)
	def __format__(self,fmt_spec=''):
		components = (format(c,fmt_spec) for c in self)
		return '({},{})'.format(*components)
	def angle(self):
		return math.atan2(self.y,self.x)