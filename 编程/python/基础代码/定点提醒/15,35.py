from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete3 = 'IOPV'
Mobile3 = convert(concrete3,task)
atall = False
content_txt3 = '陈富贵提醒您：IOPV'

dingTalk(content_txt3,Mobile3,atall)