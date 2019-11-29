from dingtest import dingTalk
from read_excel import read_excel,convert

task = read_excel()	
concrete1 = '过电子公告'
Mobile = convert(concrete1,task)
atall = False
content_txt = '陈富贵提醒您：过电子公告'
dingTalk(content_txt,Mobile,atall)