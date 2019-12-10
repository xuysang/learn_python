from array import array
import numbers
import math
import reprlib
import functools #为了使用reduce函数导入该模块
import operator #为了使用xor函数导入该模块
import itertools
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
		elif isinstance(index,numbers.Integral):
			return self._components[index]
		else:
			msg = '{.__name__} indices must be integers'
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
	def angle(self,n): # 使用n维球体词条中的公式计算某个角坐标
		r = math.sqrt(sum(x * x for x in self[n:]))
		a = math.atan2(r,self[n-1])
		if (n==len(self)-1) and (self[-1]<0):
			return math.pi*2-a
		else:
			return a
	def angles(self):  # 创建生成器表达式，按需计算所有角坐标
		return (self.angle(n) for n in range(1,len(self)))
	def __format__(self,fmt_spec=''): 
		if fmt_spec.endswith('h'): #超球面坐标
			fmt_spec = fmt_spec[:-1]
			coords = itertools.chain([abs(self)],self.angles()) # 使用itertools.chain函数生成生成器表达式，无缝迭代向量的模和各个角坐标
			outer_fmt = '<{}>' # 配置使用尖括号显示球面坐标
		else:
			coords = self
			outer_fmt = '({})' # 配置使用圆括号显示笛卡尔坐标
		components = (format(c,fmt_spec) for c in coords) # 创建生成器表达式，按需格式化各个坐标元素
		return outer_fmt.format(', '.join(components)) # 把以逗号分隔的格式化分量插入尖括号或圆括号
	@classmethod
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(memv) 