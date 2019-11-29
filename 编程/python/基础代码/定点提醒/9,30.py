from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = '补8个代码'
Mobile = convert(concrete1,task)
atall = False
content_txt = '陈富贵提醒您：港交所净值补8个代码'
dingTalk(content_txt,Mobile,atall)