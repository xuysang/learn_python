from array import array
import math
import reprlib
class Vector:
	typecode = 'd'
	def __init__(self,components):
		self._components = array(self.typecode,components) #self._components是“受保护的”实例属性，把Vector的分量保存在一个数组中。
	def __iter__(self):
		return iter(self._components) #为了迭代，我们使用self._components构建一个迭代器。
	def __repr__(self):
		components = reprlib.repr(self._components) #使用reprlib.repr（　）函数获取self._components的有限长度表示形式（如array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...])）。
		components = components[components.find('['):-1] #把字符串插入Vector的构造方法调用之前，去掉前面的array('d'和后面的)。
		return 'Vector({})'.format(components)
	def __str__(self):
		return str(tuple(self))
	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(self._components)) #直接使用self._components构建bytes对象。
	def __eq__(self,other):
		return tuple(self)==tuple(other)
	def __abs__(self):
		return math.sqrt(sum(x * x for x in self)) 
	def __bool__(self):
		return bool(abs(self))
	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(memv) #
	def __len__(self):
		return len(self._components)
	def  __getitem__(self,index):
		cls = type(self)
		if isinstance(index,slice):
			return cls(self._components[index])
		elif isinstance(index,numbers.Integral):
			return self._components[index]
		else:
			msg = '{cls.__name__} indices must be integers'
			raise TypeError(msg.format(cls=cls))