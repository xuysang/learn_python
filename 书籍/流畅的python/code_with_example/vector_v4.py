from array import array
import math
import reprlib
import functools #为了使用reduce函数导入该模块
import operator #为了使用xor函数导入该模块
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
		return len(self)==len(other) and all(a==b for a,b in zip(self,other))
	def __hash__(self):
		hashes=(hash(x) for x in self._components) #创建一个生成器表达式，惰性计算各个分量的散列值
		return functools.reduce(operator.xor,hashes,0)
	def __abs__(self):
		return math.sqrt(sum(x * x for x in self)) 
	def __bool__(self):
		return bool(abs(self))
	def __len__(self):
		return len(self._components)
	def  __getitem__(self,index):
		cls = type(self)
		if isinstance(index,slice):
			return cls(self._components[index])
		elif isinstance(index,int):
			return self._components[index]
		else:
			msg = '{cls.__name__} indices must be integers'
			raise TypeError(msg.format(cls=cls))
	shortcut_names='xyzt'
	def __getattr__(self,name):
		cls = type(self) # 获取Vector
		if len(name)==1: # 如果属性名只有一个字母，可能是shortcut_names中的一个
			pos = cls.shortcut_names.find(name) # 查找那个字母的位置
			if 0<=pos<len(self._components):
				return self._components[pos]
		msg = '{.__name__!r} object has no attribute {!r}'
		raise AttributeError(msg.format(cls,name))
	def __setattr__(self,name,value):
		cls = type(self)
	    if len(name)==1: # 特别处理名称是单个字符的属性
	    	if name in cls.shortcut_names: # 如果name是xyzt中的一个，设置特殊的错误消息
	    		error = 'readonly attribute {attr_name!r}'
	    	elif name.islower(): # 如果name是小写字母，为所有小写字母设置一个错误消息
	    		error="can't set attribute 'a' to 'z' in {cls_name!r}"
	    	else:
	    		error='' # 否则，把错误消息设为空字符串
	    	if error: # 如果有错误消息，抛出AttributeError
	    		msg = error.format(cls_name=cls.__name__,attr_name=name)
	    		raise AttributeError(msg)
	    super().__setattr__(name,value) # 默认情况：在超类上调用__setattr__方法，提供标准行为



	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(memv) #