from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = '日份额'
Mobile = convert(concrete1,task)
atall = False
content_txt = '陈富贵提醒您：处理日份额'
dingTalk(content_txt,Mobile,atall)