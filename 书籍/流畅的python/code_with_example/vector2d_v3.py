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
	@property # 使用相同的方式处理y特性
	def y(self):
		return self.__y
	def __iter__(self):
		return (i for i in (self.x,self.y)) # 通过self.x和self.y读取公开特性，不必读取私有属性
	def __hash__(self):
		return hash(self.x)^hash(self.y)
	def frombytes(cls,octets):
		typecode = chr(octets[0])
		memv = memoryview(octets[1:]).cast(typecode)
		return cls(*memv)
	def __repr__(self):
		class_name = type(self).__name__
		return '{}({!r},{!r})'.format(class_name,*self) #使用{!r}获取各个分量的表示形式，然后插值，构成一个字符串。因为Vector2d实例是可迭代对象，所以*self会把x和y分量提供给format函数。
	def __str__(self):
		return str(tuple(self))  # 从可迭代的Vector2d实例中得到一个元祖，显示为一个有序对。
	def __bytes__(self):
		return (bytes([ord(self.typecode)])+bytes(array(self.typecode,self)))  # 把typecode转换成字节序列，迭代Vector2d实例，得到一个数组，再把数组转换成字节序列。
	def __eq__(self,other):
		return tuple(self)==tuple(other)  # 为了快速比较所有分量，在操作数中构建元祖
	def __abs__(self):
		return math.hypot(self.x,self.y)  # 模是x和y分量构成的直角三角形的斜边长。
	def __bool__(self):
		return bool(abs(self))  # 计算亩，把结果换成布尔值，非零值是True.
	def angle(self):
		return math.atan2(self.y,self.x)
	def __format__(self,fmt_spec=''):
		if fmt_spec.endswith('p'):  # 如果格式代码以'p'结尾，使用极坐标
			fmt_spec = fmt_spec[:-1] # 从fmt_spec中删除'p'后缀
			coords = (abs(self),self.angle()) # 构建一个元祖，表示极坐标：(magnitude,angle)
			outer_fmt = '<{},{}>' # 把外层格式设为一对尖括号
		else:
			coords = self # 如果不以'p'结尾，使用self的x和y分量构建直角坐标
			outer_fmt = '({},{})' # 把格式外层设为一对圆括号
		components = (format(c,fmt_spec) for c in coords) #使用内置的format函数把fmt_spec应用到向量的各个分量上，构建一个可迭代的格式化字符串
		return outer_fmt.format(*components) # 把格式化字符串代入外层格式中。
@classmethod # 类方法使用classmethod装饰器修饰
def frombytes(cls,octets): # 不传入self参数；相反，通过cls传人类本身
 	typecode = chr(octets[0]) #  从第一个字节中读取typecode
	memv = memoryview(octets[1:]).cast(typecode) # 使用传入的octets字节序列创建一个memoryview,然后使用typecode转换
	return cls(*memv) # 拆包转换后的memoryview，得到构造方法所需的一对参数。
