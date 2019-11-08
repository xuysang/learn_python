import re
import reprlib
RE_WORD = re.compile('\w+')
class Sentence:
	def __init__(self,text):
		self.text = text # 不再需要words列表
	def __repr__(self):
		return 'Sentence(%s)'%reprlib.repr(self.text)
	def __iter__(self):
		return (match.group() for match in RE_WORD.finditer(self.text))

		# for match in RE_WORD.finditer(self.text): # finditer函数构建一个迭代器，包含self.text中匹配RE_WORD的单词，产出MathObject实例
			# yield match.group() # match.group()方法从MatchObject实例中提取匹配正则表达式的具体文本

class LookingGlass:
	def __enter__(self): # 除了self之外，python调用__enter__方法时不传入其他参数
		import sys 
		self.original_write = sys.stdout.write # 把原来的sys.stdout.write方法保存在一个实例属性中
		sys.stdout.write = self.reverse_write # 为sys.stdout.write打猴子补丁，替换成自己编写的方法 
		return 'JABBERWOCKY' #返回字符串，有内容存入变量what
	def reverse_write(self,text): # 
		self.original_write(text[::-1])
	def __exit__(self,exc_type,exc_value,traceback):
		import sys
		sys.stdout.write = self.original_write
		if exc_type is ZeroDivisionError:
			print('Please DO NOT divide by zero!')
			return True